
import jinja2
import flask
import time

blueprint = flask.Blueprint('journal-filters', __name__)

@blueprint.app_template_filter()
@jinja2.contextfilter
def is_list(context, value):
  """
  Allow us to check for lists in our J2 
  templates.
  """

  return isinstance(value, list)

@blueprint.app_template_filter()
@jinja2.contextfilter
def is_dict(context, value):
  """
  Allow us to check for a hash/dict in our
  J2 templates.
  """

  return isinstance(value, dict)

@blueprint.app_template_filter()
@jinja2.contextfilter
def to_human_date(context, value):
  informat = '%Y-%m-%dT%H:%M:%S'
  raw = time.strptime(value, informat)
  return time.strftime('%Y-%m-%d %H:%M:%S', raw)