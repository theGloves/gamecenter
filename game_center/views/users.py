# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger
from uuid import uuid1


from ..services.props import panic, success, error
from ..models import User
from .. import db


gc_user = Blueprint("user", __name__)


@gc_user.route("/users", methods=["GET"])
@panic()
def user():

    u = User(
        uid=str(uuid1()),
        username="test"
    )

    db.session.add(u)
    db.session.commit()
    data = {"id": "1", "msg": "test"}
    return success(data)
