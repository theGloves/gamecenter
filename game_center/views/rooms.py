# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger
from uuid import uuid1


from ..services.props import panic, success, error
from ..models import Service
from .. import db


rooms_dict = {}
rid: int = 0
gc_rooms = Blueprint("room", __name__)


class Room():
    rid: int = 0
    users: list = []

    def __init__(self, rid):
        self.rid = rid

    def to_dict(self):
        return {
            "rid": self.rid,
            "players": [u.to_dict() for u in self.users]
        }


@gc_rooms.route("/rooms", methods=["GET"])
@panic()
def room_list():
    data = []
    global rooms_dict
    for id in rooms_dict:
        data.append(rooms_dict[id].to_dict())

    resp = {

        "room_list": data
    }
    return success({"data": resp})


@gc_rooms.route("/room", methods=["POST"])
@panic()
def room_create():
    global rid, rooms_dict
    rid += 1
    room = Room(
        rid=rid
    )
    rooms_dict[rid] = room

    data = {
        "id": rid
    }

    return success(data=data)


@gc_rooms.route("/room/<rid>/<uid>", methods=["POST"])
@panic()
def room_join(rid, uid):
    global rid, rooms_dict
    rid += 1
    room = Room(
        rid=rid
    )
    rooms_dict[rid] = room

    data = {
        "id": rid
    }

    return success(data=data)
