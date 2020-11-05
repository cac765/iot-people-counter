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
        for camera in _cameraArray:

            # check if building key does not exist
            if camera.buildingID not in _occupantDict:
                
                # create building key
                _occupantDict[ camera.buildingID ] = {}

            # check if room key does not exist
            if camera.roomID not in _occupantDict[ camera.buildingID ]:

                # create room key
                _occupantDict[ camera.buildingID ][ camera.roomID ] = []

            # populate room with occupants from camera
            _occupantDict[ camera.buildingID ][
                           camera.roomID ] = _populate_room( camera )

        # resolve double counted occupants
        _resolve_double_counting()
        

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
        for building in occupantDict:
            # iterate through rooms
            for room in occupantDict[ building ]:
                occupantDict[ building ][ room ] =_resolve_room(
                                              occupantDict[ building ][ room ] )
                

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
            if ( occupant.overlapFlag ):
                if ( occupant not in tempArray ):
                    tempArray.append( occupant )
                else:
                    tempArray.remove( occupant )
                    occupantArray.remove( occupant )
        return occupantArray


print( "People Counter Class Imported" )
