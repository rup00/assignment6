a=int(input("enter first numbeer"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a==b==c:
    print("all are same")
elif a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
