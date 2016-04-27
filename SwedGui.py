import pandas as pd
import yahoo_finance as yf
import traceback
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import *
import sys

class DataFetcher():
    def __init__(self):
        b_con = False
        try:
            yf.Share("YHOO").refresh()
            b_con = True
        except:
            traceback.print_exc()
            print "connection failed....."

        if b_con:
            print "connection successfully...."

    def fetch_data_with_symbol(self, sym="YHOO", start_date="2015-02-03", end_date="2016-02-03"):
        return yf.Share(sym).get_historical(start_date, end_date)

    def to_pandas(self, input=list()):
        s = pd.DataFrame(input)
        s.set_index("Date")
        return s

class DataFetchGui(qtw.QWidget):
    def __init__(self):
        qtw.QWidget.__init__(self)
        self.init_gui()


    def init_gui(self):
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        







s = DataFetcher()
data = s.fetch_data_with_symbol()
data = s.to_pandas(data)
print data

app = qtw.QApplication(sys.argv)
w = DataFetchGui()
w.show()
sys.exit(app.exec_())

