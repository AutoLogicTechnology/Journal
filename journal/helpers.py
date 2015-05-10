
import time

def parse_date_string(date):
  return time.strptime(date, '%Y-%m-%dT%H:%M:%S')

def parse_journal_dates(journals):
  """
  We do this so that we get usable time objects
  in the J2 templates. Makes it easier to display
  nice dates.
  """

  if journals:
    for journal in journals['data']['journals']:
      journal['source']['date'] = parse_date_string(journal['source']['date'])

      for host in journal['source']['hosts']:
        for task in journal['source']['hosts'][host]['tasks']:
          if 'date' in task:
            task['date'] = parse_date_string(task['date'])

