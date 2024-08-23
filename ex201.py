# def print_coin():
#     print('비트코인')

# print_coin()

# for i in range(100):
#     print_coin()

# def print_coins():
#     for i in range(100):
#         print('비트코인')

# print_coins()

# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()

# def 함수(문자열) :
#  print(문자열)
# 함수("안녕")
# 함수("Hi")

def print_with_smile(string):
    print(string + ':D')

print_with_smile("안녕하세요")    


def print_upper_price(price):
    print(price * 1.3)

print_upper_price(100)    


def print_sum(a , b):
    print(a+b)

def  print_arithmetic_operation(a, b):
    print(f'{a} +  {b} = {a + b}')
    print(f'{a} +  {b} = {a - b}')
    print(f'{a} +  {b} = {a * b}')
    print(f'{a} +  {b} = {a / b}')

def print_max(a, b, c):
    max_val = 0

    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c

    print(max_val)


print_max(1, 2, 3)    

    
def print_score(my_list):
    print(sum(my_list)/len(my_list))


print_score([1, 2, 3, 4, 5, 6, 7, 8])

def print_event(my_list):
    for i in my_list:
        if i % 2 == 0:
            print(i)

print_event([1, 2, 3, 4, 5, 6, 7, 8])

def print_key(my_d):
    for i in my_d:
        print(i)

print_key({"이름":"김말똥", "나이":30, "성별":0})


def print_value_by_key  (my_dict, key):
    print(my_dict[key])

my_dict = {
    "10/26" : [100, 130, 100, 100],
    "10/27" : [10, 12, 10, 11]
 }

print_value_by_key(my_dict, "10/26")

def calc_monthly_salary(annual_pay):
    monthly_pay = int(annual_pay / 12)
    print(monthly_pay)

calc_monthly_salary(12000000)




def asd(asdd):
    result = [] 
    for i in asdd:
        if i % 2 == 0 :
            result.append(i)

    print(result)

asd([3, 4, 5, 6, 7, 8])


def 함수(num) :
 return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)


def 함수(num) :
    return num + 4
c = 함수(함수(함수(10)))
print(c)


def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10)
c = 함수2(a)
print(c)


def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)

def 함수0(num) :
 return num * 2
def 함수1(num) :
 return 함수0(num + 2)
def 함수2(num) :
 num = num + 10
 return 함수1(num)
c = 함수2(2)
print(c)















































