#Numeric
#1.int
#2.float
#3.complex
#4.boolean

#numeric
#none
#list
#tuple
#set
#String = "str"
#range
#dictionary

num = 1
ans= type(num)
print(ans)

#convert dt to int
a=5.6
b=int(a)
print(b)

#complex
num = 1+2j
ans= type(num)
print(ans)

#boolean
x=3
y=6
ans =x>y
print(ans)

r = list(range(0,10))
print(r)

d={'kevin': 'iphone', 'Joy':'techno' }
ans=d.keys()
v=d.values()
print(ans)
print(v)

phone= d.get('kevin')
print(phone)

phone2= d['Joy']
print(phone2)