# open(), read()

file = open("my_file.txt")  # file에 파일 객체 저장.
contents = file.read()  # 객체 자체를 print할 수 없으므로 read()로 내용물 추출
print(contents)
file.close()  # 파일을 열어놓으면 컴퓨터 자원을 소모하므로 보통 다 쓰면 닫아줌.

# with as 를 사용하면 파일을 자동으로 열고 닫음.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# 기본적으론 읽기 모드이므로 쓰기모드("w") 또는 추가모드("a")로 변경해준 다음 내용을 추가할 수 있음.
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
    print(contents)
