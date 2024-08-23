# 11
coffe = 5000
print(coffe * 5)

# 12
시가총액 = 290000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13
s = "Hello"
t = "python"
print(s + "! " + t)

# 14
print((2 + 3) * 3)

# 15
a = "132"
print(type(a))

#16
num_str = '720'
num_str = int(num_str)
print(num_str, type(num_str))

# 17
num = 100
num = str(num)
print(num, type(num))

#18
a ="15.79"
a = float(a)
print(a, type(a))

#19
year = "2024"
year = int(year)
print(year - 2)
print(year - 1)
print(year )

# 20
a = 48584
print(a * 36)
  
# 21
letters = 'python'
print (letters[0], letters[2])

# 22
license_plate ="24가 2210"
print(license_plate[4:8])
print(license_plate[4:])
print(license_plate[-4:])

# 23
string = '홀짝홀짝홀짝'
print(string[::2])

# 24
string = 'python'
print(string[::-1])

# 25
phone_number = '010-1111-2222'
print(phone_number.replace('-',' '))

# 26 
phone_number = '010-1111-2222'
print(phone_number.replace('-',''))

# 27
url = "http://sharebook.kr"
result = url.split('.')
print(result[1])

# 28
# lang = 'python'
# lang[0] ='p'
# print(lang)

#29
string = 'abcdfe2a354a32a'
result = string.replace('a','A')
print(result)

#30
string = 'abcd'
result = string.replace('b', 'B')
print(result)

#31
a = '3'
b = '4'
print(a + b)

# 32
print('hi' * 3)

# 33
print('-' * 80)

#34 
t1 ='python'
t2 = 'java'
print((t1 +" " + t2 + ' ') * 4)

#35
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print(f'이름: {name1 } 나이: {age1}')
print(f'이름: {name2 } 나이: {age2}')

#36
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print('이름: {0} 나이: {1}'.format(name1,age1))
print('이름: {0} 나이: {1}'.format(name2,age2))

#38
number = '5,969,782,550'
result = number.replace(',', '')
result = int(result)
print(result, type(result))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
print(분기[0:7])
print(분기[-19:-12])

#40
data = '  삼성전자  '
result = data.strip()
print(result)

# 41
ticker = 'btc_krw'
result = ticker.upper()
print(result)

# 42
ticker = 'BTC_KRW'
result = ticker.lower()
print(result)

# 43
string = 'hello world'
result = string.capitalize()
print(result)

# 44
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx', 'xls')))

#45
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#46
file_name = '2020_보고서.xlsx'
print(file_name.startswith('2020'))

#47
a = "hello world"
result = a.split()
print(result)

#48
ticker = "btc_krw"
result = ticker.split('_')
print(result[0])
print(result[1])

# 49
date = '2020-05-01'
reslut = date.split('-')
print(reslut)

# 50
date = "039490    "
reslut = date.strip()
print(reslut)


