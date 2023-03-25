import secrets
from flask import Flask, Blueprint, request, render_template
from flask_socketio import SocketIO
from flask_restful import Api
from flask_cors import CORS
from chatsecure.views import (
    LoginResource,
    UserListResource,
    GroupListResource,
    UserMessageResource,
    GroupMessageResource
)

socketio = SocketIO(cors_allowed_origins="*")
from chatsecure.chatsocket import *


def create_app(debug: bool = False):
    """Create Factory application."""
    app = Flask(__name__)
    app.debug = debug

    # Random secret key
    app.config['SECRET_KEY'] = secrets.token_hex(128)

    # Init restful
    api = Api(app)
    api.add_resource(LoginResource, '/login')
    api.add_resource(UserListResource, '/users')
    api.add_resource(GroupListResource, '/groups')
    api.add_resource(UserMessageResource, '/user_msg/<int:sender_id>')
    api.add_resource(GroupMessageResource, '/group_msg')

    CORS(app)  # FIXME: Check for production

    # init socketio
    socketio.init_app(app)

    return app
