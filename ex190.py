#!/usr/bin/env python
# coding: utf-8

# In[2]:


apart = [ [101, 102], [201, 202], [301, 302] ]

# apart : 총 3개의 리스트를 갖는 이차원 리스트

for row in apart:
    for col in row:
        print(col, "호") # row 안에 col이 있으면 col 호가 출력됨
        
# columns(열), row(행)
        
print("-" * 5) # 마지막 마무리 출력 / -를 5번 이은 것 출력됨


# In[ ]:




