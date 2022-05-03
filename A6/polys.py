"""
Kevin Joseph
RUID: 212003391
Object-Oriented Programming (Spring 2022)
A6: This python file contains seven classes for points and polygons.
"""
import math

class Point:

    def __init__(self, init_x = 0, init_y = 0):
        """
        This is the constructor for the Point class. The constructor has two parameters: init_x and init_y, where the default values of each are 0 and 0, respectively.
        """ 
        self.__x = init_x
        self.__y = init_y
   
    def translate(self, s, t):
        """
        This method translates the Point (self) using the two parameters: s and t, where s is the translation in the x direction and t is the translation in the y direction.
        """
        self.__x += s
        self.__y += t
   
    def rotate(self, theta):
        """
        This method rotates the Point (self) using the sole parameter: theta, where theta is the angle of rotation in degrees and rotates the Point clockwise by the angle of rotation.
        """
        preX = self.__x
        preY = self.__y
        self.__x = ((preX*math.cos(math.radians(theta)))-(preY*math.sin(math.radians(theta))))
        self.__y = ((preX*math.sin(math.radians(theta)))+(preY*math.cos(math.radians(theta))))
    
    def distance(self, p):
        """
        This method calculates the distance between the Point (self) and the sole parameter: p, where p is the other Point to determine the distance with. This method returns the distance between the two points.
        """
        return math.sqrt(((self.__x-p.__x)**2) + ((self.__y-p.__y)**2))
   
    def left_of(self, q, r):
        """
        This method determines whether or not the Point (self) is to the left of the vector qr. If the Point (self) is to the left of the vector qr, the method returns True and False otherwise.
        """
        return ((((self.__x - q.__x)*(r.__y - q.__y)) - ((self.__y - q.__y)*(r.__x - q.__x))) < 0)
    
    def right_of(self, q, r):
        """
        This method determines whether or not the Point (self) is to the right of the vector qr. If the Point (self) is to the right of the vector qr, the method returns True and False otherwise.
        """
        return ((((self.__x - q.__x)*(r.__y - q.__y)) - ((self.__y - q.__y)*(r.__x - q.__x))) > 0)

    def __str__(self):
        """
        This method overloads the str operator and returns a valid String for the Point (self).
        """
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"

    def __repr__(self):
        """
        This method overloads the repr operator and returns a valid String representation for the Point (self).
        """
        return str(self)
    
class SimplePoly(Point):

    def __init__(self, *vertices):
        """
        This is the constructor for the SimplePoly class. This constructor has one parameter, *vertices, which is a non-keyworded variable length argument of the vertices to create the simple polygon. All polygon points are stored in a private instance list.
        """
        self.__pts = []
        for vertice in vertices:
            self.__pts.append(vertice)

    def __iter__(self):
        """
        This is the iterator for the SimplePoly class. This returns an iterable object and is implemented based on the SimplePolyIterator class.
        """
        return SimplePolyIterator(self.__pts)

    def translate(self, s, t):
        """
        This method translates the SimplePoly object (self) using the two parameters: s and t, where s is the translation in the x direction and t is the translation in the y direction. Each individual point is translated.
        """
        for vtx in self:
            Point.translate(vtx, s, t)
    
    def rotate(self, theta):
        """
        This method rotates the SimplePoly object (self) using the sole parameter: theta, where theta is the angle of rotation in degrees and rotates the SimplePoly object clockwise by the angle of rotation. Each individual point is rotated.
        """
        for vtx in self:
            Point.rotate(vtx, theta)

    def __len__(self):
        """
        This method overloads the len operator and returns the length of the SimplePoly object or in simpler terms, the amount of points that the SimplePoly object has.
        """
        return len(self.__pts)

    def __getitem__(self, i):
        """
        This method overloads the [] operator and returns the Point at the specified indice in the SimplePoly object. The index is checked for validity, and if it's not valid, an IndexError is raised.
        """
        if i < 0 or i >= len(self):
            raise IndexError("An invalid index was detected, please retry your request with a new index that is positive and less than the length of the polygon.")
        else:
            return self.__pts[i]

    def __str__(self):
        """
        This method overloads the str operator and returns a valid String for the StringPoly object. The String returned contains all of the points of the SimplePoly object.
        """
        astr = ""
        for vtx in self:
            astr += str(vtx) + " "
        return astr
    
    def perimeter(self):
        """
        This method returns the perimeter of the SimplePoly object.
        """
        perim = 0
        for i in range(len(self)):
            if i+1 < len(self):
                perim += Point.distance(self[i], self[i+1])
            else: 
                perim += Point.distance(self[i], self[0])
        return perim
    
