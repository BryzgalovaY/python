__author__ = 'Брызгалова Юлия Викторовна'

# EASY
#
# # Задание-1:
# # Напишите функцию, округляющую полученное произвольное десятичное число
# # до кол-ва знаков (кол-во знаков передается вторым аргументом).
# # Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# # Для решения задачи не используйте встроенные функции и функции из модуля math.
#

#
print()
print("Easy. Задача-1")
def my_round(number, ndigits):
    a = str(number).split('.')
    b = a[-1]
    if int(b)>0 and int(b[ndigits:ndigits+1]) <= 5 and ndigits != 0:
        c = "{}.{}".format(a[0],b[:ndigits])
        return c
    elif int(b)>0 and int(b[ndigits:ndigits+1]) > 5 and ndigits != 0:
        c = "0."
        for i in range(0,ndigits-1):
            c = c + "0"
        c = c + "1"
        okrug = float("{}.{}".format(a[0],b[:ndigits])) + float(c)
        return okrug
    elif int(b) == 0:
	    return number
    elif ndigits == 0:
        if int(b[0])<=5:
            c = "{}.0".format(a[0])
            return c
        else:
            c = "{}.0".format(int(a[0])+1)
            return c
    else:
        pass	

print(my_round(34.937, 2))
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.9399967, 5))


# # Задание-2:
# # Дан шестизначный номер билета. Определить, является ли билет счастливым.
# # Решение реализовать в виде функции.
# # Билет считается счастливым, если сумма его первых и последних цифр равны.
# # !!!P.S.: функция не должна НИЧЕГО print'ить
#

print()
print("Easy. Задача-2")
def lucky_ticket(ticket_number):
    ticket_number = list(map(lambda x: int(x), str(ticket_number)))
    if sum(ticket_number[0:3]) == sum(ticket_number[3:]):
        return "Да, билет счастливый."
    else:
        return "К сожалению, билет не счастливый, попробуйте снова."


print(lucky_ticket(123006))
print(lucky_ticket(122321))
print(lucky_ticket(436751))
