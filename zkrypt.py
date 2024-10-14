#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
df = pd.read_csv("amazon.csv")
df.head()
writer = pd.ExcelWriter('C:/Users/karol/Desktop/projekt/your_file_name.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='AnotherSheet')

writer.close()

