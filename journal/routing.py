
import database
import filters

from flask import render_template

dbs = database.DocumentStore()

def ui_get():
  journals, success = journal_get_all()

  if success:
    return render_template('index.html', journals=journals)

def journal_post(journal):
  results, success = filters.process_journal_tasks(journal)

  print results

  results, success = dbs.StoreJournal(results)

  if success:
    return results, True
  else:
    return {
      'err': 'Unable to index Journal',
      'results': results,
    }, False

def journal_get_all():
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

    return paycheck, True
  else:
    return {
      'err': 'Unable to fetch Journals.',
      'results': results
    }, False

def journal_get_one(journal_id):
  results, success = dbs.FetchJournal(journal_id)

  if success:
    return {
        'data': {
          'journal': results['_source'],
          'id': results['_id']
        }
      }, True
  else:
    return {
      'err': 'Record not found.',
      'id': journal_id
    }, False


