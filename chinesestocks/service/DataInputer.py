import chinesestocks.database.CnstockDao as stkdao
import chinesestocks.model.Cnstock as stk
import chinesestocks.datareader.TushareReader as tr
import chinesestocks.BasicUtility as util

class DataInputer(object):

    tushareReader = None
    cnstockDb = None
    cnstockMarketDailyDb = None
    cnstockDatesDb = None
    cnstockCompanyDb = None

    def __init__(self):
        self.tushareReader = tr.TushareReader()
        self.cnstockDb = stkdao.CnstockDao()
        self.cnstockMarketDailyDb = stkdao.CnstockMarketDailyDao()
        self.cnstockDatesDb = stkdao.CnstockDatesDao()
        self.cnstockCompanyDb = stkdao.CnstockCompanyDao()

    def inputCnstockBasicAll(self):
        cnstockList = self.tushareReader.readCnstockList()
        self.cnstockDb.addItemList(cnstockList)

    def inputTodayMarketDaily(self):
        today = util.getTodayDateStr()
        list = self.tushareReader.readCnstockMarketDaily(today)
        self.cnstockMarketDailyDb.insertOnedayMarketDaily(list)

    def inputTodayBasicDaily(self):
        today = util.getTodayDateStr()
        list = self.tushareReader.readCnstockBasicdaily(today)
        self.cnstockMarketDailyDb.insertOnedayMarketDaily(list)


    def inputTradeDates(self, year):
        list = self.tushareReader.readTradeCalendar(year)
        self.cnstockDatesDb.insertOneyearDates(list)

    def updateCnstockBasic(self):
        todayList = self.tushareReader.readCnstockList()
        databaseList = self.cnstockDb.getAllCnstock()
        list = []
        for cnstock in todayList:
            exists = False
            for item in databaseList:
                if item.tscode == cnstock.tscode:
                    exists = True
            if not exists:
                list.append(cnstock)
        self.cnstockDb.insertCnstock(list)

    def updateCnstockCompany(self):
        databaseList = self.cnstockCompanyDb.getAllCompany()
        todayListSSE = self.tushareReader.readCnstockSSECompany()
        todayListSZSE = self.tushareReader.readCnstockSZSEompany()
        todayList = todayListSSE + todayListSZSE
        list = []
        print(len(todayList))
        print(len(databaseList))
        for cnstockCompany in todayList:
            exists = False
            for item in databaseList:
                if item.tscode == cnstockCompany.tscode:
                    exists = True
            if not exists:
                print("adding..." + cnstockCompany.tscode)
                list.append(cnstockCompany)
        print(len(list))
        self.cnstockCompanyDb.insertCompanyList(list)

