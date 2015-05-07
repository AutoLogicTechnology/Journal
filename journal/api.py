
import json
import routing

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def ui():
  return routing.ui_get(), 200

@app.route("/<int:start>/<int:finish>", methods=['GET'])
def ui_range(start, finish):
  pass

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
