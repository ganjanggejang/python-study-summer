# *args --> 여러 개(개수 제한 x)의 인자를 함수로 받고자 할 때 씀
# 여러 개의 인자는 하나의 튜플 묶음이 되어 함수로 들어옴 (튜플은 시퀀스이므로 그걸 이용해서 코딩)


def sum(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# **kw --> my_function(keyword='val') 이렇게 함수를 실행하여 인자를 받으면
# keyword는 키, val은 값으로 묶은 딕셔너리가 함수로 들어옴


def calculate(num, **keywordarg):
    num += keywordarg["add"]  # add가 키인 딕셔너리의 값을 더해줌
    num *= keywordarg["multiply"]  # multiply가 키인 딕셔너리의 값을 곱해줌
    # 요런식으로 작성하면 키워드 인자 사용 가능
    return num


calculate(2, add=3, multiply=5)  # add, multiply 키워드 인자 사용 가능


# 그냥인자, *인자, **인자 순으로 사용 가능


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
# 결과값 --> 4 (7,3,0) {'x': 10, 'y': 64}
