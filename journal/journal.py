
import json
import database

from flask import Flask, request

app = Flask(__name__)
dbs = database.DocumentStore()

@app.route("/journal", methods=['GET', 'POST'])
def journal():

  if request.method == 'POST':
    results, success = dbs.StoreJournal(json.loads(request.data))

    if not success:
      return json.dumps(results), 500
    else:
      return json.dumps(results), 201

  # GET handled from here
  results, success = dbs.FetchJournals()

  if success:
    paycheck = {
      'data': {
        'journals': []
      }
    }

    for hit in results['hits']['hits']:
      paycheck['data']['journals'].append({
        'id': hit['_id'],
        'source': hit['_source']
      })

    return json.dumps(paycheck), 200
  else:
    return json.dumps(results), 500

@app.route("/journal/<string:journal_id>", methods=['GET'])
def journal_id(journal_id):
  result, success = dbs.FetchJournal(journal_id)

  if success and journal_id == result['_id']:
    paycheck = {
      'data': {
        'journal': result['_source'],
        'id': result['_id']
      }
    }

    return json.dumps(paycheck), 200
  else:
    paycheck = {
      'err': 'Record not found.',
      'id': journal_id
    }

    return json.dumps(paycheck), 500

if __name__ == "__main__":
  # Is executed directly, we assume debugging mode.
  # If ran via gunicorn, this wouldn't be the case.
  app.run(host='0.0.0.0', port=5000, debug=True)
