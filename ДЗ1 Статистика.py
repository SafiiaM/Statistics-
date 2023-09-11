#!/usr/bin/env python
# coding: utf-8

# # Задача 1 (а)

# In[4]:


from math import factorial


# In[6]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (52,4) # число исходов извлечь 4 карты из 52


# In[7]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (13,4) # число исходов извлечь крести 


# In[12]:


def division (a,b):
  return a / b
division (715, 270725) # вероятность извлечения крестей 


# # Задача 1 (б)

# In[13]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (4,1) # сочетания из подмножества тузов 


# In[18]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (48,3) # сочетания из подмножества не тузов 


# In[19]:


def multiplication (a,b):
  return a*b                   
multiplication (4,17296) # сочетаний из 4 карт, где 1 туз 


# In[20]:


def division (a,b):
  return a / b
division (69184,270725) # вероятность извлечения 1 туза 


# In[ ]:





# # Задача 2

# In[21]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (10,3) # все возможные сочентания  


# In[22]:


def division (a,b):
  return a / b
division (1,120) # вероятность с первого раза набрать правильную комбинацию 


# In[ ]:





# # Задача 3

# In[23]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (15,3) # сочетания общего числа исходов


# In[24]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (9,3) # сочетания благоприятного числа исходов


# In[25]:


def division (a,b):
  return a / b
division (84,455) # вероятность вынуть все 3 окрашенные детали 


# In[ ]:





# # Задача 4
# 

# In[26]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (100,2) # сочетания благоприятного числа исходов


# In[27]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (2,2) # сочетания выигрышных исходов из всех возможных выигрышных исходов


# In[28]:


def combinations (n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))
combinations (98,0) # сочетания прроигрышных исходов из всех возможных проигрышных исходов


# In[48]:


def division (a,b):
  return a / b
division (1, 49450) # вероятность того, что 2 приобретенных билета окажутся выигрышными (должно быть 0,00020 - формула неправильно считает  )


# In[ ]:





# Задача 5 

# 
# p1=0,9 - Вероятность попадания для первого спортсмена 
# q2=1-p2=1-0,8=0,2 - Вероятность непопадания для второго спортсмена 
# q3=1-p3=1-0,6=0,4 - Вероятность непопадания для третьего спортсмена 
# 
# q1=1-0,9=0,1 - Вероятность непопадания для первого спортсмена 
# p2=0,8 - Вероятность попадания для второго спортсмена 
# p3=0,6 - Вероятность попадания для третьегоспортсмена 
# 
# 1) х1=p1⋅q2⋅q3+q1⋅p2⋅q3+q1⋅q2⋅p3 - вероятность попадания первым спортсменом 
# х1= 0,9*0,2*0,4+0,1*0,8*0,4+0,1*0,2*0,6=0,116
# 
# 2) х2=p1⋅p2⋅q3+p1⋅q2⋅p3+q1⋅p2⋅p3 - вероятность попадания вторым спортсменом 
# х2= 0,9*0,8*0,4+0,9*0,2*0,6+0,1*0,8*0,6=0,444
# 
# 3) х3=p1⋅p2⋅p3 - вероятность попадания третьим спортсменом 
# х3= 0,9*0,8*0,6=0,432
