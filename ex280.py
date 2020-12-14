#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = [] # 비어 있는 list
        self.withdraw_log = [] # 비어 있는 list

        self.name = name
        self.balance = balance
        self.bank = "SC은행" # 은행 이름

        # 3-2-6 계좌번호 만들기
        num1 = random.randint(0, 999) # 계좌번호의 3자리 형태
        num2 = random.randint(0, 99) # 계좌번호의 2자리 형태
        num3 = random.randint(0, 999999) # 계좌번호의 6자리 형태

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001' : 3자리 형태 유지
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01' : 2자리 형태 유지
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001' : 6자리 형태 유지
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls): # Accound class로부터 생성된 계좌의 개수 출력
        print(cls.account_count)  # Account.account_count

        # 입금
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount) # 입금이 일어날 때마다 list에 append 됨
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)
                # 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가

                # 출금
    def withdraw(self, amount):
        if self.balance > amount: # 잔고 이상 출금할 수 없음
            self.withdraw_log.append(amount) # 출금이 일어날 때마다 list에 append 됨
            self.balance -= amount

    def display_info(self):    # Account 인스턴스의 저장된 정보 출력
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log: # 출금액
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log: # 입금액 출력
            print(amount)


k = Account("Kim", 1000) # 1000원 (초기 잔액)
k.deposit(100) # 100원 예금
k.deposit(200) # 200원 예금
k.deposit(300) # 300원 예금
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()


# In[ ]:




