from Ride import Ride
from Vehicle import Vehicle

class City:

    # #
    # Init function
    #
    # @param string Path to the input file
    def __init__(self, filename):

        # Set the time
        self.time = 0

        # Save the filename
        self.filename = filename

        # List of rides
        self.ridesToDo = []
        self.ridesDone = []

        # Open the file
        with open(filename) as f:
            content = f.readlines()

        # Read the content of the target file
        content = [x.strip('\n') for x in content]

        infos = content[0].split(' ')
        infoRides = content[1:]

        # Extract the information from the first line
        self.R = int( infos[0] )
        self.C = int( infos[1] )
        self.F = int( infos[2] )
        self.N = int( infos[3] )
        self.B = int( infos[4] )
        self.T = int( infos[5] )

        # Create rides to do
        for i in range(self.N):
            infoRide = infoRides[i].split(' ')

            a = int( infoRide[0] )
            b = int( infoRide[1] )
            x = int( infoRide[2] )
            y = int( infoRide[3] )
            s = int( infoRide[4] )
            f = int( infoRide[5] )

            ride = Ride(self, i, a, b, x, y, s, f)

            self.ridesToDo.append(ride)

        # Create array of vehicles
        self.vehicles = [Vehicle(self, i) for i in range(self.F)]


    ### METHODS ###

    # #
    # Make the time run step by step
    def runTime(self):

        # Time running
        for self.time in range(self.T):

            # Select each vehicle to move it
            for v in range( len(self.vehicles) ):
                self.vehicles[v].nextStep()

    # #
    # Write the results in the output
    def saveOutput(self):
        output = ( self.filename.replace('.in', '.out') ).replace('inputs', 'outputs')
        file = open(output, "w")

        for v in range( len(self.vehicles) ):
            vehicle = self.vehicles[v]

            # Write the number of rides for this vehicle
            strVar = str( len(vehicle.pastRides) )

            for r in range( len(vehicle.pastRides) ):
                # Write the index of the ride that the vehicle will do
                strVar += " " + str( vehicle.pastRides[r].index )

            file.write( strVar  + '\n' )

        file.close()

    # #
    # Get the score of all single ride
    #
    # /!\ NOT WORKING /!\
    def getTotalScore(self):
        score = 0

        for r in range( len(self.ridesDone) ):
            score += self.ridesDone[r].getScore()

        return score
