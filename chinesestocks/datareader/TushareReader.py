import tushare as tu

import chinesestocks.model.Cnstock as stk
import chinesestocks.Configuration as cfg
import chinesestocks.BasicUtility as util


class TushareReader(object):
    pro = None
    def __init__(self):
        token = cfg.CONSTANT.Tushare_Token
        tu.set_token(token)
        self.pro = tu.pro_api()

    def readCnstockList(self):
        data = self.pro.stock_basic(exchange='', list_status='L',
                               fields='ts_code, name, area, industry, enname, market, exchange, list_status, list_date, is_hs')
        if data.empty:
            print("stock basic list is empty.  tushare.")
        list = []
        for i in range(0, len(data)):
            item = stk.Cnstock()
            item.tscode = data.iat[i, 0]
            item.name = data.iat[i, 1]
            item.area = data.iat[i, 2]
            item.industry = data.iat[i, 3]
            item.enname = data.iat[i, 4]
            item.market = data.iat[i, 5]
            item.exchange = data.iat[i, 6]
            item.listStatus = data.iat[i, 7]
            item.listDate = util.dateTushareToGina(data.iat[i, 8])
            item.isHs = data.iat[i, 9]
            list.append(item)
        return list

    def readCnstockSSECompany(self):
        data = self.pro.stock_company(exchange='SSE',
                                 fields='ts_code, exchange, chairman, manager, secretary, reg_capital, setup_date, province, city, introduction, '
                                        'website, email, office, employees, main_business, business_scope')
        if data.empty:
            print("company list for SSEis empty.  tushare")
        list = []
        for i in range(0, len(data)):
            item = stk.CnstockCompany()
            item.tscode = data.iat[i, 0]
            item.exchange = data.iat[i, 1]
            item.chairman = data.iat[i, 2]
            item.manager = data.iat[i, 3]
            item.secretary = data.iat[i, 4]
            item.regCapital = data.iat[i, 5]
            item.setupDate = util.dateTushareToGina(data.iat[i, 6])
            item.province = data.iat[i, 7]
            item.city = data.iat[i, 8]
            item.introduction = data.iat[i, 9]
            item.website = data.iat[i, 10]
            item.email = data.iat[i, 11]
            item.office = data.iat[i, 12]
            # it is an problem of tushare https://github.com/waditu/tushare/issues/1111
            item.employees = util.toInt(data.iat[i, 14])
            item.mainBusiness = data.iat[i, 13]
            item.businessScope = data.iat[i, 15]
            list.append(item)
        return list

    def readCnstockSZSEompany(self):
        data = self.pro.stock_company(exchange='SZSE',
                                      fields='ts_code, exchange, chairman, manager, secretary, reg_capital, setup_date, province, city, introduction, '
                                             'website, email, office, employees, main_business, business_scope')
        if data.empty:
            print("company list for SSEis empty.  tushare")
        list = []
        for i in range(0, len(data)):
            item = stk.CnstockCompany()
            item.tscode = data.iat[i, 0]
            item.exchange = data.iat[i, 1]
            item.chairman = data.iat[i, 2]
            item.manager = data.iat[i, 3]
            item.secretary = data.iat[i, 4]
            item.regCapital = data.iat[i, 5]
            item.setupDate = util.dateTushareToGina(data.iat[i, 6])
            item.province = data.iat[i, 7]
            item.city = data.iat[i, 8]
            item.introduction = data.iat[i, 9]
            item.website = data.iat[i, 10]
            item.email = data.iat[i, 11]
            item.office = data.iat[i, 12]
            # it is an problem of tushare https://github.com/waditu/tushare/issues/1111
            item.employees = util.toInt(data.iat[i, 14])
            item.mainBusiness = data.iat[i, 13]
            item.businessScope = data.iat[i, 15]
            list.append(item)
        return list

    def readTradeCalendar(self, year):
        start = year + '0101'
        end = year + '1231'
        data = self.pro.trade_cal(exchange='',start_date=start, end_date=end)
        if data.empty:
            print("this year trading calendar is not available: " + year)
        list = []
        for i in range(0, len(data)):
            isOpen = util.toInt(data.iat[i,2])
            if isOpen==1:
                item = stk.CnstockDates()
                item.tradeDate = util.createDateFromTushare(data.iat[i,1])
                item.exchange = 'SSE'
                list.append(item)
        return list

    def readCnstockMarketDaily(self, tradeDate):
        data = self.pro.daily(trade_date=tradeDate)
        if data.empty:
            print("today's market daily is empty: " + tradeDate)
        list = []
        for i in range(0, len(data)):
            item = stk.CnstockMarketDaily()
            item.tscode = data.iat[i,0]
            item.tradeDate = util.dateTushareToGina(data.iat[i,1])
            item.openPrice = util.toFloat(data.iat[i,2])
            item.highPrice = util.toFloat(data.iat[i,3])
            item.lowPrice = util.toFloat(data.iat[i,4])
            item.closePrice = util.toFloat(data.iat[i,5])
            item.preclosePrice = util.toFloat(data.iat[i,6])
            item.change = util.toFloat(data.iat[i,7])
            item.changeRate = util.toFloat(data.iat[i,8])
            item.vol = util.toFloat(data.iat[i,9])
            item.amount = util.toFloat(data.iat[i,10])
            list.append(item)
        return list

    def readCnstockBasicdaily(self, tradeDate):
        data = self.pro.daily_basic(ts_code='', trade_date=tradeDate,
                                    fields='ts_code, trade_date, close, turnover_rate, turnover_rate_f, volume_ratio,'
                                           'pe, pe_ttm, pb, ps, ps_ttm, dv_ratio, dv_ttm, total_share, '
                                           'float_share, free_share, total_mv, circ_mv')
        if data.empty:
            print("today's daily basic is empty: " + tradeDate)
            list = []
        for i in range(0, len(data)):
            item = stk.CnstockBasicDaily()
            item.tscode = data.iat[i,0]
            item.tradeDate = data.iat[i,1]
            item.closePrice = data.iat[i,2]
            item.turnoverRate = data.iat[i,3]
            item.turnoverRateFree = data.iat[i,4]
            item.volumeRatio = data.iat[i,5]
            item.pe = data.iat[i,6]
            item.pettm = data.iat[i,7]
            item.pb = data.iat[i,8]
            item.ps = data.iat[i,9]
            item.psttm = data.iat[i,10]
            item.dvRatio = data.iat[i,11]
            item.dvttm = data.iat[i,12]
            item.totalShare = data.iat[i,13]
            item.floatShare = data.iat[i,14]
            item.freeShare = data.iat[i,15]
            item.totalMv = data.iat[i,16]
            item.circMv = data.iat[i,17]
            list.append(item)
        return list





