# Adeptus Mechanicus Abilities Data Repo


abilities = [
    {   # Canticles of the Omnissiah
        "name":"Canticles of the Omnissiah",
        "notes":"At the start of each battle round, pick which Canticle of the Omnissiah is in effect until the end of the battle round. The same Canticle may not be picked twice during the same battle. Alternatively, you can randomly determine which Canticle of the Omnissiah is in effect by rolling a D6. Note that if you randomly determine a Canticle, it takes effect even if the same Canticle has been in effect earlier in the battle.",
        "orders":[
            {
                "ordname":"Incantation of the Iron Soul",
                "ordnotes":"You can re-roll failed Nerve tests for models in your kill team."
            },
            {
                "ordname":"Litany of the Electromancer",
                "ordnotes":"Roll a D6 for each enemy model within 1\" of any models in your kill team at the start of the Fight phase. On a 6, that enemy model suffers 1 mortal wound."
            },
            {
                "ordname":"Chant of the Remorseless Fist",
                "ordnotes":"Re-roll hit rolls of 1 for models in your kill team in the Fight phase."
            },
            {
                "ordname":"Shroudpsalm",
                "ordnotes":"When an enemy player makes a hit roll for a shooting attack that targets a model from your kill team, and that model is obscured, that hit roll suffers an additional -1 modifier."
            },
            {
                "ordname":"Inocation of Machine Might",
                "ordnotes":"Add 1 to the Strength characteristic of models in your kill team."
            },
            {
                "ordname":"Benediction of the Omnissiah",
                "ordnotes":"Re-roll hit rolls of 1 for models in your kill team in the Shooting phase."
            },
        ],
    },
    {   # Bionics
        "name":"Bionics",
        "notes":"This model has a 6+ invulnerable save.",
        "orders":""
    },
    {   # Enhanced Data-Tether
        "name":"Enhanced Data-Tether",
        "notes":"You can re-roll failed Nerve tests for Skitarii models while a friendly model with an Enhanced Data-Tether is on the battlefield and not shaken.",
        "orders":""
    },
    {   # Omnispex
        "name":"Omnispex",
        "notes":"At the start of each Shooting phase, you can choose another Skitarii model within 3\" of a friendly model equipped with an Omnispex that is not shaken. That model does not suffer penalties to their hit or injury rolls due to their target being obscured.",
        "orders":""
    },
    {   # Rad-saturation
        "name":"Rad-saturation",
        "notes":"Reduce the Toughness characteristic of enemy models by 1 whilst they are within 1\" of one or more models with this ability.",
        "orders":""
    },
    {   # Neurostatic Aura
        "name":"Neurostatic Aura",
        "notes":"Subtract 1 from the Leadership characteristic of enemy models whilst they are within 3\" of one or more models with this ability.",
        "orders":""
    },
],