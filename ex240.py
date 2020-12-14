#!/usr/bin/env python
# coding: utf-8

# In[2]:


def 함수0(num) :
    return num * 2 #6. 14 * 2 = 28임

def 함수1(num) :
    return 함수0(num + 2) #4. 12 + 2 = 14   #5. 14가 함수0(num)의 (num)이 됨

def 함수2(num) :
    num = num + 10 #2. 2 + 10 = 12
    return 함수1(num) #3. 12가 함수1(num)의 num이 됨

c = 함수2(2) #1. 함수2(num)의 num에 2 대입
print(c)

#1-6 순서로 계산됨


# In[ ]:




