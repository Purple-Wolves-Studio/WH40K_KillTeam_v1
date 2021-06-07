# Specialist Data Repo

import json


specialists = [
    {   # Leader
        "specname":"Leader",
        "tactics":[
            {
                "tacname":"Lead by Example",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this tactic when you pick a Leader from your kill team to fight in the Fight phase. Choose another friendly model within 3\" of them that is eligible to fight. You can fight with each of these models, in an order of your choice, before the next player's turn."
            },
            {
                "tacname":"Fire on my Target",
                "speclvl":2,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Leader of Level 2 or higher from your kill team to shoot in the Shooting phase. Choose another friendly model within 3\" of them that is eligible to shoot. You can make a shooting attack with each of these models, in an order of your choice, before the next player’s turn."
            },
            {
                "tacname":"Force of Will",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the battle round, if a Leader of Level 3 or higher from your kill team is on the battleeld and not shaken. In this battle round, your kill team does not suer the penalty for being broken."
            },
        ],
        "abilities":[
            {
                "abname":"Resourceful",
                "speclvl":1,
                "ablvl":1,
                "descrip":"As long as this model is on the battlefield and not shaken, you gain an additional Command Point at the beginning of the battle round."
            },
            {
                "abname":"Bold",
                "speclvl":2,
                "ablvl":2,
                "descrip":"This model automatically passes Nerve tests."
            },
            {
                "abname":"Inspiring",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Friendly models within 3\" of this model – as long as it is not shaken – automatically pass Nerve tests."
            },
            {
                "abname":"Paragon",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Re-roll hit rolls of 1 for friendly models within 3\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Tyrant",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Your opponent(s) must add 1 to Nerve tests for any enemy models within 6\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Tactician",
                "speclvl":3,
                "ablvl":3,
                "descrip":"As long as this model is on the battlefield and not shaken, roll a D6 each time you use a Tactic. On a 5+ you gain a Command Point."
            },
            {
                "abname":"Mentor",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Once per battle round, when you choose a friendly model within 3\" of this model to shoot in the Shooting phase – as long as this model is not shaken – you can re-roll failed hit rolls for that model until the end of the phase."
            },
        ],
    },
    {   # Combat
        "specname":"Combat",
        "tactics":[
            {
                "tacname":"Up and At 'em!",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic in the Fight phase, after attacking with a model from your kill team. Pick a Combat specialist from your kill team that has not yet attacked this phase: you can immediately fight with them."
            },
            {
                "tacname":"Defensive Fighter",
                "speclvl":2,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the Fight phase. Pick  a Combat specialist of Level 2 or higher from your kill team. Until the end of the phase, you must subtract 2 from that model’s Attacks characteristic (to a minimum of 1), but your opponent(s) must re-roll successful hit rolls made against that model."
            },
            {
                "tacname":"Force of Will",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic when a Combat specialist of Level 3 or higher from your kill team nishes a charge move within 1\" of an enemy model. Roll a D6; on a 5+ that enemy model suers 1 mortal wound."
            },
        ],
        "abilities":[
            {
                "abname":"Expert Fighter",
                "speclvl":1,
                "ablvl":1,
                "descrip":"Add 1 to this model’s Attacks characteristic."
            },
            {
                "abname":"Warrior Adept",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Add 1 to hit rolls for this model in the Fight phase."
            },
            {
                "abname":"Deadly Counter",
                "speclvl":2,
                "ablvl":2,
                "descrip":"If any hit rolls of 1 or less are made for a model’s attacks that target this model in the Fight phase, unless this model is shaken, roll a D6. On a 5+, the model that made the attack suffers 1 mortal wound after all of their attacks have been resolved."
            },
            {
                "abname":"Deathblow",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Any wound rolls of 6 you make for this model in the Fight phase inflict 1 mortal wound on the target in addition to any other damage."
            },
            {
                "abname":"Combat Master",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Add 1 to the Attacks characteristic of this model for each enemy model within 1\" of it at the start of the Fight phase, until the end of the phase."
            },
            {
                "abname":"Killer Instinct",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll any failed wound rolls you make for this model in the Fight phase."
            },
            {
                "abname":"Bloodlust",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll any failed charge rolls you make for this model."
            },
        ],
    },
    {   # Comms
        "specname":"Comms",
        "tactics":[
            {
                "tacname":"Rousing Transmission",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic in the Morale phase before taking any Nerve tests. Until the end of the phase you can subtract 1 from Nerve tests for models from your kill team as though the Comms specialist was within 2\" of them."
            },
            {
                "tacname":"Scanner Uplink",
                "speclvl":2,
                "comcost":2,
                "descrip":"Use this Tactic when you pick a model from your kill team that is within 6\" of a friendly Comms specialist of Level 2 or higher to shoot in the Shooting phase. That model can target an enemy model that is not visible to them. If they do so, a 6 is required for a successful hit roll irrespective of the model’s Ballistic Skill or any other modifiers, even if that weapon would normally hit automatically. The target is treated as obscured."
            },
            {
                "tacname":"New Intelligence",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic at the end of the Movemen the Movement phase. Pick a model from your kill team within 12\" of a friendly Comms specialist of Level 3 or higher. Ready that model."
            },
        ],
        "abilities":[
            {
                "abname":"Scanner",
                "speclvl":1,
                "ablvl":1,
                "descrip":"Once per Shooting phase, when you pick a model from your kill team to shoot that is within 6\" of this model, if this model is not shaken, you can add 1 to hit rolls for that model in this phase."
            },
            {
                "abname":"Expert",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Roll a D6 at the start of each battle round if this model is not shaken. On a 5+, you gain 1 additional Command Point. This additional Command Point is lost at the end of the battle round if not used."
            },
            {
                "abname":"Static Screech",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Once per battle at the start of the Fight phase, if this model is not shaken, subtract 1 from hit rolls for enemy models that make attacks while they are within 6\" of this model until the end of the phase."
            },
            {
                "abname":"Vox Ghost",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Subtract 1 from the Leadership characteristic of enemy models while this model is on the battlefield, as long as it is not shaken."
            },
            {
                "abname":"Command Relay",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Roll a D6 each time you use a Tactic while this model is on the battlefield and not shaken. On a 6 the Command Points spent on that Tactic are immediately refunded."
            },
            {
                "abname":"Triangulator",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Once per Shooting phase, when you pick a model from your kill team to shoot a Heavy weapon, if this model is not shaken, you can re-roll the dice when determining the number of attacks that model can make."
            },
            {
                "abname":"Vox Hacker",
                "speclvl":3,
                "ablvl":3,
                "descrip":"After each battle in which this model was in your kill team, if this model is not in Convalescence or dead, roll a D6. On a 5+ you gain 1 Intelligence."
            },
        ],
    },
    {   # Demolitions
        "specname":"Demolitions",
        "tactics":[
            {
                "tacname":"Custom Ammo",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Demolitions specialist from your kill team to shoot in the Shooting phase. You can add 1 to wound rolls for that model’s ranged weapons in this phase."
            },
            {
                "tacname":"Defensive Fighter",
                "speclvl":2,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the Shooting phase. Pick a Demolitions specialist of Level 2 or higher from your kill team. Roll a D6 each time that model loses a wound in this phase; on a 5+ that wound is not lost."
            },
            {
                "tacname":"Force of Will",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Demolitions specialist of Level 3 or higher from your kill team to shoot in the Shooting phase. In this Shooting phase, they can only shoot a single weapon, and that weapon can only fire 1 shot (even if it would normally fire more). However, that weapon’s Damage characteristic is increased by 2. You cannot use this Tactic in the same battle round as the Custom Ammo Tactic."
            },
        ],
        "abilities":[
            {
                "abname":"Breacher",
                "speclvl":1,
                "ablvl":1,
                "descrip":"You can add 1 to this model’s wound rolls against targets that are obscured."
            },
            {
                "abname":"Pyromaniac",
                "speclvl":2,
                "ablvl":2,
                "descrip":"You can re-roll wound rolls of 1 for this model when it is attacking with a weapon that hits automatically."
            },
            {
                "abname":"Grenadier",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Add 3\" to the range of any Grenade weapon this model uses. You can reroll hit rolls of 1 for Grenade weapons this model uses."
            },
            {
                "abname":"Saboteur",
                "speclvl":3,
                "ablvl":3,
                "descrip":"If this model is in your kill team and not out of action when you make your Casualty rolls, roll a D6. On a 5+ choose an opponent who played that mission to lose 1 Materiel."
            },
            {
                "abname":"Sapper",
                "speclvl":3,
                "ablvl":3,
                "descrip":"If this model is in your kill team and you choose the Plant Traps strategy, you can add 1 to the number of pieces of terrain you can booby trap."
            },
            {
                "abname":"Siegemaster",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can add 1 to Injury rolls caused by this model’s attacks in the Shooting phase if those Injury rolls are for models that are obscured."
            },
            {
                "abname":"Ammo Hound",
                "speclvl":3,
                "ablvl":3,
                "descrip":"If this model is in your kill team and not out of action when you make your Casualty rolls, roll a D6. On a 5+ you gain 1 Materiel."
            },
        ],
    },
    {   # Heavy
        "specname":"Heavy",
        "tactics":[
            {
                "tacname":"More Bullets",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Heavy specialist from your kill team to shoot in the Shooting phase. You can add 1 to the number of shots fired by that model’s ranged weapons, with the exception of weapons that would otherwise fire 1 shot (e.g. an Assault 2 weapon would fire 3 shots, but a Rapid Fire 1 weapon at long range would fire 1 shot) in this Shooting phase."
            },
            {
                "tacname":"Overwhelming Firepower",
                "speclvl":2,
                "comcost":2,
                "descrip":"Use this Tactic when you pick a Heavy specialist of Level 2 or higher from your kill team to shoot in the Shooting phase. that model can shoot twice in this Shooting phase; after they have shot a first time, immediately shoot with them again. You cannot use this Tactic in the same battle round as the More Bullets Tactic."
            },
            {
                "tacname":"Unkillable",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic at the start of your turn in the Morale phase. Pick a Heavy specialist of Level 3 or higher from your kill team that has one or more flesh wounds. Remove one of that model’s flesh wounds."
            },
        ],
        "abilities":[
            {
                "abname":"Relentless",
                "speclvl":1,
                "ablvl":1,
                "descrip":"This model does not suffer the -1 penalty for shooting with a Heavy weapon after moving in the preceding Movement phase, or for shooting an Assault weapon after Advancing."
            },
            {
                "abname":"Suppressor",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Enemy models that are targeted by this model in the Shooting phase suer a -1 penalty to their hit rolls until the end of the phase."
            },
            {
                "abname":"Extra Armour",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Ignore AP characteristics of -1 for attacks that target this model."
            },
            {
                "abname":"Devastator",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can reroll the damage for this model’s ranged weapons that have a random Damage characteristic."
            },
            {
                "abname":"Rigorous",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll hit rolls of 1 for this model in the Shooting phase."
            },
            {
                "abname":"Indomitable",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Once per battle round, you can make your opponent re-roll the Injury dice for this model."
            },
            {
                "abname":"Heavily Muscled",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll wound rolls of 1 for this model in the Fight phase."
            },
        ],
    },
    {   # Medic
        "specname":"Medic",
        "tactics":[
            {
                "tacname":"Stimm-shot",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the Movemen the Movement phase. Pick a model from your kill team within 2\" of a friendly Medic specialist that is not shaken. You can add 1 to Advance rolls and charge rolls for that model, and add 1 to that model’s Attacks characteristic until the end of the battle round."
            },
            {
                "tacname":"Painkiller",
                "speclvl":2,
                "comcost":2,
                "descrip":"Use this Tactic at the end of the Movemen the Movement phase. Pick a model from your kill team within 2\" of a friendly Medic specialist of Level 2 or higher that is not shaken. Add 2 to that model’s Toughness characteristic until the end of the battle round."
            },
            {
                "tacname":"Emergency Resuscitation",
                "speclvl":3,
                "comcost":2,
                "descrip":"Use this Tactic when a Medic specialist of Level 3 or higher from your kill team that is not shaken is within 2\" of another model from your kill team that suffers an Out of Action Injury roll result. That model suffers a Flesh Wound result instead."
            },
        ],
        "abilities":[
            {
                "abname":"Reassuring",
                "speclvl":1,
                "ablvl":1,
                "descrip":"This model is never treated as being shaken when taking Nerve tests for other models in your kill team."
            },
            {
                "abname":"Field Medic",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Roll a D6 when a friendly model within 3\" of this model suffers a wound, as long as this model is not shaken; on a 6 that wound is not lost."
            },
            {
                "abname":"Anatomist",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Re-roll wound rolls of 1 for this model in the Fight phase."
            },
            {
                "abname":"Trauma Specialist",
                "speclvl":3,
                "ablvl":3,
                "descrip":"When an Injury roll is made for a friendly model within 3\" of this model, as long as this model is not shaken, roll an additional dice and use the lowest result."
            },
            {
                "abname":"Triage Expert",
                "speclvl":3,
                "ablvl":3,
                "descrip":"If this model is in your kill team and not out of action at the end of a battle, and you roll a Dead result when making a Casualty roll for a model from your kill team, you can roll a D6. On a 4+ apply the Convalescence result for that model instead."
            },
            {
                "abname":"Interrogator",
                "speclvl":3,
                "ablvl":3,
                "descrip":"At the end of any battle in which you were victorious, if this model was in your kill team and not out of action, roll a D6. On a 5+ you gain 1 Intelligence."
            },
            {
                "abname":"Toxin Synthesiser",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Before deployment, you can pick up to D3 models from your kill team. Until the end of the battle, add 1 to wound rolls for attacks made with melee weapons those models are armed with."
            },
        ],
    },
    {   # Scout
        "specname":"Scout",
        "tactics":[
            {
                "tacname":"Quick March",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Scout specialist from your kill team to move in the Movement phase. You can either increase the model’s Move characteristic by 2\" this phase or you can re-roll the dice when this model Advances in this phase."
            },
            {
                "tacname":"Marked Positions",
                "speclvl":2,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the Shooting phase. Pick an enemy model within 6\" of a Scout specialist of Level 2 or higher from your kill team that is not shaken. You can re-roll hit rolls of 1 for shooting attacks made by models in your kill team that target that enemy model until the end of the phase."
            },
            {
                "tacname":"Move Unseen",
                "speclvl":3,
                "comcost":2,
                "descrip":"Use this Tactic at the start of your turn in the Movement phase. Pick a Scout specialist of Level 3 or higher from your kill team that is not shaken. Remove that model from the battlefield and set it up again anywhere within 18\" of its previous position and more than 3\" from any enemy models. It is considered to have Advanced."
            },
        ],
        "abilities":[
            {
                "abname":"Swift",
                "speclvl":1,
                "ablvl":1,
                "descrip":"You can re-roll Advance rolls for this model."
            },
            {
                "abname":"Forward Scout",
                "speclvl":2,
                "ablvl":2,
                "descrip":"This model automatically passes dangerous terrain tests."
            },
            {
                "abname":"Pathfinder",
                "speclvl":2,
                "ablvl":2,
                "descrip":"If this model is not in Convalescence, you can add or subtract 1 from the result when you roll to determine a mission. If you do, this model must be included in your kill team."
            },
            {
                "abname":"Skirmisher",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Your opponent(s) must subtract 1 from hit rolls for shooting attacks that target this model if the firing model is more than 12\" from this model and this model is not shaken or obscured."
            },
            {
                "abname":"Vanguard",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll hit rolls of 1 in the Shooting phase for attacks made by models from your kill team against enemy models that are within 6\" of this model, as long as this model is not shaken."
            },
            {
                "abname":"Observer",
                "speclvl":3,
                "ablvl":3,
                "descrip":"If this model is in your kill team, you can roll a D6 at the start of the Scouting phase. On a 4+ you can pick an additional strategy."
            },
            {
                "abname":"Explorer",
                "speclvl":3,
                "ablvl":3,
                "descrip":"After each battle in which this model was in your kill team, if this model is not in Convalescence, you can roll a D6. On a 5+ you gain 1 Territory."
            },
        ],
    },
    {   # Sniper
        "specname":"Sniper",
        "tactics":[
            {
                "tacname":"Careful Aim",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic when you choose a Sniper specialist from your kill team to shoot in the Shooting phase. You can add 1 to hit rolls for that model until the end of the phase."
            },
            {
                "tacname":"Headshot",
                "speclvl":2,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Sniper specialist of Level 2 or higher from your kill team to shoot in the Shooting phase. Until the end of the phase, when that model shoots at obscured targets they are considered not to be obscured."
            },
            {
                "tacname":"Quick Shot",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Sniper specialist of Level 3 or higher from your kill team to shoot in the Shooting phase. In this Shooting phase, double the number of shots fired by that model’s ranged weapons (e.g. an Assault 2 weapon would fire 4 shots), but subtract 1 from hit rolls for that model. You cannot use this Tactic in the same battle round as the Headshot Tactic."
            },
        ],
        "abilities":[
            {
                "abname":"Marksman",
                "speclvl":1,
                "ablvl":1,
                "descrip":"You can re-roll hit rolls of 1 for this model when it makes a shooting attack."
            },
            {
                "abname":"Assassin",
                "speclvl":2,
                "ablvl":2,
                "descrip":"You can re-roll wound rolls of 1 for this model when it makes a shooting attack."
            },
            {
                "abname":"Sharpshooter",
                "speclvl":2,
                "ablvl":2,
                "descrip":"If this model is Readied, add 1 to hit rolls when it makes a shooting attack."
            },
            {
                "abname":"Deadeye",
                "speclvl":3,
                "ablvl":3,
                "descrip":"On an unmodified wound roll of 6 for this model’s shooting attacks, increase the Damage characteristic of that attack by 1."
            },
            {
                "abname":"Armour Piercing",
                "speclvl":3,
                "ablvl":3,
                "descrip":"On an unmodified wound roll of 6 for this model’s shooting attacks, improve the AP characteristic of that attack by 1."
            },
            {
                "abname":"Mobile",
                "speclvl":3,
                "ablvl":3,
                "descrip":"This model does not suffer the -1 penalty for shooting with a Heavy weapon after moving in the preceding Movement phase, or for shooting an Assault weapon after Advancing."
            },
            {
                "abname":"Eagle-eye",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Increase the Range characteristic of all Rapid Fire and Heavy weapons this model is armed with by 6\"."
            },
        ],
    },
    {   # Veteran
        "specname":"Veteran",
        "tactics":[
            {
                "tacname":"Adaptive Tactics",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic at the start of the first battle round, but before the Initiative phase. Pick a Veteran specialist from your kill team. They can make a normal move or Advance. You can only use this Tactic once per battle."
            },
            {
                "tacname":"Well Drilled",
                "speclvl":2,
                "comcost":2,
                "descrip":"Use this Tactic at the start of your turn in the Shooting phase. Pick a Veteran specialist of Level 2 or higher from your kill team. Ready them unless they are within 1\" of an enemy. They can shoot in that phase as if they had not moved in the Movement phase."
            },
            {
                "tacname":"Roll with the Hits",
                "speclvl":3,
                "comcost":1,
                "descrip":"Use this Tactic during your opponent’s turn in the Shooting phase. Pick a Veteran specialist of Level 3 or higher from your kill team that has been Injured, before your opponent makes the Injury roll. Your opponent can only roll a single dice for that Injury roll."
            },
        ],
        "abilities":[
            {
                "abname":"Grizzled",
                "speclvl":1,
                "ablvl":1,
                "descrip":"This model ignores penalties to its Leadership characteristic and Nerve tests."
            },
            {
                "abname":"Practised",
                "speclvl":2,
                "ablvl":2,
                "descrip":"You can re-roll one hit roll or wound roll for this model in each battle round."
            },
            {
                "abname":"Seen It All",
                "speclvl":2,
                "ablvl":2,
                "descrip":"You can subtract 1 from Nerve tests for models from your kill team within 3\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Survivor",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can add 1 to saving throws for this model."
            },
            {
                "abname":"One-man Army",
                "speclvl":3,
                "ablvl":3,
                "descrip":"This model generates 1 Command Point at the beginning of each battle round, unless it is shaken or out of action. This Command Point can only be used for Veteran Tactics."
            },
            {
                "abname":"Battle Scarred",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Enemy models suffer -1 Leadership whilst they are within 6\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Nerves of Steel",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll failed hit rolls for this model when it fires Overwatch."
            },
        ],
    },
    {   # Zealot
        "specname":"Zealot",
        "tactics":[
            {
                "tacname":"Killing Frenzy",
                "speclvl":1,
                "comcost":1,
                "descrip":"Use this Tactic when you pick a Zealot specialist from your kill team to fight in the Fight phase. Until the end of the phase, each time you make a hit roll of 6+ for that model you can make an additional attack with the same weapon against the same target. These attacks cannot themselves generate any further attacks."
            },
            {
                "tacname":"Martyr",
                "speclvl":2,
                "comcost":2,
                "descrip":"Use this Tactic when a Zealot specialist of Level 2 or higher from your kill team loses their last wound, before any player rolls on the Injury  table. You may immediately shoot with one of its weapons as if it were the Shooting phase, or pile in and make one attack as if it were the Fight phase."
            },
            {
                "tacname":"Terrifying Rampage",
                "speclvl":3,
                "comcost":2,
                "descrip":"Use this Tactic at the start of the Morale phase. Pick a Zealot specialist of Level 3 or higher from your kill team that took an enemy model out of action in the preceding Fight phase. Each enemy model within 6\" of the Zealot must take a Nerve test. If the test is failed the model is shaken."
            },
        ],
        "abilities":[
            {
                "abname":"Frenzied",
                "speclvl":1,
                "ablvl":1,
                "descrip":"You can add 1 to this model’s Attacks and Strength characteristics in a battle round in which they charged."
            },
            {
                "abname":"Exultant",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Opponents must re-roll unmodified hit rolls of 6 for models from their kill team within 3\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Flagellant",
                "speclvl":2,
                "ablvl":2,
                "descrip":"Roll a D6 each time this model loses a wound. On a 6 the wound is ignored."
            },
            {
                "abname":"Puritan",
                "speclvl":3,
                "ablvl":3,
                "descrip":"You can re-roll hit rolls in the Fight phase for this model against enemy models that do not have a Faction keyword in common with it."
            },
            {
                "abname":"Rousing",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Add 1 to the Leadership characteristic of models from your kill team within 6\" of this model, as long as it is not shaken."
            },
            {
                "abname":"Fanatical",
                "speclvl":3,
                "ablvl":3,
                "descrip":"This model automatically passes Nerve tests."
            },
            {
                "abname":"Strength of Spirit",
                "speclvl":3,
                "ablvl":3,
                "descrip":"Subtract 1 for Injury rolls made for this model."
            },
        ],
    },
],