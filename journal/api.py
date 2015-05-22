
import json
import routing

from flask import Blueprint, request

blueprint = Blueprint('journal-api', __name__)
lgs = None

def init(app):
  lgs = app.config['logging']
  routing.init(app)

@blueprint.errorhandler(404)
def return_404(e):
  return {
    'err': 'Page not found.'
  }, 404

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

