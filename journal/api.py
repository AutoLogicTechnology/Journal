
import json
import routing

from werkzeug.local import LocalProxy
from flask import Blueprint, request, current_app

blueprint = Blueprint('journal-api', __name__)

logging = LocalProxy(lambda: current_app.config['logging'])


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
      logging.LogMessage(results)
      return json.dumps(results), 201

  if request.method == 'GET':
    results, success = routing.journal_get_all()

    if success:
      return json.dumps(results), 200
    else:
      logging.LogMessage(results)
      return json.dumps(results), 500

@blueprint.route("/api/journal/<string:journal_id>", methods=['GET'])
def journal_id(journal_id):
  results, success = routing.journal_get_one(journal_id)

  if success:
    return json.dumps(results), 200
  else:
    logging.LogMessage(results)
    return json.dumps(results), 404

@blueprint.route("/api/logs", methods=['GET'])
def logs():
  results, success = logging.RetrieveLogs()

  if success:
    return json.dumps(results), 200
  else:
    logs.LogMessage(results)
    return json.dumps(results), 404

