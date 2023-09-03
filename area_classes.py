import math
class shape:
    def out(self):
        print('-----')
class triangle(shape): 
 
 def getdime(self):
        self.a=float(input("Enter side a of triangle : "))
        self.b=float(input("Enter side b of triangle : "))
        self.c=float(input("Enter side c of triangle : "))
 
 def area(self):
        s=(self.a+self.b+self.c)/2
        if s<=self.a or s<=self.b or s<=self.c:
            print("Triangle is not possible by this measurement.")
            return
        else:
            ar=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            print("Area of triangle =",ar)
 
 
class circle(shape): 
    def getdime(self):
        self.r=float(input("Enter radius of circle : "))
    def area(self):
        ar=math.pi*self.r*self.r
        print("Area of circle = ",ar)

class rectangle(shape): 
    def getdime(self):
        self.l=float(input("Enter length of rectangle : "))
        self.w=float(input("Enter width of rectangle : "))
    def area(self):
        ar=self.l*self.w
        print("Area of rectangle = ",ar)


t1=triangle() 
c1=circle()
r1=rectangle()

t1.getdime()
t1.area()
t1.out()
c1.getdime()
c1.area()
c1.out()
r1.getdime()
r1.area()