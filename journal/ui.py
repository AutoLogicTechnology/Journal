
import json
import routing

from werkzeug.local import LocalProxy
from flask import Blueprint, render_template, request, current_app

blueprint = Blueprint('journal-ui', __name__)

logging = LocalProxy(lambda: current_app.config['logging'])

@blueprint.route("/", methods=['GET'])
def ui_index():
  return routing.ui_get_index(), 200

@blueprint.route("/users", methods=['GET'])
def ui_users():
  return routing.ui_get_users(), 200

@blueprint.route("/users/<string:user_id>", methods=['GET'])
def ui_users_id(user_id):
  pass

@blueprint.route("/view/<string:journal_id>", methods=['GET'])
def ui_view_id(journal_id):
  return routing.ui_get_view_journal(journal_id), 200

@blueprint.route("/view/system/<string:system_id>/<string:journal_id>", methods=['GET'])
def ui_view_system_id(system_id, journal_id):
  return routing.ui_get_view_system(system_id, journal_id), 200

