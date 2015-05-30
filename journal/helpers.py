
def system_stats(journals):
  stats = {}

  for journal in journals:
    for host in journal['source']['hosts']:
      target = journal['source']['hosts'][host]

      if host in stats:
        stats[host]['hits'] += target['success'] 
      else:
        stats[host] = {
          'name': host,
          'hits': target['success']
        }

  return stats
