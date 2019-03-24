import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import requests
import json
from pandas import DataFrame
import time
import datetime
from matplotlib import style

# URLs for getting coins information through API

URL = 'https://coincheck.com/api/rate/eth_jpy'
URL2 = 'https://coincheck.com/api/rate/xrp_jpy'
URL3 = 'https://coincheck.com/api/rate/rep_jpy'
URL4 = 'https://coincheck.com/api/rate/xem_jpy'
URL5 = 'https://coincheck.com/api/rate/btc_jpy'
URL6 = 'https://coincheck.com/api/rate/etc_jpy'
URL7 = 'https://coincheck.com/api/rate/lsk_jpy'
URL8 = 'https://coincheck.com/api/rate/fct_jpy'
URL9 = 'https://coincheck.com/api/rate/xmr_jpy'
URL10 = 'https://coincheck.com/api/rate/zec_jpy'
URL11 = 'https://coincheck.com/api/rate/ltc_jpy'
URL12 = 'https://coincheck.com/api/rate/dash_jpy'
URL13 = 'https://coincheck.com/api/rate/bch_jpy'

# Variables that holds market average for different duration
five_min_market_average = 0
ten_min_market_average = 0
one_hour_market_average = 0
one_day_market_average = 0

#Variables that holds coins average for different duration
five_min_eth_average = 0
ten_min_eth_average = 0
one_hour_eth_average = 0
one_day_eth_average = 0

five_min_xrp_average = 0
ten_min_xrp_average = 0
one_hour_xrp_average = 0
one_day_xrp_average = 0

five_min_rep_average = 0
ten_min_rep_average = 0
one_hour_rep_average = 0
one_day_rep_average = 0

five_min_xem_average = 0
ten_min_xem_average = 0
one_hour_xem_average = 0
one_day_xem_average = 0

five_min_btc_average = 0
ten_min_btc_average = 0
one_hour_btc_average = 0
one_day_btc_average = 0

five_min_etc_average = 0
ten_min_etc_average = 0
one_hour_etc_average = 0
one_day_etc_average = 0

five_min_lsk_average = 0
ten_min_lsk_average = 0
one_hour_lsk_average = 0
one_day_lsk_average = 0

five_min_fct_average = 0
ten_min_fct_average = 0
one_hour_fct_average = 0
one_day_fct_average = 0

five_min_xmr_average = 0
ten_min_xmr_average = 0
one_hour_xmr_average = 0
one_day_xmr_average = 0

five_min_zec_average = 0
ten_min_zec_average = 0
one_hour_zec_average = 0
one_day_zec_average = 0

five_min_ltc_average = 0
ten_min_ltc_average = 0
one_hour_ltc_average = 0
one_day_ltc_average = 0

five_min_dash_average = 0
ten_min_dask_average = 0
one_hour_dash_average = 0
one_day_dash_average = 0

five_min_bch_average = 0
ten_min_bch_average = 0
one_hour_bch_average = 0
one_day_bch_average = 0

#Variables for holding exchange fees
buy_fees = 0.036
sell_fees = 0.036

# Variables for holding Wallet Coins amount and value
eth_coins = 0
eth_values = 0

xrp_coins = 0
xrp_values = 0

rep_coins = 0
rep_values = 0

xem_coins = 0
xem_values = 0

btc_coins = 0
btc_values = 0

etc_coins = 0
etc_values = 0

lsk_coins = 0
lsk_values = 0

fct_coins = 0
fct_values = 0

xmr_coins = 0
xmr_values = 0

zec_coins = 0
zec_values = 0

ltc_coins = 0
ltc_values = 0

dask_coins = 0
dash_values = 0

bch_coins = 0
bch_values = 0


#Variables for Plots
fig, axis = plt.subplots(4,2)
ax = axis[0,0]
ax2 = axis[1,0]
ax3 = axis[2,0]
ax4 = axis[0,1]
ax5 = axis[1,1]
ax6 = axis[2,1]
ax7 = axis[3,0]
ax8 = axis[3,1]
#fig, (ax,ax2) = plt.subplots(1,2, sharex=True)
xdata, ydata = [], []
ydata2, ydata3 = [], []
ydata4 = []
# ax = plt.axes(xlim=(0, 300), ylim=(89000, 90000))
# ax2 = plt.axes(xlim=(0, 300), ylim=(0, 1000))
ax.set_ylim(89000, 90000)
ax2.set_ylim(0, 250)
ax3.set_ylim(8000,11000)
ax4.set_ylim(89000, 90000)
ax5.set_ylim(0, 250)
ax6.set_ylim(8000,11000)
ax7.set_ylim(0,250)
ax8.set_ylim(0,250)
ax.set_xlim(0, 100)
ax2.set_xlim(0, 100)
ax3.set_xlim(0, 100)
ax4.set_xlim(0, 100)
ax5.set_xlim(0, 100)
ax6.set_xlim(0, 100)
ax7.set_xlim(0, 100)
ax8.set_xlim(0, 100)
ax.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()
ax7.grid()
ax8.grid()

line1, = ax.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line3, = ax3.plot([], [], lw=2, color='k')
line4, = ax4.plot([], [], lw=2)
line5, = ax5.plot([], [], lw=2, color='r')
line6, = ax6.plot([], [], lw=2, color='k')
line7, = ax7.plot([], [], lw=2, color='g')
line8, = ax8.plot([], [], lw=2, color='g')
lines = [line1, line2, line3, line4, line5, line6,line7,line8]

def init():    
    for line in lines:
        line.set_data([], [])
    return lines

def animate(frame):
    coincheck = requests.get(URL).json()
    coincheck2 = requests.get(URL2).json()
    coincheck3 = requests.get(URL3).json()
    coincheck4 = requests.get(URL4).json()
    y = round(float(coincheck['rate']),2)
    y2 = round(float(coincheck2['rate']),2)
    y3 = round(float(coincheck3['rate']),2)
    y4 = round(float(coincheck4['rate']),2)
    #t = datetime.datetime.now()
    xdata.append(frame)
    ydata.append(y)
    ydata2.append(y2)
    ydata3.append(y3)
    ydata4.append(y4)
    #for j,line in enumerate(lines):
    line1.set_data(xdata, ydata)
    line2.set_data(xdata, ydata2)
    line3.set_data(xdata, ydata3)
    line7.set_data(xdata, ydata4)
    line4.set_data(xdata, ydata)
    line5.set_data(xdata, ydata2)
    line6.set_data(xdata, ydata3)
    line8.set_data(xdata, ydata4)
    xmin, xmax = ax4.get_xlim()
    xmin2, xmax2 = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ymin2, ymax2 = ax2.get_ylim()
    ymin3, ymax3 = ax3.get_ylim()
    ymin4, ymax4 = ax7.get_ylim()
    
    if(((frame+1)%300) == 0):
        ax4.set_xlim(xmin+300, xmin+600)
        ax4.figure.canvas.draw()
        ax5.set_xlim(xmin+300, xmin+600)
        ax5.figure.canvas.draw()
        ax6.set_xlim(xmin+300, xmin+600)
        ax6.figure.canvas.draw()
        ax8.set_xlim(xmin+300, xmin+600)
        ax8.figure.canvas.draw()
        
    if frame >= xmax:
        ax4.set_xlim(xmin, 2*xmax)
        ax4.figure.canvas.draw()
        ax5.set_xlim(xmin, 2*xmax)
        ax5.figure.canvas.draw()
        ax6.set_xlim(xmin, 2*xmax)
        ax6.figure.canvas.draw()
        ax8.set_xlim(xmin, 2*xmax)
        ax8.figure.canvas.draw()
        
    if frame >= xmax2:
        ax.set_xlim(0, 2*xmax2)
        ax.figure.canvas.draw()
        ax2.set_xlim(0, 2*xmax2)
        ax2.figure.canvas.draw()
        ax3.set_xlim(0, 2*xmax2)
        ax3.figure.canvas.draw()
        ax7.set_xlim(0, 2*xmax2)
        ax7.figure.canvas.draw()
        
    if y >= ymax:
        ax.set_ylim(ymin, ymax*1.1)
        ax.figure.canvas.draw()
        ax4.set_ylim(ymin, ymax*1.1)
        ax4.figure.canvas.draw()

    if(y <= ymin):
        ax.set_ylim(ymin*0.9, ymax)
        ax.figure.canvas.draw()
        ax4.set_ylim(ymin*0.9, ymax)
        ax4.figure.canvas.draw()

    if y2 >= ymax2:
        ax2.set_ylim(ymin2, ymax2*1.1)
        ax2.figure.canvas.draw()
        ax5.set_ylim(ymin2, ymax2*1.1)
        ax5.figure.canvas.draw()

    if(y2 <= ymin2):
        ax2.set_ylim(ymin2*0.9, ymax2)
        ax2.figure.canvas.draw()
        ax5.set_ylim(ymin2*0.9, ymax2)
        ax5.figure.canvas.draw()

    if y3 >= ymax3:
        ax3.set_ylim(ymin3, ymax3*1.1)
        ax3.figure.canvas.draw()
        ax6.set_ylim(ymin3, ymax3*1.1)
        ax6.figure.canvas.draw()

    if(y3 <= ymin3):
        ax3.set_ylim(ymin3*0.9, ymax3)
        ax3.figure.canvas.draw()
        ax6.set_ylim(ymin3*0.9, ymax3)
        ax6.figure.canvas.draw()
        
    if y4 >= ymax4:
        ax7.set_ylim(ymin4, ymax4*1.1)
        ax7.figure.canvas.draw()
        ax8.set_ylim(ymin4, ymax4*1.1)
        ax8.figure.canvas.draw()

    if(y4 <= ymin4):
        ax7.set_ylim(ymin4*0.9, ymax4)
        ax7.figure.canvas.draw()
        ax8.set_ylim(ymin4*0.9, ymax4)
        ax8.figure.canvas.draw()   

    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10000000, interval=1000, blit=True)

plt.show()