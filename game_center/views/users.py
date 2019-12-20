# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger
from uuid import uuid1


from ..services.props import panic, success, error
from ..models import User
from ..types import RegistryUserSchema, RegistryUserSchema
from .. import db, score


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

@gc_user.route("/score", methods=["GET"])
@panic()
def get_score():
    items = score.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse=True)     

    resp = []

    for i in range(min(10, len(backitems))):
        resp.append({"username": backitems[i][1], "score": backitems[i][0]})
    pretty_logger.debug("{}".format(resp))
    return success(resp)


@gc_user.route("/score", methods=["POST"])
@panic(RegistryUserSchema)
def post_score(args):
    uid = args.get("user_id")
    s = args.get("score")

    if uid not in score.keys():
        score[uid] = s
    else:
        score[uid] = max(int(score[uid]), s)
    pretty_logger.debug("{}".format(score))
    return success()