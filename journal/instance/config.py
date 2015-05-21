DEBUG = True
SECRET_KEY="SIDHUBWVEGFUD82YFVWBCIOQUHDGTVWY3CHJIUDFYGVWX"
JOURNAL = {
  'database': {
    'index': 'journal-data',
    'servers': [
      {
        'server': 'localhost',
        'port': 9200
      },
    ]
  },
  'logging': {
    'index': 'journal-logs',
  }
}
