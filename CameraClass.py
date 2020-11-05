from package import *

class CameraClass:
    
    def __init__(self, devID, roomID, buildingID, minX, maxX, minY, maxY):
        self.devID         = devID
        self.roomID        = roomID
        self.buildingID    = buildingID
        self.occupantArray = []
        self.overlap       = (minX, minY, maxX, maxY)

    # GETTER
    def get_num_occupants(self):
        return len(self.occupantDict)

    def get_device_id(self):
        return self.devID

    def get_room_id(self):
        return self.roomID

    def get_building_id(self):
        return self.buildingID

    def get_overlap(self):
        return self.overlap

    def get_occupant(self, uuid):
        for occupant in self.occupantArray:
            if uuid == occupant.uuid:
                return uuid
        return None
    
    # SETTER
    def set_device_id(self, devID):
        self.devID = devID

    def set_room_id(self, roomID):
        self.roomID = roomID

    def set_building_id(self, buildingID):
        self.buildingID = buildingID
    
    def set_overlap(self, minX, maxX, minY, maxY):
        self.overlap = (minX, minY, maxX, maxY)

    # DISPLAY
    def print_occupants(self):
        for occupant in self.occupantArray:
            occupant.to_string()


print( "Camera Class Imported" )
