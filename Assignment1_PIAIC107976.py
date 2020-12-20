#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array(15)
a


# In[4]:


x=np.zeros((5,5))
x


# In[6]:


np.ndim(x)


# In[8]:


a=np.arange(15,40)     
a


# In[9]:


b=a*2                 
b


# In[10]:


c=a+b                 
c


# In[11]:


1/c*c    


# In[12]:



c>50                  


# In[14]:


c[9]  


# In[15]:


d=c[c>78]             #10
d


# In[16]:


np.sqrt(d)


# In[18]:


np.power(5,2)


# In[19]:


np.exp(d) 


# In[21]:


x=np.ones((6,6))        
x


# In[22]:


x[1:-1,1:-1]=0          
x


# In[23]:


x[1:,1:]+=2            
x


# In[25]:


z=np.random.random((2,2))    
z


# In[26]:


z.min()  


# In[27]:


z.max()


# In[28]:


z.mean()


# In[29]:


z[1:2]**2  


# In[30]:


a=np.array([8,0,8,6,4])
a


# In[31]:


a[::-1]    #Prints in reverse form


# In[32]:


a = np.arange(-4,8).reshape(4, 3)   #Creates an array from the range and then converts to 4 x 3
a


# In[33]:


a[::2]  #parses the first two rows


# In[36]:


a[-1,1]=1     
a


# In[37]:


np.linspace(1,2,5) 


# In[38]:


y=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
y


# In[40]:


y[0]=0                 
y


# In[43]:


c=np.arange(0,12).reshape(4,3)
c


# In[47]:


c[1:3,2:3]  #works only if the second number is bigger than the first


# In[48]:


u=[-3,-2,0,1,2,4,6,7,9]


# In[49]:


v=[-4,5,6,8,9,8,9,2,-2]


# In[50]:


w=np.intersect1d(u,v)    #displays common elements in 1D
w


# In[51]:


np.where(w)  


# In[52]:


np.setdiff1d(u,v)


# In[53]:


k=np.concatenate((u,v))   
k


# In[54]:


k[k%2==1] 


# In[55]:


k[k%2==0]   


# In[56]:


np.where(k%2==1,-1,k)


# In[58]:


j=np.arange(9).reshape(3,3) #reshape index's product must be equal to the arrange number
j


# In[62]:


j[[0,2,1,],:] #rearranges the array to the input index


# In[63]:


j[[0],:]+2 


# In[64]:


m=np.arange(20)
m


# In[65]:


np.set_printoptions(threshold=8)


# In[66]:


np.where(m<5,4,np.where(m>15,3,m))


# In[67]:


np.random.seed(50)


# In[69]:


a=np.random.uniform(1,9)            
a


# In[70]:


np.cos(a)


# In[71]:


a=np.arange(3)
b=np.arange(1,4)                     
c=np.arange(0,2,5)


# In[72]:


d=np.array([a,b,c])                 
d


# In[73]:


x=np.zeros((7,7))
x


# In[74]:


x+=np.arange(7)                    
x


# In[77]:


y=np.random.random(4)             
y.sort()
y


# In[79]:


z=np.arange(10)                     
np.add.reduce(z)


# In[80]:


a=np.random.random(4)              
a[a.argmax()]=0
a


# In[82]:


a= [0,2,4,6,8]                     
b= [1,3,5,7,9]
c= np.bincount(a,b)
c


# In[83]:


a= np.arange(16).reshape(4,4)      
a[[0,1]] = a[[1,0]]
a


# In[84]:


z=np.random.randint(0,20,30)        
print(np.bincount(z).argmax())


# In[ ]:




