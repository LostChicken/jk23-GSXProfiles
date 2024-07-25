# -- coding: utf-8 --

msfs_mode = 1
icao = "haab"

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

    table = {
        0: 0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )
    
Terminal1 = CustomizedName ("Terminal 1 - Gates (N1-N9) | Gate N#§",1)
Terminal2 = CustomizedName ("Terminal 2 - Gates (N10-N25) | Gate N#§",2)
GAT = CustomizedName ("GAT and Storage - Stands (G1-G48) | Stand#§",3)
Cargo = CustomizedName ("Cargo Ramp - Stands (C1-C8) | Stand#§",4)
Storage = CustomizedName ("Storage Positions - (S1-S22) | Gate S#§",5)

parkings = {
	GATE_N : {
		None : ( ),
		1 : (Terminal1, ),
		2 : (Terminal1, ),
		3 : (Terminal1, ),
		4 : (Terminal1, ),
		5 : (Terminal1, ),
		6 : (Terminal1, ),
		7 : (Terminal1, ),
		8 : (Terminal1, ),
		9 : (Terminal1, ),
		
		10 : (Terminal2, ),
		11 : (Terminal2, ),
		12 : (Terminal2, ),
		13 : (Terminal2, ),
		14 : (Terminal2, ),
		15 : (Terminal2, ),
		16 : (Terminal2, ),
		17 : (Terminal2, ),
		18 : (Terminal2, ),
		19 : (Terminal2, ),
        20 : (Terminal2, ),
        21 : (Terminal2, ),
	},
	
	PARKING : {
		None : ( ) ,
		"1G" : (GAT, ),
		"2G" : (GAT, ),
		"3G" : (GAT, ),
		"4G" : (GAT, ),
		"5G" : (GAT, ),
		"6G" : (GAT, ),
		"7G" : (GAT, ),
		"8G": (GAT, ),
		"9G" : (GAT, ),
		"10G" : (GAT, ),
		"11G" : (GAT, ),
		"12G" : (GAT, ),
		"13G" : (GAT, ),
		"14G" : (GAT, ),
		"15G" : (GAT, ),
		"16G" : (GAT, ),
		"17G" : (GAT, ),
		"18G" : (GAT, ),
		"19G" : (GAT, ),
		"20G" : (GAT, ),
		"21G" : (GAT, ),
        "22G" : (GAT, ),
        "23G" : (GAT, ),
        "24G" : (GAT, ),
        "25G" : (GAT, ),
        "26G" : (GAT, ),
        "27G" : (GAT, ),
        "28G" : (GAT, ),
        "29G" : (GAT, ),
        "30G" : (GAT, ),
        "31G" : (GAT, ),
        "32G" : (GAT, ),
        "33G" : (GAT, ),
        "34G" : (GAT, ),
		"35G" : (GAT, ),
		"36G" : (GAT, ),
		"37G" : (GAT, ),
		"38G" : (GAT, ),
		"39G" : (GAT, ),
		"40G" : (GAT, ),
		"41G" : (GAT, ),
		"42G" : (GAT, ),
        "43G" : (GAT, ),
        "44G" : (GAT, ),
        "45G" : (GAT, ),
        "46G" : (GAT, ),
        "47G" : (GAT, ),
		"48G" : (GAT, ),
		"1C" : (Cargo, ),
		"2C" : (Cargo, ),
		"3C" : (Cargo, ),
		"4C" : (Cargo, ),
		"5C" : (Cargo, ),
		"6C" : (Cargo, ),
		"7C" : (Cargo, ),
		"8C" : (Cargo, ),
        "22N" : (Terminal2, ),
        "23N" : (Terminal2, ),
        "24N" : (Terminal2, ),
        "25N" : (Terminal2, ),
        "23S" : (Storage, ),
        "24S" : (Storage, ),
        "25S" : (Storage, ),
        "26S" : (Storage, ),
        "27S" : (Storage, ),
		},

	GATE_S: {
		None : ( ),
		1 : (Storage, ),
		2 : (Storage, ),
		3 : (Storage, ),
		4 : (Storage, ),
		5 : (Storage, ),
		6 : (Storage, ),
		7 : (Storage, ),
		8 : (Storage, ),
		9 : (Storage, ),
		10 : (Storage, ),
		11 : (Storage, ),
		12 : (Storage, ),
		13 : (Storage, ),
		14 : (Storage, ),
		15 : (Storage, ),
		16 : (Storage, ),
		17 : (Storage, ),
		18 : (Storage, ),
		19 : (Storage, ),
		20 : (Storage, ),
		21 : (Storage, ),
		22 : (Storage, ),
		},
}