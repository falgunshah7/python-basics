class Polygon:
    def render(self):
        print("Rendering a polygon")

class Square(Polygon):
    def render(self):
        print("Rendering a square")

class Circle(Polygon):
    def render(self):
        print("Rendering a circle")

# create a list of Square
s1 = Square()
s1.render()

# create a list of Circle
c1 = Circle()
c1.render()

p1 = Polygon()
p1.render()