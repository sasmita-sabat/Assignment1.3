
# coding: utf-8

# In[1]:


#Input your name and reverse the name 
l=[]
F_name=input("Enter your first name ")
L_name=input("Enter your second name ")
#Concatenating the firstname and lastname to frame the Name.
Name=F_name + " " + L_name
#To get the length of the String(Name)
i=len(Name)-1
print ("The name is "+Name)
#Loop from reverse till the 0th index of the String(Name)
while(i>=0):
    l.append(Name[i])
    i-=1
l=''.join(l)
print("The reversed string is "+l)

