import turtle
turt = turtle.Turtle()
turt.screen.bgcolor('black')
turt.pensize(2)
turt.color('green')
turt.left(90)
turt.backward(100)
turt.speed(9000)
turt.shape('turtle')

def treeLove(i):
    if i < 10:
        return i
    else:
        turt.forward(i)
        turt.color('red')
        turt.circle(2)
        turt.color('gold')
        turt.left(30)
        treeLove(3*i/4)
        turt.right(60)
        treeLove(3*i/4)
        turt.left(30)
        turt.backward(i)
    
treeLove(100)
turtle.done()
