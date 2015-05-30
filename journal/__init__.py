
import journal.ui
import journal.api
import journal.filters
import journal.database

from flask import Flask

def create_app(config_file):
  try:
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.config['database'] = database.init_documentstore(app)
    app.config['logging'] = database.init_logstore(app)

    app.register_blueprint(filters.blueprint)
    app.register_blueprint(ui.blueprint)
    app.register_blueprint(api.blueprint)
  except:
    raise

  return app
