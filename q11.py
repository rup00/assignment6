a=int(input("enter the month"))

if a==2:
   b=int(input("enter the year:"))
   if b%4==0:
        print("29days")
   else:
        print("28days")
elif a%2==0:
    print("30 days")
else:
    print("31 days")
