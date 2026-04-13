import tkinter as tk
from tkinter import messagebox
import turtle
from math import sqrt

from matplotlib.pylab import sort

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
def draw_triangle(a, b, c):
    x=(a**2+c**2-b**2)/(2*c)
    y=(a**2-x**2)**0.5
    coord=[[0,0],[c,0],[x,y]]
    center_x=(max(coord[0][0],coord[1][0],coord[2][0])+min(coord[0][0],coord[1][0],coord[2][0]))/2
    center_y=(max(coord[0][1],coord[1][1],coord[2][1])+min(coord[0][1],coord[1][1],coord[2][1]))/2 + min(coord[0][1],coord[1][1],coord[2][1])/2
    total_x=sort([coord[0][0],coord[1][0],coord[2][0]])[2]
    total_y=sort([coord[0][1],coord[1][1],coord[2][1]])[2]
    scale=350/max(total_x,total_y) 
    scaled_coord=[[coord[0][0]*scale,coord[0][1]*scale],[coord[1][0]*scale,coord[1][1]*scale],[coord[2][0]*scale,coord[2][1]*scale]]
    scaled_coord_with_center=[[scaled_coord[0][0]-center_x*scale,scaled_coord[0][1]-center_y*scale],[scaled_coord[1][0]-center_x*scale,scaled_coord[1][1]-center_y*scale],[scaled_coord[2][0]-center_x*scale,scaled_coord[2][1]-center_y*scale]]
    t.penup()
    t.hideturtle()
    t.pensize(6)
    t.speed(0)
    t.clear()
    t.goto(scaled_coord_with_center[0][0],scaled_coord_with_center[0][1])
    t.pendown()
    t.goto(scaled_coord_with_center[1][0],scaled_coord_with_center[1][1])
    t.goto(scaled_coord_with_center[2][0],scaled_coord_with_center[2][1])
    t.goto(scaled_coord_with_center[0][0],scaled_coord_with_center[0][1])
def calculate_perimeter(a, b, c):
    return a + b + c
def calculate_area(a, b, c, p):
    return sqrt(p * (p - a) * (p - b) * (p - c))
def run_calculations(a, b, c):
    if not is_triangle(a, b, c):
        messagebox.showerror("Error", "Not a valid triangle.")
        return
    perimeter = calculate_perimeter(a, b, c)
    area = calculate_area(a, b, c, perimeter / 2)
    # print(f"Perimeter: {perimeter}")
    # print(f"Area: {area}")
    draw_triangle(a, b, c)
    messagebox.showinfo("Triangle Information", f"Perimeter: {perimeter}\nArea: {area}\nRight Triangle: {'Yes' if is_right_triangle(a, b, c) else 'No'}\nLongest Side: {max(a, b, c)}\nMedium Side: {sorted([a, b, c])[1]}\nShortest Side: {min(a, b, c)}")
def main():
    global t
    root = tk.Tk()
    root.title("All About Triangles")
    label = tk.Label(root, text="All About Triangles")
    label.pack()
    entry_a = tk.Entry(root)
    entry_a.pack()
    entry_b = tk.Entry(root)
    entry_b.pack()
    entry_c = tk.Entry(root)
    entry_c.pack()
    button = tk.Button(root, text="Calculate Area", command=lambda: run_calculations(int(entry_a.get()), int(entry_b.get()), int(entry_c.get())))
    button.pack()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    # draw_triangle(4, 4, 4)
    t.penup()
    t.hideturtle()
    t.pensize(6)
    t.speed(0)
    t.clear()
    root.mainloop()
if __name__ == "__main__":
    main()