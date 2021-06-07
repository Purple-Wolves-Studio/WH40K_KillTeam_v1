# Weapon Data Repo


weapons = [
    {   # Arc Maul
        "name":"Arc Maul",
        "notes":"",
        "profiles":[
            {
                "pname":"Arc Maul",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+2",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Arc Pistol
        "name":"Arc Pistol",
        "notes":"",
        "profiles":[
            {
                "pname":"Arc Pistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Arc Rifle
        "name":"Arc Rifle",
        "notes":"",
        "profiles":[
            {
                "pname":"Arc Rifle",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Big Choppa
        "name":"Big Choppa",
        "points":2,
        "notes":"",
        "profiles":[
            {
                "pname":"Big Choppa",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+2",
                        "armorpen":"-1",
                        "damage":"2",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Big Shoota
        "name":"Big Shoota",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Big Shoota",
                "stats":[
                    {
                        "range":"36\"",
                        "type":"Assault 3",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Bolt Pistol
        "name":"Bolt Pistol",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Bolt Pistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Burna
        "name":"Burna",
        "points":0,
        "notes":"This weapon can be used as a ranged weapon and a melee weapon. When making shooting attacks or firing Overwatch with this weapon, use the ranged profile; when making close combat attacks, use the melee profile.",
        "profiles":[
            {
                "pname":"Burna [Ranged]",
                "stats":[
                    {
                        "range":"8\"",
                        "type":"Assault D3",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
            {
                "pname":"Burna [Melee]",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"-2",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Burst Cannon
        "name":"Burst Cannon",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Burst Cannon",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 4",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Chainsword
        "name":"Chainsword",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Chainsword",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time the bearer fights, it can make 1 additional attack with this weapon."
                    },
                ],
            },
        ],
    },
    {   # Choppa
        "name":"Choppa",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Choppa",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time the bearer fights, it can make 1 additional attack with this weapon."
                    },
                ],
            },
        ],
    },
    {   # Chordclaw
        "name":"Chordclaw",
        "notes":"",
        "profiles":[
            {
                "pname":"Chordclaw",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"0",
                        "damage":"D3",
                        "abilities":"A chordclaw can only be used to make one attack each time this model fights. Each time you make a wound roll of 6+ with this weapon, the target suffers D3 mortal wounds instead of the normal damage."
                    },
                ],
            },
        ],
    },
    {   # Deffgun
        "name":"Deffgun",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Deffgun",
                "stats":[
                    {
                        "range":"48\"",
                        "type":"Heavy D3",
                        "strength":"7",
                        "armorpen":"-1",
                        "damage":"2",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Flamer
        "name":"Flamer",
        "points":3,
        "notes":"",
        "profiles":[
            {
                "pname":"Flamer",
                "stats":[
                    {
                        "range":"8\"",
                        "type":"Assault D6",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
        ],
    },
    {   # Flechette Blaster
        "name":"Flechette Blaster",
        "notes":"",
        "profiles":[
            {
                "pname":"Flechette Blaster",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 5",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Frag Grenades
        "name":"Frag Grenades",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Frag Grenade",
                "stats":[
                    {
                        "range":"6\"",
                        "type":"Grenade D6",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Fusion Blaster
        "name":"Fusion Blaster",
        "points":4,
        "notes":"",
        "profiles":[
            {
                "pname":"Fusion Blaster",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 1",
                        "strength":"8",
                        "armorpen":"-4",
                        "damage":"D6",
                        "abilities":"If the target is within half range of this weapon, roll two dice when inflicting damage with it and discard the lowest result."
                    },
                ],
            },
        ],
    },
    {   # Galvanic Rifle
        "name":"Galvanic Rifle",
        "notes":"",
        "profiles":[
            {
                "pname":"Galvanic Rifle",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Rapid Fire 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you make a wound roll of 6+ for this weapon, that hit is resolved with an AP of -1."
                    },
                ],
            },
        ],
    },
    {   # Grenade Launcher
        "name":"Grenade Launcher",
        "points":2,
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Grenade Launcher [Frag]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault D6",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Grenade Launcher [Krak]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault 1",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Grot Blasta
        "name":"Grot Blasta",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Grot Blasta",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Hot-shot Lasgun
        "name":"Hot-shot Lasgun",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Hot-shot Lasgun",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Rapid Fire 1",
                        "strength":"3",
                        "armorpen":"-2",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Hot-shot Laspistol
        "name":"Hot-shot Laspistol",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Hot-shot Laspistol",
                "stats":[
                    {
                        "range":"6\"",
                        "type":"Pistol 1",
                        "strength":"3",
                        "armorpen":"-2",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Hot-shot Volley Gun
        "name":"Hot-shot Volley Gun",
        "points":3,
        "notes":"",
        "profiles":[
            {
                "pname":"Hot-shot Volley Gun",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Heavy 4",
                        "strength":"4",
                        "armorpen":"-2",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Ion Rifle
        "name":"Ion Rifle",
        "points":3,
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Ion Rifle [Standard]",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Rapid Fire 1",
                        "strength":"7",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Ion Rifle [Overcharge]",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Heavy D3",
                        "strength":"8",
                        "armorpen":"-1",
                        "damage":"2",
                        "abilities":"If you make one or more unmodified hit rolls of 1, the bearer suffers a mortal wound after all of this weapon’s shots have been resolved."
                    },
                ],
            },
        ],
    },
    {   # Kombi-Weapon w/ Rokkit Launcha
        "name":"Kombi-Weapon w/ Rokkit Launcha",
        "points":3,
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Kombi-Weapon w/ Rokkit Launcha [Rokkit Launcha]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault 1",
                        "strength":"8",
                        "armorpen":"-2",
                        "damage":"3",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Kombi-Weapon w/ Rokkit Launcha [Shoota]",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Kombi-Weapon w/ Skorcha
        "name":"Kombi-Weapon w/ Skorcha",
        "points":4,
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Kombi-Weapon w/ Skorcha [Skorcha]",
                "stats":[
                    {
                        "range":"8\"",
                        "type":"Assault D6",
                        "strength":"5",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
            {
                "pname":"Kombi-Weapon w/ Skorcha [Shoota]",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Krak Grenades
        "name":"Krak Grenades",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Krak Grenade",
                "stats":[
                    {
                        "range":"6\"",
                        "type":"Grenade 1",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Kustom Mega-Blasta
        "name":"Kustom Mega-Blasta",
        "points":0,
        "profiles":[
            {
                "pname":"Kustom Mega-Blasta",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault 1",
                        "strength":"8",
                        "armorpen":"-3",
                        "damage":"D3",
                        "abilities":"On an unmodified hit roll of 1, the bearer suffers a mortal wound."
                    },
                ],
            },
        ],
    },
    {   # Lasgun
        "name":"Lasgun",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Lasgun",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"-1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Laspistol
        "name":"Laspistol",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Laspistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Markerlight
        "name":"Markerlight",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Markerlight",
                "stats":[
                    {
                        "range":"36\"",
                        "type":"Heavy 1",
                        "strength":"",
                        "armorpen":"",
                        "damage":"",
                        "abilities":[
                            {
                                "marknum":"1",
                                "benefit":"You can re-roll hit rolls of 1 for attacks that target this model."
                            },
                            {
                                "marknum":"2",
                                "benefit":"Add 1 to hit rolls for attacks that target this model if it is obscured."
                            },
                            {
                                "marknum":"3",
                                "benefit":"Models attacking this model do not suffer the penalty for moving and firing Heavy weapons or Advancing and firing Assault weapons."
                            },
                            {
                                "marknum":"4+",
                                "benefit":"Add 1 to hit rolls for attacks that target this model."
                            },
                        ],
                    },
                ],
            },
        ],
    },
    {   # Meltagun
        "name":"Meltagun",
        "points":3,
        "notes":"",
        "profiles":[
            {
                "pname":"Meltagun",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Assault 1",
                        "strength":"8",
                        "armorpen":"-4",
                        "damage":"D6",
                        "abilities":"If the target is within half range of this weapon, roll two dice when inflicting damage with it and discard the lowest result."
                    },
                ],
            },
        ],
    },
    {   # Missle Pod
        "name":"Missile Pod",
        "points":7,
        "notes":"",
        "profiles":[
            {
                "pname":"Missile Pod",
                "stats":[
                    {
                        "range":"36\"",
                        "type":"Assault 2",
                        "strength":"7",
                        "armorpen":"-1",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Phosphor Blast Pistol
        "name":"Phosphor Blast Pistol",
        "notes":"",
        "profiles":[
            {
                "pname":"Phosphor Blast Pistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"5",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":"Attacks made with this weapon do not suffer the penalty to hit rolls for the target being obscured."
                    },
                ],
            },
        ],
    },
    {   # Photon Grenade
        "name":"Photon Grenade",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Photon Grenade",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Grenade D6",
                        "strength":"",
                        "armorpen":"",
                        "damage":"",
                        "abilities":"This weapon does not inflict any damage. Your opponent must subtract 1 from hit rolls made for INFANTRY models that have suffered any hits from photon grenades until the end of the battle round."
                    },
                ],
            },
        ],
    },
    {   # Plasma Caliver
        "name":"Plasma Caliver",
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Plasma Caliver [Standard]",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"7",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Plasma Caliver [Supercharge]",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"8",
                        "armorpen":"-3",
                        "damage":"2",
                        "abilities":"On an unmodified hit roll of 1, the bearer is taken out of action after all of this weapon’s shots have been resolved."
                    },
                ],
            },
        ],
    },
    {   # Plasma Gun
        "name":"Plasma Gun",
        "points":3,
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Plasma Gun [Standard]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"7",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Plasma Gun [Supercharge]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"8",
                        "armorpen":"-3",
                        "damage":"2",
                        "abilities":"On an unmodified hit roll of 1, the bearer is taken out of action after all of this weapon’s shots have been resolved."
                    },
                ],
            },
        ],
    },
    {   # Plasma Pistol
        "name":"Plasma Pistol",
        "points":1,
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Plasma Pistol [Standard]",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"7",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Plasma Pistol [Supercharge]",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"8",
                        "armorpen":"-3",
                        "damage":"2",
                        "abilities":"On an unmodified hit roll of 1, the bearer is taken out of action."
                    },
                ],
            },
        ],
    },
    {   # Power Fist
        "name":"Power Fist",
        "points":2,
        "notes":"",
        "profiles":[
            {
                "pname":"Power Fist",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"x2",
                        "armorpen":"-3",
                        "damage":"D3",
                        "abilities":"When attacking with this weapon, you must subtract 1 from the hit roll."
                    },
                ],
            },
        ],
    },
    {   # Power Klaw
        "name":"Power Klaw",
        "points":4,
        "notes":"",
        "profiles":[
            {
                "pname":"Power Klaw",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"x2",
                        "armorpen":"-3",
                        "damage":"D3",
                        "abilities":"When attacking with this weapon, you must subtract 1 from the hit roll."
                    },
                ],
            },
        ],
    },
    {   # Power Sword
        "name":"Power Sword",
        "points":1,
        "notes":"",
        "profiles":[
            {
                "pname":"Power Sword",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Pulse Blaster
        "name":"Pulse Blaster",
        "points":0,
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Pulse Blaster [Close Range]",
                "stats":[
                    {
                        "range":"5\"",
                        "type":"Assault 2",
                        "strength":"6",
                        "armorpen":"-2",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Pulse Blaster [Medium Range]",
                "stats":[
                    {
                        "range":"10\"",
                        "type":"Assault 2",
                        "strength":"5",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Pulse Blaster [Long Range]",
                "stats":[
                    {
                        "range":"15\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Pulse Carbine
        "name":"Pulse Carbine",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Pulse Carbine",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Pulse Pistol
        "name":"Pulse Pistol",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Pulse Pistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Pulse Rifle
        "name":"Pulse Rifle",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Pulse Rifle",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Rapid Fire 1",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Radium Carbine
        "name":"Radium Carbine",
        "notes":"",
        "profiles":[
            {
                "pname":"Radium Carbine",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 3",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you make a wound roll of 6+ for this weapon, that hit is resolved with a Damage of 3."
                    },
                ],
            },
        ],
    },
    {   # Radium Pistol
        "name":"Radium Pistol",
        "notes":"",
        "profiles":[
            {
                "pname":"Radium Pistol",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you make a wound roll of 6+ for this weapon, that hit is resolved with a Damage of 2."
                    },
                ],
            },
        ],
    },
    {   # Rail Rifle
        "name":"Rail Rifle",
        "points":5,
        "notes":"",
        "profiles":[
            {
                "pname":"Rail Rifle",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Rapid Fire 1",
                        "strength":"6",
                        "armorpen":"-4",
                        "damage":"D3",
                        "abilities":"For each wound roll of 6+ made for this weapon, the target model suffers a mortal wound in addition to the normal damage."
                    },
                ],
            },
        ],
    },
    {   # Rokkit Launcha
        "name":"Rokkit Launcha",
        "points":3,
        "notes":"",
        "profiles":[
            {
                "pname":"Rokkit Launcha",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault 1",
                        "strength":"8",
                        "armorpen":"-2",
                        "damage":"3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Shoota
        "name":"Shoota",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Shoota",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Slugga
        "name":"Slugga",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Slugga",
                "stats":[
                    {
                        "range":"12\"",
                        "type":"Pistol 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Smart Missle System
        "name":"Smart Missle System",
        "points":5,
        "notes":"",
        "profiles":[
            {
                "pname":"Smart Missle System",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Heavy 4",
                        "strength":"5",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"This weapon can be fired at models that are not visible to the bearer. If the target is not visible to the bearer, a 6 is required for a successful hit roll, irrespective of the firing model’s Ballistic Skill or any modifiers."
                    },
                ],
            },
        ],
    },
    {   # Sniper Rifle
        "name":"Sniper Rifle",
        "points":1,
        "notes":"",
        "profiles":[
            {
                "pname":"Sniper Rifle",
                "stats":[
                    {
                        "range":"36\"",
                        "type":"Heavy 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"A model firing a sniper rifle does not suffer the penalty to hit rolls for the target being at long range. If you roll a wound roll of 6+ for this weapon, it inflicts a mortal wound in addition to its normal damage."
                    },
                ],
            },
        ],
    },
    {   # Stikkbomb
        "name":"Stikkbomb",
        "points":0,
        "notes":"",
        "profiles":[
            {
                "pname":"Stikkbomb",
                "stats":[
                    {
                        "range":"6\"",
                        "type":"Grenade D6",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Stubcarbine
        "name":"Stubcarbine",
        "notes":"",
        "profiles":[
            {
                "pname":"Stubcarbine",
                "stats":[
                    {
                        "range":"18\"",
                        "type":"Pistol 3",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Taser Goad
        "name":"Taser Goad",
        "notes":"",
        "profiles":[
            {
                "pname":"Taser Goad",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+2",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each hit roll of 6+ with this weapon causes 3 hits rather than 1."
                    },
                ],
            },
        ],
    },
    {   # Transonic Blades
        "name":"Transonic Blades",
        "notes":"",
        "profiles":[
            {
                "pname":"Transonic Blades",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+1",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you make a wound roll of 6+ with this weapon, the target suffers a mortal wound instead of the normal damage."
                    },
                ],
            },
        ],
    },
    {   # Transonic Razor
        "name":"Transonic Razor",
        "notes":"",
        "profiles":[
            {
                "pname":"Transonic Razor",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you make a wound roll of 6+ with this weapon, the target suffers a mortal wound instead of the normal damage."
                    },
                ],
            },
        ],
    },
    {   # Transuranic Arquebus
        "name":"Transuranic Arquebus",
        "notes":"",
        "profiles":[
            {
                "pname":"Transuranic Arquebus",
                "stats":[
                    {
                        "range":"60\"",
                        "type":"Heavy 1",
                        "strength":"7",
                        "armorpen":"-2",
                        "damage":"D3",
                        "abilities":"This weapon cannot be fired if the firing model moved during the Movement phase. A model firing a Transuranic Arquebus does not suffer the penalty to hit rolls for the target being at long range. Each time you make a wound roll of 6+ for this weapon, it inflicts a mortal wound in addition to the normal damage."
                    },
                ],
            },
        ],
    },
],