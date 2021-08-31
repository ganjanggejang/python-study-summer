# /user/Project/talk.ppt --> root에서부터 시작하는 경로 표시 방식
# ./talk.ppt 아니면 그냥 talk.ppt --> 현재 Project 폴더에 있을 때 (같은 층위에 있을 때) 사용함
# ../report.docx --> Project 폴더 바깥의 user 폴더(한 단계 위)에 접근할 때 사용함

with open("../../Desktop/test.txt") as file:
    contents = file.read()
    print(contents)
