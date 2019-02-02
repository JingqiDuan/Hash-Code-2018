class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # #
    # Allow to quickly display a point
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # #
    # Change the coordinates of the point
    def set(self, x, y):
        self.x = x
        self.y = y

    # #
    # Calculates the distance between this point and the point in parameter
    def distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    # #
    # Calculates the next move for an object to be directed to this point
    def goTo(self, point):

        # If we need to increase x
        if self.x > point.x:
            return [point.x +1, point.y]

        # If we need to decrease x
        elif self.x < point.x:
            return [point.x -1, point.y]

        # If x are equals
        else:

            #If we need to increase y
            if self.y > point.y:
                return [point.x, point.y +1]

            # If we need to decrease x
            elif self.y < point.y:
                return [point.x, point.y -1]

        return True

    ### Comparators ###

    # #
    # Set which parameters should be compared when 2 points are compared to be equal (p1 == p2)
    def __eq__(self, point):
        return (self.x == point.x) and (self.y == point.y)
