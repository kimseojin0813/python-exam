# 101

#  bool 자료형

# 111
# a = str(input(''))
# print(a * 2)


# 112
# a = int(input('입력:'))
# print(a + 10)

# 113
# a = int(input('입력:'))
# if a % 2 ==0:
#     print('짝수')
# else:
#     print('홀수')    

# 114
# a = int(input('입력:'))
# if a + 20 > 255:
#     print(225)
# else:
#     print(a + 20) 

# 115
# a = int(input('입력:'))
# if a - 20 > 255:
#     print(255)
# elif a - 20 < 0:
#     print(0)
# else:
#     print(a - 20)

# 116
# a = str(input('현재시간:'))
# if a[-2:] == '00':
#     print('정각')
# else:
#     print('정각x')    

# # 117
# fruit = ["사과", "포도", "홍시"]

# user = input("좋아하는 과일은:")

# # for 변수 in 리스트, 튜플, 문자열, 딕션어리:

# if user in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')    

# 118

# it_company_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# user = input('회사명 :')

# if user in it_company_list:
#     print('입사희망 회사입니다.')
# else:
#     print('입사를 희망하지 않는 회사 입니다') 

 #119

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# user = input('제가 좋아하는 계절은:')

# # if 변수 in 딕션어리: 사용할 때, in 뒤에 딕션너리가 올때는 변수 key 값을 비교해야 된다.
# if user in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.') 

# 120

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# user = input('좋아하는 과일은:')

# if user in fruit.values():
#     print('장답입니다.')
# else:
#     print('오답입니다.')

# 121

# a = input('입력:')

# b = a.islower()

# if b == True:
#     print(a.upper())
# else:
#     print(a.lower())

# 122

# score = int(input('score:'))

# if 81 <= score <= 100:
#     print('grade is A')
# elif 61 <= score<=80:
#     print('grade is B')
# elif 41 <= score <= 60:
#     print('grade is C')
# elif 21 <= score <= 40:
#     print('grade is D')
# else:
#     print('grade is E')

# 123

# 환율 = {
#     '달러': 1167,
#     '엔': 1.096,
#     '유로' : 1268,
#     '위안' : 171
# }

# user =  input('입력:')

# # result = user.split(' ')

# # split() 함수로 생성된 리스트를 언팩킹 한 것...
# num, currency = user.split(' ')

# print(float(num) * 환율[currency], '원')

#124

# user = input('숫자 세게 입력:')

# num1, num2, num3 = user.split()
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1> num2 and num1 > num3:
#     print(num1)
# elif num2 >  num1 and num2 >num3:
#     print(num2)
# else:
#     print(num3)    

#  125

# number = input('전화 번호:')

# num = number.split('-')[0]

# if num == "011":
#     com =" skt"
# elif num == '016':
#     com = 'kt'    
# elif num == '019':
#     com == 'lgu'

#126

# zip_code = input('우편번호:')
# zip_code = zip_code[:3]

# if zip_code in ['010', '011', '012']:
#     print('강북구')
# elif zip_code in ['013', '014', '015']:
#     print('도봉구')
# elif zip_code in ['016', '017', '018', '019']:
#     print('노원구')
# else:
#     print('잘못 됨')



#127

# user = input('주민번호:')
# user = user.split('-')[1][0]

# if user == '1' or '3':
#     print('남자')
# elif user == '2' or '4':
#     print('여자')
# else:
#     print('잘못 됨')

# 128

# 주민번호 = input('주민번호:')

# 뒷자리 = 주민번호.split('-')[1]

# if 0<= int(뒷자리[1:3]) <=8:
#     print('서울입니다')
# else:
#     print('서울이 아닙니다.')


# 129

# num = input('주민등록 번호:')

# 계산1 = int(num[0]) * 2 + \
#         int(num[1]) * 3 + \
#         int(num[2]) * 4 + \
#         int(num[3]) * 5 + \
#         int(num[4]) * 6 + \
#         int(num[5]) * 7 + \
#         int(num[7]) * 8 + \
#         int(num[8]) * 9 + \
#         int(num[9]) * 2 + \
#         int(num[10]) * 3 + \
#         int(num[11]) * 4 +\
#         int(num[12]) * 5 
       
# 계산2 = 11 -  (계산1 % 11)
# 계산2 = str(계산2)

# if num[-1] == 계산2[-1]:
#     print('유효하지 않는번호입니다')
# else:
#     print('유효한 번호입니다.')


# 130

# import requests

# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if (시가 + 변동폭) > 최고가:
#     print('상승장')
# else:
#     print('하락장')


