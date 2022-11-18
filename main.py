from SomeClass import SomeClass

input_number = int(input())  # how to input from console

a = 10
b = 20
if a < b:
    print("true")
else:
    print("false")
# print("true" if a < b else "false")

if a == 10 and b == 20:  # or 'or' (da)
    print("yes")

while a < 20:
    a += 1

for i in range(1, 10):  # not including 10
    print(i)

some_random_list = [1, 2, 3, 4]
for i in some_random_list[0:2:1]:
    print(i)


# тут по-русски потому что я не ебу как это написать, короче 0:2 - это индексы(начала и конца)
# :1 - это шаг
# break the same shit


def random_fun(a: int, b: int):  # перед(после) функцией должно быть два пробела(перед методами можно 1 huy)
    return a + b


print(random_fun(a, b))

a1 = 10
b1 = 10
some_class_obj = SomeClass(a1, b1)
print(some_class_obj.sum())
print(some_class_obj)  # Вызываем repr
print(some_class_obj.a)
# по сути тот же геттер только сам геттер нахуй не нужен потому что как сказал Санек питону похуй
