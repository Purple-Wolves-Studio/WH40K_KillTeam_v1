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
    {   # Bolt Gun
        "name":"Bolt Gun",
        "notes":"",
        "profiles":[
            {
                "pname":"Bolt Gun",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Big Shoota
        "name":"Big Shoota",
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
    {   # Combi-melta
        "name":"Combi-melta",
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Combi-melta [Boltgun]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Combi-melta [Meltagun]",
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
    {   # Combi-melta
        "name":"Combi-plasma",
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Combi-melta [Boltgun]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Combi-melta [Plasma Gun]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 1",
                        "strength":"7",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":"This weapon can be supercharged by the bearer before firing. If they do so, increase the Strength and Damage of the weapon by 1 this turn. On any unmodified hit rolls of 1 when firing supercharge, the bearer is taken out of action after all of the weapon’s shots have been resolved."
                    },
                ],
            },
        ],
    },
    {   # Deathwatch Frag Cannon
        "name":"Deathwatch Frag Cannon",
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Deathwatch Frag Cannon [Frag Round]",
                "stats":[
                    {
                        "range":"8\"",
                        "type":"Assault 2D6",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
            {
                "pname":"Deathwatch Frag Cannon [Shell]",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Assault 2",
                        "strength":"7",
                        "armorpen":"-2",
                        "damage":"2",
                        "abilities":"If the target is within half range of this weapon, its attacks are resolved with a Strength of 9 and an AP of -3."
                    },
                ],
            },
        ],
    },
    {   # Deathwatch Shotgun
        "name":"Deathwatch Shotgun",
        "notes":"When attacking with this weapon, choose one of the profiles below.",
        "profiles":[
            {
                "pname":"Deathwatch Shotgun [Cryptclearer Round]",
                "stats":[
                    {
                        "range":"16\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"You can re-roll failed wound rolls for this weapon."
                    },
                ],
            },
            {
                "pname":"Deathwatch Shotgun [Xenopurge Slug]",
                "stats":[
                    {
                        "range":"16\"",
                        "type":"Assault 2",
                        "strength":"4",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":"If the target is within half range of this weapon, its attacks are resolved with a Damage of 2."
                    },
                ],
            },
            {
                "pname":"Deathwatch Shotgun [Wyrmsbreath Shell]",
                "stats":[
                    {
                        "range":"7\"",
                        "type":"Assault D6",
                        "strength":"3",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
        ],
    },
    {   # Deffgun
        "name":"Deffgun",
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
    {   # Frag Grenade
        "name":"Frag Grenade",
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
    {   # Heavy Thunder Hammer
        "name":"Heavy Thunder Hammer",
        "notes":"",
        "profiles":[
            {
                "pname":"Heavy Thunder Hammer",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"x2",
                        "armorpen":"-3",
                        "damage":"D6",
                        "abilities":"When attacking with this weapon, you must subtract 1 from the hit roll. Each time you make a wound roll of 6+ with this weapon, that hit is resolved with a Damage of 6."
                    },
                ],
            },
        ],
    },
    {   # Hot-shot Lasgun
        "name":"Hot-shot Lasgun",
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
    {   # Incinerator
        "name":"Incinerator",
        "notes":"",
        "profiles":[
            {
                "pname":"Incinerator",
                "stats":[
                    {
                        "range":"8\"",
                        "type":"Assault D6",
                        "strength":"6",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":"This weapon automatically hits its target."
                    },
                ],
            },
        ],
    },
    {   # Infernus Heavy Bolter
        "name":"Infernus Heavy Bolter",
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Infernus Heavy Bolter [Heavy Bolter]",
                "stats":[
                    {
                        "range":"36\"",
                        "type":"Heavy 3",
                        "strength":"5",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
            {
                "pname":"Infernus Heavy Bolter [Heavy Flamer]",
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
        ],
    },
    {   # Ion Rifle
        "name":"Ion Rifle",
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
    {   # Kombi-weapon w/ Rokkit Launcha
        "name":"Kombi-weapon w/ Rokkit Launcha",
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Kombi-weapon w/ Rokkit Launcha [Rokkit Launcha]",
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
                "pname":"Kombi-weapon w/ Rokkit Launcha [Shoota]",
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
    {   # Kombi-weapon w/ Skorcha
        "name":"Kombi-weapon w/ Skorcha",
        "notes":"When attacking with this weapon, choose one or both of the profiles below. If you choose both, subtract 1 from all hit rolls made for this weapon.",
        "profiles":[
            {
                "pname":"Kombi-weapon w/ Skorcha [Skorcha]",
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
                "pname":"Kombi-weapon w/ Skorcha [Shoota]",
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
    {   # Krak Grenade
        "name":"Krak Grenade",
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
    {   # Kustom Mega-blasta
        "name":"Kustom Mega-blasta",
        "profiles":[
            {
                "pname":"Kustom Mega-blasta",
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
    {   # Nemesis Daemon Hammer
        "name":"Nemesis Daemon Hammer",
        "notes":"",
        "profiles":[
            {
                "pname":"Nemesis Daemon Hammer",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"x2",
                        "armorpen":"-3",
                        "damage":"3",
                        "abilities":"When attacking with this weapon, you must subtract 1 from the hit roll."
                    },
                ],
            },
        ],
    },
    {   # Nemesis Falchion
        "name":"Nemesis Falchion",
        "notes":"",
        "profiles":[
            {
                "pname":"Nemesis Falchion",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"-2",
                        "damage":"D3",
                        "abilities":"If a model is armed with two Nemesis Falchions, each time it fights it can make 1 additional attack with them."
                    },
                ],
            },
        ],
    },
    {   # Nemesis Force Halberd
        "name":"Nemesis Force Halberd",
        "notes":"",
        "profiles":[
            {
                "pname":"Nemesis Force Halberd",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+1",
                        "armorpen":"-2",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Nemesis Force Sword
        "name":"Nemesis Force Sword",
        "notes":"",
        "profiles":[
            {
                "pname":"Nemesis Force Sword",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"-3",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Nemesis Warding Stave
        "name":"Nemesis Warding Stave",
        "notes":"",
        "profiles":[
            {
                "pname":"Nemesis Warding Stave",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"+2",
                        "armorpen":"-1",
                        "damage":"D3",
                        "abilities":"A model armed with this weapon has a 5+ invulnerable save against attacks made in the Fight phase. If it already has an invulnerable save, add 1 to invulnerable saving throws you make for it in the Fight phase instead."
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
    {   # Power Maul
        "name":"Power Maul",
        "notes":"",
        "profiles":[
            {
                "pname":"Power Maul",
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
    {   # Power Sword
        "name":"Power Sword",
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
    {   # Psilencer
        "name":"Psilencer",
        "notes":"",
        "profiles":[
            {
                "pname":"Psilencer",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Heavy 6",
                        "strength":"4",
                        "armorpen":"0",
                        "damage":"D3",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Psycannon
        "name":"Psycannon",
        "notes":"",
        "profiles":[
            {
                "pname":"Psycannon",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Heavy 4",
                        "strength":"7",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Psyk-out Grenade
        "name":"Psyk-out Grenade",
        "notes":"",
        "profiles":[
            {
                "pname":"Psyk-out Grenade",
                "stats":[
                    {
                        "range":"6\"",
                        "type":"Grenade D3",
                        "strength":"2",
                        "armorpen":"0",
                        "damage":"1",
                        "abilities":"Each time you roll a hit of 6+ for this weapon when targeting a Psyker or Daemon, the target suffers a mortal wound instead of the normal damage."
                    },
                ],
            },
        ],
    },
    {   # Pulse Blaster
        "name":"Pulse Blaster",
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
    {   # Stalker Pattern Boltgun
        "name":"Stalker Pattern Boltgun",
        "notes":"",
        "profiles":[
            {
                "pname":"Stalker Pattern Boltgun",
                "stats":[
                    {
                        "range":"30\"",
                        "type":"Heavy 2",
                        "strength":"4",
                        "armorpen":"-1",
                        "damage":"1",
                        "abilities":""
                    },
                ],
            },
        ],
    },
    {   # Stikkbomb
        "name":"Stikkbomb",
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
    {   # Storm Bolter
        "name":"Storm Bolter",
        "notes":"",
        "profiles":[
            {
                "pname":"Storm Bolter",
                "stats":[
                    {
                        "range":"24\"",
                        "type":"Rapid Fire 2",
                        "strength":"4",
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
    {   # Xenophase Blade
        "name":"Xenophase Blade",
        "notes":"",
        "profiles":[
            {
                "pname":"Xenophase Blade",
                "stats":[
                    {
                        "range":"Melee",
                        "type":"Melee",
                        "strength":"User",
                        "armorpen":"-3",
                        "damage":"1",
                        "abilities":"Your opponent must re-roll successful invulnerable saves for wounds caused by this weapon."
                    },
                ],
            },
        ],
    },
],