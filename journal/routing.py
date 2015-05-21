
from flask import render_template
import plugins

dbs = None
lgs = None 

def init(app):
  global dbs, lgs
  
  dbs = app.config['db_conn']
  lgs = app.config['logging']

# Views
def ui_get_index():
  journals, success = journal_get_all()

  if success:
    journals['data']['journals'].sort(key=lambda item:item['source']['date'], reverse=True)
    return render_template('index.html', journals=journals)
  else:
    lgs.LogMessage(journals)
    return render_template('index.html', journals=False)

def ui_get_view_system(system_id, journal_id):
  journal, success = journal_get_one(journal_id)

  if success:
    for host in journal['data']['hosts']:
      if host != system_id:
        journals['data']['hosts'].pop(host, None)

    return render_template('view_system.html', journal=journal)
  else:
    lgs.LogMessage(journal)
    return render_template('view.html', journal=False)

def ui_get_view_journal(journal_id):
  journal, success = journal_get_one(journal_id)

  if success:
    return render_template('view.html', journal=journal)
  else:
    lgs.LogMessage(journal)
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
  lgs.LogMessage(results)

  return {
    'err': msg,
    'results': results
  }

def journal_post(journal):
  results, success = plugins.process_journal_tasks(journal)

  if not success:
    return error('Unable to index journal - filter related failure.', results), False

  results, success = dbs.StoreJournal(results)

  if success:
    return results, True
  else:
    return error('Unable to index journal.', results), False

def journal_get_limit(limit=10):
  results, success = dbs.FetchJournals(limit=limit)

  if success:
    return paycheck(results), True
  else:
    return error('Unable to fetch Journals.', results), False

def journal_get_all():
  results, success = dbs.FetchJournals()

  if success:
    return paycheck(results), True
  else:
    return error('Unable to fetch Journals.', results), False

def journal_get_one(journal_id):
  results, success = dbs.FetchJournal(journal_id)

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

    lgs.LogMessage(error) 
    return error, False


