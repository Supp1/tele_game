from flask import Blueprint, request, jsonify, make_response

from app import bot
from app.bot_api.bot_control import trigger_controls

bp = Blueprint('tgbot', __name__, url_prefix='/bot')


@bp.route('/<token>', methods=['POST'])
def handle(token):
    if token == bot.token:
        request_body_dict = request.json
        trigger_controls(request_body_dict)
        response = make_response(jsonify(
            response='OK'
        ), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(jsonify(
            response='OK'
        ), 200)
        response.headers['Content-Type'] = 'application/json'
        return response


@bp.route('/test', methods=['POST, GET'])
def handle2():
    print('EVRYTHING IS FINE')
    response = make_response(jsonify(
        response='OK'
    ), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
