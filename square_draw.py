import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    stephane = turtle.Turtle()
    turn_times = 4
    turn_count = 0
    while (turn_count < turn_times):
        stephane.forward(100)
        stephane.right(90)
        turn_count = turn_count + 1

    window.exitonclick()

draw_square()
