import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("grey")
    

    stephane = turtle.Turtle()
    turn_times = 4
    turn_count = 0

    stephane.shape("turtle")
    shape_colors = ["blue", "green", "yellow", "black"]
    while (turn_count < turn_times):
        stephane.color(shape_colors[turn_count])
        stephane.forward(100)
        stephane.right(90)
        turn_count = turn_count + 1

    window.exitonclick()

draw_square()
