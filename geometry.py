#  File: geometry.py
#  Description: Assignment 5 - Basic Geometry
#  Student's Name: Kayla Mayberry
#  Student's UT EID: km35829
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/15/15
#  Date Last Modified: 10/16/15

import math

#function to check the equality of two floating point numbers
def is_equal(a, b):
	tolerance = 1.0e-16
	if (abs(a-b) < tolerance):
		return True
	else:
		return False

class Point:

	#initialize
	def __init__(self, x, y):
		self.x = x
		self.y = y

	#method to calculate the distance between two points
	def dist(self, other):
		distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
		return distance

	#method to print out a point with the right format
	def __str__(self):
		x = round(self.x, 3)
		y = round(self.y, 3)
		x = str(x)
		y = str(y)
		return str('(' + x + ', ' + y + ')')

	#method to check if two points are equal to each other
	def __eq__(self, other):
		if (self.x == other.x) and (self.y == other.y):
			return True
		else:
			return False

class Line:

	#initialize
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	#method to calculate the slope of a line
	def slope(self):
		if self.isVertical():
			return float('inf')
		else:
			slope = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
			return slope

	#method to check if a line is horizontal
	def isHorizontal(self): 
		if self.p1.y == self.p2.y:
			return True
		else:
			return False

	#method to check if a line is vertical
	def isVertical(self):
		if self.p1.x == self.p2.x:
			return True
		else:
			return False

	#method to find the x-intercept of the line
	def xIntercept(self):
		if self.isHorizontal():
			return float('inf')
		elif self.isVertical():
			return self.p1.x
		else:
			x = ( -(self.yIntercept()) / (self.slope()) )
			return x

	#method to find the y-intercept of the line
	def yIntercept(self):
		if self.isVertical():
			return float('inf')
		elif self.isHorizontal():
			return self.p1.y			
		else:
			y = self.p1.y - (self.slope() * self.p1.x)
			return y

	#method to check if two lines are parallel
	def isParallel(self, other):
		if is_equal(self.slope(), other.slope()) == True:
			return True
		else:
			return False

	#method to check if two lines are perpendicular
	def isPerpendicular(self,other):
		if self.isVertical():
			if other.isHorizontal():
				return True
			else:
				return False
		elif other.isVertical():
			if self.isHorizontal():
				return True
			else:
				return False
		else:
			slopeTest = (self.slope() * other.slope())
			slopeTest = round(slopeTest)
			if is_equal(slopeTest, -1.0) == True:
				return True
			else:
				return False

	#method to check if a point lies on a line
	def isOnLine(self, pt):
		if self.isVertical():
			if self.p1.x == pt.x:
				return True
			else:
				return False
		elif self.isHorizontal():
			if self.p1.y == pt.y:
				return True
			else:
				return False
		else:
			y = ((self.slope() * pt.x) + self.yIntercept())
			y = round(y, 5)
			if is_equal(y, pt.y) == True:
				return True
			else:
				return False

	#method to find the distance a point lies from a line
	def perpDist(self, pt):
		if self.isVertical():
			return abs(self.p1.x - pt.x)
		elif self.isHorizontal():
			return abs(self.p1.y - pt.y)
		else:
			b = pt.y - ((-1/self.slope()) * pt.x)
			pt2 = Point(0, b)
			if pt == pt2:
				x = 1
				y = ((-1/self.slope()) * x) + b
				pt2 = Point(x, y)
			line2 = Line(pt, pt2)
			intersection = self.intersectionPoint(line2)
			return pt.dist(intersection)

	#method to find the point where two lines intersect
	def intersectionPoint(self, other):
		if self.isParallel(other):
			return float('inf')
		elif self.isVertical():
			y = (other.slope() * self.p1.x) + other.yIntercept()
			return Point(self.p1.x, y)
		elif other.isVertical():
			y = (self.slope() * other.p1.x + self.yIntercept())
			return Point(other.p1.x, y)
		elif self.isHorizontal():
			x = (self.p1.y - other.yIntercept()) / other.slope()
			return Point(x, self.p1.y)
		elif other.isHorizontal():
			x = (other.p1.y - self.yIntercept()) / self.slope()
			return Point(x, other.p1.y)			
		else:
			x = (self.yIntercept() - other.yIntercept()) / (other.slope() - self.slope())
			y = (other.slope() * x + other.yIntercept())
			return Point(x, y)

	#method to print out the equation of a line
	def __str__(self):
		y = round(self.p1.y, 3)
		x = round(self.p1.x, 3)
		slope = round(self.slope(), 3)
		yInt = round(self.yIntercept(), 3)
		y = str(y)
		x = str(x)
		slope = str(slope)
		yInt = str(yInt)
		if self.isVertical():
			return str('x = ' + y)
		elif self.isHorizontal():
			return str('y = ' + x)
		else:
			return str('y = ' + slope + 'x + ' + yInt)

