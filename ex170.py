#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1부터 10까지의 숫자를 모두 곱하기

result = 1
for i in range(1,11) :
    # (1,11)은 1부터 10까지
    result *= i
    # result *= i는 result = result + i
    # a += i는 a = a + i
print(result)


# In[ ]:




