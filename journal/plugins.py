
from yapsy.PluginManager import PluginManager

manager = PluginManager()
manager.setPluginPlaces(["./plugins", "./journal/plugins"])
manager.collectPlugins()

def process_journal_tasks(journal):
  """
  Essentially we're refinding and building a new
  journal. The information will be easier for the
  frontend UI template to work with, not to mention
  generally more readable.
  
  We don't do this at the callback plugin level because
  we want that process to be fast - collect and dump,
  then process later.
  """

  sandbox = {
    'date': journal['date'],
    'user': journal['user'],
    'hosts': {}
  }

  if 'environment' in journal:
    sandbox['environment'] = journal['environment']

  for host in journal['hosts']:
    sandbox['hosts'][host] = {
      'name': journal['hosts'][host]['name'],
      'failed': journal['hosts'][host]['failed'],
      'success': journal['hosts'][host]['success'],
      'tasks': [],
    }

    for task in journal['hosts'][host]['tasks']:
      filter_name = task['ansible_raw_results']['invocation']['module_name']
      results, success = call_plugin(filter_name, task)

      if success:
        sandbox['hosts'][host]['tasks'].append(results)
      else:
        return {
          'err': 'Issue processing tasks for: %s[task][%s]' % (host, filter_name)
        }, False 

  return sandbox, True

def call_plugin(module_name, task):
  plugin = manager.getPluginByName(module_name)

  if plugin:
    return plugin.plugin_object.parse_task(task)

  # Unable to find a plugin, so we use default
  plugin = manager.getPluginByName('default')

  if plugin:
    return plugin.plugin_object.parse_task(task)
  else:
    return {
      'err': 'Unable to load given module_name: %s. Also unable to load default plugin.' % module_name
    }, False
