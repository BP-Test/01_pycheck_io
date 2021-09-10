# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 00:00:26 2021

@author: tatsu
"""
import numpy as np
import pandas as pd
import swifter


a = 'hello world'
a.split()
b = 'hello this is BBC world news'
b.split()

c = 'what is 3 + 4'
c = c.split()
c
sum(filter(lambda i: isinstance(i, int), c)) 

sum(c)

[sum(x) for x in c  if int(x)!='ValueError']


'my numbers is 2'





def sum_numbers(text: str) -> int:
    # your code here
    text = str(text)
    text = text.split()
    empty_list = []
    for x in text.split():
        try:
            int(x)
            empty_list.append(int(x))
        except ValueError:
            print("Variable x is not defined")
        except:
            print("Something else went wrong")
    sum(empty_list)