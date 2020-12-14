#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 시가에 매수해서 종가에 매도했을 경우 총 수익금은?

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# 1일차 수익 : 100 - 100 = 0
# 2일차 수익 : 190 - 200 = -10
# 3일차 수익 : 310 - 300 = 10
# 총수익 0 + (-10) + 10 = 0

profit = 0
for row in ohlc[1:]: 
    profit += (row[3] - row[0])
    # profit = profit + (row[3] - row[0]) 
    # row[3] - row[0] : 네 번째 원소 - 첫 번째 원소
print(profit)


# In[ ]:




