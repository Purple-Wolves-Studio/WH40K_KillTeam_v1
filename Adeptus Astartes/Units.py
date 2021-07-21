# Adeptus Astartes Unit Data


units = [
    {   # Scout Unit List
        "model":"Scout",
        "faction":"Adeptus Astartes",
        "keywords":[
            "Imperium",
            "Infantry",
            "Scout"
        ],
        "notes":"This model is armed with a Boltgun, Bolt Pistol, Frag Grenades and Krak Grenades.",
        "types":[
            {   # Scout
                "name":"Scout",
                "points":10,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"4+",
                    "maxnum":""
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Combat Knife",
                    "Astartes Shotgun",
                    "Sniper Rifle",
                    "Camo Cloak"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Camo Cloak"
                ],
                "specialists":[
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper"
                ],
            },
            {   # Scout Gunner
                "name":"Scout Gunner",
                "points":11,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"4+",
                    "maxnum":"2"
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Heavy Bolter",
                    "Missile Launcher",
                    "Sniper Rifle",
                    "Camo Cloak"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Camo Cloak"
                ],
                "specialists":[
                    "Heavy",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper"
                ],
            },
            {   # Scout Sergeant
                "name":"Scout Sergeant",
                "points":11,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"8",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Astartes Shotgun",
                    "Chainsword",
                    "Sniper Rifle",
                    "Camo Cloak"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Camo Cloak"
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper"
                ],
            },
        ],
    },
    {   # Tactical Marine Unit List
        "model":"Tactical Marine",
        "faction":"Adeptus Astartes",
        "keywords":[
            "Imperium",
            "Infantry",
            "Tactical Marine"
        ],
        "notes":"This model is armed with a Boltgun, Bolt Pistol, Frag Grenades, and Krak Grenades.",
        "types":[
            {   # Tactical Marine
                "name":"Tactical Marine",
                "points":12,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":""
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                ],
                "specialists":[
                    "Comms",
                    "Demolitions",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Tactical Marine Gunner
                "name":"Tactical Marine Gunner",
                "points":13,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":"2"
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Flamer",
                    "Meltagun",
                    "Plasma Gun",
                    "Grav-gun",
                    "Heavy Bolter",
                    "Missile Launcher"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology"
                ],
                "specialists":[
                    "Heavy",
                    "Comms",
                    "Demolitions",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Tactical Marine Sergeant
                "name":"Tactical Marine Sergeant",
                "points":13,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"8",
                    "save":"3+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Boltgun",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Combi-flamer",
                    "Combi-grav",
                    "Combi-melta",
                    "Combi-plasma",
                    "Plasma Pistol",
                    "Grav-pistol",
                    "Chainsword",
                    "Power Fist",
                    "Power Sword",
                    "Auspex",
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Auspex"
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Sniper",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Reiver Unit List
        "model":"Reiver",
        "faction":"Adeptus Astartes",
        "keywords":[
            "Imperium",
            "Infantry",
            "Primaris",
            "Reiver"
        ],
        "notes":"This model is armed with a Bolt Carbine, Heavy Bolt Pistol, Frag Grenades, Krak Grenades, and Shock Grenades",
        "types":[
            {   # Reiver
                "name":"Reiver",
                "points":16,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":""
                },
                "weapons":[
                    "Bolt Carbine",
                    "Heavy Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades",
                    "Shock Grenades"
                ],
                "wargear":[
                    "Grav-chute",
                    "Grapnel Launcher",
                    "Combat Knife"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Grapnel Launcher",
                    "Grav-chute",
                    "Terror Troops"
                ],
                "specialists":[
                    "Combat",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Reiver Sergeant
                "name":"Reiver Sergeant",
                "points":17,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"3",
                    "ldrship":"8",
                    "save":"3+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Bolt Carbine",
                    "Heavy Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades",
                    "Shock Grenades"
                ],
                "wargear":[
                    "Grav-chute",
                    "Grapnel Launcher",
                    "Combat Knife",
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Grapnel Launcher",
                    "Grav-chute",
                    "Terror Troops"
                ],
                "specialists":[
                    "Leader",
                    "Combat",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Intercessor Unit List
        "model":"Intercessor",
        "faction":"Adeptus Astartes",
        "keywords":[
            "Imperium",
            "Infantry",
            "Primaris",
            "Intercessor"
        ],
        "notes":"This model is armed with a Bolt Rifle, Bolt Pistol, Frag Grenades, and Krak Grenades",
        "types":[
            {   # Intercessor
                "name":"Intercessor",
                "points":15,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":""
                },
                "weapons":[
                    "Bolt Rifle",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Auto Bolt Rifle",
                    "Stalker Bolt Rifle"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology"
                ],
                "specialists":[
                    "Combat",
                    "Comms",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Intercessor Gunner
                "name":"Intercessor Gunner",
                "points":16,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":"2"
                },
                "weapons":[
                    "Bolt Rifle",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Auto Bolt Rifle",
                    "Stalker Bolt Rifle",
                    "Auxiliary Grenade Launcher"
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology",
                    "Auxiliary Grenade Launcher"
                ],
                "specialists":[
                    "Demolitions",
                    "Combat",
                    "Comms",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Intercessor Sergeant
                "name":"Intercessor Sergeant",
                "points":16,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"4",
                    "tough":"4",
                    "wounds":"2",
                    "attack":"3",
                    "ldrship":"8",
                    "save":"3+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Bolt Rifle",
                    "Bolt Pistol",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Auto Bolt Rifle",
                    "Stalker Bolt Rifle"
                    "Power Sword",
                    "Chainsword",
                ],
                "psyker":0,
                "abilities":[
                    "And They Shall Know No Fear",
                    "Transhuman Physiology"
                ],
                "specialists":[
                    "Leader",
                    "Combat",
                    "Comms",
                    "Sniper",
                    "Veteran"
                ],
            },
        ],
    },
],