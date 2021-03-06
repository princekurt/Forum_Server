# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

DBNAME = "forum"


def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  return c.fetchall()
  db.close

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  output = bleach.clean(content)
  c.execute("insert into posts values (%s)", (output,))
  db.commit()
  db.close()


