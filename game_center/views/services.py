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


gc_services = Blueprint("service", __name__)


@gc_services.route("/services", methods=["GET"])
@panic()
def user():
    s = Service(
        name="service",
        type="wuziqi",
        url="www.baidu.com",
        desc = "descrition"
    )

    db.session.add(s)
    db.session.commit()
    data = {"data": "{}".format(s)}
    return success(data)