class SimplePolyIterator():

    def __init__(self, lst):
        """
        This is the constructor for the SimplePolyIterator. This constructor has one parameter: lst, which is the passed list of points of the SimplePoly object. This constructor creates a index variable which is used to iterate in the next() method.
        """
        self.__pts = lst
        index = -1
    
    def __next__(self):
        """
        This method overloads the next operator. This method steps through the iterator instance and returns the next object whilst updating the index of the instance.
        """
        if index >= len(lst) - 1:
            raise StopIteration()
        index += 1
        return self.__pts[index]

class ConvPoly(SimplePoly):

    def __init__(self, *vertices):
        """
        This is the constructor for the ConvPoly class. This constuctor has one parameter: *vertices, which is the non-keyworded variable-length argument list that contains all of the vertices of the polygon. The vertices are each checked in order to ensure that they form a convex polygon before using the SimplePoly class constructor to create the ConvPoly object, otherwise an Exception is raised.
        """
        test = []
        for vtx in vertices:
            test.append(vtx)
        for i in range(len(test)):
            if i+2 < len(test):
                if not Point.right_of(test[i+2], test[i+1], test[i]):
                    raise Exception("The vertices do not create a convex polygon.")
            elif i+2 == len(test): 
                if not Point.right_of(test[0], test[i+1], test[i]):
                    raise Exception("The vertices do not create a convex polygon.")
        SimplePoly.__init__(self, *vertices)
    
class EquiTriangle(ConvPoly):

    def __init__(self, len):
        """
        This is the constructor for the EquiTraingle class. This consructor produces an equilateral triangle with its sole parameter: len, the length of each side and has its vertex at (0,0). Once each point is formed, a convex polygon is created for the equilateral triangle.
        """
        xVal = len/2
        yVal = xVal*math.sqrt(3)
        p1 = Point()
        p2 = Point(((-1.0)*xVal), ((-1.0)*yVal))
        p3 = Point(xVal, ((-1.0)*yVal))
        ConvPoly.__init__(self, p1, p2, p3)

    def area(self):
        """
        This method returns the area of the equilateral triangle.
        """
        a = Point.distance(self[1], self[2])
        return (math.sqrt(3)/4)*(a**2)
    
class Rectangle(ConvPoly):

    def __init__(self, len, width):
        """
        This is the constructor for the Rectangle class. This constructor has two parameters: len and width, where len is the length of the Rectangle and width is the width of the Rectangle. The vertex of the Rectangle is (0,0) and a convex polygon is created for the Rectangle.
        """
        p1 = Point(0, 0)
        p2 = Point(init_y=((-1)*width))
        p3 = Point(len, ((-1)*width))
        p4 = Point(init_x=len)
        ConvPoly.__init__(self, p1, p2, p3, p4)
    
    def area(self):
        """
        This method returns the area of the rectangle.
        """
        s1 = Point.distance(self[0], self[1])
        s2 = Point.distance(self[1], self[2])
        return abs(s1*s2)

class Square(Rectangle):

    def __init__(self, len):
        """
        This is the constructor for the Square class. This constructor has one parameter: len, which is the length of each side of the square. The Rectangle constructor is used in order to produce a Rectangle with all equal sides, thus a Square with all equal sides, len.
        """
        Rectangle.__init__(self, len, len)
