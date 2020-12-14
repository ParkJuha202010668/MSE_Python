#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 비트코인의 가격 정보를 Dict로 가져오기
# import 가져오기

import requests
btc = requests.get("http://api.bithumb.com/public/ticker/").json()['data']
# btc Dict에 opening_price, closing_price, min_price, max_price 저장되어 있음.

# 데이터 타입 : 실수(float)_8byte

변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 변동폭 = 최근 24시간 내 최고 거래금액 - 최근 24시간 내 최저 거래금액

시가 = float(btc['opening_price'])
# 시가 = 최근 24시간 내 시작 거래금액

최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가: # 이 조건을 만족하면
    print("상승장") # 상승장 출력
    
else: # 만족하지 않으면 
    print("하락장") # 하락장 출력


# In[ ]:




