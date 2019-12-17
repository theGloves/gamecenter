# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger


from ..services.props import panic, success, error
from ..services.user import query_user_id
from ..services.gobang import Gobang
from ..models import Room
from ..types import CreateRoomSchema, JoinGameSchema, DropChessSchema
from .. import db


# 全局变量，维护房间id和房间的字典
g_rooms_dict: dict = {}

# 全局变量，维护自增的房间id，从i开始
# 指向最后一个生成的roomid，使用前自增
g_room_id: int = 0


gc_rooms = Blueprint("room", __name__)


@gc_rooms.route("/rooms", methods=["GET"])
@panic()
def room_list():
    data = []
    global g_rooms_dict
    for rid in g_rooms_dict:
        data.append(g_rooms_dict[rid].to_dict())

    resp = {
        "room_list": data
    }
    return success(resp)

# 获取某个房间的信息
@gc_rooms.route("/<int:rid>", methods=["GET"])
@panic()
def room_info(rid):
    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")
    return success(data=room.to_dict())


# 返回棋局状态
'''{
    is_gaming: bool 
    is_end: bool
    #如果is_end为True，则有winner&msg
    winner: 返回获胜方id
    msg: str获胜原因
    
    # 如果is_gaming为True则有chess_board
    chess_board: [][]int
}
'''
@gc_rooms.route("/<int:rid>/status", methods=["GET"])
@panic()
def game_status(rid):
    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")
    resp = {
        "is_gaming": room.isgaming(),
        "is_end": False,
    }

    res = room.is_end()

    if res is not None and res[0] != 0:
        resp["is_end"] = True
        resp["winner"] = room.creator.uid if res[0] == 1 else room.participator.uid
        resp["msg"] = res[1]

    if room.isgaming() == True:
        resp["chess_board"] = room.game_status()

    return success(data=resp)


@gc_rooms.route("/dropchess", methods=["POST"])
@panic(DropChessSchema)
def drop_chess(args):
    rid = args.get("room_id")
    uid = args.get("user_id")
    x = args.get("x")
    y = args.get("y")

    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    u = query_user_id(uid)
    if u is None:
        return error(reason="用户不存在")

    if room.isgaming() == False:
        return error(reason="游戏未开始")

    room.drop(x, y, uid)
    return success()


@gc_rooms.route("/createroom", methods=["POST"])
@panic()
def room_create():
    # 查询用户是否存在

    global g_room_id, g_rooms_dict
    g_room_id += 1
    room = Room(
        rid=g_room_id,
    )
    g_rooms_dict[g_room_id] = room

    return success(data={
        "room_id": g_room_id
    })


@gc_rooms.route("/<int:rid>/startgame", methods=["POST"])
@panic()
def start_game(rid):
    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    # 验证session中的user
    if room.creator is None or room.participator is None:
        return error(reason="人数不够")

    if room.isgaming() == True:
        return error(reason="游戏已开始")
    game = Gobang()
    room.start_game(game)
    return success()


@gc_rooms.route("/joingame", methods=["POST"])
@panic(JoinGameSchema)
def join_game(args):
    rid = args.get("room_id")
    uid = args.get("user_id")

    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    if room.isgaming() == True:
        return error(reason="游戏已开始")

    u = query_user_id(uid)
    if u is None:
        return error(reason="用户不存在")

    if room.is_inroom(uid) == True:
        return error(reason="你已在房间中")

    if room.is_full() == True:
        return error(reason="房间已满")
    room.join_room(u)
    return success()


@gc_rooms.route("/quitgame", methods=["POST"])
@panic(JoinGameSchema)
def quit_game(args):
    rid = args.get("room_id")
    uid = args.get("user_id")

    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    if room.isgaming() == True:
        return error(reason="游戏已开始")

    u = query_user_id(uid)
    if u is None:
        return error(reason="用户不存在")

    if room.is_inroom(uid) == False:
        return error(reason="你不在该房间中")

    room.quit_room(uid)
    return success()

def _get_room_by_id(rid):
    global g_rooms_dict
    if rid not in g_rooms_dict.keys():
        return None

    room = g_rooms_dict[rid]
    return room
