# -- coding: utf-8 --

msfs_mode = 1
icao = "eick"

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
    major_id = aircraftData.idMajor
    minor_id = aircraftData.idMinor

    if major_id in specificTables:
        specific_table, fallback_key = specificTables[major_id]
        result = specific_table.get(minor_id)
        if result is None:
            result = specific_table.get(fallback_key)
    else:
        result = genericTable.get(major_id, 0)

    return result

@AlternativeStopPositions
def customOffsetequal(aircraftData):
    return Distance.fromMeters(0)
    
Ter1 = CustomizedName ("Terminal - Gates (7-12) | Gate #§",1)
Carg = CustomizedName ("Cargo Terminal - Stands (13-20 | Stands #§",2)
Apr = CustomizedName ("Apron - Stands (1-6) | Stands #§",3)
GA = CustomizedName ("GAT - Stands (21-23) | Stands #§",4)

parkings = {
    GATE : {
        None : (),
        8 : (Ter1, ),
        9 : (Ter1, ),
    },

    0 : {
        None : (),
        1 : (Apr, ),
        2 : (Apr, ),
        3 : (Apr, ),
        4 : (Apr, ),
        5 : (Apr, ),
        6 : (Apr, ),
        7 : (Ter1, ),
        10 : (Ter1, ),
        11 : (Ter1, ),
        12 : (Ter1, ),
        13 : (Carg, ),
        14 : (Carg, ),
        15 : (Carg, ),
        16 : (Carg, ),
        18 : (Carg, ),
        20 : (Carg, ),
        21 : (GA, ),
        22 : (GA, ),
        23 : (GA, ),
    },
}