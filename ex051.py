# 51

movie_rank = [ '닥터스트레인지', '스플릿', '러키' ]

# 52

movie_rank.append('배트맨')

print(movie_rank)

# 53

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

movie_rank.insert(1, "슈퍼맨")

print(movie_rank)

# 54

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

del movie_rank[3] # 인덱스 : 3

print(movie_rank)

# 55

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

del movie_rank[2]
del movie_rank[2]

print(movie_rank)

# 56

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang2 + lang1

print(langs)

# 57

nums = [1, 2, 3, 4, 5, 6, 7]

print('max:', max(nums))
print('min:', min(nums))

# 58

nums = [1, 2, 3, 4, 5]

print(sum(nums))

# 59

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

result = len(cook)
print(result)

# 60

nums = [1, 2, 3, 4, 5]

result = sum(nums) / len(nums)
print(result)

# 61

price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])

# 62 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])

# 63

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[1::2])

# 64

nums = [1, 2, 3, 4, 5]

print(nums[::-1])

# 65

interest = ['삼성전자', 'LG전자', 'Naver']

print(interest[0], interest[2])

# 66

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(' '.join(interest))

# 67

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print('/'.join(interest))

# 68

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print('\n '.join(interest))

# 69

string = "삼성전자/LG전자/Naver"

print(string.split("/"))

# 70 

data = [2, 4, 3, 1, 5, 10, 9]

data.sort() # 리스트에 메서드 사용

print(data)

# 다른방법 : 전역함수 sorted()

data = [2, 4, 3, 1, 5, 10, 9]

data1 = sorted(data) # 새로운 리스트를 반환
print(data1)

# 71 

my_variable = ()
print(type(my_variable))

# 72

movie_rank = ('닥터스트레인지', '스플릿', '럭키')

# 73

a = (1,)
print(type(a))

# 74

# 튜플은 값 변경 X

# 75

t = 1, 2, 3, 4

# 76

t = ('a', 'b', 'c')

#77

interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 78

interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 79
# range(시작값, 끝값, step)

data = tuple(range(2, 100, 2))
print(data)

# 80

temp = ('apple', 'banana', 'cake')
a,b,c = temp   

# 81

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

# 82

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 83

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score = scores, _
print(valid_score)

# 84

temp = {}
print(type(temp))

# 85

a = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}

print(a)

# 86

a = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}

a['죠스바'] = 1200
a['월드콘'] = 1500
print(a)

# 87

ice = {
 '메로나': 1000,
 '폴로포': 1200,
 '빵빠레': 1800,
 '죠스바': 1200,
 '월드콘': 1500
 }

result = ice['메로나']
print(result)

# 88

ice = {
 '메로나': 1000,
 '폴로포': 1200,
 '빵빠레': 1800,
 '죠스바': 1200,
 '월드콘': 1500
 }

ice['메로나'] = 1300
print(ice)

# 89

ice = {
 '메로나': 1000,
 '폴로포': 1200,
 '빵빠레': 1800,
 '죠스바': 1200,
 '월드콘': 1500
 }

del ice['메로나']
print(ice)

# 90

#  없는 키를 이용해서 

# 91

inventory = {
    '메로나' : [300, 20],
    '비비빅' : [400, 3],
    '죠스바' : [250, 100]
}

print(inventory)

print(inventory['메로나'])

# 92

inventory = {
 "메로나": [300, 20],
 "비비빅": [400, 3],
 "죠스바": [250, 100]
 }

print(inventory['메로나'][0])

# 93

inventory = {
 "메로나": [300, 20],
 "비비빅": [400, 3],
 "죠스바": [250, 100]
 }

print(inventory['메로나'][1])

# 94 

inventory = {
 "메로나": [300, 20],
 "비비빅": [400, 3],
 "죠스바": [250, 100]
 }

inventory['월드콘'] = [500, 7]
print(inventory)

# 95

icecream = {
    '탱크보이': 1200,
    '폴라포': 1200,
    '빵빠레': 1800,
    '월드콘': 1500,
    '메로나': 1000
}

result = list(icecream.keys())
print(result)

# 96

icecream = {
    '탱크보이': 1200,
    '폴라포': 1200,
    '빵빠레': 1800,
    '월드콘': 1500,
    '메로나': 1000
}

result = list(icecream.values())
print(result)

# 97

icecream = {
    '탱크보이': 1200,
    '폴라포': 1200,
    '빵빠레': 1800,
    '월드콘': 1500,
    '메로나': 1000
}

result = sum(icecream.values())
print(result)

# 98

icecream = {
    '탱크보이': 1200,
    '폴라포': 1200,
    '빵빠레': 1800,
    '월드콘': 1500,
    '메로나': 1000
}


new_product = {
    '팥빙수':2700,
    '아맛나':1000
}

icecream.update(new_product)
print(icecream)

# 99

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
result = dict(zip(date, close_price))
print(result)


































