# Astra Militarum Units Data Repo


units = [
    {   # Infantry Squad Guardsman  Unit List
        "model":"Infantry Squad Guardsman",
        "faction":"Astra Militarum",
        "keywords":[
            "Imperium",
            "Infantry",
            "Infantry Squad Guardsman"
        ],
        "notes":"This model is armed with a lasgun and frag grenades.",
        "types":[
            {   # Guardsman
                "name":"Guardsman",
                "points":5,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
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
                    "Lasgun",
                    "Frag Grenades"
                ],
                "wargear":"Vox-Caster",
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
                ],
                "specialists":[
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Guardsman Gunner
                "name":"Guardsman Gunner",
                "points":5,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
                    "bskill":"4+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"5+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Lasgun",
                    "Frag Grenades"
                ],
                "wargear":[
                    "Flamer",
                    "Grenade Launcher",
                    "Meltagun",
                    "Plasma Gun",
                    "Sniper Rifle"
                ],
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
                ],
                "specialists":[
                    "Heavy",
                    "Demolitions",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Sergeant
                "name":"Sergeant",
                "points":5,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
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
                    "Laspistol",
                    "Chainsword",
                    "Frag Grenades"
                ],
                "wargear":[
                    "Bolt Pistol",
                    "Plasma Pistol",
                    "Power Sword"
                ],
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
                ],
                "specialists":[
                    "Leader",
                    "Demolitions",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Militarum Tempestus Scion  Unit List
        "model":"Militarum Tempestus Scion",
        "faction":"Astra Militarum",
        "keywords":[
            "Imperium",
            "Militarum Tempestus",
            "Infantry",
            "Militarum Tempestus Scion"
        ],
        "notes":"This model is armed with a hot-shot lasgun, frag grenades and krak grenades.",
        "types":[
            {   # Scion
                "name":"Scion",
                "points":9,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"4+",
                    "maxnum":""
                },
                "weapons":[
                    "Hot-Shot Lasgun",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":"Vox-Caster",
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
                ],
                "specialists":[
                    "Comms",
                    "Medic",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Scion Gunner
                "name":"Scion Gunner",
                "points":10,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"6",
                    "save":"4+",
                    "maxnum":"4"
                },
                "weapons":[
                    "Hot-Shot Lasgun",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Flamer",
                    "Meltagun",
                    "Plasma Gun",
                    "Hot-Shot Volley Gun"
                ],
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
                ],
                "specialists":[
                    "Demolitions",
                    "Heavy",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Tempestor
                "name":"Tempestor",
                "points":10,
                "stats":{
                    "move":"6\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"2",
                    "ldrship":"7",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Hot-Shot Laspistol",
                    "Chainsword",
                    "Frag Grenades",
                    "Krak Grenades"
                ],
                "wargear":[
                    "Bolt Pistol",
                    "Plasma Pistol",
                    "Power Sword",
                    "Power Fist"
                ],
                "psyker":0,
                "abilities":[
                    "Voice of Command",
                    "Vox-Caster"
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
    {   # Special Weapons Squad Guardsman  Unit List
        "model":"Special Weapons Squad Guardsman",
        "faction":"Astra Militarum",
        "keywords":[
            "Imperium",
            "Infantry",
            "Special Weapons Squad Guardsman"
        ],
        "notes":"This model is armed with a lasgun and frag grenades.",
        "types":[
            {   # Special Weapons Squad Guardsman
                "name":"Special Weapons Guardsman",
                "points":5,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
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
                    "Lasgun",
                    "Frag Grenades"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":"Voice of Command",
                "specialists":[
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
            {   # Special Weapons Gunner
                "name":"Special Weapons Gunner",
                "points":5,
                "stats":{
                    "move":"6\"",
                    "wskill":"4+",
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
                    "Lasgun",
                    "Frag Grenades"
                ],
                "wargear":[
                    "Flamer",
                    "Grenade Launcher",
                    "Meltagun",
                    "Plasma Gun",
                    "Sniper Rifle"
                ],
                "psyker":0,
                "abilities":"Voice of Command",
                "specialists":[
                    "Heavy",
                    "Leader",
                    "Comms",
                    "Demolitions",
                    "Scout",
                    "Sniper",
                    "Veteran"
                ],
            },
        ],
    },
],