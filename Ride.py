from Point import Point

class Ride:

    # #
    # Init function
    #
    # city is a link to the parent
    # index is the line where the ride is parsed in the input
    def __init__(self, city, index, a, b, x, y, s, f):
        self.city = city
        self.index = index

        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

        # Create points
        self.start = Point(a,b)
        self.end = Point(x,y)

        # Time relative start and end
        self.startRide = -1
        self.endRide = -1

    # #
    # A way to display a ride
    def __repr__(self):
        return "From " + str(self.start) + " to " + str(self.end) + ". s=" + str(self.s) + " and f=" + str(self.f)


    ###### METHODS ######

    # #
    # Calculates the number of time steps there is between the beginning
    def timeBeforeStart(self):
        return self.s - self.city.time

    # #
    # Get the weight of the ride based on the vehicle.
    # It will optimise the ride to set to each vehicle.
    def getWeight(self, vehicle):
        return max( self.timeBeforeStart(), self.start.distance(vehicle.position) )

    # #
    # Get the score of the ride when it's finished
    #
    # /!\ NOT WORKING /!\
    def getScore(self):
        score = self.f - self.endRide

        if score<0:
            return 0

        return score
