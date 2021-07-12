n=int(input("enter the n terms"))
n1=0;
n2=1;
count=0
print("fibonacci sequence:")
while count<n:
    print(n1)
    next=n1+n2
    n1=n2
    n2=next
    count = count+1
