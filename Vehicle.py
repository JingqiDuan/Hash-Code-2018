from Point import Point

class Vehicle:

    # #
    # Init function
    #
    # city is a link to the parent
    # index is the number associated with the vehicle
    def __init__(self, city, index):
        self.position = Point(0,0)
        self.index = index
        self.city = city

        self.inRide = False
        self.ride = self.nextRide()
        self.pastRides = []

    # #
    # Allow to quickly display a vehicle
    def __repr__(self):
        return "Vehicle n°" + str(self.index) + " at the position " + str(self.position)

    # #
    # Move the car to the next step
    def nextStep(self):

        if self.inRide:
            newPosition = self.ride.end.goTo( self.position )
            self.position.set(newPosition[0], newPosition[1])

        elif not(self.inRide) and (self.ride != False) and self.ride != None:
            newPosition = self.ride.start.goTo( self.position )

            if newPosition != True:
                self.position.set(newPosition[0], newPosition[1])

        # Check if we stop the ride
        if self.inRide and self.position == self.ride.end:
            # print("Stop ride ", self.ride)
            self.inRide = False
            self.ride.endRide = self.city.time
            self.pastRides.append(self.ride)
            self.ride = self.nextRide()

        # Check if we start the ride
        if not(self.inRide) and (self.ride != False) and (self.ride.start == self.position) and (self.ride.s <= self.city.time):
            self.inRide = True
            self.ride.startRide = self.city.time
            # print("Start ride", self.ride)


    # #
    # Find the next ride
    #
    # This function is subjected to optimisation
    def nextRide(self):

        if( len(self.city.ridesToDo) == 0 ):
            return False

        # Highest weight ever !
        weight = self.city.T

        for ride in self.city.ridesToDo:
            if ride.getWeight(self) < weight:
                weight = ride.getWeight(self)
                closestRide = ride

        # Change the array of rides
        self.city.ridesToDo.remove(closestRide)
        self.city.ridesDone.append(closestRide)

        return closestRide