class Circle:

	#initialize
	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	#method to find the circumference of a circle
	def circumference(self):
		return 2 * math.pi * self.radius

	#method to find the area of a circle
	def area(self):
		return math.pi * (self.radius) ** 2

	#method to check if a point is contained within a circle
	def containsPoint(self, pt):
		if self.center.dist(pt) < self.radius:
			return True
		else:
			return False 

	#method to check if a line is tangent to a circle
	def hasTangentLine(self, line):
		distance = line.perpDist(self.center)
		distance = round(distance, 4)
		if is_equal(distance, self.radius):
			return True
		else:
			return False

	#method to print out a circle object
	def __str__(self):
		radius = round(self.radius, 3)
		radius = str(radius)
		center = str(self.center)
		return str('Circle: \n' + '  Radius = ' + radius + '\n  Center = ' + center)

def main():

	# open file "geometry.txt" for reading
	file = open ('geometry.txt', 'r')

	# read the coordinates of Point A
	pointA = file.readline()
	pointA = pointA.strip()
	pointA = pointA.split(" ")
	x = float(pointA[0])
	y = float(pointA[1])
	pointA = Point(x, y)

	# print Point A
	print(pointA)

	# read the coordinates of Point B
	pointB = file.readline()
	pointB = pointB.strip()
	pointB = pointB.split(" ")
	x = float(pointB[0])
	y = float(pointB[1])
	pointB = Point(x, y)

	# print Point B
	print(pointB)

	# print the distance between A and B
	print(pointA.dist(pointB))

	# create a line AB
	lineAB = Line(pointA, pointB)

	# print the slope of AB
	print(lineAB.slope())

	# print the x-intercept of the line AB
	print(lineAB.xIntercept())

	# print the y-intercept of the line AB
	print(lineAB.yIntercept())

	# read the coordinates of Point C
	pointC = file.readline()
	pointC = pointC.strip()
	pointC = pointC.split(" ")
	x = float(pointC[0])
	y = float(pointC[1])
	pointC = Point(x, y)	
			 
	# read the coordinates of Point D
	pointD = file.readline()
	pointD = pointD.strip()
	pointD = pointD.split(" ")
	x = float(pointD[0])
	y = float(pointD[1])
	pointD = Point(x, y)	

	# create a line CD
	lineCD = Line(pointC, pointD)

	# print the string representation of the line AB
	print(lineAB)

	# print the string representation of the line CD
	print(lineCD)

	# print if the lines AB and CD are parallel or not
	print(lineAB.isParallel(lineCD))

	# if they are not parallel, print the intersection point of AB and CD
	if (lineAB.isParallel(lineCD)):
		None
	else:
		print(lineAB.intersectionPoint(lineCD))

	# print if the lines AB and CD are perpendicular or not
	print(lineAB.isPerpendicular(lineCD))

	# read the radius of circle1 and the coordinates of its center
	circle1 = file.readline()
	circle1 = circle1.strip()
	circle1 = circle1.split(" ")
	radius = float(circle1[0])
	x = float(circle1[1])
	y = float(circle1[2])
	circle1 = Circle(Point(x, y), radius)

	# read the radius of circle2 and the coordinates of its center
	circle2 = file.readline()
	circle2 = circle2.strip()
	circle2 = circle2.split(" ")
	radius = float(circle2[0])
	x = float(circle2[1])
	y = float(circle2[2])
	circle2 = Circle(Point(x, y), radius)
	
	# print the string representations of circle1 and circle2
	print(circle1)
	print(circle2)

	# read the coordinates of Point P
	pointP = file.readline()
	pointP = pointP.strip()
	pointP = pointP.split(" ")
	x = float(pointP[0])
	y = float(pointP[1])
	pointP = Point(x, y)

	# read the coordinates of Point Q
	pointQ = file.readline()
	pointQ = pointQ.strip()
	pointQ = pointQ.split(" ")
	x = float(pointQ[0])
	y = float(pointQ[1])
	pointQ = Point(x, y)

	# determine if point P is inside circle1
	print(circle1.containsPoint(pointP))

	# determine if point Q is inside circle1
	print(circle1.containsPoint(pointQ))

	# print whether line CD is tangent to circle2
	print(circle2.hasTangentLine(lineCD))

	# close file "geometry.txt"
	file.close()

main()