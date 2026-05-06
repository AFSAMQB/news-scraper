import tkinter as tk

# Create window
root = tk.Tk()
root.title("Circle Click Program")
root.geometry("400x400")

# Create canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

click_count = 0  # Counter

def draw_circle(event):
    global click_count
    click_count += 1

    radius = 30

    x, y = event.x, event.y

    # Determine quadrant
    if x < 200 and y < 200:
        # Top-left → filled RED
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                           fill="red", outline="red")

    elif x >= 200 and y < 200:
        # Top-right → unfilled RED
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                           outline="red", width=2)

    elif x >= 200 and y >= 200:
        # Bottom-right → filled BLUE
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                           fill="blue", outline="blue")

    else:
        # Bottom-left → unfilled BLUE
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                           outline="blue", width=2)

    # Close window after 12 clicks
    if click_count >= 12:
        root.destroy()

# Bind mouse click
canvas.bind("<Button-1>", draw_circle)

# Run program
root.mainloop()