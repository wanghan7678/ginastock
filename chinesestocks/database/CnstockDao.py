from sqlalchemy.sql import func

import chinesestocks.model.Cnstock as stk
import chinesestocks.database.DaoBase as db
import chinesestocks.BasicUtility as util

class CnstockDao(db.DaoBase):

    def insertCnstock(self, cnstockList):
        super().addOneItem(cnstockList)

    def findByTscode(self, tscode):
        session = super().getSession()
        result = session.query(stk.Cnstock).filter(stk.Cnstock.tscode==tscode).all()
        return result

    def checkIfExist(self, tscode):
        session = super().getSession()
        result = session.query(func.count(stk.Cnstock.tscode)).filter(stk.Cnstock.tscode==tscode).scalar()
        return result > 0

    def getAllCnstock(self):
        session = super().getSession()
        result = session.query(stk.Cnstock).all()
        return result

class CnstockMarketDailyDao(db.DaoBase):
    def insertOnedayMarketDaily(self, dataList):
        super().addItemList(dataList)

    def checkIfTradeDayRecords(self, tradeDayStr):
        session = super().getSession()
        result = session.query(func.count(stk.CnstockMarketDaily.tscode)).filter(stk.CnstockMarketDaily.tradeDate==tradeDayStr).scalar()
        if result > 3000:
            return True
        else:
            return False


class CnstockDatesDao(db.DaoBase):

    def insertOneyearDates(self, dataList):
        super().addItemList(dataList)

    def checkIfTradedates(self, dateStr):
        session = super().getSession()
        result = session.query(func.count(stk.CnstockDates.id)).filter(stk.CnstockDates.tradeDate==dateStr).scalar()
        if result>0:
            return True
        else:
            return False

    def getAllTradeDaysBeforeToday(self):
        session = super().getSession()
        today = util.getTodayDateStr()
        todayDate = util.createDateFromGina(today)
        result = session.query(stk.CnstockDates).filter(stk.CnstockDates.tradeDate < todayDate).all()
        return result

class CnstockCompanyDao(db.DaoBase):

    def insertCompanyList(self, dataList):
        super().addItemList(dataList)


    def getAllCompany(self):
        session = super().getSession()
        result = session.query(stk.CnstockCompany).all()
        return result