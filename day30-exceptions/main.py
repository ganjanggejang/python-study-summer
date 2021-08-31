"""
try:
    에러가 날지 안날지 궁금한 코드 작성
except condition-a:
    condition-a에 해당하는 에러가 try 블록에서 발생시 코드 실행
except condition-b:
    condition-b에 해당하는 에러가 try 블록에서 발생시 코드 실행
else:
    try 블록에서 에러가 없을 때 실행
finally:
    try 블록에서의 에러 여부와 상관없이 실행
"""

try:
    file = open("a-file.txt")
    a_dict = {"key": "value"}
    print(a_dict["ss"])  # 에러
except FileNotFoundError:
    file = open("a-file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"{error_message} That key does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise Exception("나만의 에러 빼애액")  # raise는 에러 만드는 키워드


