
from yapsy.IPlugin import IPlugin

class Default(IPlugin):

  def parse_task(self, task):
    entry = {
      'filter': 'default',
      'is_raw': True,
      'date': task['date'],
      'position': task['position'],
      'raw': task['ansible_raw_results']
    }

    return entry, True
