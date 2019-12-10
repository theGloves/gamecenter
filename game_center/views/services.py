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
from ..types import RegistryServiceSchema, RequestServiceSchema

gc_services = Blueprint("service", __name__)


@gc_services.route("/services", methods=["GET"])
@panic()
def services_list():
    s = {"id": 12, "type": "wuziqi"}
    data = {"data": "{}".format(s)}
    return success(data)


@gc_services.route("/service", methods=["POST"])
@panic(RegistryServiceSchema)
def service_registry(args):
    pretty_logger.debug("origin data from post: {}".format(args))

    s = Service(
        name=args.get("service_name"),
        type=args.get("service_type"),
        url=args.get("service_url"),
        desc=args.get("service_desc")
    )

    db.session.add(s)
    db.session.commit()
    return success()


@gc_services.route("/service/<stype>", methods=["POST"])
@panic(RequestServiceSchema)
def service_request(args, stype):
    pretty_logger.debug("request {} service".format(stype))
    pretty_logger.debug("request param: {}".format(args))

    # 调度策略！暂时选取第一个匹配的服务
    s: Service = None
    try:
        s = Service.query.filter().first()
    except Exception as e:
        s = None
        pretty_logger.error("{} service doesn't exist".format(stype))

    if s is None:
        return error(None, "service not exist")

    parser_rsp = requests.post(s.url, json=args.get("server_data")).json()
    if parser_rsp.get("status") != 200:
        return error(None, "call service failed, reason: {}".format(parser_rsp))

    return success(None, "request success. wait for call callback")
