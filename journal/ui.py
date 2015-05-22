
import json
import routing

from flask import Blueprint, render_template, request

blueprint = Blueprint('journal-ui', __name__)
lgs = None

def init(app):
  lgs = app.config['logging']
  routing.init(app)

@blueprint.route("/", methods=['GET'])
def ui():
  return routing.ui_get_index(), 200

@blueprint.route("/view/<string:journal_id>", methods=['GET'])
def ui_view_id(journal_id):
  return routing.ui_get_view_journal(journal_id), 200

@blueprint.route("/view/system/<string:system_id>/<string:journal_id>", methods=['GET'])
def ui_view_system_id(system_id, journal_id):
  return routing.ui_get_view_system(system_id, journal_id), 200

