from package import *

"""
  Main driver method for the prototype classes

  Author: Corey Cline
"""
def main():
    # create cameras
    camA = CameraClass( "CamA", 234, 69, 0, 0, 0, 0 )
    camB = CameraClass( "CamB", 234, 69, 0, 0, 0, 0 )
    camC = CameraClass( "CamC", 235, 69, 0, 0, 0, 0 )
    camD = CameraClass( "CamD", 235, 69, 0, 0, 0, 0 )
    camE = CameraClass( "CamE", 237, 69, 0, 0, 0, 0 )
    camF = CameraClass( "CamF", 237, 69, 0, 0, 0, 0 )
    camG = CameraClass( "CamG", 191, 54, 0, 0, 0, 0 )
    camH = CameraClass( "CamH", 191, 54, 0, 0, 0, 0 )
    camI = CameraClass( "CamI", 192, 54, 0, 0, 0, 0 )
    camJ = CameraClass( "CamJ", 192, 54, 0, 0, 0, 0 )

    # create occupants detected by cameras
    occ1A       = OccupantClass( "1A", 0, 0, False, False )
    occ1AB_camA = OccupantClass( "1AB", 0, 0, True, False )
    occ1AB_camB = OccupantClass( "1AB", 0, 0, True, False )
    occ2AB_camA = OccupantClass( "2AB", 0, 0, True, False )
    occ2AB_camB = OccupantClass( "2AB", 0, 0, True, False )
    occ1B       = OccupantClass( "1B", 0, 0, False, False )
    
    occ1C       = OccupantClass( "1C", 0, 0, False, False )
    occ1CD_camC = OccupantClass( "1CD", 0, 0, True, False )
    occ1CD_camD = OccupantClass( "1CD", 0, 0, True, False )
    occ2CD_camC = OccupantClass( "2CD", 0, 0, True, False )
    occ2CD_camD = OccupantClass( "2CD", 0, 0, True, False )
    occ3CD_camC = OccupantClass( "3CD", 0, 0, True, False )
    occ3CD_camD = OccupantClass( "3CD", 0, 0, True, False )

    occ1E       = OccupantClass( "1E", 0, 0, False, False )
    occ1EF_camE = OccupantClass( "1EF", 0, 0, True, False )
    occ1EF_camF = OccupantClass( "1EF", 0, 0, True, False )
    occ1F       = OccupantClass( "1F", 0, 0, False, False )

    occ1G       = OccupantClass( "1G", 0, 0, False, False )
    occ2G       = OccupantClass( "2G", 0, 0, False, False )
    occ3G       = OccupantClass( "3G", 0, 0, False, False )
    occ1GH_camG = OccupantClass( "1GH", 0, 0, True, False )
    occ1GH_camH = OccupantClass( "1GH", 0, 0, True, False )
    occ1H       = OccupantClass( "1H", 0, 0, False, False )

    occ1I       = OccupantClass( "1I", 0, 0, False, False )
    occ2I       = OccupantClass( "2I", 0, 0, False, False )
    occ1J       = OccupantClass( "1J", 0, 0, False, False )
    occ2J       = OccupantClass( "2J", 0, 0, False, False )

    # populate camera occupant arrays
    camA.occupantArray = [ occ1A, occ1AB_camA, occ2AB_camA ]
    camB.occupantArray = [ occ1AB_camB, occ1B, occ2AB_camB ]
    camC.occupantArray = [ occ1C, occ1CD_camC, occ2CD_camC, occ3CD_camC ]
    camD.occupantArray = [ occ1CD_camD, occ2CD_camD, occ3CD_camD ]
    camE.occupantArray = [ occ1E, occ1EF_camE ]
    camF.occupantArray = [ occ1EF_camF, occ1F ]
    camG.occupantArray = [ occ1G, occ2G, occ3G, occ1GH_camG ]
    camH.occupantArray = [ occ1GH_camH, occ1H ]
    camI.occupantArray = [ occ1I, occ2I ]
    camJ.occupantArray = [ occ1J, occ2J ]

    # create people counter
    camArray = [ camA, camB, camC, camD, camE, camF, camG, camH, camI, camJ ]
    pcc = PeopleCounterClass( camArray )

    print( "Current occupant data: " )
    pcc.print_occupant_dict()

    print( "Updating with cameras: " )
    pcc.print_camera_array()
    
    pcc.update_occupant_dict()
    print( "Updated occupant data: " )
    pcc.print_occupant_dict()


if __name__ == "__main__":
    main()
