__author__ = 'Брызгалова Юлия Викторовна'
print("Домашнее задание №6")
#EASY-NORMAL

# Задача-1:
# 
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)

print()
print("EASY-NORMAL. Задача-1")

class Create_Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if (a+b<c) or (a+c<b) or (b+c<a) or a<0 or b<0 or c<0:
            print("К сожалению, треугольник с такими параметрами создать невозможно! Попробуйте снова!")
            exit(1)

	
    def Get_Area_Triangle(self):
        p = (self.a + self.b + self.c)/2
        Area = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return Area
		
    def Get_Perimeter_Triangle(self):
        Perimeter = self.a + self.b + self.c
        return Perimeter 	
	
    def Print_Triangle(self):
        print("Дан треугольник со сторонами:")
        print("    a = ", self.a)
        print("    b = ", self.b)
        print("    c = ", self.c)
	
Triangle = Create_Triangle(6,12,7)
Triangle.Print_Triangle()
print("Периметр равен:", Triangle.Get_Perimeter_Triangle())
print("Площадь равна:", Triangle.Get_Area_Triangle())