import numpy as np
import datetime
import chinesestocks.Configuration as cfg


def toFloat(input):
    a = 0
    if input is None:
        return 0
    if input == '-':
        return -1;
    else:
        try:
            a = float(np.nan_to_num(input))
        except Exception as err:
            print("input is %s"%str(input))
            print("number to float exception: %s" %str(err))
            a = -1
        return a

def toInt(input):
    a=0
    if input is None:
        return 0
    else:
        try:
            a = int(np.nan_to_num(input))
        except Exception as err:
            print("input is %s" % str(input))
            print("number to int exception: %s" %str(err))
        return a

def toStd(input):
    array = np.array(input)
    array -= array.mean(axis=0)
    array /= array.std(axis=0)
    array = np.nan_to_num(array)
    return array

def dateTushareToGina(dateStr):
    dt = datetime.datetime.strptime(dateStr, cfg.CONSTANT.DateFormatTushare)
    d = dt.strftime(cfg.CONSTANT.DateFormatGina)
    return d

def dateGinaToTushare(dateStr):
    dt = datetime.datetime.strptime(dateStr, cfg.CONSTANT.DateFormatGina)
    d = dt.strftime(cfg.CONSTANT.DateFormatTushare)
    return d

def getTodayDateStr():
    dt = datetime.datetime.now().strftime(cfg.CONSTANT.DateFormatGina)
    return dt

def createDateFromGina(dateStr):
    dt = datetime.datetime.strptime(dateStr, cfg.CONSTANT.DateFormatGina)
    return dt

def createDateFromTushare(dateStr):
    dt = datetime.datetime.strptime(dateStr, cfg.CONSTANT.DateFormatTushare)
    date = dt.date()
    return date