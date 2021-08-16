# Adeptus Astartes Abilities Data


abilities = [
    {   # Adrenal Glands
        "name":"Adrenal Glands",
        "notes":"If a model has adrenal glands, add 1\" to the distance it can move when it Advances or charges.",
        "orders":"",
    },
    {   # All is Dust
        "name":"All is Dust",
        "notes":"Add 1 to saving throws for a Rubric Marine or Rubric Marine Gunner if the attack has a Damage characteristic of 1. In addition, the -1 modifier to hit rolls for moving and shooting Heavy weapons does not apply to Rubric Marine Gunners.",
        "orders":""
    },
    {   # Ancient Doom
        "name":"Ancient Doom",
        "notes":" You can re-roll failed hit rolls in the Fight phase for this model in a battle round in which it charges or is charged by a Slaanesh model. However, you must add 1 to Nerve tests for this model if it is within 3\" of any Slaanesh models.",
        "orders":""
    },
    {   # And They Shall Know No Fear
        "name":"And They Shall Know No Fear",
        "notes":"You can re-roll failed Nerve tests for this model.",
        "orders":""
    },
    {   # Atonement Through Honour
        "name":"Atonement Through Honour",
        "notes":"You can re-roll failed charge rolls for a Black Shield.",
        "orders":""
    },
    {   # Aura of Dark Glory
        "name":"Aura of Dark Glory",
        "notes":"This model has a 5+ invulnerable save.",
        "orders":""
    },
    {   # Auspex
        "name":"Auspex",
        "notes":"At the start of the Shooting phase, you can choose another Adeptus Astartes model within 3\" of a friendly model equipped with an Auspex that is not shaken. That model does not suffer penalties to their hit or injury rolls due to their target being obscured.",
        "orders":""
    },
    {   # Auxiliary Grenade Launcher
        "name":"Auxiliary Grenade Launcher",
        "notes":"If a model is armed with an Auxiliary Grenade Launcher, increase the range of any Grenade weapons they have to 30\".",
        "orders":""
    },
    {   # Battle Focus
        "name":"Battle Focus",
        "notes":"If this model moves or Advances in its Movement phase, weapons (excluding Heavy weapons) are used as if the model had remained stationary.",
        "orders":""
    },
    {   # Battle Fortune
        "name":"Battle Fortune",
        "notes":"A Dire Avenger Exarch has a 4+ invulnerable save.",
        "orders":""
    },
    {   # Bestial Vigour
        "name":"Bestial Vigour",
        "notes":"When inflicting damage on this model, reduce the damage of the attack by 1 to a minimum of 1.",
        "orders":""
    },
    {   # Bionics
        "name":"Bionics",
        "notes":"This model has a 6+ invulnerable save.",
        "orders":""
    },
    {   # Bonding Knife Ritual
        "name":"Bonding Knife Ritual",
        "notes":"You can subtract 1 from Nerve tests for Shas’las or Shas’uis from your kill team within 3\" of any friendly models with this ability that are not shaken.",
        "orders":""
    },
    {   # Bounding Leap
        "name":"Bounding Leap",
        "notes":"Whenever this model piles in or consolidates, it can move up to 6\".",
        "orders":"",
    },
    {   # Brayhorn
        "name":"Brayhorn",
        "notes":"Add 1 to Advantage and charge rolls made for Tzaangors within 6\" of any friendly models equipped with a Brayhorn.",
        "orders":""
    },
    {   # Cameleoline Cloak
        "name":"Cameleoline Cloak",
        "notes":"When an enemy player makes a hit roll for a shooting attack that targets this model, and this model is obscured, that hit roll suffers an addiotional -1 modifier.",
        "orders":""
    },
    {   # Camouflage Fields
        "name":"Camouflage Fields",
        "notes":"Your opponent must subtract 1 from all hit rolls for attacks that target this model.",
        "orders":""
    },
    {   # Camo Cloak
        "name":"Camo Cloak",
        "notes":"When an opponent makes a hit roll for a shooting attack that targets a model equipped with a camo cloak, and that model is obscured, that hit roll suffers an additional -1 modifier.",
        "orders":""
    },
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
    {   # Chameleonic Skin
        "name":"Chameleonic Skin",
        "notes":"When an enemy player makes a hit roll for a shooting attack that targets this model, and this model is obscured, that hit roll suffers an additional -1 modifier.",
        "orders":"",
    },
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
    {   # Crewed Weapon
        "name":"Crewed Weapon",
        "notes":"A Heavy Weapon Platform can only move, Advance, React, shoot or fight if a friendly Guardian Defender, that is not shaken, is within 3\" of it. If a Heavy Weapon Platform shoots, you must choose one such Guardian Defender that could still shoot its own ranged weapons in that phase: that Guardian Defender may not fire any of its own ranged weapons this phase. Heavy Weapon Platforms may not charge, may not be specialists, are not part of a fire team, and do not gain experience.",
        "orders":""
    },
    {   # Cult Ambush
        "name":"Cult Ambush",
        "notes":"After deployment, but before the first battle round, roll a D6 for this model. On a 5+, this model can immediately move up to 6\".",
        "orders":""
    },
    {   # Cult Icon
        "name":"Cult Icon",
        "notes":"You can re-roll hit rolls of 1 for models within 6\" of a friendly model with a Cult Icon in the Fight phase.",
        "orders":""
    },
    {   # Daemon Hunters
        "name":"Daemon Hunters",
        "notes":"If this model attacks any Daemons in the Fight phase, you can re-roll failed wound rolls for those attacks.",
        "orders":""
    },
    {   # Death to the False Emperor
        "name":"Death to the False Emperor",
        "notes":"If a model with this ability makes an attack in the Fight phase which targets an Imperium model, each time you roll a hit roll of 6+ you may make an additional attack with the same weapon against the same target. These attacks cannot themselves generate any further attacks.",
        "orders":""
    },
    {   # Defence Tactics
        "name":"Defence Tactics",
        "notes":"When this model fires Overwatch, they successfully hit on a roll of 5 or 6.",
        "orders":""
    },
    {   # Disgustingly Resilient
        "name":"Disgustingly Resilient",
        "notes":"Each time a model with this ability loses a wound, roll a D6; on a 5+ the model does not lose that wound.",
        "orders":""
    },
    {   # Dodge
        "name":"Dodge",
        "notes":"",
        "orders":"This model has a 4+ invulnerable save in the Fight phase."
    },
    {   # Enhanced Data-Tether
        "name":"Enhanced Data-Tether",
        "notes":"You can re-roll failed Nerve tests for Skitarii models while a friendly model with an Enhanced Data-Tether is on the battlefield and not shaken.",
        "orders":""
    },
    {   # 'Ere We Go
        "name":"'Ere We Go",
        "notes":"Re-roll failed charge rolls for a model with this ability",
        "orders":""
    },
    {   # Extended Carapace
        "name":"Extended Carapace",
        "notes":"A model with an extended carapace has a Save characteristic of 4+ but loses the Swift and Deadly ability.",
        "orders":"",
    },
    {   # Favoured of Tzeentch
        "name":"Favoured of Tzeentch",
        "notes":"This model has a 5+ invulnerable save.",
        "orders":""
    },
    {   # Flip Belt
        "name":"Flip Belt",
        "notes":"This model can move across other models and terrain as if they were not there. In addition, it never suffers falling damage, and never falls on another model. If it would, instead place this model as close as possible to the point where it would have landed. This can bring it within 1\" of an enemy model.",
        "orders":"",
    },
    {   # Fortis Kill Team
        "name":"Fortis Kill Team",
        "notes":"When you add an Intercessor or a Reiver to your command roster you can choose for it to have the Deathwatch Faction keyword instead of the Adeptus Astartes Faction keyword. If you do so, it gains the Special Issue Ammunition ability but you must use the points values for its ranged weapons.",
        "orders":""
    },
    {   # For the Greater Good
        "name":"For the Greater Good",
        "notes":"When an enemy model declares a charge against a model from your kill team, models from your kill team with this ability within 6\" of one of the charging model’s targets may fire Overwatch as if they were also targeted. Once a model has done so, they cannot fire Overwatch or Retreat for the rest of the phase.",
        "orders":""
    },
    {   # Grapnel Launcher
        "name":"Grapnel Launcher",
        "notes":"A model with a grapnel launcher can climb any distance vertically, up or down, when it makes a normal move. Do not measure the distance moved this way.",
        "orders":""
    },
    {   # Grav-chute
        "name":"Grav-chute",
        "notes":"A model with a Grav-chute never suffers falling damage, and never falls on another model. If it would, instead place this model as close as possible to the point where it would have landed. This can bring it within 1\" of an enemy model.",
        "orders":""
    },
    {   # Gravity Wave Projector
        "name":"Gravity Wave Projector",
        "notes":"Enemy models beginning a charge move within 12\" of any Grav-inhibitor Drones reduce their charge distance by D3\".",
        "orders":""
    },
    {   # Guardian Fields
        "name":"Guardian Fields",
        "notes":"A Guardian Drone has a 5+ invulnerable save. Friendly T'au Empire models within 6\" of this model have a 6+ invulnerable save.",
        "orders":""
    },
    {   # Holo-suit
        "name":"Holo-suit",
        "notes":"This model has a 4+ invulnerable save.",
        "orders":"",
    },
    {   # Icon of Despair
        "name":"Icon of Despair",
        "notes":"Subtract 1 from the Leadership characteristic of enemy models within 6\" of any models equipped with an Icon of Despair.",
        "orders":""
    },
    {   # Icon of Flame
        "name":"Icon of Flame",
        "notes":"At the start of your turn in the Psychic phase, roll a D6 for each model from your kill team equipped with an Icon of Flame. On a 6 inflict 1 mortal wound on the closest enemy model within 12\" of the model being rolled for.",
        "orders":""
    },
    {   # Instinctive Behaviour
        "name":"Instinctive Behaviour",
        "notes":"Unless this model is within 24\" of a friendly Synapse model, you must subtract 1 from any hit rolls made for it when shooting any target other than the nearest visible enemy model, and subtract 2 from charge rolls made for it if it declares a charge against any model other than the nearest enemy model.",
        "orders":"",
    },
    {   # Lightning Reflexes
        "name":"Lightning Reflexes",
        "notes":"This model has a 5+ invulnerable save.",
        "orders":"",
    },
    {   # Mark of Chaos
        "name":"Mark of Chaos",
        "notes":"When you add a model with the Mark of Chaos keyword to your kill team, you can choose to replace it with one of the following keywords: Khorne, Nurgle, Tzeentch, or Slaanesh, or you can choose for it to have no mark. If you choose a mark, note this on the model's datacard.",
        "orders":""
    },
    {   # Neurostatic Aura
        "name":"Neurostatic Aura",
        "notes":"Subtract 1 from the Leadership characteristic of enemy models whilst they are within 3\" of one or more models with this ability.",
        "orders":""
    },
    {   # No Escape
        "name":"No Escape",
        "notes":"If an Infantry model within 1\" of any enemy models with this ability would Fall Back, the controlling players roll off. The model that would Fall Back can only do so if the player controlling it wins.",
        "orders":""
    },
    {   # Omnispex
        "name":"Omnispex",
        "notes":"At the start of each Shooting phase, you can choose another Skitarii model within 3\" of a friendly model equipped with an Omnispex that is not shaken. That model does not suffer penalties to their hit or injury rolls due to their target being obscured.",
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
    {   # Pulse Accelerator
        "name":"Pulse Accelerator",
        "notes":"Whilst a T'au Empire Infantry model is within 3\" of a friendly Pulse Accelerator Drone, increase the Range characteristic of that model’s pulse pistol, pulse carbine or pulse rifle by 6\".",
        "orders":""
    },
    {   # Rad-saturation
        "name":"Rad-saturation",
        "notes":"Reduce the Toughness characteristic of enemy models by 1 whilst they are within 1\" of one or more models with this ability.",
        "orders":""
    },
    {   # Reanimation Protocols
        "name":"Reanimation Protocols",
        "notes":"When an Injury roll is made for this model, on an unmodified roll of 6 the model is not taken out of action and does not suffer a flesh wound. Instead it is restored to 1 wound remaining with no flesh wounds.",
        "orders":""
    },
    {   # Recon Suite
        "name":"Recon Suite",
        "notes":"At the start of the Shooting phase, you can choose a Pathfinder from your kill team within 6\" of a friendly Recon Drone. Until the end of the phase, that model does not suffer penalties to their hit and Injury rolls due to their target being obscured.",
        "orders":""
    },
    {   # Rising Crescendo
        "name":"Rising Crescendo",
        "notes":"You may roll 3D6 instead of 2D6 for this model when making a charge roll, and may choose an enemy model within 18\" of this model as the target of a charge, rather than 12\".",
        "orders":"",
    },
    {   # Rites of Banishment
        "name":"Rites of Banishment",
        "notes":"When this model manifests the Psybolt psychic power it has a range of 12\". If Psybolt is successfully manifested, and the target model is a Daemon, the target suffers D3 mortal wounds, even if the result of the Psychic test was not 11+.",
        "orders":""
    },
    {   # Saviour Protocols
        "name":"Saviour Protocols",
        "notes":"If a Drone is within 3\" of a friendly T'au Empire Infantry model when an enemy attack successfully wounds it, you can inflict a mortal wound on the Drone, and the target model does not suffer any damage from this attack.",
        "orders":""
    },
    {   # Shadow in the Warp
        "name":"Shadow in the Warp",
        "notes":"Subtract 1 from any psychic tests made for enemy Psykers within 18\" of a model with this ability. Tyranids Psykers are not affected.",
        "orders":"",
    },
    {   # Shield Generator
        "name":"Shield Generator",
        "notes":"A model with a shield generator has a 4+ invulnerable save.",
        "orders":""
    },
    {   # Shimmershield
        "name":"Shimmershield",
        "notes":"Dire Avenger models within 2\" of a friendly model with a shimmershield have a 5+ invulnerable save.",
        "orders":""
    },
    {   # Sneaky Gits
        "name":"Sneaky Gits",
        "notes":"When an enemy player makes a hit roll for a shooting attack that targets this model, and this model is obscured, that hit roll suffers an additional -1 modifier.",
        "orders":""
    },
    {   # Special Issue Ammunition
        "name":"Special Issue Ammunition",
        "notes":"When this model fires an Auto Bolt Rifle, Bolt Carbine, Bolt Pistol, Bolt Rifle, Boltgun, Combi-Melta (Boltgun profile only), Combiplasma (Boltgun profile only), Heavy Bolt Pistol, Stalker Bolt Rifle or Stalker Pattern Boltgun, you can choose one kind of ammunition and apply the corresponding modifier.",
        "orders":[
            {
                "ordname":"Dragonfire Bolt",
                "ordnotes":"Add 1 to hit rolls for this weapon when targeting a model that is obscured."
            },
            {
                "ordname":"Hellfire Round",
                "ordnotes":"This weapon always wounds on a 2+."
            },
            {
                "ordname":"Kraken Bolt",
                "ordnotes":"Add 3\" to the range of this weapon if it is a Pistol – or 6\" otherwise – and improve the AP of the attack by 1, to a maximum AP of -2."
            },
            {
                "ordname":"Vengeance Round",
                "ordnotes":"Subtract 3\" from the range of this weapon if it is a Pistol – or 6\" otherwise – and improve the AP of the attack by 2, to a maximum AP of -3."
            },
        ],
    },
    {   # Storm Shield
        "name":"Storm Shield",
        "notes":"A model with a storm shield has a 3+ invulnerable save.",
        "orders":""
    },
    {   # Support Subroutines
        "name":"Support Subroutines",
        "notes":"Drones cannot be specialists, are not part of a fire team and cannot gain experience.",
        "orders":""
    },
    {   # Swift and Deadly
        "name":"Swift and Deadly",
        "notes":"You can re-roll failed charge rolls for this model.",
        "orders":"",
    },
    {   # Synapse
        "name":"Synapse",
        "notes":"Tyranids models automatically pass Nerve tests while within 12\" of any friendly models with this ability.",
        "orders":"",
    },
    {   # Target Lock
        "name":"Target Lock",
        "notes":"A model with a target lock does not suffer the penalty to their hit rolls for Advancing and firing Assault weapons.",
        "orders":""
    },
    {   # Terror Troops
        "name":"Terror Troops",
        "notes":"Enemy models must subtract 1 from their Leadership if they are within 3\" of any Reiver or Reiver Sergeant models.",
        "orders":""
    },
    {   # Toxin Sacs
        "name":"Toxin Sacs",
        "notes":"Any wound rolls of 6+ in the Fight phase for a model with toxin sacs cause 1 additional damage.",
        "orders":"",
    },
    {   # Transhuman Physiology
        "name":"Transhuman Physiology",
        "notes":"Ignore the penalty to this model's hit rolls from one flesh wound it has suffered.",
        "orders":""
    },
    {   # Voice of Command
        "name":"Voice of Command",
        "notes":"Once per battle round, if your Leader is on the battlefield and not shaken, they can issue an order to other members of your kill team at the start of the Shooting phase. To issue an order, pick another friendly Astra Militarum model within 12\" of your Leader and choose which order you wish to issue from the list opposite. A model may only be affected by one order per battle round.",
        "orders":[
            {
                "ordname":"Take Aim!",
                "ordnotes":"Re-roll hit rolls of 1 for the ordered model until the end of the phase."
            },
            {
                "ordname":"Bring it Down!",
                "ordnotes":"Re-roll wound rolls of 1 for the ordered model until the end of the phase."
            },
            {
                "ordname":"Forwards, for the Emperor!",
                "ordnotes":"The ordered model can shoot even if it Advanced in the previous Movement phase."
            },
            {
                "ordname":"Get Back in the Fight!",
                "ordnotes":"The ordered model can shoot this phase, even if it Fell Back in the Movement phase."
            },
            {
                "ordname":"Move! Move! Move!",
                "ordnotes":"Instead of shooting this phase, the ordered model immediately makes an Advance move as if it were the Movement phase."
            },
            {
                "ordname":"Fix Bayonets!",
                "ordnotes":"This order can only be issued to a model within 1\" of an enemy model. The ordered model immediately fights as if it were the Fight phase."
            },
        ],
    },
    {   # Vox-Caster
        "name":"Vox-Caster",
        "notes":"You can re-roll failed Nerve tests for Astra Militarum models while a friendly model with a Vox-Caster is on the battlefield and not shaken.",
        "orders":""
    },
],