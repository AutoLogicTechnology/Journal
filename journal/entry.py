
import json
import routing
import filters

from flask import Flask, request

app = Flask(__name__)
app.config.from_object('configuration.Debugging')
app.register_blueprint(filters.blueprint)

# UI:
@app.route("/", methods=['GET'])
def ui():
  return routing.ui_get_index(), 200

@app.route("/view/<string:journal_id>", methods=['GET'])
def ui_view_id(journal_id):
  return routing.ui_get_view_journal(journal_id), 200

@app.route("/view/system/<string:system_id>/<string:journal_id>", methods=['GET'])
def ui_view_system_id(system_id, journal_id):
  return routing.ui_get_view_system(system_id, journal_id), 200

@app.route("/<int:start>/<int:finish>", methods=['GET'])
def ui_range(start, finish):
  pass

# API:
@app.route("/journal", methods=['GET', 'POST'])
def journal():
  if request.method == 'POST':
    results, success = routing.journal_post(json.loads(request.data))

    if not success:
      return json.dumps(results), 500
    else:
      return json.dumps(results), 201

  if request.method == 'GET':
    results, success = routing.journal_get_all()

    if success:
      return json.dumps(results), 200
    else:
      return json.dumps(results), 500

@app.route("/journal/<string:journal_id>", methods=['GET'])
def journal_id(journal_id):
  results, success = routing.journal_get_one(journal_id)

  if success:
    return json.dumps(results), 200
  else:
    return json.dumps(results), 404
