#FIBONACCI GENERATOR
a=int(input("Enter number for finding fibonacci series"))
f=0
s=1
print(f)
print(s)
for i in range(2,a):
    l=f+s
    f=s
    s=l
    print(l)

    
