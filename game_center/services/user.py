# -*- coding:utf-8 -*-
import requests
import json
import traceback
from flask import Blueprint, request, current_app, Response, make_response, copy_current_request_context
from pretty_logging import pretty_logger


from ..models import User

def query_user_id(uid):
    if uid is None or uid == "":
        return None
    u: User = None
    pretty_logger.debug("query uid: {}".format(uid))
    try:
        u = User.query.filter(User.uid == uid).one_or_none()
    except Exception:
        pretty_logger.debug("{}".format(traceback.print_exc()))
        u = None

    return u
