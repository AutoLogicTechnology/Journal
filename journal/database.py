
"""
Example output/POST-data from journal-callback:

{
    "date":"2015-05-22T20:50:55",
    "environment":{
        "HOME":"/root",
        "LANG":"en_US.UTF-8",
        "LC_CTYPE":"en_US.UTF-8",
        "LOGNAME":"root",
        "MAIL":"/var/mail/vagrant",
        "PATH":"/sbin:/bin:/usr/sbin:/usr/bin",
        "PWD":"/home/vagrant",
        "SHELL":"/bin/bash",
        "SHLVL":"1",
        "SUDO_COMMAND":"/bin/sh -c echo BECOME-SUCCESS-ccjeavulhdpobdhmtvcbratkeyzhbedh; LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 /usr/bin/python /home/vagrant/.ansible/tmp/ansible-tmp-1432291855.39-225077294988208/setup; rm -rf /home/vagrant/.ansible/tmp/ansible-tmp-1432291855.39-225077294988208/ >/dev/null 2>&1",
        "SUDO_GID":"500",
        "SUDO_UID":"500",
        "SUDO_USER":"vagrant",
        "TERM":"xterm-256color",
        "USER":"root",
        "USERNAME":"root",
        "_":"/usr/bin/python"
    },
    "hosts":{
        "sandbox":{
            "failed":0,
            "name":"sandbox",
            "success":9,
            "tasks":[
                {
                    "ansible_raw_results":{
                        "changed":true,
                        "invocation":{
                            "module_args":"",
                            "module_name":"yum"
                        },
                        "item":"wget,tcpdump,nc",
                        "msg":"",
                        "rc":0,
                        "results":[
                            "wget-1.12-5.el6_6.1.x86_64 providing wget is already installed",
                            "tcpdump-4.0.0-3.20090921gitdf3cb4.2.el6.x86_64 providing tcpdump is already installed",
                            "Loaded plugins: fastestmirror\nSetting up Install Process\nLoading mirror speeds from cached hostfile\n * base: centos.mirror.crucial.com.au\n * extras: centos.mirror.crucial.com.au\n * updates: centos.mirror.crucial.com.au\nResolving Dependencies\n--> Running transaction check\n---> Package nc.x86_64 0:1.84-22.el6 will be installed\n--> Finished Dependency Resolution\n\nDependencies Resolved\n\n================================================================================\n Package       Arch              Version                  Repository       Size\n================================================================================\nInstalling:\n nc            x86_64            1.84-22.el6              base             57 k\n\nTransaction Summary\n================================================================================\nInstall       1 Package(s)\n\nTotal download size: 57 k\nInstalled size: 109 k\nDownloading Packages:\nRunning rpm_check_debug\nRunning Transaction Test\nTransaction Test Succeeded\nRunning Transaction\n\r  Installing : nc-1.84-22.el6.x86_64                                        1/1 \n\r  Verifying  : nc-1.84-22.el6.x86_64                                        1/1 \n\nInstalled:\n  nc.x86_64 0:1.84-22.el6                                                       \n\nComplete!\n"
                        ]
                    },
                    "date":"2015-05-22T20:51:04",
                    "position":1
                },
                {
                    "ansible_raw_results":{
                        "changed":true,
                        "invocation":{
                            "module_args":"",
                            "module_name":"yum"
                        },
                        "msg":"",
                        "rc":0,
                        "results":[
                            "Loaded plugins: fastestmirror\nSetting up Remove Process\nResolving Dependencies\n--> Running transaction check\n---> Package nc.x86_64 0:1.84-22.el6 will be erased\n--> Finished Dependency Resolution\n\nDependencies Resolved\n\n================================================================================\n Package       Arch              Version                 Repository        Size\n================================================================================\nRemoving:\n nc            x86_64            1.84-22.el6             @base            109 k\n\nTransaction Summary\n================================================================================\nRemove        1 Package(s)\n\nInstalled size: 109 k\nDownloading Packages:\nRunning rpm_check_debug\nRunning Transaction Test\nTransaction Test Succeeded\nRunning Transaction\n\r  Erasing    : nc-1.84-22.el6.x86_64                                        1/1 \n\r  Verifying  : nc-1.84-22.el6.x86_64                                        1/1 \n\nRemoved:\n  nc.x86_64 0:1.84-22.el6                                                       \n\nComplete!\n"
                        ]
                    },
                    "date":"2015-05-22T20:51:06",
                    "position":2
                },
                {
                    "ansible_raw_results":{
                        "changed":false,
                        "gid":501,
                        "invocation":{
                            "module_args":"",
                            "module_name":"group"
                        },
                        "name":"superusers",
                        "state":"present",
                        "system":false
                    },
                    "date":"2015-05-22T20:51:06",
                    "position":3
                },
                {
                    "ansible_raw_results":{
                        "append":false,
                        "changed":false,
                        "comment":"",
                        "group":502,
                        "groups":"superusers",
                        "home":"/home/michaelc",
                        "invocation":{
                            "module_args":"",
                            "module_name":"user"
                        },
                        "item":"michaelc",
                        "move_home":false,
                        "name":"michaelc",
                        "shell":"/bin/bash",
                        "state":"present",
                        "uid":501
                    },
                    "date":"2015-05-22T20:51:06",
                    "position":4
                },
                {
                    "ansible_raw_results":{
                        "append":false,
                        "changed":false,
                        "comment":"",
                        "group":503,
                        "groups":"superusers",
                        "home":"/home/michelled",
                        "invocation":{
                            "module_args":"",
                            "module_name":"user"
                        },
                        "item":"michelled",
                        "move_home":false,
                        "name":"michelled",
                        "shell":"/bin/bash",
                        "state":"present",
                        "uid":502
                    },
                    "date":"2015-05-22T20:51:06",
                    "position":5
                },
                {
                    "ansible_raw_results":{
                        "append":false,
                        "changed":false,
                        "comment":"",
                        "group":504,
                        "groups":"superusers",
                        "home":"/home/obamab",
                        "invocation":{
                            "module_args":"",
                            "module_name":"user"
                        },
                        "item":"obamab",
                        "move_home":false,
                        "name":"obamab",
                        "shell":"/bin/bash",
                        "state":"present",
                        "uid":503
                    },
                    "date":"2015-05-22T20:51:06",
                    "position":6
                },
                {
                    "ansible_raw_results":{
                        "append":false,
                        "changed":false,
                        "comment":"",
                        "group":505,
                        "groups":"superusers",
                        "home":"/home/barryb",
                        "invocation":{
                            "module_args":"",
                            "module_name":"user"
                        },
                        "item":"barryb",
                        "move_home":false,
                        "name":"barryb",
                        "shell":"/bin/bash",
                        "state":"present",
                        "uid":504
                    },
                    "date":"2015-05-22T20:51:07",
                    "position":7
                },
                {
                    "ansible_raw_results":{
                        "append":false,
                        "changed":false,
                        "comment":"",
                        "group":506,
                        "groups":"superusers",
                        "home":"/home/user01",
                        "invocation":{
                            "module_args":"",
                            "module_name":"user"
                        },
                        "item":"user01",
                        "move_home":false,
                        "name":"user01",
                        "shell":"/bin/bash",
                        "state":"present",
                        "uid":505
                    },
                    "date":"2015-05-22T20:51:07",
                    "position":8
                },
                {
                    "ansible_raw_results":{
                        "changed":true,
                        "cmd":[
                            "rpm",
                            "-qa",
                            "wget"
                        ],
                        "delta":"0:00:00.207260",
                        "end":"2015-05-22 11:51:07.077666",
                        "invocation":{
                            "module_args":"rpm -qa wget",
                            "module_name":"command"
                        },
                        "rc":0,
                        "start":"2015-05-22 11:51:06.870406",
                        "stderr":"",
                        "stdout":"wget-1.12-5.el6_6.1.x86_64",
                        "warnings":[
                            "Consider using yum module rather than running rpm"
                        ]
                    },
                    "date":"2015-05-22T20:51:07",
                    "position":9
                }
            ]
        }
    },
    "user":"michaelc"
}
"""

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

  def FetchJournals(self, limit=10, user=None):
    """
    Fetchs ALL or a limited number of the Journals
    from the datastore.

    Returns a tuple: (results, success)
    """
    try:
      if not user:
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
