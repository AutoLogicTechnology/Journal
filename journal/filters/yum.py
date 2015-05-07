
import re

from yapsy.IPlugin import IPlugin

class Yum(IPlugin):

  def __init__(self):
    self.installed_reg  = re.compile('[Dependency ]?Installed:\\n[ ]+?(.*)')
    self.updated_reg    = re.compile('Updated:\\n[ ]+?(.*)')
    self.replaced_reg   = re.compile('Replaced:\\n[ ]+?(.*)')
    self.ignored_reg    = re.compile('(.*) providing (.*) is already installed')

  def parse_task(self, task):
    """
    Process the horrible Ansible Yum module output and provide a better
    way of indexing and reading it.
    """

    if task['ansible_raw_results']['invocation']['module_name'] == 'yum':
      entry = {
        'filter': 'yum',
        'is_raw': False,
        'date': task['date'],
        'position': task['position'],
        'yum': {
          'installed': [],
          'replaced': [],
          'updated': [],
          'ignored': [],
        }
      }

      results = task['ansible_raw_results']['results']
      for result in results:

        installed = self.installed_reg.search(result)
        if installed:
          entry['yum']['installed'].append(installed.group(1).strip())
          continue

        updated = self.updated_reg.search(result)
        if updated:
          entry['yum']['updated'].append(updated.group(1).strip())
          continue

        replaced = self.replaced_reg.search(result)
        if replaced:
          entry['yum']['replaced'].append(replaced.group(1).strip())
          continue

        ignored = self.ignored_reg.search(result)
        if ignored:
          entry['yum']['ignored'].append(ignored.group(1).strip())
          continue
    else:
      return {
        'err': 'This task was not a Yum module task.'
      }, False

    return entry, True