#131

# fruits = ["사과", "귤", "수박"]

# for i in fruits: # 리스트, 튜플, 딕션어리, 문자열
#     print(i)

# 132

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#  print("#####")


# for 변수 in ["A", "B", "C"]:
#  print(변수)

# for 변수 in ["A", "B", "C"]:
#  print("출력:", 변수)

# for 변수 in ['10', '20', '30']:
#     print(변수)

# 리스트 = [100, 200, 300]
# for i in 리스트:
#     print(i +10)


# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트:
#     print(len(i))


# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0])

# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print(f'3 * {i}')

# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print(f'3 * {i} = {i * 3}')


# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[1::]:
#     print(i)

# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::2]:
#     print(i)

# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::-1]:
#     print(i)

# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i < 0:
#         print(i)


# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in  리스트:
#     if i % 3 == 0 and i < 20:
#         print(i)


# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) >= 3:
#         print(i)


# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)


# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.islower():
#         print(i)


# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i.capitalize())


# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     print(i.split('.')[0])

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if i.split('.')[1] == 'h':
#         print(i)
        
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if i.split('.')[1] == 'h' or i.split('.')[1] == 'c' :
#         print(i)

# for i in range(100):
#     print(i)

# for i in range(2002,2051,4):
#     print(i)

# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)

# for i in range(99,-1, -1):
#     print(i)

# for i in range(0,10):
#     print(i/10)

# for i in range(1, 10 ):
#     print(f'3x{i} = {3 * i}')

# for i in range(1, 10, 2  ):
#      print(f'3x{i} = {3 * i}')

# a = 0
# for i in range(1, 11):
#     a = a + i
# print(a)

# a = 0
# for i in range(1, 11, 2):
#     a = a + i
# print(a)

# a = 1
# for i in range(1, 11):
#     a = a * i
# print(a)

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])
    

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])
    
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(len(price_list)-1 -i, price_list[i])

# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, len(price_list)):
#      print( 90+10*i, price_list[i])


# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) -1 ):
#     print(my_list[i], my_list[i +1])


# my_list = ["가", "나", "다", "라", "마"]
# for i in range(1, len(my_list) -1  ):
#     print(my_list[i-1], my_list[i ], my_list[i+1])

# my_list = ["가", "나", "다", "라"]
# for i in range(3,0,-1  ):
#     print(my_list[i], my_list[i -1])

# my_list = [100, 200, 400, 800]

# for i in range(1, len(my_list)):
#     print(my_list[i] - my_list[i-1])

# my_list = [100, 200, 400, 800, 1000, 1300]

# for i in range(1, len(my_list) -1):
#     print((my_list[i-1] + my_list[i] + my_list[i+1] /3) )

# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# a =[]
# for i in range(len(low_prices)):
#     a.append(high_prices[i]- low_prices[i])
# print(a)

# apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]

# ㅁ = {
#     '시가':[100, 200, 300],
#     '종가': [80, 210, 330]
#     }

# ㅁ = {
#     '10/10': [80, 110, 70, 90],
#     '10/11': [210, 230, 190, 200]
# }

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,' 호')

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for  j in i:
#         print(j,' 호')

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for  j in i[::-1]:
#         print(j,' 호')


# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in apart:
#    for j in i:
#        print(j,' 호')
#        print('-------------')



# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#    for j in i:
#        print(j,' 호')
#    print('-------------')

# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#    for j in i:
#        print(j,' 호')
# print('-------------')


# data = [
#  [ 2000,  3050,  2050,  1980],
#  [ 7500,  2050,  2050,  1980], 
#  [15450, 15050, 15550, 14900]
#  ]

# result = []
# for i in data:
#     for j in i:
#         result.append(j*1.00014)

# print(result)



# data = [
#  [ 2000,  3050,  2050,  1980],
#  [ 7500,  2050,  2050,  1980], 
#  [15450, 15050, 15550, 14900]
#  ]

# result = []
# for i in data:
#     data = []
#     for j in i:
#         data.append(j*1.00014)
#         result.append(data)

# print(result)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc[1:]:
#     print(i[3])


# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#    if i[3] > 150:
#     print(i[3])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#    if i[3] >= i[0]:
#     print(i[3])


# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# volatility = []
# for i in ohlc[1:]:
#    volatility.append(i[1]-i[2])
# print(volatility)

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[3] > i[0]:
#         print(i[1]-i[2])

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# a = 0
# for i in ohlc[1:]:
#     a = a + (i[3]-i[0])

# print(a)






















































