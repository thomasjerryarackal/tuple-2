jum=[]
a=int( input("enter the limit"))
for i in range (0,a):
	new=int(input("enter the number"))
	jum=jum+[new]
j=tuple(jum)
print(j)
b=int(input("enter element to remove"))
for l in range (0,a):
	if(l==b):
		jum.remove(b)
u=tuple(jum)
print(u)
