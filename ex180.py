#!/usr/bin/env python
# coding: utf-8

# In[2]:


low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]


volatility = [] # 리스트
for i in range(len(low_prices)) : # low_price의 원소 개수 = 5 : 5번
    volatility.append(high_prices[i] - low_prices[i])
    # 변동폭(volatility) = 고가 - 저가
    # a.append 는 리스트 안으로 원소 넣기
    
print(volatility)


# In[ ]:




