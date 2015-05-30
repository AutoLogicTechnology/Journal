
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
      'raw': task['ansible_raw_results']
    }

    if 'changed' in task['ansible_raw_results']:
      entry['changed'] = task['ansible_raw_results']['changed']

    if 'warnings' in task['ansible_raw_results']:
      if len(task['ansible_raw_results']['warnings']) >= 1:
        entry['has_warnings'] = True

    return entry, True
