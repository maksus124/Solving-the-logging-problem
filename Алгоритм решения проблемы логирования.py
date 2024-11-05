#!/usr/bin/env python
# coding: utf-8

# In[21]:


with open('C:/Project/example.txt', 'r', encoding = 'utf-8' ) as example:
    a = example.readlines()
if len(a) >= 200:
    slice1 = a[:100]
    slice2 = a[-100:]
    slice1.extend(slice2)
elif len(a) == 0:
    slice1 = 'Изначальный список пуст'
else:
    slice1 = a
with open('C:/Project/logs.txt', 'w', encoding = 'utf-8' ) as logs:
    logs.writelines(slice1)


# In[16]:




