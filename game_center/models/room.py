# -*- coding:utf-8 -*-
from pretty_logging import pretty_logger

from . import User
from ..services.gobang import Gobang


class Room():
    room_id: int = 0
    creator: User = None
    participator: User = None

    # status
    is_gaming: bool = False

    # 五子棋局
    game: Gobang = None
    turn = None

    # 定时器部分，暂时搁置

    def __init__(self, rid):
        self.room_id = rid

    def start_game(self, gobang):
        self.game = gobang
        self.turn = 1
        self.is_gaming = True

    #玩家加入房间，第一个玩家为creator
    def join_room(self, player):
        if self.creator is None:
            self.creator = player
        elif self.participator is None:
            self.participator = player
        else:
            pretty_logger.error("房间已满")

    # 玩家退出房间，如果房主退出则将参与人转为房主
    def quit_room(self, uid):
        if self.is_inroom(uid) == False:
            return False
        role: int = self.__uid2player(uid)
        if role == 1:
            self.creator = self.participator
            self.participator = None
        elif role == 2:
            self.participator = None
        

    # 房间状态获取，是否已满
    def is_full(self):
        return self.creator is not None and self.participator is not None

    def is_inroom(self, uid):
        return self.__uid2player(uid) != -1

    # 对gobang.is_end的封装
    # 判断棋局是否结束
    # return: (status, msg) - (0, "") - 未结束; (1/2, "normal") - 正常结束，黑棋/白棋获胜; (1,/2 , "timeout") - 对方超时
    def is_end(self):
        if self.game is None:
            return None
        res = self.game.is_end()
        if res == 0:
            return (0, "")
        elif res == 1:
            self.is_gaming = False
            return (1, "normal")
        elif res == 2:
            self.is_gaming = False
            return (2, "normal")
        else:
            raise Exception("gobang logic error.")

    def drop(self, x, y, uid):
        player_id = self.__uid2player(uid)
        if player_id == -1 or player_id != self.turn:
            pretty_logger.error(
                "player {} not in the game or not your turn".format(uid))
            return

        pretty_logger.debug("{} want to drop: {} {}".format(uid, x, y))
        if self.game is None or self.is_gaming == False:
            return
        # 落子
        res = self.game.drop_chess(x, y, player_id)
        if res == 0:
            # 没有落子
            return
        self.is_end()
        # 换手
        self.turn = 1 if player_id == 2 else 2
        # 重置定时器

    def isgaming(self):
        return self.is_gaming

    def game_status(self):
        if self.game is not None:
            return self.game.chess_status()
        return []

    def __uid2player(self, uid):
        if self.creator and uid == self.creator.uid:
            return 1
        elif self.participator and uid == self.participator.uid:
            return 2
        else:
            return -1

    def to_dict(self):
        return {
            "id": self.room_id,
            "creator": self.creator.to_dict(),
            "participarot": self.participator.to_dict() if self.participator is not None else None
        }
