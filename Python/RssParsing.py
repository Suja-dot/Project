# -*- coding: utf-8 -*-
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.

# Module File
import msvcrt
import datetime

# Personal File
from RssParser import *
import Display
from Display import *
from Lotto import *
from Finance import *

'''[TODO] Totaliy file need to exception process'''

# Functions
def init():
    print("Invalid Mode")

def NewsMode():
    crawl_keyword_rss()

def LottoMode():
    res = []
    latest_round = CalcLatestRound()
    eR = latest_round+1
    sR = latest_round
    static_lotto = StaticLotto()

    lotto_mode = printLottoMode()
    if lotto_mode == '1':
        lotto_winnum_mode = printLottoWinnumMode()
        if lotto_winnum_mode == '2':
            sR = getStratRound()
            eR = getEndRound()
        for i in range(sR, eR):
            res = ReceiveLottoData(i)
            PrintLottoWinnum(res, i)
    if lotto_mode == '2':
        sR = getStratRound()
        eR = getEndRound()
        if eR == '':
            eR = latest_round
        lotto_stat_mode = printLottoNumberStatMode()
        for i in range(sR, eR):
            res = ReceiveLottoData(i)
            AddWinnumCnt(res,static_lotto)
        PrintLottoStatResult(lotto_stat_mode,static_lotto)
    if lotto_mode == '3':
        my_num = input("Please Enter your number : ").split()
        score = CompareWithMyNum(my_num,latest_round)
        PrintLottoScore(score)

def FinanceMode():
    finance_mode = printFinanceMode()
    load_stock_table()
    if finance_mode == '1':
        print_stock_table()
    if finance_mode == '2':
        stk = Stock()
        stk.set_stock_name()
        #[TODO] Keyboard event not properly action..
        #[TODO] add if prev price and cur price not equal, print
        #[TODO] custom setting and event
        print("If you want to stop, please enter the 'q'")
        print("Receive '"+stk.get_stock_name()+"' price...")
        while True:
            if msvcrt.kbhit():
                print("Stop receive stock price##")
                break
            print(str(datetime.datetime.now())+" - "+str(receive_stock_price(stk.get_stock_code())))
            time.sleep(0.5)



def Quit():
    print("Bye!")
    exit()

# Function Dictionary
dict_func = {
    '0' : init,
    '1' : NewsMode,
    '2' : LottoMode,
    '3' : FinanceMode,
    'q' : Quit
}

# Main
def main():
    #main_window = main_widget()
    #main_window.get_tk().mainloop()

    mode = '0'
    while(mode!='q'):
        mode = printMode()
        dict_func[mode]()
        if printContinue() == 'n':
            Quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
