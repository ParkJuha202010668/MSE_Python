#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률): # per, pbr, 배당수익률은 float(실수) type
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# set_name 메서드는 객체에 종목명을 입력
# set_code 메서드는 객체에 종목코드를 입력
# get_name, get_code는 종목명과 종목코드를  리턴함

종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문


# In[ ]:




