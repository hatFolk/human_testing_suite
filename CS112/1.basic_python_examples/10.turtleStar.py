# draw a star using turtle graphics.

# bring all of the turtle graphics code in, so we can use it.
import turtle

# let's choose a color other than black.
turtle.color("red")

#draw just half a line, since we're starting in the center of the palette.
turtle.forward(50)
#turn 144 degrees to the right.
turtle.right(144)

# draw a full length, turn again.
turtle.forward(100)
turtle.right(144)

# draw a full length, turn again.
turtle.forward(100)
turtle.right(144)

# draw a full length, turn again.
turtle.forward(100)
turtle.right(144)

# draw a full length, turn again.
turtle.forward(100)
turtle.right(144)

# draw the other half of the original line.  No need to turn since we're done.
turtle.forward(50)

# let's hide the turtle (arrow head) so it looks better.
turtle.hideturtle()

# print this to the console and wait for 'input', so that the user can see our wonderful creation!
input("\n\npress enter to quit...")
