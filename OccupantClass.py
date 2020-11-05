from package import *

class OccupantClass:

    def __init__(self, uuid, locationX, locationY, overlapFlag, counterFlag):
        self.uuid        = uuid
        self.location    = (locationX, locationY)
        self.overlapFlag = overlapFlag
        self.counterFlag = counterFlag

    # GETTER
    def get_uuid(self):
        return self.uuid

    def get_location(self):
        return self.location

    # SETTER
    def set_uuid(self, uuid):
        self.uuid = uuid

    def set_location(self, locationX, locationY):
        self.location = (locationX, locationY)

    def set_overlap(self, overlapFlag):
        self.overlapFlag = overlapFlag

    def set_counted(self, countedFlag):
        self.coutnerFlag = counterFlag

    # DISPLAY
    def to_string(self):
        print("UUID: {}".format(occupant.uuid))
        print("\tLocation: {}".format(occupant.location))
        print("\toverlapFlag: {}".format(occupant.location))
        print("\tcountedFlag: {}".format(occupant.location))

    # MISC
    def is_in_overlap(self):
        return self.overlapFlag

    def is_counted(self):
        return self.counterFlag

print( "Occupant Class Imported" )
