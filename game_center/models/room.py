# -*- coding:utf-8 -*-

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

    def __init__(self, rid, creator):
        self.room_id = rid
        self.creator = creator

    def start_game(self, gobang):
        self.game = gobang
        self.turn = 1
        self.is_gaming = True

    # 对gobang.is_end的封装
    # 判断棋局是否结束
    # return: (status, msg) - (0, "") - 未结束; (1/2, "normal") - 正常结束，黑棋/白棋获胜; (1,/2 , "timeout") - 对方超时

    def is_finish(self):
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
            return

        # 落子
        self.game.drop_chess(x, y, player_id)
        # 换手
        self.turn = 1 if player_id == 2 else 1
        # 重置定时器

    def isgaming(self):
        return self.is_gaming

    def game_status(self):
        if self.game is not None:
            return self.game.chess_status()
        return []

    def __uid2player(self, uid):
        if uid == self.creator.uid:
            return 1
        elif uid == self.participator:
            return 2
        else:
            return -1

    def to_dict(self):
        return {
            "id": self.room_id,
            "creator": self.creator.to_dict(),
            "participarot": self.participator.to_dict() if self.participator is not None else None
        }
