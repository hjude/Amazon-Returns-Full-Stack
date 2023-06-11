from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca":"/etc/ssl/cert.pem"
    } 
  })


def load_queue_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tracking_ids"))
    queue=[]
    for row in result.all():
      queue.append(dict(row))
    return queue

def load_returnDetails_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from return_details"))
    return_details=[]
    for row in result.all():
      return_details.append(dict(row))
    return return_details

def load_tracking_id_to_search():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tracking_id_to_search"))
    trackingID=[]
    for row in result.all():
      trackingID.append(dict(row))
    return trackingID
  