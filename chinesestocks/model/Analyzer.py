from __future__ import unicode_literals, absolute_import

from sqlalchemy import Column, Integer, String, Date, Float, Text, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()

class AnaylzerSignals(ModelBase):
    __table__ = 'analyzersignals'
    id = Column('id', Integer, primary_key=True)
    signalType = Column('signaltype', Integer)
    signalDate = Column('signaldate', Date)
    tscode = Column('tscode', String(45))
    algorithmId = Column('algorithmid', Integer)
    binaryLabel = Column('binarylabel', Boolean)
    binaryForcast = Column('binaryForcast', Boolean)
    probabilityLabel = Column('proababilitylabel', Float)
    probabilityForcast = Column('proabailityforcast', Float)
    __table_args__ = {"mysql_charset": "utf8mb4"}
