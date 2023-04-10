# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

"""
dig = int(input('Input three digit number: '))

num1 = dig // 100
num2 = (dig // 10) % 10
num3 = dig % 10

sum = num1 + num2 + num3

print (f'{num1} + {num2} + {num3} -> {sum}')
"""



"""
dig = int(input('Input three digit number: '))
sum = 0

if dig > 99 and dig < 1000:
    while dig > 0:

        dig1 = dig % 10
        dig = dig // 10

        sum += dig1

    print (sum)

else:
    print('Input correct digit!')
"""

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

"""
sum = int(input('Input count of elements: '))

x = int(sum // 6)
x1 = int(x * 4)

p = x
s = x
k = x1

print(f'Kate made {k} elements')
print(f'Petr made {p} elements')
print(f'Sergey made {s} elements')
"""

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

"""
num = str(input('Input digit from 6 number: '))

t1 = num[:3]
t2 = num[3:]

print(t1)
print(t2)

sum1 = int(t1[0]) + int(t1[1]) + int(t1[2])

print (int(sum1))

sum2 = int(t2[0]) + int(t2[1]) + int(t2[2])

print (int(sum2))

if sum1 == sum2:
    print('yes')
else:
    print('no')
"""

# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

size_n = int(input('Input side a: '))
size_m = int(input('Input side b: '))

size_k = int(input('Input count of element: '))

if size_k % size_n == 0 or size_k % size_m == 0:
    print (f'{size_n} {size_m} {size_k} -> yes')

else:
    print (f'{size_n} {size_m} {size_k} -> no')

