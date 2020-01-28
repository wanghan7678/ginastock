from sqlalchemy.sql import func

import chinesestocks.model.Analyzer as an
import chinesestocks.database.DaoBase as db
import chinesestocks.BasicUtility as util

class AnalyzerSignalsDao(db.DaoBase):

    def insetAnalyzerSignals(self, analyzerSignals):
        super().addOneItem(analyzerSignals)

    def updateBinaryLebel(self, tscode, signalDate, binaryLabel):
        session = super().getSession()
        query = session.query(an.AnaylzerSignals)
        query.filter(an.AnaylzerSignals.tscode==tscode).filter(an.AnaylzerSignals.signalDate==signalDate).update(
            {an.AnaylzerSignals.binaryLabel : binaryLabel})
        session.flush()

