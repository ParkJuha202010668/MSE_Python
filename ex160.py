#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일 출력하기

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".") # 변수를 .있는 데에서 나눔
    
    if (split[1] == "h") or (split[1] == "c"):
        # 두 번째에 h나 c가 있으면
        print(변수)
        # 출력


# In[ ]:




