from __future__ import unicode_literals, absolute_import

from sqlalchemy import Column, Integer, String, Date, Float, Text, BigInteger
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()

class Cnstock(ModelBase):
    __tablename__ = 'cnstock'
    id = Column('id', Integer, primary_key=True)
    tscode = Column('tscode', String(length=45))
    name = Column('name', String(length=45))
    area = Column('area', String(length=45))
    industry = Column('industry', String(length=45))
    enname = Column('enname', String(length=200))
    market = Column('market', String(length=45))
    exchange = Column('exchange', String(length=45))
    listStatus = Column('liststatus', String(length=45))
    listDate = Column('listdate', Date)
    isHs = Column('ishs', String(length=45))
    __table_args__ = {"mysql_charset":"utf8mb4"}


class CnstockCompany(ModelBase):
    __tablename__ = 'cnstockcompany'
    id = Column('id', Integer, primary_key=True)
    tscode = Column('tscode', String(length=45))
    exchange = Column('exchange', String(length=45))
    chairman = Column('chairman', String(length=45))
    manager = Column('manager', String(length=45))
    secretary = Column('secretary', String(length=45))
    regCapital = Column('recaptial', String(length=45))
    setupDate = Column('setupdate', Date)
    province = Column('province', String(length=45))
    city = Column('city', String(length=45))
    introduction = Column('introduction', Text)
    website = Column('website', String(length=200))
    email = Column('email', String(length=45))
    office = Column('office', String(length=200))
    employees = Column('employee', Integer)
    mainBusiness = Column('mainbuisness', Text)
    businessScope = Column('businessscope', Text)
    lastUpdate = Column('lastupdate', Date)
    status = Column('status', String(length=45))
    __table_args__ = {"mysql_charset": "utf8mb4"}

class CnstockDates(ModelBase):
    __tablename__ = 'cnstockdates'
    id = Column('id', Integer, primary_key=True)
    tradeDate = Column('tradedate', Date)
    exchange = Column('exchange', String(length=45))
    __table_args__ = {"mysql_charset": "utf8mb4"}

class CnstockBasicDaily(ModelBase):
    __tablename__ = 'cnstockbasicdaily'
    id = Column('id', BigInteger, primary_key=True)
    tscode = Column('tscode', String(45))
    tradeDate = Column('tradedate', Date)
    closePrice = Column('closeprice', Float)
    turnoverRate = Column('turnoverrate', Float)
    turnoverRateFree = Column('turnoverratefree', Float)
    volumeRatio = Column('volumeratio', Float)
    pe = Column('pe', Float)
    pettm = Column('pettm', Float)
    pb = Column('pb', Float)
    ps = Column('ps', Float)
    psttm = Column('psttm', Float)
    dvRatio = Column('dvratio', Float)
    dvttm = Column('dvttm', Float)
    totalShare = Column('totalshare', Float)
    floatShare = Column('floatshare', Float)
    freeShare = Column('freeshare', Float)
    totalMv = Column('totalmv', Float)
    circMv = Column('circmv', Float)
    __table_args__ = {"mysql_charset": "utf8mb4"}

class CnstockMarketDaily(ModelBase):
    __tablename__ = 'cnstockmarketdaily'
    id = Column('id', BigInteger, primary_key=True)
    tradeDate = Column('tradedate', String(45))
    tscode = Column('tscode', String(45))
    openPrice = Column('openprice', Float)
    highPrice = Column('highprice', Float)
    lowPrice = Column('lowprice', Float)
    closePrice = Column('closeprice', Float)
    preclosePrice = Column('precloseprice', Float)
    change = Column('change', Float)
    changeRate = Column('changerate', Float)
    vol = Column('vol', Float)
    amount = Column('amount', Float)
    __table_args__ = {"mysql_charset": "utf8mb4"}



