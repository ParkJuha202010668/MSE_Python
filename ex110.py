#!/usr/bin/env python
# coding: utf-8

# In[1]:


# bool 타입

if True : 
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

# 기본값이 True이기 때문에 if True: -> else: 이기 때문에 3이 print 됨.
# 마지막 print("5")는 조건문이 아니기 때문에 그냥 print 됨.

