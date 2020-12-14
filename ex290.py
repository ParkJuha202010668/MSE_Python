#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:
  def __init__(self): # class를 호출할 때, 최초로 자동으로 호출되는 함수로 초기화 할 때 사용
    print("부모생성")

class 자식(부모):
  def __init__(self): # init함수와 self는 항상 같이 사용됨.
    print("자식생성")
    super().__init__()  # 자식class에서 부모class의 내용을 가져올 때

나 = 자식()


# In[ ]:




