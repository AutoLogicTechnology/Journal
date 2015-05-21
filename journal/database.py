
import elasticsearch as es 

def init_logstore(app):
  return LogStore(app.config)

def init_documentstore(app):
  return DocumentStore(app.config)

class LogStore():
  """A generic class for handling log messages and
  storing them in ElasticSearch.

  Hopefully this class's generic nature mean it can 
  be swapped in and out for better examples.
  """

  def __init__(self, config=None):
    if config and 'JOURNAL' in config:
      self.index = config['JOURNAL']['logging']['index']
    else:
      self.index = 'journal-logs'

    print config

    self.dbs = es.Elasticsearch(hosts=config['JOURNAL']['database']['servers'])

  def LogMessage(self, message):
    """
    Store a message as a document in ElasticSearch 
    """

    log_message = {
      'message': message 
    }

    try: 
      result = self.dbs.index(index=self.index, doc_type='log_message', body=log_message)
    except es.ElasticsearchException as e:
      return {
        'err': e
      }, False

    if result['created']:
      return {
        'created': result['created'],
        'id': result['_id']
      }, True
    else:
      {
        'err': 'Error logging message. No exception was raised'
      }, False

  def RetrieveLogs(self, limit=100):
    try:
      results = self.dbs.search(index=self.index, doc_type="log_message", size=limit)
    except es.ElasticsearchException as e:
      return {
          'err': e.error,
        }, False

    return results, True

class DocumentStore():
  """
  A generic class (which can easily be replaced) used
  for storing documents in ElasticSearch.

  The generic nature will hopefully allow for a more flexible
  system in the future.
  """

  def __init__(self, config=None):
    if config and 'JOURNAL' in config:
      self.index = config['JOURNAL']['database']['index']
    else:
      self.index = 'journal-logs'

    self.dbs = es.Elasticsearch(hosts=config['JOURNAL']['database']['servers'])

  def StoreJournal(self, journal):
    """
    Stores a single Journal in the datastore. 

    Returns a tuple: (results, successful).

    Details: A dictionary containing further information,
    if available.

    Successful: A boolean that is True if successful or
    False otherwise.
    """

    if isinstance(journal, dict):
      try:
        result = self.dbs.index(index=self.index, doc_type='journal', body=journal)
      except es.ElasticsearchException as e:
        return {
          'err': e
        }, False

      if result['created']:
        return {
          'created': result['created'],
          'id': result['_id'],
          'index': result['_index'],
        }, True
      else:
        return {
          'err': 'Unable to index document. No exception was raised.'
        }, False
    else:
      return {
        'err': 'Invalid journal given: is not a dictionary, is a %s' % type(journal)
      }, False

  def FetchJournals(self, limit=10):
    """
    Fetchs ALL or a limited number of the Journals
    from the datastore.

    Returns a tuple: (results, success)
    """
    try:
      results = self.dbs.search(index=self.index, doc_type="journal", size=limit)
    except es.ElasticsearchException as e:
      return {
          'err': e.error,
        }, False

    return results, True

  def FetchJournal(self, journal_id):
    """
    Fetches a single Journal from the datastore.

    Returns a tuple: (result, success)
    """
    if journal_id:
      try:
        results = self.dbs.get(index=self.index, doc_type='journal', id=journal_id)
      except es.ElasticsearchException as e:
        return {
          'err': e.error
        }, False

      return results, True
    else:
      return {
        'err': 'Unable to find a Journal without an id'
      }, False

