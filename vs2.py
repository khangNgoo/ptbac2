import math 

a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b / (2*a)
    print("Phuong trinh co hai nghiem kep la:", x)
else:
   x1 = (-b + math.sqrt(delta)) / (2*a)
   x2 = (-b - math.sqrt(delta)) / (2*a)
   print("Phuong trinh co hai nghiem phan biet la:", "x1 =", x1, "x2 =", x2)

