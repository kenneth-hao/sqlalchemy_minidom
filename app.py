# -*- coding: utf-8 -*-
__author__ = 'haoyuewen'

import msg_convert

from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String, CHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

db_config = {
    'host': '192.168.0.55',
    'user': 'haoyw',
    'passwd': 'bjyappam',
    'db': 'cadillac_wechat',
    'charset': 'utf8'
}

convert_config = {
    'domain': 'wechat.cadillac-1.com'
}

engine = create_engine('mysql://%s:%s@%s/%s?charset=%s' %
                       (db_config['user'], db_config['passwd'],
                        db_config['host'], db_config['db'], db_config['charset']),
                       echo=True)

BaseModel = declarative_base()

class OfOffline(BaseModel):
    __tablename__ = 'ofoffline'

    username = Column(String(64), primary_key=True)
    messageID = Column(Integer, primary_key=True)
    creationDate = Column(CHAR, primary_key=True)
    messageSize = Column(Integer, primary_key=True)
    stanza = Column(TEXT, primary_key=True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

query = session.query(OfOffline)

xdc = msg_convert.XmlDomainConvert()

for ofoffline in query:
    print ofoffline.stanza

    stanza_new = xdc.convert(ofoffline.stanza, convert_config['domain'])

    ofoffline.stanza = stanza_new
    # update
    session.merge(ofoffline)

session.flush()
session.commit()
