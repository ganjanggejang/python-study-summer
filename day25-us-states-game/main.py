import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(height=491, width=725)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# 못 맞춘 주 이름을 missing_states 리스트에 넣음
missing_states = [x for x in all_states if x not in guessed_states]

new_data_dict = {
    "states": missing_states
}

new_dataframe = pandas.DataFrame(new_data_dict)
new_dataframe.to_csv("new_data.csv")  # 새롭게 생성한 csv 파일


screen.exitonclick()
