'Zadanie2'
kat1, kat2, gip = float(input("Введите длину 1 катета: ")), float(input("Введите длину 2 катета: ")), float(input("Введите длину гипотенузы: "))
if kat1**2+kat2**2==gip**2:
    perimeter = kat1+kat2+gip #Вычисляем периметр треугольника
    square = kat1*kat2/2 #Вычисляем площадь треугольника
    print(perimeter, " ", square)
else:
    print("Треугольник не является прямоугольным")