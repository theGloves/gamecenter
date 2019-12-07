# -*- coding:utf-8 -*-


from flask import request, g
from flask import jsonify
import functools
import traceback
from pretty_logging import pretty_logger


def panic():
    """异常"""
    def outter(func):
        run_func = func

        @functools.wraps(func)
        def warpper(*args, **kwargs):
            try:
                return run_func(*args, **kwargs)
            except Exception as e:
                traceback.print_exc()
                return error(reason="{}".format(e))
        return warpper
    return outter


def success(data: dict = None, msg: str = None):
    s = {
        "code": 200,
        "msg": msg,
    }
    if data:
        s.update(data)
    return jsonify(s)


def error(data: dict = None, reason: str = None, code: int = None):
    s = {
        "code": 500,
        "msg": reason
    }
    if not code is None:
        s.update({"code": code})
    if data:
        s.update(data)
    return jsonify(s)
