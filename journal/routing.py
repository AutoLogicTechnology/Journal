
from werkzeug.local import LocalProxy
from flask import render_template, current_app

import plugins
import helpers

database = LocalProxy(lambda: current_app.config['database'])
logging = LocalProxy(lambda: current_app.config['logging'])

# Views
def ui_get_index():
  journals, success = journal_get_all()

  if success:
    journals['data']['journals'].sort(key=lambda item:item['source']['date'], reverse=True)
    sys_stats = helpers.system_stats(journals['data']['journals'])

    print sys_stats

    return render_template('index.html', journals=journals, stats=sys_stats)
  else:
    logging.LogMessage(journals)
    return render_template('index.html', journals=False)

def ui_get_users():
  journals, success = journal_get_all()

def ui_get_view_system(system_id, journal_id):
  journal, success = journal_get_one(journal_id)

  if success:
    for host in journal['data']['hosts']:
      if host != system_id:
        journals['data']['hosts'].pop(host, None)

    return render_template('view_system.html', journal=journal)
  else:
    logging.LogMessage(journal)
    return render_template('view.html', journal=False)

def ui_get_view_journal(journal_id):
  journal, success = journal_get_one(journal_id)

  if success:
    return render_template('view.html', journal=journal)
  else:
    logging.LogMessage(journal)
    return render_template('view.html', journal=False)


# Data
def paycheck(results):
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

  return paycheck

def error(msg, results):
  logging.LogMessage(results)

  return {
    'err': msg,
    'results': results
  }

def journal_post(journal):
  results, success = plugins.process_journal_tasks(journal)

  if not success:
    return error('Unable to index journal - filter related failure.', results), False

  results, success = database.StoreJournal(results)

  if success:
    return results, True
  else:
    return error('Unable to index journal.', results), False

def journal_get_limit(limit=10):
  results, success = database.FetchJournals(limit=limit)

  if success:
    return paycheck(results), True
  else:
    return error('Unable to fetch Journals.', results), False

def journal_get_all():
  results, success = database.FetchJournals()

  if success:
    return paycheck(results), True
  else:
    return error('Unable to fetch Journals.', results), False

def journal_get_one(journal_id):
  results, success = database.FetchJournal(journal_id)

  if success:
    return {
        'data': results['_source'],
        'id': results['_id']
      }, True
  else:
    error = {
      'err': 'Record not found.',
      'id': journal_id
    }

    logging.LogMessage(error) 
    return error, False


