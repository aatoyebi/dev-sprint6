# This is where chapter 15 exercises go.
import copy
class Point(object):
	'''point'''
class Rectangle(object):
	'''rectangle'''

def main():
    blank = Point()
    blank.x = 3
    blank.y = 4

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0


def move_rectangle(rect, dx, dy):
	box.corner.x += dx
	box.corner.y += dy

def move_rectangle_new(box, dx, dy):
	box2 = copy.deepcopy(box)
	move_rectangle(box2, 8 , 9)	
	return box2



if __name__ == '__main__':
    main()
