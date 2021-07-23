# Asuryani Units Data


units = [
    {   # Dire Avenger
        "model":"Dire Avenger",
        "faction":"Asuryani",
        "keywords":[
            "Aeldari",
            "Aspect Warrior",
            "Infantry",
            "Dire Avenger"
        ],
        "notes":"This model is armed with an Avenger Shuriken Catapult and Plasma Grenades.",
        "types":[
            {   # Dire Avenger
                "name":"Dire Avenger",
                "points":10,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"8",
                    "save":"4+",
                    "maxnum":""
                },
                "weapons":[
                    "Avenger Shuriken Catapult",
                    "Plasma Grenade"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus",
                    "Defence Tactics",
                    "Shimmershield"
                ],
                "specialists":[
                    "Combat",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Dire Avenger Exarch
                "name":"Dire Avenger Exarch",
                "points":11,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"2",
                    "attack":"2",
                    "ldrship":"8",
                    "save":"4+",
                    "maxnum":"1"
                },
                "weapons":[
                    "Avenger Shuriken Catapult",
                    "Plasma Grenade"
                ],
                "wargear":[
                    "Shuriken Pistol",
                    "Power Glaive",
                    "Diresword",
                    "Shimmershield"
                ],
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus",
                    "Defence Tactics",
                    "Battle Fortune",
                ],
                "specialists":[
                    "Leader",
                    "Combat",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Guardian Defender
        "model":"Guardian Defender",
        "faction":"Asuryani",
        "keywords":[
            "Aeldari",
            "Warhost",
            "Infantry",
            "Guardian",
            "Guardian Defender"
        ],
        "notes":"This model is armed with a Shuriken Catapult and Plasma Grenades.",
        "types":[
            {   # Guardian Defender
                "name":"Guardian Defender",
                "points":7,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":[
                    "Shuriken Catapult",
                    "Plasma Grenade"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus"
                ],
                "specialists":[
                    "Leader",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
    {   # Heavy Weapon Platform
        "model":"Heavy Weapon Platform",
        "faction":"Asuryani",
        "keywords":[
            "Aeldari",
            "Warhost",
            "Infantry",
            "Artillery",
            "Guardian",
            "Heavy Weapon Platform"
        ],
        "notes":"One Guardian Defender in your kill team can be a Heavy Weapon Platform. A Heavy Weapon Platform is instead armed with a Shuriken Cannon.",
        "types":[
            {   # Heavy Weapon Platform
                "name":"Heavy Weapon Platform",
                "points":8,
                "stats":{
                    "move":"7\"",
                    "wskill":"6+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"2",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"3+",
                    "maxnum":"1"
                },
                "weapons":"Shuriken Cannon",
                "wargear":[
                    "Aeldari Missile Launcher",
                    "Bright Lance",
                    "Scatter Laser",
                    "Starcannon"
                ],
                "psyker":0,
                "abilities":"Crewed Weapon",
                "specialists":""
            },
        ],
    },
    {   # Ranger
        "model":"Ranger",
        "faction":"Asuryani",
        "keywords":[
            "Aeldari",
            "Warhost",
            "Infantry",
            "Ranger"
        ],
        "notes":"This model is armed with a Shuriken Pistol and Ranger Long Rifle.",
        "types":[
            {   # Ranger
                "name":"Ranger",
                "points":11,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":[
                    "Shuriken Pistol",
                    "Ranger Long Rifle"
                ],
                "wargear":"",
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus",
                    "Cameleoline Cloak"
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
    {   # Storm Guardian
        "model":"Storm Guardian",
        "faction":"Asuryani",
        "keywords":[
            "Aeldari",
            "Warhost",
            "Infantry",
            "Guardian",
            "Storm Guardian"
        ],
        "notes":"This model is armed with a Shuriken Pistol, Aeldari Blade, and Plasma Grenades.",
        "types":[
            {   # Storm Guardian
                "name":"Storm Guardian",
                "points":6,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"5+",
                    "maxnum":""
                },
                "weapons":[
                    "Shuriken Pistol",
                    "Aeldari Blade",
                    "Plasma Grenade"
                ],
                "wargear":"Chainsword",
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus"
                ],
                "specialists":[
                    "Leader",
                    "Combat",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
            {   # Storm Guardian Gunner
                "name":"Storm Guardian Gunner",
                "points":7,
                "stats":{
                    "move":"7\"",
                    "wskill":"3+",
                    "bskill":"3+",
                    "strength":"3",
                    "tough":"3",
                    "wounds":"1",
                    "attack":"1",
                    "ldrship":"7",
                    "save":"5+",
                    "maxnum":"2"
                },
                "weapons":[
                    "Shuriken Pistol",
                    "Aeldari Blade",
                    "Plasma Grenade"
                ],
                "wargear":[
                    "Chainsword",
                    "Flamer",
                    "Fusion Gun"
                ],
                "psyker":0,
                "abilities":[
                    "Ancient Doom",
                    "Battle Focus"
                ],
                "specialists":[
                    "Leader",
                    "Combat",
                    "Comms",
                    "Medic",
                    "Scout",
                    "Veteran"
                ],
            },
        ],
    },
],