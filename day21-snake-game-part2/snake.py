from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  # self.segments 리스트에 객체(Turtle 클래스로 만듦)를 통째로 저장

    def reset(self):
        for seg in self.segments:  # 죽은 뱀을 화면 밖의 지점으로 보내서 안보이게 함
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # 0번째 세그먼트(머리)만 조작하여 움직이고, 나머지 세그먼트는 앞 세그먼트를 따라가게끔 설계
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # 상하좌우 이동 메서드. 방향을 180도 반대로 전환할 수 없게함
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
