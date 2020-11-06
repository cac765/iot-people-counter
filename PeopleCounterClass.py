from package import *

"""
  class for managing the total counting of people from multiple spaces

  Author: Corey Cline
"""
class PeopleCounterClass:

    """
      Public
      Constructor

      Param: _cameraArray array of CameraClass objects -> CameraClass[]
      Param: _occupantDict nested dictionary of OccupantClass object arrays
             with rooms as keys and multiple room dictionaries with buildings
             as keys -> dict
    """
    def __init__( self, cameraArray = [], occupantDict = {} ):
        self._cameraArray = cameraArray
        self._occupantDict = occupantDict

    """
      Public
      Updates the occupant dictionary through checking and counting the camera
      data
    """
    def update_occupant_dict( self ):
        # initialize method

        # iterate through camera class array
        for camera in self._cameraArray:

            # check if building key does not exist
            if camera.buildingID not in self._occupantDict:
                
                # create building key
                self._occupantDict[ camera.buildingID ] = {}

            # check if room key does not exist
            if camera.roomID not in self._occupantDict[ camera.buildingID ]:

                # create room key
                self._occupantDict[ camera.buildingID ][ camera.roomID ] = []

            # populate room with occupants from camera
            self._occupantDict[ camera.buildingID ][
                                camera.roomID ] += self._populate_room( camera )
        print( "=====DEBUG" )
        self.print_occupant_dict()
        # resolve double counted occupants
        self._resolve_double_counting()
        

    """
      Private
      Helper method for update_occupant_dict
      Populates a roomID dictionary with counted occupant objects

      Param: camera CameraClass object to count occupants from

      Return: array of OccupantClass objects -> list
    """
    def _populate_room( self, camera: CameraClass ) -> list:
        occupantArray = []
        for occupant in camera.occupantArray:
            occupantArray.append( occupant )
        return occupantArray

    """
      Private
      Merges two given OccupantClass objects into a single occupant object using
      the first object as key data

      Param: thisObj OccupantClass object to merge into -> OccupantClass
      Param: otherObj OccupantClass object to merge from -> OccupantClass

      Return: OccupantClass newly merged object -> OccupantClass
    """
    def _merge_occupants( self, thisObj: OccupantClass,
                          otherObj: OccupantClass ) -> OccupantClass:
        mergedItem = OccupantClass( thisObj.uuid, 0, 0, True, True )
        return mergedItem

    """
      Private
      Resolves the double counting issues within the occupant dictionary
    """
    def _resolve_double_counting( self ):
        # iterate through buildings
        for building in self._occupantDict:
            # iterate through rooms
            for room in self._occupantDict[ building ]:
                self._occupantDict[ building ][ room ] = self._resolve_room(
                                    self._occupantDict[ building ][ room ] )
                

    """
      Private
      Resolves the overlapped occupants in a single room given the occupant
      array

      Param: occupantArray list of occupants in the room -> list

      Return: newly resolved list of occupants
    """
    def _resolve_room( self, occupantArray: list ) -> list:
        tempArray = []
        for occupant in occupantArray:
            print("=== occupant: {}".format(occupant.uuid))
            if ( occupant.overlapFlag ):
                print( "\t===Found overlap uuid: {}".format( occupant.uuid ) )
                if ( occupant.uuid not in tempArray ):
                    print("\t\t===Appending to temp array: {}".format(occupant.uuid))
                    tempArray.append( occupant.uuid )
                else:
                    print("\t\t===Duplicate found: {}".format(occupant.uuid))
                    tempArray.remove( occupant.uuid )
                    occupantArray.remove( occupant )
        return occupantArray

    """
      Public
      Display method for the occupant dictionary data
    """
    def print_occupant_dict( self ):
        for building in self._occupantDict:
            for room in self._occupantDict[ building ]:
                for occupant in self._occupantDict[ building ][ room ]:
                    print( occupant.to_string() )

    """
      Public
      Display method for the camera array data
    """
    def print_camera_array( self ):
        for camera in self._cameraArray:
            print( camera.to_string() )


print( "People Counter Class Imported" )
