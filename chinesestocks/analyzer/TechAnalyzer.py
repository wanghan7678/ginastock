import numpy as np
import talib
import chinesestocks.BasicUtility as util
import chinesestocks.model.Cnstock as cs

class TechAnalyzer(object):
    dataSize = 60
    calculateSize = 200

    fastKPeriod = 10
    fastDPeriod = 3
    bbandPeriod = 10
    dmiPeriod = 14
    wr1Period = 6
    wr2Period = 13
    mtmPeriod = 12

    # in the asc order of time.
    openList, closeList, highList, lowList, volList = [0],[0],[0],[0],[0]
    tscode = ''
    length = 0

    def setDailyData(self, inputData, tscode):
        self.openList = np.array(inputData['open'], dtype=float)
        self.closeList = np.array(inputData['close'], dtype = float)
        self.highList = np.array(inputData['high'], dtype = float)
        self.lowList = np.array(inputData['low'], dtype = float)
        self.volList= np.array(inputData['volume'], dtype = float)
        self.length = util.toInt(len(inputData['close']))
        self.tscode = tscode

    def getSMA(self, period = 5, close=[]):
        array = np.array(close, dtype=float)
        ma = []
        try:
            ma = talib.SMA(array, timeperiod=period)
        except Exception as err:
            print("talib sma exception: %s" %str(err))
        ma = np.nan_to_num(ma)
        return ma

    def getMa5upMa10IndexList(self):
        ma5 = self.getSMA(5)
        ma10 = self.getSMA(10)
        n = len(ma5) - 1
        list = []
        for i in range(0, n-1):
            upCheck = False
            if ma10[i] >= ma5[i] and ma10[i+1] < ma5[i+1]:
                upCheck = True
            if upCheck:
                list.append(i)
        return list

    def getMa5upMa10List(self, marketdailylist):
        list = sorted(marketdailylist, key=lambda marketdaily:marketdaily.tradeDate, reverse=False)
        closeList = []
        for marketdaily in list:
            closeList.append(marketdaily.closePrice)
        ma5 = self.getSMA(5, closeList)
        ma10 = self.getSMA(10, closeList)
        n = len(ma5)
        indexList = []
        for i in range(0, n-1):
            upCheck = False
            if ma10[i] >= ma5[i] and ma10[i+1] < ma5[i+1]:
                upCheck = True
            if upCheck:
                indexList.append(i+1)
        result = []
        for i in range(0, len(indexList)):
            result.append(list[indexList[i]])
        return result

