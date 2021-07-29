# Drukhari Abilities Data


abilities = [
    {   # Combat Drugs
        "name":"Combat Drugs",
        "notes":"Models with this ability gain a bonus during the battle depending on the drugs they have taken. Before the battle, roll to see which combat drug your kill team is using. This bonus applies to all models in your kill team with the Combat Drugs ability.",
        "orders":[
            {
                "ordname":"1 - Adrenalight",
                "ordnotes":"+1 to Attacks characteristic."
            },
            {
                "ordname":"2 - Grave Lotus",
                "ordnotes":"+1 to Strength characteristic."
            },
            {
                "ordname":"3 - Hypex",
                "ordnotes":"+2 to Move characteristic."
            },
            {
                "ordname":"4 - Painbringer",
                "ordnotes":"+1 to Toughness characteristic."
            },
            {
                "ordname":"5 - Serpentin",
                "ordnotes":"+1 to Weapon Skill characteristic. (3+ > 2+)"
            },
            {
                "ordname":"6 - Splintermind",
                "ordnotes":"+2 to Leadership characteristic."
            },
        ],
    },
    {   # Dodge
        "name":"Dodge",
        "notes":"",
        "orders":"This model has a 4+ invulnerable save in the Fight phase."
    },
    {   # No Escape
        "name":"No Escape",
        "notes":"If an Infantry model within 1\" of any enemy models with this ability would Fall Back, the controlling players roll off. The model that would Fall Back can only do so if the player controlling it wins.",
        "orders":""
    },
    {   # Power From Pain
        "name":"Power From Pain",
        "notes":"Models with this ability gain a bonus per battle round. All bonuses are cumulative.",
        "orders":[
            {
                "ordname":"Battle Round 1 - Inured to Suffering",
                "ordnotes":"Roll a D6 each time this model loses a wound; on a 6 that wound is not lost."
            },
            {
                "ordname":"Battle Round 2 - Eager to Flay",
                "ordnotes":"You can re-roll the dice when determining how far this model moves when it Advances of charges."
            },
            {
                "ordname":"Battle Round 3 - Flensing Fury",
                "ordnotes":"Add 1 to hit rolls for this model in the Fight phase."
            },
            {
                "ordname":"Battle Round 4 - Emboldened by Bloodshed",
                "ordnotes":"Re-roll failed Nerve tests for this model."
            },
            {
                "ordname":"Battle Round 5+ - Mantle of Agony",
                "ordnotes":"Subtract 1 from the Leadership characteristic of enemy models that are within 6\" of any models from your kill team with this bonus."
            },
        ],
    },
],