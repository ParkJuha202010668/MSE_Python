#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 사용자가 입력한 값이 Dict value에 불포함시켜 "오답입니다." 출력

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    
    # Dict fruit에 사용자가 입력한 값이 values에 포함되어 있냐?
    
    print("정답입니다.")
    
else:
    print("오답입니다.")


# In[ ]:




