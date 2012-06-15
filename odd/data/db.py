# -*- coding: utf-8 -*-

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from odd import app

db_engine = create_engine(app.config['DATABASE_URI'],
                          convert_unicode=True,
                          **app.config['DATABASE_CONNECT_OPTIONS'])

db_session = scoped_session(sessionmaker(bind=db_engine, autocommit=True))

Model = declarative_base(name='Model')
# Model.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()    
    Model.metadata.create_all(bind=db_engine)


'''
import logging
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
'''
