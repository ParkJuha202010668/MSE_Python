#!/usr/bin/env python
# coding: utf-8

# In[14]:


# print_max() : 세 개의 숫자를 입력 받아 가장 큰 수를 출력하는 함
# if문을 사용해 수 비교


def print_max(a, b, c) :   # 함수를 정의하기
    max_val = 0
    if a > max_val :
        max_val = a    # a에 위치한 숫자가 나머지 두 숫자보다 크면 a 출력
    if b > max_val :
        max_val = b    # b에 위치한 숫자가 나머지 두 숫자보다 크면 b 출력
    if c > max_val :
        max_val = c    # c에 위치한 숫자가 나머지 두 숫자보다 크면 c 출력
    print(max_val)
    
print_max(3, 7, 8) 


# In[ ]:




