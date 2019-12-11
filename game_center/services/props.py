# -*- coding:utf-8 -*-


from flask import request, g
from flask import jsonify
import functools
import traceback
from webargs.flaskparser import FlaskParser


from pretty_logging import pretty_logger


# def panic():
#     """异常"""
#     def outter(func):
#         run_func = func

#         @functools.wraps(func)
#         def warpper(*args, **kwargs):
#             try:
#                 return run_func(*args, **kwargs)
#             except Exception as e:
#                 traceback.print_exc()
#                 return error(reason="{}".format(e))
#         return warpper
#     return outter


class ValidateException(Exception):
    pass


parser = FlaskParser()


def panic(schema=None):
    """异常"""
    def outter(func):
        if schema:
            @parser.use_args(schema)
            def run_func(*args, **kwargs):
                return func(*args, **kwargs)
        else:
            run_func = func

        @functools.wraps(func)
        def warpper(*args, **kwargs):
            try:
                return run_func(*args, **kwargs)
            except ValidateException as e:
                return error(reason="{}".format(e))
            except Exception as e:
                traceback.print_exc()
                return error(reason="{}".format(e))
        return warpper
    return outter


def success(data: dict = None, msg: str = None):
    s = {
        "code": 200,
        "msg": msg,
        "data": data if data is not None else None
    }
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
