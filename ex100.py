#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 두 개의 List (data, close_price) 을 하나의 Dictionery (close_table) 로 변환 

data = ['09/05', '09/06', '09/07', '09/08', '09/09'] # List1
close_price = [10500, 10300, 10100, 10800, 11000] # List2
close_table = dict(zip(data, close_price))

# zip()는 동일한 개수로 이루어진 자료형을 묶어주는 내장함수

print(close_table)

