#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 함수 정의 def

def message1():
    print("A")
    
def message2():
    print("B")
    
def message3():
    for i in range (3) :
        message2()    # B 출력
        print("C")    # C 출력
                      # 3번 반복
    message1()        # A 출력
    
message3()


# In[ ]:




