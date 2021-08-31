# 모듈: 특정 기능(함수, 변수, 클래스)이 구현되어있는 ㅏ일
# 패키지: 여러 모듈을 모아놓은 것
# 라이브러리: 여러 모듈과 패키지를 모아놓은 것

# 패키지를 사용하려면 설치해야함.
# File > Settings > day16-oop > "+" 아이콘 클릭 > 패키지 검색해서 설치

from prettytable import PrettyTable # "prettytable"이라는 패키지를 설치했음

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electirc"],
        ["Squirtle", "Water"],
        ["Charamander", "Fire"]
    ]
)

table.align = "l"

print(table)










