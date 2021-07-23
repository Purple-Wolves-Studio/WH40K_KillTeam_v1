# T'au Empire Units Data Repo


units = [
    {   # Fire Warrior Unit List
        "model":"Fire Warrior",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Infantry",
            "Fire Warrior",
        ],
        "notes":"A Shas’la or Shas’ui is equipped with a pulse rifle and photon grenades",
        "types":[
            {   # Shas'la
                "name":"Shas'la",
                "points":8,
                "stats":{
                    "move":"6\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"4+",
                    "maxnum":""
                },
                "weapons":[
                    "Pulse Rifle",
                    "Photon Grenades",
                ],
                "wargear":[
                    "Pulse Carbine",
                    "Pulse Pistol",
                    "DS8 Tactical Support Turret"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Comms",
                    "Medic",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Shas’ui
                "name":"Shas'ui",
                "points":8,
                "stats":{
                    "move":"6\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Pulse Rifle",
                    "Photon Grenades",
                ],
                "wargear":[
                    "Pulse Carbine",
                    "Pulse Pistol",
                    "Markerlight"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual",  
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Pathfinder Unit List
        "model":"Pathfinder",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Infantry",
            "Pathfinder",
        ],
        "notes":"This model is armed with a pulse carbine, markerlight and photon grenades",
        "types":[
            {   # Pathfinder
                "name":"Pathfinder",
                "points":6,
                "stats":{
                    "move":"7\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":[
                    "Pulse Carbine",
                    "Markerlight",
                    "Photon Grenades",
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Comms",
                    "Demolitions",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Pathfinder Gunner
                "name":"Pathfinder Gunner",
                "points":7,
                "stats":{
                    "move":"7\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"3"
                },
                "weapons":[
                    "Pulse Carbine",
                    "Markerlight",
                    "Photon Grenades",
                ],
                "wargear":[
                    "Ion Rifle",
                    "Rail Rifle"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Sniper",
                    "Comms",
                    "Demolitions",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Pathfinder Shas'ui
                "name":"Pathfinder Shas'ui",
                "points":7,
                "stats":{
                    "move":"7\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Pulse Carbine",
                    "Markerlight",
                    "Photon Grenades",
                ],
                "wargear":"Pulse Pistol",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Breacher Unit List
        "model":"Fire Warrior Breacher",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Infantry",
            "Fire Warrior Breacher",
        ],
        "notes":"A Breacher Shas’la or Breacher Shas’ui is armed with a pulse blaster and photon grenades",
        "types":[
            {   # Breacher Shas'la
                "name":"Breacher Shas'la",
                "points":8,
                "stats":{
                    "move":"6\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"4+",
                    "maxnum":"-"
                },
                "weapons":[
                    "Pulse Blaster",
                    "Photon Grenades",
                ],
                "wargear":[
                    "Pulse Pistol",
                    "DS8 Tactical Support Turret"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Comms",
                    "Demolitions",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Breacher Shas'ui
                "name":"Breacher Shas'ui",
                "points":8,
                "stats":{
                    "move":"6\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Pulse Blaster",
                    "Photon Grenades",
                ],
                "wargear":[
                    "Pulse Pistol",
                    "Markerlight"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual"  
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # XV25 Unit List
        "model":"XV25 Stealth Battlesuit",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Battlesuit",
            "Infantry",
            "Jet Pack",
            "Fly",
            "XV25 Stealth Battlesuit"
        ],
        "notes":"This model is armed with a burst cannon.",
        "types":[
            {   # Stealth Shas'ui
                "name":"Stealth Shas'ui",
                "points":20,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":"-"
                },
                "weapons":"Burst Cannon",
                "wargear":"Fusion Blaster",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual",
                    "Camouflage Fields"  
                ],
                "specialists":[
                    "Comms",
                    "Heavy",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Stealth Shas'vre
                "name":"Stealth Shas'vre",
                "points":20,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"4+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"3",
                    "ldrship":"8",
                    "save":"3+",
                    "maxnum":"1"
                },
                "weapons":"Burst Cannon",
                "wargear":[
                    "Markerlight",
                    "Target Lock"
                ],
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Bonding Knife Ritual",
                    "Camouflage Fields"  
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Heavy",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Drone Unit List
        "model":"Drone",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Drone",
            "Fly"
        ],
        "notes":"Drones cannot be specialists, are not part of a fire team and cannot gain experience.",
        "types":[
            {   # MV1 Gun Drone
                "name":"MV1 Gun Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":[
                    "Pulse Carbine",
                    "Pulse Carbine"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols"  
                ],
                "specialists":"",
            },
            {   # MV4 Shield Drone
                "name":"MV4 Shield Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":"",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols",
                    "Shield Generator"  
                ],
                "specialists":"",
            },
            {   # MV7 Marker Drone
                "name":"MV7 Marker Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":"Markerlight",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols"  
                ],
                "specialists":"",
            },
            {   # MV36 Guardian Drone.
                "name":"MV36 Guardian Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":"",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols",
                    "Guardian Fields"  
                ],
                "specialists":"",
            },
            {   # MV33 Grav-inhibitor Drone
                "name":"MV33 Grav-inhibitor Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":"",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols",
                    "Gravity Wave Projector"
                ],
                "specialists":"",
            },
            {   # MV31 Pulse Accelerator Drone
                "name":"MV31 Pulse Accelerator Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"3",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":"",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols",
                    "Pulse Accelerator"  
                ],
                "specialists":"",
            },
            {   # MB3 Recon Drone
                "name":"MB3 Recon Drone",
                "points":7,
                "stats":{
                    "move":"8\"",
                    "wskill":"5+",
                    "bskill":"5+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":"Burst Cannon",
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "For the Greater Good",
                    "Support Subroutines",
                    "Saviour Protocols",
                    "Recon Suite"  
                ],
                "specialists":"",
            },
        ],
    },
    {   # DS8 Tactical Support Turret
        "model":"DS8 Tactical Support Turret",
        "faction":"T'au Empire",
        "fackey":"T'au Empire",
        "keywords":[
            "Infantry",
            "Fire Warrior"
        ],
        "notes":"A DS8 Tactical Support Turret is equipped with either a missile pod or smart missile system.",
        "types":[
            {   # DS8 Tactical Support Turret
                "name":"DS8 Tactical Support Turret",
                "points":0,
                "stats":{
                    "move":"",
                    "wskill":"",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"0",
                    "ldrship":"4",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":"",
                "wargear":[
                    "Missle Pod",
                    "Smart Missle System"
                ],
                "psyker":0,
                "abilities":"A Tactical Support Turret is set up within 2\" of the model it accompanies when that model is set up on the battlefield. It is treated as a separate model, but cannot move for any  reason. If this model is more than 2\" from the model it accompanies at any point, it is removed from the battlefield. It does not count as having been taken out of action. Tactical Support Turrets may not be specialists, are not part of a fire team and do not gain experience.",
                "specialists":"",
            },
        ],
    },
],