import turtle
import tkinter as tk


def get_curr_screen_geometry():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    geometry = root.winfo_geometry()
    root.destroy()
    return geometry


def get_curr_screen(geometry):
    return (int(geometry[0:geometry.find('x')]), int(geometry[geometry.find('x')+1:geometry.find('+')]))


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600, startx=get_curr_screen(
    get_curr_screen_geometry())[0]//4, starty=None)
wn.tracer(0)

# Paddle 1
paddleA = turtle.Turtle()
paddleA.speed(1)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)
# Paddle 2

# Ball

while True:
    wn.update()
