
import elasticsearch as es 

dbs = es.Elasticsearch()

class DocumentStore():
  """
  A generic class (which can easily be replaced) used
  for storing documents in ElasticSearch.

  The generic nature will hopefully allow for a more flexible
  system in the future.
  """

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
        result = dbs.index(index='journals', doc_type='journal', body=journal)
      except es.ElasticsearchException as e:
        return {
          'err': e,
          'code': None,
          'details': None
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

  def FetchJournals(self, limit=10):
    """
    Fetchs ALL or a limited number of the Journals
    from the datastore.

    Returns a tuple: (results, success)
    """
    try:
      results = dbs.search(index='journals', doc_type="journal", size=limit)
    except es.ElasticsearchException as e:
      return {
          'err': e.error,
          'code': e.status_code,
          'details': e.info
        }, False

    return results, True

  def FetchJournal(self, journal_id):
    """
    Fetches a single Journal from the datastore.

    Returns a tuple: (result, success)
    """
    if journal_id:
      try:
        results = dbs.get(index='journals', doc_type='journal', id=journal_id)
      except es.ElasticsearchException as e:
        return {
          'err': e.error,
          'code': e.status_code,
          'details': e.info
        }, False

      return results, True
    else:
      return {
        'err': 'Unable to find a Journal without an id'
      }, False

