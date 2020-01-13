import chinesestocks.database.CnstockDao as stkdao
import chinesestocks.model.Cnstock as stk
import chinesestocks.datareader.TushareReader as tr
import chinesestocks.BasicUtility as util

class InitSetting(object):

    tushareReader = None
    cnstockDb = None
    cnstockMarketDailyDb = None
    cnStockDatesDb = None

    def __init__(self):
        self.tushareReader = tr.TushareReader()
        self.cnstockDb = stkdao.CnstockDao()
        self.cnstockMarketDailyDb = stkdao.CnstockMarketDailyDao()
        self.cnStockDatesDb = stkdao.CnstockDatesDao()

    def setCnstockBasicAll(self):
        cnstockList = self.tushareReader.readCnstockList()
        self.cnstockDb.addItemList(cnstockList)

    def insertTodayMarketDaily(self):
        today = util.getTodayDateStr()
        list = self.tushareReader.readCnstockMarketDaily(today)
        self.cnstockMarketDailyDb.insertOnedayMarketDaily(list)



    def insertTradeDates(self, year):
        list = self.tushareReader.readTradeCalendar(year)
        self.cnStockDatesDb.insertOneyearDates(list)
