# Astra Militarum Abilities Data Repo


abilities = [
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