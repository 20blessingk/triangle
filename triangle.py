#Made by Kyle Blessing
### TRIANGLE CONGRUITY CHECKER ###

from graphics import *

def main():
    win = GraphWin('Draw a Triangle', 800, 600)
    '''
 #   win.yUp() # right side up coordinates
    win.setBackground('yellow')
    message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)
    '''

    instructions = Text(Point(win.getWidth()/2, 40),
                                        "Enter your name.\nThen click the mouse.")
    instructions.draw(win)

    entry1 = Entry(Point(win.getWidth()/2, 200),10)
    entry1.draw(win)

    Text(Point(win.getWidth()/2, 230),'Name:').draw(win) # label for the Entry
    
    win.getMouse()  # To know the user is finished with the text.

    name = entry1.getText() 

    greeting1 = 'Hello, ' + name + '!'
    Text(Point(win.getWidth()/3, 150), greeting1).draw(win)
                     
    greeting2 = 'Bonjour, ' + name + '!'
    Text(Point(2*win.getWidth()/3, 100), greeting2).draw(win)

    instructions = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    instructions.draw(win)
    
    instructions.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()

