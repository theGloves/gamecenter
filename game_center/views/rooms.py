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
from ..types import CreateRoomSchema
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


@gc_rooms.route("/<int:rid>/status", methods=["GET"])
@panic()
def game_status(rid):
    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    if room.isgaming() == False:
        return success()
    return success(data=room.game_status())


@gc_rooms.route("/createroom", methods=["POST"])
@panic(CreateRoomSchema)
def room_create(args):
    # 查询用户是否存在
    uid = args.get("creator_id")

    creator = query_user_id(uid)
    if creator is None:
        return error(reason="创建者不存在")

    global g_room_id, g_rooms_dict
    g_room_id += 1
    room = Room(
        rid=g_room_id,
        creator=creator
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
@panic()
def join_game(rid):
    room = _get_room_by_id(rid)
    if room is None:
        return error(reason="房间不存在")

    if room.creator is None or room.participator is None:
        return error(reason="人数不够")

    if room.isgaming() == True:
        return error(reason="游戏已开始")
    game = Gobang()
    room.start_game(game)
    return success()


def _get_room_by_id(rid):
    global g_rooms_dict
    if rid not in g_rooms_dict.keys():
        return None

    room = g_rooms_dict[rid]
    return room
