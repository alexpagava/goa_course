from turtle import*

speed(30)
#we want paint a house
forward(200)
#step1:draw a squaer

color("purple")
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of squaer

#drawing a door


forward(70)
color("yellow")
left(90)
begin_fill()
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()