# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger
from uuid import uuid1


from ..services.props import panic, success, error
from ..models import User
from ..types import RegistryUserSchema
from .. import db


gc_user = Blueprint("user", __name__)


@gc_user.route("/register", methods=["POST"])
@panic(RegistryUserSchema)
def registry(args):
    username = args.get("username")

    u_list = User.query.filter(User.username == username).all()
    if u_list is not None and len(u_list) > 0:
        return error(reason="username already used")

    u = User(
        uid=username,
        username=username
    )
    db.session.add(u)
    db.session.commit()
    resp = {
        "uid": u.username
    }
    return success(resp)


@gc_user.route("/login", methods=["GET"])
@panic(RegistryUserSchema)
def login(args):
    username = args.get("username")
    u: User = None
    try:
        u = User.query.filter(User.username == username).one_or_none()
    except Exception:
        u = None
    if u is None:
        return error(reason="该用户不存在")
    return success({"uid": u.uid})
