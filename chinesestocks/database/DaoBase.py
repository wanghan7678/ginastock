import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

import chinesestocks.Configuration as cf

class DaoBase(object):
    def getSession(self):
        engine = sqlalchemy.create_engine(cf.CONSTANT.Database_Url2, poolclass=sqlalchemy.pool.NullPool,echo=False)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def addItemList(self, itemList):
        session = self.getSession()
        if itemList is None:
            print("input list is None")
            session.close()
            return
        for item in itemList:
            session.add(item)
        try:
            session.commit()
        except Exception as err:
            print("add_item list integrity error")
            print("Duplicated item....skipped.        "+str(err))
        else:
            print("insert data...")
        finally:
            print("close sql session")
            session.close()

    def addOneItem(self, oneItem):
        ls = [oneItem]
        self.addItemList(ls)