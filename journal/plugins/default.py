
from yapsy.IPlugin import IPlugin

class Default(IPlugin):

  def parse_task(self, task):
    entry = {
      'filter': 'default',
      'is_raw': True,
      'date': task['date'],
      'position': task['position'],
      'module': task['ansible_raw_results']['invocation']['module_name'],
      'module_args': task['ansible_raw_results']['invocation']['module_args'],
      'has_warnings': False,
      'changed': task['ansible_raw_results']['changed'],
      'raw': task['ansible_raw_results']
    }

    if 'warnings' in task['ansible_raw_results']:
      if len(task['ansible_raw_results']['warnings']) >= 1:
        entry['has_warnings'] = True

    return entry, True
