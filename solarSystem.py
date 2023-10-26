import turtle
import math

#universe constants
G = 0.1
dt = 0.9



class StarSystem:
    def __init__(self):
        self.__star = None
        self.__planets = []
        self.__moons = []
        self.__screen = turtle.Screen()
        self.__screen.bgcolor("#242626")

    def addPlanet(self, planet):
        self.__planets.append(planet)

    def addStar(self, star):
        self.__star = star

    def addMoon(self, moon):
        self.__moons.append(moon)

    def runSimulation(self):
        while True:
            for planet in self.__planets:
                planet.move()

            for moon in self.__moons:
                moon.move()

    def printInfo(self):
        print("Star:", self.__star.getName())
        print("Planets, sorted from closest to the sun to the furthest:")

        sortedList = sorted(self.__planets, key=lambda p: p.getDistance())

        for p in sortedList:
            print(p.getName(), "-", p.getDistance())


class StellarObject:
    def __init__(self, name, radius, mass, color):
        self.__name = name

        #pysical atributes
        self.__radius = radius
        self.__mass = mass
        self.x = None
        self.y = None

        #turtle stuff
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color(color)
        self.t.shapesize(self.__radius)


    def getRadiusInPixels(self):
        return self.__radius * 10
    
    def getMass(self):
        return self.__mass
    
    def getName(self):
        return self.__name

    



class Star(StellarObject):

    def __init__(self, name, radius, mass, color, x, y):
        super().__init__(name, radius, mass, color)
        self.x = x
        self.y = y

        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()

    
class MovingObject(StellarObject):

    def __init__(self, name, radius, mass, color, orbitableStar, distance, velX, velY):
        super().__init__(name, radius, mass, color)
        self.x = orbitableStar.x + orbitableStar.getRadiusInPixels() + self.getRadiusInPixels() + distance
        self.y = orbitableStar.y
        self.__orbitableStar = orbitableStar
        self.__distance = distance

        self.__velX = velX
        self.__velY = velY 

        self.t.up()
        self.t.goto(self.x, self.y)
        self.t.down()


    def getDistance(self):
        return self.__distance
    
    def move(self):
        #update positon       
        self.x = self.x + dt * self.__velX
        self.y = self.y + dt * self.__velY
        self.t.goto(self.x, self.y)
        
        #update velocity
        rX = self.__orbitableStar.x - self.x
        rY = self.__orbitableStar.y - self.y
        r = math.sqrt(rX**2 + rY**2)

        accX = G * self.__orbitableStar.getMass() * rX/r**3
        accY = G * self.__orbitableStar.getMass() * rY/r**3

        self.__velX = self.__velX + dt * accX
        self.__velY = self.__velY + dt * accY








SolarSystem = StarSystem()

sun = Star("Sun", 4, 5000, "yellow", 0, 0)
earth = MovingObject("Earth", 1, 5000, "blue", sun, 70, 0, 2)
moon = MovingObject("Moon", 0.5, 10, "grey", earth, 5, 0, 6)
jupiter = MovingObject("Jupiter", 2, 20000, "orange", sun, 250, 0, 1)
venus = MovingObject("Venus", 0.3, 400, "red", sun, 50, 0, 2)
europa = MovingObject("Europa", 0.3, 100, "white", jupiter, 40, 0, 5)
mercury = MovingObject("Mercury", 0.2, 600, "turquoise", sun, 30, 0, 2.3)

SolarSystem.addStar(sun)
SolarSystem.addPlanet(earth)
SolarSystem.addMoon(moon)
SolarSystem.addPlanet(jupiter)
SolarSystem.addPlanet(mercury)
SolarSystem.addMoon(europa)
SolarSystem.addPlanet(venus)



SolarSystem.printInfo()
SolarSystem.runSimulation()

    






        



