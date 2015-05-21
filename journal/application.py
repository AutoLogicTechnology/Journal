
import sys
import json
import routing

from flask import Blueprint, render_template, request

blueprint = Blueprint('journal', __name__)
lgs = None

def init(app):
  lgs = app.config['logging']
  routing.init(app)

# Error handling
@blueprint.errorhandler(404)
def return_404(e):
  return {
    'err': 'Page not found.'
  }, 404

# @blueprint.errorhandler(500)
# def return_500(e):
#   return {
#     'err': 'Internal server error.'
#   }, 500

# UI:
@blueprint.route("/", methods=['GET'])
def ui():
  return routing.ui_get_index(), 200

@blueprint.route("/view/<string:journal_id>", methods=['GET'])
def ui_view_id(journal_id):
  return routing.ui_get_view_journal(journal_id), 200

@blueprint.route("/view/system/<string:system_id>/<string:journal_id>", methods=['GET'])
def ui_view_system_id(system_id, journal_id):
  return routing.ui_get_view_system(system_id, journal_id), 200

# API:
@blueprint.route("/api/journal", methods=['GET', 'POST'])
def journal():
  if request.method == 'POST':
    results, success = routing.journal_post(json.loads(request.data))

    if not success:
      return json.dumps(results), 500
    else:
      lgs.LogMessage(results)
      return json.dumps(results), 201

  if request.method == 'GET':
    results, success = routing.journal_get_all()

    if success:
      return json.dumps(results), 200
    else:
      lgs.LogMessage(results)
      return json.dumps(results), 500

@blueprint.route("/api/journal/<string:journal_id>", methods=['GET'])
def journal_id(journal_id):
  results, success = routing.journal_get_one(journal_id)

  if success:
    return json.dumps(results), 200
  else:
    lgs.LogMessage(results)
    return json.dumps(results), 404

@blueprint.route("/api/logs", methods=['GET'])
def logs():
  results, success = lgs.RetrieveLogs()

  if success:
    return json.dumps(results), 200
  else:
    logs.LogMessage(results)
    return json.dumps(results), 404

