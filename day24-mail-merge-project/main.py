# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# 편지 보낼 사람의 이름들을 names 리스트에 저장
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# \n 제거한 이름을 stripped_names 리스트에 저장
stripped_names = []
for name in names:
    stripped_name = name.strip("\n")
    stripped_names.append(stripped_name)

# 편지 내용을 letters 리스트에 저장
with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    letters = []
    for name in stripped_names:
        new_contents = contents.replace("[name]", f"{name}")
        letters.append(new_contents)

# 새로운 편지 파일 생성
for i in range(len(stripped_names)):
    with open(f"./Output/ReadyToSend/to_{stripped_names[i]}.txt", mode='w') as file:
        file.write(letters[i])
