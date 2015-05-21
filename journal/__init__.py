
from flask import Flask

def create_app(config_file):
  try:
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    # from database import init_logstore, init_documentstore
    from journal.database import init_logstore, init_documentstore

    app.config['db_conn'] = init_documentstore(app)
    app.config['logging'] = init_logstore(app)

    import journal.application
    import journal.filters

    app.register_blueprint(filters.blueprint)
    app.register_blueprint(application.blueprint)

    application.init(app)
  except:
    raise

  return app
