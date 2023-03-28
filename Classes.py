import turtle

class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        #Using Polygon table
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()

square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)
print(square.interior_angles)
print(square.angle)

print(pentagon.sides)
print(pentagon.name)
#checkout KITE for documentation

#square.draw()
#pentagon.draw()
hexagon = Polygon(6, "Hexagon")
hexagon.draw()
