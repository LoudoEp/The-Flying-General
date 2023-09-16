# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[h]", color ="#00ffff", what_prefix='"', what_suffix='"')
define bull = Character("Bull", color ="#fff", what_prefix='"', what_suffix='"')
define bandit = Character("Bandit", color ="#fff", what_prefix='"', what_suffix='"')
define intro = Character(None, kind=nvl, what_italic = True)

default h = "Me"

################################################################################

### TRANSFORMS ###

transform bounce:
    yoffset 0
    easein .175 yoffset -14
    easeout .175 yoffset 0
    yoffset 0

transform ride:
    pause 0.4
    yoffset 0
    easein .175 yoffset -14
    easeout .175 yoffset 0
    yoffset 0
    easein .175 yoffset -8
    easeout .175 yoffset 0
    yoffset 0
    easein .175 yoffset -25
    easeout .175 yoffset 0
    yoffset 0
    repeat

################################################################################

### WOLF ###

define wolf = Character("[w]", color ="#cc6600", what_prefix='"', what_suffix='"')
define sidewolf = Character("[w]", color ="#cc6600", what_prefix='"', what_suffix='"', image="wolf")

default w = "Wolf"

layeredimage wolf:
    group weapon:
        attribute sword:
            "images/wolf/wolf_sword.avif"
    group body:
        attribute cross default:
            "images/wolf/wolf_cross.avif"
        attribute open:
            "images/wolf/wolf_open.avif"
    group face:
        attribute normal default:
            "images/wolf/wolf_normal.avif"
        attribute angry:
            "images/wolf/wolf_angry.avif"
        attribute blush:
            "images/wolf/wolf_blush.avif"
        attribute concerned:
            "images/wolf/wolf_concerned.avif"
        attribute crying:
            "images/wolf/wolf_crying.avif"
        attribute happy:
            "images/wolf/wolf_happy.avif"
        attribute lovey:
            "images/wolf/wolf_lovey.avif"
        attribute sad:
            "images/wolf/wolf_sad.avif"
        attribute serious:
            "images/wolf/wolf_serious.avif"
        attribute shocked:
            "images/wolf/wolf_shocked.avif"
    group eyes:
        attribute lookdown:
            "images/wolf/wolf_lookdown.avif"
    group clothing:
        attribute shirt:
            "images/wolf/wolf_shirt.avif"
        attribute shirt2:
            "images/wolf/wolf_shirt2.avif"
        attribute shirt3:
            "images/wolf/wolf_shirt3.avif"
    group band:
        attribute sash:
            "images/wolf/wolf_sash.avif"
        attribute sashcross:
            "images/wolf/wolf_sashcross.avif"
        attribute wounds:
            "images/wolf/wolf_wounds.avif"

image side wolf = LayeredImageProxy("wolf")

################################################################################

### DRAGON ###

define dragon = Character("[d]", color ="#ff6666", what_prefix='"', what_suffix='"')
define sidedragon = Character("[d]", color ="#ff6666", what_prefix='"', what_suffix='"', image="dragon")

default d = "Dragon"

layeredimage dragon:
    group body:
        attribute base default:
            "images/dragon/dragon_base.avif"
        attribute campfire:
            "images/dragon/dragon_campfire.avif"
    group face:
        attribute angry:
            "images/dragon/dragon_angry.avif"
        attribute awake:
            "images/dragon/dragon_awake.avif"
        attribute campangry:
            "images/dragon/dragon_campangry.avif"
        attribute campconcerned:
            "images/dragon/dragon_campconcerned.avif"
        attribute camphappy:
            "images/dragon/dragon_camphappy.avif"
        attribute campsad:
            "images/dragon/dragon_campsad.avif"
        attribute campserious:
            "images/dragon/dragon_campserious.avif"
        attribute campshocked:
            "images/dragon/dragon_campshocked.avif"
        attribute concerned:
            "images/dragon/dragon_concerned.avif"
        attribute happy:
            "images/dragon/dragon_happy.avif"
        attribute relax:
            "images/dragon/dragon_relax.avif"
        attribute sad:
            "images/dragon/dragon_sad.avif"
        attribute serious:
            "images/dragon/dragon_serious.avif"
        attribute shocked:
            "images/dragon/dragon_shocked.avif"
        attribute sleepy:
            "images/dragon/dragon_sleepy.avif"

image side dragon = LayeredImageProxy("dragon")

################################################################################

### MANATEE ###

define manatee = Character("[m]", color ="#999966", what_prefix='"', what_suffix='"')
define sidemanatee = Character("[m]", color ="#999966", what_prefix='"', what_suffix='"', image="manatee")

default m = "Manny"

layeredimage manatee:
    always:
        "images/manatee/manatee_base.avif"
    group face:
        attribute calm default:
            "images/manatee/manatee_calm.avif"
        attribute angry:
            "images/manatee/manatee_angry.avif"
        attribute concerned:
            "images/manatee/manatee_concerned.avif"
        attribute happy:
            "images/manatee/manatee_happy.avif"
        attribute sad:
            "images/manatee/manatee_sad.avif"
        attribute shocked:
            "images/manatee/manatee_shocked.avif"

image side manatee = LayeredImageProxy("manatee")

################################################################################

### COLOSSUS ###

layeredimage colossus:
    group body:
        attribute resting:
            "images/Strike/Colossus_resting.avif"
        attribute strike:
            "images/Strike/Colossus_strike.avif"
        attribute moving:
            "images/Strike/Colossus_moving.avif"
    group boom:
        attribute boom:
            "images/Strike/Boom.avif"
    group explosion:
        attribute exp1:
            "images/Strike/Exp1.avif"
        attribute exp2:
            "images/Strike/Exp2.avif"
        attribute exp3:
            "images/Strike/Exp3.avif"
        attribute exp4:
            "images/Strike/Exp4.avif"
        attribute exp5:
            "images/Strike/Exp5.avif"

################################################################################

### BACKGROUNDS ###

image black = "#000"
image outside = "images/bg/romeo-varga-qUd3m6puYGM-unsplash.avif"
image startingtent = "images/bg/scott-goodwill-y8Ngwq34_Ak-unsplash.avif"
image starting_point = "images/bg/starting_point.avif"
image ridewiththedragon = "images/bg/motorbike-by-Vovaas-Montenegro-from-Pixabay.avif"
image pavedroad = "images/bg/pexels-marcos-miranda-672597.avif"
image bg_strike = "images/Strike/pexels-bas-masseus-1253639.avif"
image fatedroad = "images/bg/pexels-dn-milk-935484.avif"
image thatnight = "images/bg/thatnight.avif"
image bikers = "images/bg/bike-by-Masud-Rana-from-Pixabay.avif"
image minotaur = "images/bg/man-by-Harshal-from-Pixabay.avif"
image pooryote = "images/bg/asphalt-by-Samson-Jay-from-Pixabay.avif"
image pitstop = "images/bg/pexels-kaique-rocha-775203.avif"
image campire = "images/bg/bonfire-by-Pexels-from-Pixabay.avif"
image fox = "images/bg/sebastiaan-stam-EwjBfu6j9Xg-unsplash.avif"
image asphalt = "images/bg/asphalt-by-JillJJekins-from-Pixabay.avif"
image camp = "images/bg/camp.avif"
image camp2 = "images/bg/camp2.avif"
image banditcity = "images/bg/eve-56232_640-by-Reimund-Bertrams-from-pixabay.avif"
image alley = "images/bg/lost-places-by-Peter-H-from-Pixabay.avif"
image building = "images/bg/house-by-Joe-Kniesek-from-Pixabay.avif"
image countingfloors = "images/bg/ansaf-ahmad-80NCypGsSNk-unsplash.avif"
image skyline = "images/bg/sydney-skyline-by-Theresa-Schenk-from-Pixabay.avif"
image intheair = "images/bg/milky-way-by-FelixMittermeier-from-Pixabay.avif"
image nightsky = "images/bg/constellations-by-StockSnap-from-Pixabay.avif"
image corridor = im.MatrixColor(
    "images/bg/scary-by-robinsonk26-from-pixabay.avif",
    im.matrix.desaturate()*im.matrix.tint(0.7, 0.7, 1.0))
image beds = im.MatrixColor(
    "images/bg/urban-by-Pixxel-Worx-from-Pixabay.avif",
    im.matrix.desaturate()*im.matrix.tint(0.7, 0.7, 1.0))
image homebase = "images/bg/vadim-sadovski-Um22Cte8XbQ-unsplash.avif"
image hug = "images/bg/astronomy-by-LoveArtLiveArt-from-Pixabay.avif"
image canyon = "images/bg/fairyland-canyon-by-Adam-Derewecki-from-Pixabay.avif"
image moon = "images/bg/moon-by-Robert-Karkowski-from-Pixabay.avif"
image cabin = "images/bg/cabin-by-Dorothe-from-Pixabay.avif"
image xiangqi = "images/bg/chinese-chess-by-An-Wang-from-Pixabay.avif"
image cattura = "images/bg/cattura.avif"
image cattura2 = "images/bg/cattura2.avif"
image redgeneral = "images/bg/redgeneral.avif"
image soldier = "images/bg/soldier.avif"
image flyinggeneral = "images/bg/flyinggeneral.avif"
image generalmove = "images/bg/generalmove.avif"
image castle = "images/bg/castle.avif"
image bridge = "images/bg/bridge-by-Kevan-Craft-from-Pixabay.avif"
image titanus = "images/bg/titanium-2812785.avif"
image challenge = "images/bg/sword-by-Bruce-from-Pixabay.avif"
image credits = "images/bg/credits.avif"

# IMAGES #

image wsword = "images/sabre-by-Ryaszard-Porzynski-from-Pixabay.avif"
image mysword = "images/mysword.avif"
image slash = "images/bg/slash.avif"
image slash2 = "images/bg/slash2.avif"
image bigjump = "images/bigjump.avif"

################################################################################

### AUDIO ###

define audio.rap = "audio/342359__stankbeast__city-rap-beat.ogg"
define audio.resonance = "audio/Resonance.ogg"
define audio.xiangqi = "audio/airtone_-_blackSnow_1.ogg"
define audio.precarity = "audio/airtone_-_precarity_10.ogg"
define audio.timebeing = "audio/airtone_-_timebeing_1.ogg"
define audio.road = "audio/Apoxode_-_44.ogg"
define audio.bandits = "audio/Apoxode_-_Enchanted_ft._Rewob.ogg"
define audio.epic = "audio/Audiorezout - Wolf.ogg"
define audio.theme = "audio/djlang59_-_Peace_and_Blessings.ogg"
define audio.dying = "audio/essesq_-_With_These_Wings_1.ogg"

### SOUND EFFECTS ###

define audio.swordclang = "audio/soundeffects/CC0 574043__thecrow_br__sword.mp3"
define audio.motorbike = "audio/soundeffects/Attribution 4 to Satoration 54901__satoration__drive-by-moped.ogg" ### DA CONVERTIRE
define audio.fire = "audio/soundeffects/CC0 624425__foleyhaven__fire_burning_03.flac"
define audio.birds = "audio/soundeffects/CC0__hargissssound__spring-birds-raw-new-jersey.ogg"

################################################################################


# The game starts here.

#TODO FIX MUSIC X
#TODO CONSISTENT USE OF ... X
#TODO BETTER COMESTHEDEVIL CG X
#TODO REMOVE RANDOM DUDES FROM CAMPFIRE CG X
#TODO FIX THEO'S SPRITE X
#TODO CONSISTENT USE OF THE WORDS VILLAGE/CITY X
#TODO FIX WOLF'S CLOTHES+SWORD POSE X

label start:
    stop music fadeout 6.0
    scene black
    intro "This is a work of fiction."
    intro "None of the characters featured in this story are based on real people."
    intro "This story is SFW, but contains descriptions of violence."
    intro "Please enjoy."
    nvl clear
    play music birds fadein 10.0
    pause 5
    wolf "I can't believe you really want to go back to the normal world."
    show outside:
        zoom 0.4
        xpos 0.1
    show startingtent:
        zoom 0.45
    show wolf shirt at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    mc "I'm not going back to the normal world."
    pause 1.5
    wolf "Why are you packing your stuff then?"
    pause 0.2
    mc "My friend needs me."
    pause 1
    wolf "You {i}are{/i} going back to the normal world then."
    pause 0.2
    "I can no longer contain my irritation at his stubbornness."
    mc "Because my friend needs me!"
    "I search his eyes for some trace of understanding."
    "He's not even looking at me. His gaze is fixed on my backpack, which I am filling with the few supplies I have, gathered in our tent."
    show wolf concerned
    mc "Fuck! Did all the hits you took on the head make you forget what it's like to have a friend?"
    show wolf normal
    "I immediately regret raising my voice."
    "But he just stands there, unmoving, as solid as a statue."
    "Huffing in exasperation, I close my backpack and begin the difficult process of rolling the sleeping bag that has been my bed for the past… how many years has it been?"
    show wolf lookdown open shirt2:
        easein 2.0 ypos 1.5
    show mysword:
        zoom 0.8
        xpos 0.273
        ypos 0.46
    "He bends down. For a moment I delude myself into thinking he's finally relented and he's going to help me pack my things."
    show wolf open shirt2:
        easein 2.0 ypos 1.1
    show mysword:
        easein 2.0 ypos 0.06
    "Instead, he gets back up almost as soon as he's picked something off the ground… my sword."
    "I interrupt my struggle against my sleeping bag, that is stubbornly refusing to fold, and I stare at the blade, my whole body tense and ready to try a desperate but futile escape."
    "But even now, he doesn't deign to glance at me. His gaze is firmly focused on my blade in his paws, as if he's examining it for the first time."
    show wolf -lookdown
    wolf "I did forget."
    ####
    "It's hard to discern his emotions as he says that. His words sound sad but not regretful, they're filled with solemnity."
    "As if in admitting it, he has made a final decision."
    mc "I am sorry."
    "What a stupid response. But what else is there to say?"
    "The wolf offers me the hilt of my sword, keeping the blade towards himself."
    wolf "You'll find you've forgotten it too."
    wolf "Because we are Seekers."
    scene black with dissolve
    ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    scene starting_point at center:
        zoom 0.4
    show dragon sleepy at center:
        zoom 0.5
        ypos 1.0
        rotate 20
    with Dissolve(2.0)
    mc "I'm ready."
    show dragon awake at bounce
    pause 0.4
    show dragon:
        easein 1.2 xpos 0.7 rotate 0
    "The dragon, who was dozing off in the sun leaning against his bike, jumps up and places a paw on one of the handlebars."
    show dragon concerned with Dissolve(0.2)
    "He glances at the sword hanging by my side and then looks for something behind me."
    show dragon serious with Dissolve(0.2)
    dragon "And the wolf?"
    mc "He's not coming."
    dragon "I gathered as much. But shouldn't we wait for him to come and say bye?"
    "I swallow a lump of saliva stuck in my throat, as I resist my instinct to peek over my shoulder, driven by a vain hope of finding him there, ready to follow me on this stranger's bike."
    mc "We've already said goodbye."
    "I say it peremptorily, hoping it will get the message across that I don't want to hear any more questions in the same vein."
    show dragon:
        xzoom -1
        easein 1.0 xpos 0.6 ypos 0.95
    pause 1
    show dragon -serious
    "The effect is immediate: the dragon hops on his motorbike and, with a decisive flick of his wrist, the engine begins to roar."
    dragon "Let's go then."
    scene black with Dissolve(0.5)
    "The dragon slides forward on the saddle, squeezing as much as he can in an attempt to make enough room for me to climb on board."
    "It isn't easy, and my movements are much more indecisive than his. Between the weight of my backpack and my sword, and the limited space afforded to me by his huge butt and tail, it takes me some shifting around before I find a comfortable position."
    sidedragon "Are you okay back there?"
    sidedragon "You can sit on my tail if it's more cozy, Manny always does it. You won't crush me, don't worry."
    mc "No, it's alright."
    "I have never been on a motorcycle, and the seat isn't exactly comfortable, but the idea of piggybacking on the larger reptile is out of the question, despite his chubby shape making him surprisingly inviting."
    mc "Let's go. To save your boyfriend."
    play music motorbike ###########
    "The bike roars in agreement. As soon as the dragon takes his foot off the ground, the wind starts whipping on my face."
    scene ridewiththedragon at ride:
        zoom 1.1 ypos -0.1
    with Dissolve(5.0)
    "My first impression of riding a motorcycle is bad."
    "It shakes and wobbles so much that I have to keep my legs squeezed together in order not to get thrown off."
    "At the same time, the impredictable sudden jerks make the whole experience very unpleasant on my balls."
    "I can't help but wonder what makes a man desperate enough to ride these infernal machines, when the discomfort abruptly disappears."
    "The bike is darting smoothly now, so much so that it makes me wonder if we took flight."
    scene pavedroad at ride:
        zoom 0.4
    with dissolve
    "But looking down I realize that the stark difference is due to us having reached one of the paved roads built before the apocalypse."
    "They're not perfect, and looking ahead of me, over the big dragon's shoulders, I can see plenty of spots where the ancient material, called asphalt, is cracked."
    "Not to mention the literal holes here and there, which force the dragon to swerve and move in a zigzag fashion."
    "But after the hellish experience of a few seconds ago, I silently thank the Ancestors for their technology. It's no surprise that old relics of the past civilization like these are still so essential today."
    pause 3
    "I can't see much looking ahead of me, other than the seemingly endless asphalt path."
    "So I decide to finally turn around and glance behind me."
    scene black with None
    show bg_strike
    show colossus resting
    with dissolve
    pause 0.5
    show bg_strike:
        ypos 2.5
    show colossus:
        ypos 2.5
    with MoveTransition(5.0)
    "And, of course, the first thing I see, even at this distance, is Him."
    "The Colossus."
    pause 2
    "It's so strange to see Him from this far away. If I wasn't aware of how much distance we have already covered, I might have mistaken Him for a normal person's silhouette, instead of the several hundreds feet tall monstrosity He really is."
    "Looking up to Him while standing at His feet, in all His grandeur, it is almost impossible to appreciate His very human shape."
    "At His feet, the Colossus looks as far removed from a human as one can be. From the very first time I have laid eyes on Him, I've always thought of Him as a force of nature."
    pause 1
    "But seeing Him again from this angle reminds me that He is not."
    pause 1
    "He is very artificial, created by men to be used against other men."
    "To keep them out{w=0.3}.{w=0.3}.{w=0.3}. On this side."
    "I'm pulled away from my reverie when the Colossus's body starts to move."
    show bg_strike
    show colossus moving
    with Dissolve(1.0)
    "My body responds by instinct, stiffening, and I have to consciously refrain from bringing my hand to my sword."
    "We're so far away now that I don't even feel the ground shaking under my feet as the Colossus assumes a fighting stance. Or maybe the shaking is masked by the moving motorcycle."
    "The Colossus' halberd comes down with incredible speed, until it comes to a sudden stop in mid-air."
    show colossus strike with vpunch
    pause 0.05
    show colossus boom
    pause 0.05
    show colossus exp1
    pause 0.05
    show colossus exp2
    pause 0.05
    show colossus exp3
    pause 0.05
    show colossus exp4
    pause 0.05
    show colossus exp5 with vpunch
    pause 0.5
    show colossus -boom -exp5 with dissolve
    "Even though I should be too far to see it from here, I swear I can distinguish a tiny blurred figure, who impossibly blocks their gargantuan opponent's blow."
    "Is it… a wolf?"
    pause 2
    "He wasted no time in resuming his endless battle."
    stop music fadeout 3.5

###### NEW SCENE ######

    scene black with Dissolve(5.0)
    scene fatedroad:
        zoom 0.7
    with Dissolve(2.0)
    play music bandits
    "This paved road. I remember traveling it under very different circumstances."
    "I was still a few moons away from my coming of age then. That means it's already been five years."
    scene thatnight:
        zoom 0.7
    with Dissolve(5.0)
    "I wasn't hurtling at superhuman speeds back then, carried by a miraculous machine from the antediluvian times."
    "No. I was on foot."
    "Each step was a herculean victory against the demands of my body, worn out by days of forced marching and scarce food, of just lying down in defeat."
    scene bikers with Dissolve (2.0)
    "The shackles on my and the other prisoners' wrists jangled constantly throughout the march, a sound far more intolerable than the roaring motors of the bandits' bikes."
    "Not that that noise wasn't there to torment us as well. Some of our captors darted on these powerful mounts, and they had no qualms about taunting and intimidating us with their superiority."
    "They sped forward down the road, as if to leave us behind, and then back again, to remind us that escape was impossible."
    scene thatnight:
        zoom 0.7
    with Dissolve(2.0)
    "The memories of this whole ordeal are fuzzy, except for one, indelibly burned into my brain."
    "There was another boy, a coyote, just a couple of years younger than me."
    scene ontheroad:
        zoom 0.55
    with Dissolve(2.0)
    "He threw himself on the ground without even slowing down, exhausted, and in a weak voice he prayed our captors. He couldn't take another step."
    "The entire caravan had come to a halt at that point, and despite the pathetic sight, what I was feeling in that moment was not sympathy for my companion, but hope. Hope that they would be forced to give us just a few hours to rest."
    "Maybe a sip of water."
    scene comesthedevil:
        zoom 0.55
    with Dissolve(2.0)
    pause 4
    scene minotaur:
        zoom 0.5 ypos -1250
    with Dissolve(2.0)
    "One of the bikers, a middle-aged bull, pulled up beside us, demanding to know from his accomplices on foot why the caravan had stopped."
    "The other lower ranking gang members explained the situation to him, pointing to the gasping coyote on the ground."
    scene minotaur:
        zoom 0.5 ypos -1250
        ease 6.0 ypos -550
    "The bull didn't even have a moment's hesitation."
    scene black with Dissolve(2.0)
    "He got off his bike, even though he left the engine running."
    "As the rest of us watched in horror, he pulled out a rope, securely anchored to the back of his motorcycle, and tied the boy by the ankles at the other end."
    "The coyote was too exhausted to struggle. He only groaned pathetically."
    "And the rest of us, even knowing what was about to happen, were too afraid to do anything."
    "His work finished, the bandit got back on his bike and turned his head towards us."
    bull "If anyone else of you worms needs a ride, don't hesitate to ask."
    "His grin was so wide, so unrestrained, I could count all the teeth in his mouth."
    "Having got no reaction other than terrified stares, the bull turned around and revved the engine. The next moment he was hurtling down the paved road at full speed."
    "I did have time to see the poor coyote's body, dragged by the uncaring mechanical monster and its even more uncaring monstrous driver, slammed into the asphalt a couple of times before they disappeared from view."
    scene pooryote with Dissolve(2.0)
    "When the bike finally came back several minutes later, the poor boy's corpse was in an indescribable state."
    "He had only one eye remaining, red and swollen."
    "The other was gone, together with much of that side of his head…"
    stop music fadeout 5.0
    scene black with Dissolve(5.0)
    pause 0.1
    ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    play music road fadein 3.5
    scene pitstop:
        zoom 0.6 ypos -1700
    with Dissolve(5.0)
    "It's pitch dark when we finally stop."
    show dragon serious at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    dragon "Let's get away from the road. It's not safe to stay here when we're not on the move."
    "I nod in agreement, even though he can't see me from behind his back. I'd rather not bump into bandits prematurely. And despite the Ancestors' gifts, my little butt is sore after so many hours on the road."
    "The dragon leads his bike by the handlebars and together we head into the vegetation by the roadside. It is especially thick, which is probably why he decided to stop here."
    "It's not too impenetrable, camping won't be a problem. But dense enough to shield us from any possible passerby once we get a little further."
    mc "I'll build a campfire."
    "Hunger is starting to take a hold of my stomach."
    show dragon -serious
    dragon "You're kidding, right? {i}I'm{/i} the dragon, I'll be the one on fire duty."
    "His tone is surprisingly warm and friendly, considering the circumstances. I'm surprised he isn't more worried about Manny's fate, or at least, he doesn't show it as much since we've left."
    mc "Okay, I'll set up the tent then."
    hide dragon with dissolve
    "We are both very quick in our respective tasks."
    "The dragon demonstrates remarkable strength. He manages to break branches with its bare paws, building a pile in a short time."
    "Having collected the wood, all that's left for him to do is breathe."
    #sound
    stop music fadeout 5.0
    play music fire volume 1.5
    scene campire at center
    with Dissolve(2.0)
    "As for me, having spent the last five years in a tent, setting it up and folding it away has become a daily routine."
    show dragon campfire relax at right:
        zoom 0.8
        ypos 1.3
    with dissolve
    "The wood in the campfire crackles invitingly. I sit down next to the dragon, who is already lying on his side, perfectly comfortable next to the flames."
    "I drag my backpack to my legs and undo the knot. I take out the rations I've prepared, wrapped in fabric salvaged from the ruins."
    mc "I have fish."
    "Better to start from the fresh food."
    "The dragon draws air from his nostrils as I take out the fish from its wrapping, and the fire seems to dance in response, as if he was blowing on a candle."
    show dragon -relax with dissolve
    dragon "Sounds delicious. Thanks Unagi."
    $ h = "Unagi"
    "I stare at him suspiciously at hearing him say my name. But I find none of the incredulity and amusement I spotted in his eyes a few hours ago, when I told him my new name for the first time."
    "He had the kind of look that said \"that's the most ridiculous name I've ever heard\"."
    "I offer him one of my two fish to roast and in exchange he offers me a branch, that I can use to pierce my meal and cook it on the fire. I do not hesitate to do just that, perhaps getting the fish a bit too close to the fire in my impatience."
    "A smell of burned food fills the air."
    mc "I'm sorry. I forgot your name."
    "I am sure he said it to me when he introduced himself. I thought I'd have no trouble remembering the name of the first new person I've interacted with in months, but I guess old habits die hard."
    $ d = "Theo"
    show dragon camphappy with dissolve
    dragon "Theo. And there's no need to apologize."
    dragon "In fact, I'm afraid I didn't even ask for your… mate's name?"
    "I'm pretty sure Theo had tried to ask him, but the wolf had shut him up with a look."
    show dragon -camphappy with dissolve
    mc "Cody."
    show dragon campshocked with dissolve
    dragon "Uh."
    show dragon -campshocked with dissolve
    "The dragon pulls his fish away from the fire, chuckling."
    dragon "Your names are not as scary as I expected, considering…"
    "With a loud {i}chomp{/i}, Theo swallows half of his fish in one bite."
    show dragon camphappy with dissolve
    dragon "If you don't mind me asking… Why Unagi?"
    show dragon -camphappy with dissolve
    dragon "That's not the name Manny told me to look for."
    "I pull my fish away from the fire, but I don't eat it just yet. I stare into its blank eye, lost in thought."
    show dragon campserious with dissolve
    mc "I changed my name when I became a Seeker."
    mc "I chose Unagi because…"
    "I wave the stick with my roasted fish in front of me, meaningfully."
    mc "Well, our diet consists of a lot of fish that we catch from the river ourselves."
    show dragon campconcerned with dissolve
    dragon "Isn't it dangerous?"
    "It is the first time that his tone is less than jovial. Seeing {i}Him{/i} for the first time must have left an impression."
    mc "No. The Colossus only attacks those attempting to cross the bridge. Or the river. As long as you don't venture too far from the riverside, it's safe."
    show dragon campsad with dissolve
    "The air feels heavier as soon as I mention the word \"Colossus\". I am reminded that, for normal people, that monster is an object of religious awe, while for us Seekers… it's just part of our lives."
    show dragon campserious with dissolve
    dragon "Has anyone ever managed to cross the bridge?"
    "It's my turn to remain silent. Of course, this is the first thing they always want to know."
    mc "No."
    show dragon campshocked with dissolve
    dragon "Never?"
    show dragon campserious with dissolve
    mc "Never."
    pause 1
    show dragon campsad with dissolve
    pause 5
    show dragon -campsad with dissolve
    dragon "I hope I'm not making you uncomfortable. Am I asking too many questions?"
    mc "Not really."
    "It's just that I'm not used to talking to other people anymore."
    "Even with other Seekers, relationships are kept at a minimum. Everyone is busy with their own training and there's not many of us to begin with."
    "I spend all my days with Cody, so much so that we hardly need to talk amongst ourselves to understand each other."
    show dragon campconcerned with dissolve
    dragon "Sounds like a lonely life."
    dragon "May I ask what made you want to become a Seeker?"
    mc "If Manny told you about me, you should already know."
    stop music fadeout 3.5
    play music bandits
    pause 2
    scene black with dissolve
    "When the bandit biker gang came to Manny's and my village, our families were faced with a choice."
    "Give away freely what the bandits demanded: supplies, valuables… and slaves. Young, strong, healthy boys and young, attractive girls are always the most desired."
    "Or fight. Defend their children."
    "My parents and Manny's, along with everyone else in the village, picked the easy option."
    "They chained us in the public square, while my parents watched in silence. And they took us away."
    scene thatnight:
        zoom 0.7
    with Dissolve(2.0)
    "Sometimes I still wonder what kind of life I would have had."
    scene pooryote with Dissolve(2.0)
    "I have nightmares of that terrible march, that constant struggle to find the strength to take the next step towards…"
    scene black with Dissolve(2.0)
    stop music fadeout 3.5
    "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    play music resonance
    $ w = "???"
    wolf "Hey!"
    scene thatnight:
        zoom 0.7
    show wolf open angry sash sword at right:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
        zoom 0.6 ypos 0.8
    with Dissolve(2.0)
    "A young wolf, with an imposing physique. He wears some pants made with that special fabric from before the apocalypse, the kind that bends but doesn't stretch, and carries a sword secured to his back."
    $ w = "Wolf"
    wolf "Where are you taking them?"
    "There is a moment of confusion as the sad procession stops, bandits and prisoners alike trying to find the voice's origin."
    "It takes me a moment to make out the warrior's features in the pitch black night, but the defiant gleam in his eyes is unmistakable."
    "Did anyone really come to save us?"
    "My faint hope is prompty dashed when one of the bandits, a fox, roars in laughter."
    scene fox:
        zoom 0.35 ypos -150
    with dissolve
    bandit "Got any problem, doggy?"
    "A dozen guns appear in our captors' paws, all idly pointed at the stranger."
    bandit "Do you miss any of your friends? Don't worry, you can join them."
    bandit "Drop that sword, raise your paws up, and come have your leash put on."
    "The bandit and his partners burst out laughing some more, like the guy just made the funniest joke they have ever heard."
    scene thatnight:
        zoom 0.7
    show wolf open normal sash sword at right:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
        zoom 0.6 ypos 0.8
    with dissolve
    "The wolf gives that guy a sharp look, but spreads his arms wide and slowly raises his hands, towards the hilt of his sword."
    scene black
    play audio swordclang
    pause 0.5
    show slash with Dissolve(0.1)
    pause 0.2
    hide slash with Dissolve(0.25)
    "The next instant he's disappeared and an unnatural scream rings out in the night. A sharp, desperate, bubbling cry, as if it were coming from under a layer of mud."
    "It belongs to the bandit who was making fun of the stranger: his body has been cut cleanly in two. The two halves are dropping to the ground, as if in slow motion."
    "I don't have time to see them hit the ground, because in another instant I'm surrounded by screams, gunshots, splashes of blood."
    "Someone next to me is waving their arms around in a panic and they push me face down on the asphalt."
    scene asphalt:
        matrixcolor BrightnessMatrix(-0.6)
    with vpunch
    "A sharp pain assaults my nose and the taste of blood fills my mouth."
    "But I don't move, I stay there on the ground, paralyzed with fear, my face pushed against the hard road surface."
    "All hell is breaking loose around me, and I am sure that, if I were to get up, I would be shot dead by one of the stray gunshots ringing all around me."
    "I stay like this for what feels simultaneously like a few seconds and an eternity."
    "Until suddenly: silence."
    show wolf open sash sword at center:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
        zoom 1.4 ypos 0.6
    with dissolve
    "I risk looking up and the first thing I see is the stranger's open paw next to my head."
    wolf "Are you okay?"
    "Am I?"
    "I finally bring a hand to my face. As soon as I touch my nose it stings."
    "I must have broken it. But right now I'm just glad I'm still alive."
    mc "I'm okay."
    wolf "Let me see it."
    show wolf:
        linear 2.0 ypos 1.7
    "His paws grab my shoulders and, as if I weighed nothing, he lifts me up off the ground. I'm a bit wobbly on my feet, but the wolf keeps holding me up with one paw to help me keep my balance."
    "Meanwhile, with his other paw he cups my face between his digits. He's a bit rough with it, and I can feel the strength of those fingers, but he handles me carefully enough not to hurt me with his claws."
    wolf "Yeah, you're fine, you just hit your nose a bit hard."
    "He takes a step back."
    scene thatnight:
        zoom 0.7
    show wolf sashcross sword at right:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
        zoom 0.8 ypos 1.1
    with dissolve
    wolf "Put your hands forward and spread them as wide as you can."
    "Instinctively, I do as he  tells me. My short period in captivity has accustomed me to obeying orders without hesitation, but in his case there is something more."
    "The way he took control of the situation makes me feel like a child, who knows he can trust his parents' demands."
    show wolf open sash with dissolve
    "He raises his sword."
    wolf "Do not move."
    scene black
    play sound swordclang
    pause 0.5
    show slash with Dissolve(0.1)
    pause 0.2
    hide slash with Dissolve(0.25)
    pause 0.1
    scene thatnight:
        zoom 0.7
    show wolf open sash at right:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
        zoom 0.8 ypos 1.1
    show wsword:
        zoom 0.8
        xpos 0.545
        ypos 0.06
    with dissolve
    "In one fluid motion, he cuts the handcuffs as if they were paper and they drop to the ground with a loud {i}clang{/i}. Finally being able to move my hands after what feels like an eternity, I rub my aching wrists."
    wolf "Now let's also free your mates."
    stop music fadeout 3.5
    scene black with Dissolve(2.0)
    pause 2
    play music fire volume 1.5
    scene campire at center
    show dragon campfire campserious at right:
        zoom 0.8
        ypos 1.3
    with Dissolve(4.0)
    mc "He saved us that night. And he agreed to train me as his disciple."
    $ w = "Cody"
    show dragon -campserious with dissolve
    dragon "Mmm, Manny told me about that. He saved both you and Manny that night, as well as many others. And yet…"
    show dragon campserious with dissolve
    dragon "Only you followed him and became a Seeker. Why's that?"
    scene black
    pause 2
    wolf "Are you sure?"
    pause 1
    wolf "I must warn you, it's a lonely life."
    pause 1
    mc "We will have each other, for as long as you'll allow me to stay, sir!"
    scene campire at center
    show dragon campfire at right:
        zoom 0.8
        ypos 1.3
    with Dissolve(1.0)
    mc "He is… an inspiring person."
    "What should I have done? Go back to my parents, as if nothing had happened? {i}He{/i} was the one who fought for me."
    mc "He looked like someone worth following."
    show dragon camphappy with dissolve
    dragon "So, you only stayed for the wolf, huh?"
    show dragon -camphappy with dissolve
    mc "At first, maybe, that was my reason for staying. That, and he could train me. To fight like Seekers do."
    mc "Plus, there was nothing for me out here. The Seeker's Quest gave me a goal."
    show dragon campserious with dissolve
    dragon "The Seeker's Quest? You mean defeating the Colossus?"
    dragon "That's the Seekers' mission, isn't it?"
    mc "No."
    "I've finished my fish at this point. I throw the stick into the campfire and it is immediately engulfed in flames."
    mc "Our Quest is…"
    play music theme fadeout 1.5 fadein 2.5
    scene black with Dissolve(3.0)
    sidewolf serious shirt "This is where I live."
    show camp2:
        zoom 1.3 ypos -300
    with Dissolve(5.0)
    "There's a tinge of embarassment in his voice. These are the most desolate ruins I have ever been in. People are usually quick to settle in them."
    sidewolf normal shirt "There it is. Can you see it?"
    "Cody points to a spot on the horizon."
    "I pause for a moment to catch my breath after the long walk, then move closer to him."
    show camp2:
        ease 5.0 zoom 1.0 ypos 0
    "The first thing I see in the distance is the Colossus. It is impossible to live in this area of the continent without always having Him silhouetted on the horizon, an immutable point of reference."
    "But it's the first time I've been this close. His mighty figure fills much of the sky in front of me."
    "His size is not that of something that can be alive."
    "Yet, I do know that the Colossus can move, I have occasionally seen His shape change position in the distance."
    sidewolf "Can you see it?"
    mc "Yeah, it's the Colossus…"
    "I feel my legs shaking under me and I have to fight the desire to retrace my steps, as far away from here as possible."
    "The Colossus is standing still, motionless, apparently indifferent. But if He were to start moving, He could be upon us in a couple of seconds and swat us like flies."
    sidewolf "No, not that! Look at His feet."
    "I hear the frustration in the wolf's voice, as if I'm missing on an obvious but crucial detail."
    show camp2:
        ease 5.0 zoom 1.2 xpos -300
    mc "The bridge."
    sidewolf "Yes. The Colossus is a machine, created to prevent anyone from crossing."
    mc "And you Seekers try anyway."
    sidewolf "Yes."
    "He points at something closer to us, in the ruins of the village."
    sidewolf "I don't know if you can see them from here, but Seekers are camped all around the village. We live here, training day and night."
    sidewolf "My tent is over there."
    "My gaze follows the direction of his claw, but I see no notable feature where he's pointing."
    "The whole village appears empty, and in a wild state."
    pause 2
    "How can normal people hope to defeat that monster? It's madness."
    "I stare into the wolf's eyes. He looks determined, composed, like when he saved me."
    "I don't know if I really believe that it is possible to fight the Colossus on equal terms. But from the light in his eyes, one thing I'm sure of: he believes it."
    mc "Who created the Colossus? What is He protecting?"
    "The wolf once again directs my gaze back towards the river."
    "With his claw he points further, beyond the bridge, beyond the Colossus."
    hide camp2
    show camp:
        zoom 1.2 xpos -300
    with Dissolve(5.0)
    "There is a village there, unlike any village I have ever seen."
    "Its architecture vaguely reminds me of all the other ruins I've seen, but its design is different. Elegant, immaculate, seemingly untouched by the passage of time."
    "It looks like I've always imagined those past civilizations to look like in their prime."
    scene black with dissolve
    pause 0.1
    scene camp
    show wolf normal shirt3 sashcross sword at center:
        zoom 1.5 ypos 1.9
    with dissolve
    wolf "That's Glimmering City. The city that survived the apocalypse."
    "His voice is a whirlwind of emotions as he says these words, they're difficult to pin down."
    "Longing. Pride. Contempt. Hope."
    show wolf blush with dissolve
    mc "It's… beautiful."
    "The first beautiful thing I have ever laid my eyes on."
    stop music fadeout 5.0

###### NEW SCENE ######

    scene black with Dissolve(5.0)
    pause 0.1
    play music rap fadein 5.0
    scene banditcity:
        zoom 3.0
    with Dissolve(2.0)
    "We arrive at the biker gang's village late the following afternoon. It consists of ruins from some pre-apocalyptic civilization that the bandits have taken over."
    "In particular, I recognize a large rectangular building, simple and utilitarian, with the ancient mysterious word \"Costco\" written on its side."
    "\"Costco\". I know it is one of those words the Ancestors used to identify special vaults scattered all around the continent, storing rations and artifacts."
    "They didn't help the Ancestors much when the apocalypse came, but they are highly coveted by all sorts of groups today."
    show dragon angry at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    dragon "I saw them take Manny there."
    "Theo points to a different building, not far from the vault. Unlike the latter, the facade of this one is covered with windows, a sure sign that it is a structure with several floors inside."
    show dragon concerned with dissolve
    mc "Let's hide here. I'm going to rescue Manny under the cover of darkness."
    show dragon angry with dissolve
    dragon "{i}We{/i} will save him! I'm also ready to risk my life!"
    "They really do love each other."
    show dragon sad with dissolve
    mc "No. No offense, but you'd only slow me down."
    "I don't want to have to worry about nothing bad happening to him."
    mc "You wait here. Be ready to run away with your bike as soon as I get Manny back."
    "He glances at the bike, doubtful."
    show dragon concerned with dissolve
    dragon "I don't know if there's going to be room enough for the three of us. I know I take up a lot of space."
    dragon "You and Manny should use it to escape. He will show you where we live, and I will join you there as soon as I can."
    show dragon shocked with dissolve
    mc "No."
    "This dragon's selflessness is almost irritating. He's too eager to throw away his own life."
    show dragon serious with dissolve
    mc "When I get back with Manny, you two use the motorbike. I'll cover your escape if necessary."
    mc "And then I'll run after you."
    show dragon concerned with dissolve
    "The dragon raises an eyebrow."
    mc "I can run very fast, it's part of my training."
    "It is impossible to face the Colossus one-on-one without moving as fast as He does."
    hide dragon with Dissolve(2.0)
    "He still needs some convincing, but after some back-and-forth he agrees on my plan of action."
    "Together we let the hours pass. I remain alert, watching from a distance the daily lives of this den of outlaws."
    "Theo stays by my side the whole day, but it's clear he doesn't know how to spend his time productively. His gaze wanders, and he anxiously alternates between standing still and pacing back and forth."
    scene black with dissolve
    "The sun finally sets behind the vault and the constellations soon fill the sky to shine some light on this cloudless night."
    "A few bonfires and electric lights appear around the village, but for the most part it's hard to make anything out."
    "After spending the last few years gazing in envy and wonder at Glimmering City from across the river, I'm reminded of what the average village on the continent looks like."
    "Moving undetected under these circumstances will be a kid's game."
    mc "I'm going."
    "I'm already headed towards my goal at full speed before Theo's answer has a chance to reach me."
    scene alley:
        matrixcolor BrightnessMatrix(-0.2)*SaturationMatrix(0.5)
    with dissolve
    "Keeping out of view, I dash from tree to tree, from building to building, stopping each time to assess my surroundings."
    "It's clear that this village is used to being left alone: there are no guards at its edges and sneaking only starts to become difficult once I'm already deep inside."
    "Even when I have to sneak close to some passerby, they're not too observant."
    "The only difficult part will be getting into the building."
    "There too, there are no guards outside, but it is possible to glimpse silhouettes moving beyond a transparent entrance door."
    "I lift my gaze upwards. Unlike the entrance hall, no light is shining from the windows of the upper floors. It will be easier to enter from above."
    "I circle the building to avoid the main entrance. On the opposite side, I lean my back against a wall and catch my breath."
    scene countingfloors:
        matrixcolor BrightnessMatrix(-0.1)*SaturationMatrix(0.8)
        zoom 0.38
    with dissolve
    "I've already counted the windows above me during the day. Nine floors."
    "The hardest part will be to avoid jumping too high. {w=0.5}This is a much shorter distance than I'm used to when I fight the Colossus."
    scene black with dissolve
    "I spread my legs wide and close my eyes, feeling the ground beneath my feet."
    show wolf shirt at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    wolf "Remember{w=0.5}, our bodies aren't made to jump hundreds of feet in the air. That's impossible."
    wolf "You'll never do it if you rely on your own strength."
    wolf "Instead, you must channel the force of the Earth beneath you. For the whole planet, feet are an insignificant unit of measure."
    hide wolf with dissolve
    pause 1
    sidewolf angry shirt "Borrow that strength!"
    pause 2
    "I can feel it. The strength stored under the Earth's crust."
    "I need to borrow less than I usually do."
    "I flex my legs and open my eyes."
    "The next instant I'm arrowing through the air, the ground already distant below me."
    show intheair:
        zoom 2.0
    with dissolve
    "Unfortunately, it seems I miscalculated my distance after all. I'm already flying far past the building."
    show skyline:
        zoom 1.3
    with dissolve
    "Somersaulting in midair, I turn my body so that my head points towards one of the top floor windows."
    "And I kick the air behind me."
    "My body violently changes direction, shooting at a downward angle towards the window."
    show skyline:
        linear 2 zoom 20
    pause 0.1
    scene black
    "Luckily the glass was already shattered, so I make less noise than expected upon landing, when I crash through the window and roll onto the floor."
    scene corridor:
        matrixcolor BrightnessMatrix(-0.1)
    with dissolve
    "I waste no time getting up and running down the hall, in case anyone heard me."
    "I hear footsteps echoing down the corridor. Looks like the upper floors are not abandoned after all. But I have to start my search from somewhere."
    "I open all the doors I come across. I prefer being fast to being sneaky now, because the footsteps are getting closer and closer."
    "All the doors I open just lead to dark and empty rooms. Until…"
    stop music fadeout 6.0
    scene beds:
        matrixcolor BrightnessMatrix(-0.1)
    with Dissolve(2.0)
    "There are a dozen guys in this room, including Manny, lying or sitting on as many dirty looking beds."
    "Their gazes are broken, emptied of any vitality, all except Manny's, who lights up upon recognizing me."
    show manatee happy at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    manatee "Dwain!"
    show manatee concerned with dissolve
    "I brush away the discomfort at being called by my old name."
    pause 1
    "It's not just their gazes that are broken. These poor people's bodies speak of the torture they suffered."
    "Manny takes half a step towards me and the noise his feet make draws my gaze and makes me notice the thick chain confining him to the bed."
    play music epic
    show manatee shocked with dissolve
    bull "Stop right there, ape-boy!"
    hide manatee with dissolve
    "I turn to see half a dozen bandits rushing to the scene, guns already drawn."
    "But I pay no attention to any of them, except one."
    "I recognized his voice when he spoke."
    scene black with dissolve
    pause 0.1
    scene minotaur:
        matrixcolor BrightnessMatrix(-0.1)
        zoom 0.5 xpos -200 ypos -550
    with Dissolve (2.0)
    "He's been haunting my dreams all these years, but this time he's here, in the flesh."
    "Surrounded by the kind of miserable fate my imagination has been conjuring up in my mind, in my nightmares, without ever being able to visualize it accurately."
    "Today, I see it with clarity."
    "The veil has been lifted on what fate would have awaited me at the end of that paved road. If it hadn't been for him."
    "And they had the gall to spit on Cody's act of kindness on that day, and take Manny away again."
    "I draw my sword. The goons are yelling at me words that my mind doesn't even register."
    "I'm not thinking anymore."
    "My hand moves automatically."
    "Why did I sneak here?"
    "These pathetic guys are nothing compared to the danger I've been facing every day for the last five years."
    "Why was I trying to avoid fighting them?"
    "To spare {i}their{/i} lives?"
    "What a joke."
    "The world would be better off with them {i}dead{/i}."
    scene black
    "I swing my sword as if it were an executioner's axe, and this time I hold back none of the strength I would use against the Colossus."
    stop music fadeout 3.5
    play sound swordclang
    pause 0.5
    show slash:
        zoom 0.8
    with Dissolve(0.1)
    pause 0.5
    hide slash
    play sound swordclang
    pause 0.5
    show slash2:
        zoom 0.8
    with Dissolve(0.25)
    pause 0.5
    hide slash2
    play sound swordclang
    pause 0.5
    show slash at left:
        xzoom -1 zoom 0.8
    with Dissolve(0.1)
    pause 0.3
    hide slash
    pause 3
    "The two halves of the bull's body fall to the ground, just as the whole building begins to shake."
    scene building:
        matrixcolor BrightnessMatrix(-0.1)*SaturationMatrix(0.8)
    with vpunch
    "My attack didn't just cut the bandit in half. This entire side of the building was slid like a pie. And now the structure is collapsing."
    "All around me the terrified screams of the prisoners, unable to escape, fill the room, together with the equally desperate cries of their tormentors, who are running towards the corridor."
    "Shit. I shouldn't have lost my control."
    "He taught me better than that."
    play music precarity
    scene black with Dissolve (2.0)
    pause 0.1
    scene homebase:
        zoom 0.7 ypos -1700
    show wolf serious shirt at center:
        zoom 0.8
        ypos 1.1
    with Dissolve(3.0)
    wolf "Does it hurt?"
    "I respond with nothing but a grunt as Cody disinfects my wound with some vodka he probably saved for much happier occasions."
    show wolf -serious with dissolve
    wolf "Drink."
    "He hands me the rest of the bottle."
    mc "You shouldn't waste your liquor like that."
    wolf "It isn't wasted."
    "He shoves it into my hands."
    wolf "You'll need it to block out the pain. I need to stitch up this wound."
    "He stares at me with an intense gaze, a gaze that says \"Don't you dare argue.\""
    "I don't start a battle that I already know I will lose. I've had enough with losing today."
    hide wolf with dissolve
    "I gulp down the alcoholic contents of the bottle, stopping to catch my breath only when I run out of air. It's strong and my body immediately feels warmer, and more relaxed."
    "Meanwhile, Cody produces a needle from somewhere among his supplies. He is holding it close to the flame."
    mc "I am sorry."
    show wolf concerned shirt at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    wolf "What are you sorry for?"
    pause 3.
    wolf "What happened?"
    show wolf shocked with dissolve
    mc "What do you mean \"what happened\"? I lost."
    wolf "Won't be the last time."
    show wolf -shocked with dissolve
    wolf "But something was different today."
    "I look away."
    wolf "The way you were fighting was different."
    show wolf angry with dissolve
    wolf "You were reckless. Unfocused."
    wolf "You looked angry."
    show wolf -angry with dissolve
    mc "Maybe I am!"
    "I blurt it out with such force that it's pretty clear there is no \"maybe\"."
    wolf "Tell me why."
    "Again, I stay silent. I'm not sure I know the answer myself."
    wolf "It's important. The way you fought is not good."
    wolf "You're lucky you got away with just a scratch. You can't let anger cloud your mind when you're up against the Colossus."
    "His utilitarianism is making me even more angry, so much so that I blurt out a response without worrying about how he's going to react."
    show wolf shocked with dissolve
    mc "I've been thinking about leaving."
    show wolf sad with dissolve
    pause 2
    "I expect him to say something, but he's just staring at me, patiently waiting for me to continue."
    mc "It's no longer how it was when I first got here."
    mc "I… I don't believe anymore it's possible to beat the Colossus."
    "I expect him to contradict me, but once again his mouth remains closed, his expression unchanged."
    pause 1.0
    "He knows it too, doesn't he?"
    show wolf normal with dissolve
    wolf "Why were you angry? You haven't told me yet."
    pause 1.0
    mc "It's the only thing that keeps me going."
    mc "Whenever the thought of giving up crosses my mind… "
    extend "I think about{w=0.5} {i}them{/i}."
    "He understands who I'm talking about."
    mc "I cannot stand it. Countless Seekers, who've been training their whole lives, destroyed their bodies, and coughed up blood for this cause, died without ever setting foot in Glimmering City."
    show wolf sad with dissolve
    mc "And I know {i}you{/i} will be one of them!"
    show wolf concerned with dissolve
    mc "And me too, if I don't run away now!"
    mc "Meanwhile, countless children will have been born in the City since the apocalypse."
    mc "They've been given {i}for free{/i} what we're fighting for and we'll never have."
    pause 2
    mc "Why?"
    "There's a knot in my throat I can't get rid of. The last speck of frustration that is burning in my chest."
    show wolf shocked with dissolve
    mc "HOW {w=0.5}{i}DARE{/i}{w=0.5} THEY {w=0.2}KEEP {w=0.5}{i}US{/i} {w=0.5}OUT?"
    hide wolf with dissolve
    "There. I said it."
    "I feel such uncontrollable rage at those people, even the little children who are blameless…"
    "… that if I had the power to finally enter Glimmering City…"
    "… or destroy it for good…"
    "… I'm not sure what option I'd pick."
    pause 1
    show wolf blush shirt at center:
        zoom 0.8
        ypos 1.1
    with dissolve
    wolf "Unagi?"
    mc "Uh?"
    pause 2
    show wolf happy
    wolf "I love you."
    stop music fadeout 5.0
    scene black with Dissolve(6.0)
    # ROUGH SCRIPT, DELETED SCENE
    # "I was ready to throw you out, you know that? That boy I rescued from the street, Dwain, was full of hopes and illusions."
    # "I saw the way you looked at me, full of admiration for the young warrior who saved you from bad men, for the hero who in your eyes had the strength to right every wrong and fix the world."
    # "I knew it would be wrong to take that Dwain under my wing."
    # "You understand that now, don't you… Unagi?"
    # He says it almost [leading].
    # "A young man with the delusion of saving the world, of being able to save the world...the world would have eaten him alive, chewed up and spat his carcass contemptuously into the waters below the bridge along with so many other madmen."
    # He shows me the needle, [which is by now searing with white light].
    # "But when I showed you Glimmering City that time, and saw your eyes shine and fill with tears, I knew I was wrong about you."
    # "I knew you understood the truth. That this is a hopeless endevour.
    # That this world is beyond saving.

###### NEW SCENE ######

    play music theme fadein 0.5
    "Because of my sloppiness, in the end I had no other choice."
    "After I saved Manny and as many other prisoners from the collapsing building as I could, any more attempts at sneaking my way out were out of the window. I had to slaughter the entire biker gang village."
    sidemanatee "Is Theo with you?"
    mc "He's waiting for us, come with me."
    "He and I sneak away from the other freed slaves. They'll have to fend for themselves now, we can't take them all away on Theo's bike."
    "They'll manage: the old Costco is theirs now if they want it. They can take what they need and try to go back to their home villages, or take over this one and start from scratch."
    sidedragon happy "Manny!"
    "The dragon says his boyfriend's name too loudly for a whisper and too softly for a scream."
    scene hug with dissolve
    "In an instant he leaps out of the foliage he was hiding in and crushes the poor manetee in his arms, causing him to let out a pained groan."
    "The dragon releases him from his mighty grip and wastes no time examining his wounds."
    sidedragon angry "Oh my God, baby. I'm so sorry. What did those animals do to you?"
    sidemanatee concerned "Don't worry, I'm fine. I'll survive."
    sidemanatee happy "All thanks to Dw… Unagi."
    "I quickly raise a hand to interrupt their attempts to thank me."
    "Thank me for what? At the end of the day, this mission hardly required any effort on my part."
    mc "Let's beat it. The way we agreed."
    "I stare meaningfully at the dragon. My voice is firm, in a challenge to him against arguing with me again."
    "He simply nods. Not without a few weak complaints from Manny, the dragon loads him onto the bike and the two set off without me."
    scene canyon:
        zoom 1.5
    with Dissolve(2.0)
    ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    show bigjump:
        xpos 1700 ypos 700
    "The noise of Theo's engine gets weaker and weaker. Soon I won't be able to hear it over the cheers of the prisoners I've freed, still partying behind me."
    "My mission here is over. There's still time to go back to Cody immediately, try to cross the bridge together today."
    "But I barely had time to talk to Manny, someone who is… used to?… be my friend."
    "And even if the \"normal world\" is still the same cesspool of violence and exploitation I remembered, there is also a strange feeling of nostalgia that has stayed with me since I got on the bike with Theo."
    "I'll never have to fear any bandit again. I guess I already knew it, but only now that I've slaughtered them in the dozens does that thought truly sink in within me."
    "Is it possible that,{w=0.2} maybe,{w=0.2} there might something worth fighting for {i}here{/i}?"
    ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    "I start running and in a moment I see Theo and Manny reappear and get closer."
    "I wonder if they've maybe slowed down to wait for me. But when Theo acknowledges me with a grin and keeps going at the same speed, I realize this is not the case."
    "In fact, it is me who need to slow down so as to not lose them."
    "I jump high, a way to waste some energy without covering too much ground."
    stop music fadeout 10.0
    show bigjump:
        easein 20 xpos 250 ypos -400
    "From this height, just turning my head, I can still see the former bandit village. Theo and Manny are like ants under my feet."
    "I can't help but laugh. This is truly another world."
    "One I can leave behind with a small jump."
    scene moon
    with Dissolve(2.0)
    "But to go where? No matter how high I jump, the moon will still be as unreachable as it's been all my life."

    scene black with Dissolve(5.0)
    pause 0.1
    scene cabin with Dissolve(5.0)
    "Theo and Manny's house is… interesting."
    "Unlike many, it is not the ruin of some antediluvian building. It's just a wood cabin that they are proud to say they built with their own four hands."
    "It's quaint, really. There is something fascinating about being inside a building and not feeling surrounded by decay and memories of a long gone era."
    "But at the same time…"
    ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    "Is this really the best left to be found on this side of the bridge?"
    pause 2
    "We have dinner together.{w=1} We laugh. {w=1}We talk."
    "It is something I haven't done in a long time. It's comforting."
    "Most of the time it's just Theo and Manny talking among themselves, referencing things only they could possibly understand."
    "But their voices are soothing, their laughter warms my heart."
    "I feel like I could lay down my sword and finally rest, wrapped in this strange welcoming energy I sort of remember from when I was little."
    "The feeling of home."
    "Instead, when I finally go to sleep, everyone's chatter has long died out."
    scene black with Dissolve(2.0)
    play music xiangqi
    mc "What is that?"
    scene xiangqi:
        xalign 0 yalign 0
    with Dissolve (5.0)
    "He's placing black and red disks on a wooden board. The disks have curious drawings on them."
    sidewolf shirt "It's called xiangqi."
    sidewolf "It's a game similar to chess that was played before the apocalypse."
    sidewolf "From now on, we will play each night before we go to bed."
    "I stare at the game board quizzically. He seems to be placing the wooden pieces at the intersection points of the lines drawn on the board, although many of them are left empty."
    mc "Is this part of our training?"
    sidewolf concerned "Huh? No."
    sidewolf "This is just for fun."
    sidewolf blush "Err."
    "He seems to struggle."
    sidewolf serious "We don't have to play if you don't want to. I've just always wanted someone to play with."
    sidewolf "It'll be good for us not having to think about the Quest from time to time."
    "I study him. I'm so used to him giving orders and me just following them when it comes to fighting or training."
    "But now that he wants to do something else, he looks almost timid. I'm intrigued."
    mc "Sure, let's play."
    mc "But you'll have to explain the rules to me."
    sidewolf normal "Right!"
    "Cody seems to be pondering something."
    sidewolf "So this is pretty similar to chess, except…"
    mc "I've never played chess either."
    sidewolf blush "Oh.{w=0.3} Right."
    "Some more thinking."
    sidewolf normal "So these two pieces here are the Generals. You play as Red and I'll play as Black. The objective of the game is to checkmate the opposing General."
    "He shuffles the pieces around in a new configuration."
    scene black
    show cattura at top
    with dissolve
    sidewolf shirt "Like so. Checkmate means your General is under attack and it's impossible to save it."
    sidewolf concerned "So you have to capture the enemy General, but not like, by surprise, get it? It must be because it can't be saved."
    sidewolf normal "It's actually illegal to let your General get captured otherwise."
    "I stare at the board."
    mc "Wait, who's checkmating who?"
    sidewolf angry "Red is being checkmated. Argh!"
    "Cody massages his temples."
    sidewolf serious "I guess I should explain how the pieces move before you understand."
    sidewolf "Here."
    hide cattura
    show cattura2 at top
    with dissolve
    "He shuffles the pieces some more, but this time only a few are left on the board."
    show redgeneral at top with dissolve
    sidewolf normal"Let's start with the General."
    hide redgeneral
    show generalmove at top
    with dissolve
    sidewolf "The General can move one point horizontally or vertically. Not diagonally."
    hide generalmove
    show castle at top
    with dissolve
    sidewolf "Most importantly, it can never leave this area of the board, called the Palace."
    hide castle with dissolve
    mc "That sounds like a huge handicap. This is supposed to be my weakpoint, isn't it?"
    sidewolf normal shirt "Yes. You've got to use the other pieces to protect your General."
    sidewolf happy "However! There is an exception to these rules."
    sidewolf "The General has another rule to its movement."
    sidewolf normal "If the two General are facing each other, with no intervening pieces to block their view, they can perform a special move."
    show flyinggeneral at top
    with dissolve
    sidewolf "Only in that case, your General is allowed to move vertically along the whole length of the board, leaving the Palace, and capture the enemy General directly."
    sidewolf happy "This special move is called the Flying General."
    hide flyinggeneral with dissolve
    pause 2.0
    "He looks weirdly excited about this game. He's grinning."
    "I smile at him as an encouragement, but he's stopped in his tracks and he's staring back at me expectantly."
    sidewolf happy shirt "Have you noticed?"
    mc "Huh?"
    sidewolf serious "Ok, hear me out."
    sidewolf "I've just told you this is a special move that can only be played to capture the opposing General with your own, right?"
    mc "Yes?"
    sidewolf "But I've also told you that it's illegal to move your General into check, right? I mean, you can't let your General be captured."
    mc "Yes."
    sidewolf happy "So you see, it's actually impossible to play the Flying General."
    sidewolf "Because the player who'd be creating the conditions to play this move would also be getting his General into check."
    "This must be something very funny to him, because he's giggling and waving his tail."
    mc "So you were just wasting my time."
    "I accuse him in a joking manner, to humor him."
    mc "What's the point of a special move that can never be executed?"
    sidewolf happy shirt "That was my reaction as well when they taught me, ahah!"
    sidewolf serious "But as I started to play the game, I realized something. Even if the move can never be played, it still affects the game."
    sidewolf "Since you have to avoid putting your General in check at all costs, all pieces on the board need to move {i}as if{/i} the move could be executed."
    sidewolf "Look here, for example."
    show soldier at top
    with Dissolve(2.0)
    sidewolf "The Generals are safe from each other because of your Soldier in between."
    sidewolf "But because the Flying General rule exists, it means you {i}cannot{/i} move your Soldier out of the way."
    sidewolf "It's stuck on this file."
    sidewolf "It's a bit like gravity, it isn't something you can observe directly, but it still affects how everything moves."
    hide soldier with Dissolve(2.0)
    sidewolf happy "So you see… the game would play completely different if this impossible move wasn't there."
    scene black with Dissolve(2.0)
    wolf "Now, these next two pieces are called…"
    stop music fadeout 10.0
    pause 2
    "He actually went on to lose that first game between us. As well as many others."
    "I remember he being flustered about it at first, but he laughed it off. Said that's why he needed a partner to play with in the first place, he hardly had any real experience playing the game."
    "We did end up playing almost every night."
    "It was a nice distraction whenever our bodies were sore, after having been smacked around by the Colossus."
    scene cabin with Dissolve(5.0)
    "{w=0.5}.{w=0.5}.{w=0.5}."
    "I sneak out in the middle of night, without saying goodbye to Manny and Theo."

###### NEW SCENE ######

    play music dying
    scene black with Dissolve(5.0)
    pause 0.1
    show camp
    with Dissolve(5.0)
    "I'm back home."
    "I hadn't even realized how anxious I was until I got back here."
    "Everything is quiet. It's probably still early for Cody to be attempting a bridge crossing."
    "I walk towards the place where Cody was last camping. He shouldn't have moved from there, unless he wishes not to be found."
    "Unless he was angry with me…"
    "But no, I'm sure he doesn't hold a grudge. He was just trying to teach me something about how this world works, like he always does. In his own way."
    pause 1
    show wolf sad open wounds at center:
        zoom 0.8
        ypos 1.2
    with Dissolve(2.0)
    mc "Cody!"
    "I drop my backpack and rush to his side."
    "I've never seen him get himself hurt this badly."
    show wolf blush with dissolve
    wolf "Unagi~"
    mc "What happened?"
    "I inspect his wound, lifting the badly wrapped bandages. He's lost quite a bit of blood, but it shouldn't be lethal."
    "Not with a stamina like his."
    show wolf sad with dissolve
    wolf "I'll live."
    "His voice breaks as he says it, like this isn't supposed to be good news."
    "I don't say anything. I just wrap his head in a tight warm hug, resting my chin between his ears, avoiding his chest altogether."
    show wolf crying with dissolve
    "His ears flick at first, then his whole body starts shaking."
    wolf "The Seeker's Curse. It's got me."
    "The Seeker's Curse…"
    "Age."
    mc "That's impossible, you're only…"
    "I try to remember."
    mc "28?"
    pause 1.0
    wolf "I can feel it in my bones, Unagi."
    wolf "Lately, all the training I've done has just been to keep my body in its current conditions."
    wolf "I cannot get better than this."
    wolf "This is as good as I'll ever get. And it's not good enough."
    pause 2.0
    "I kiss him tenderly on the head and rock his body in my arms."
    "I want to comfort him, but there's nothing I can do."
    "This is how the world works, no amount of empty words will change that."
    "The Seeker's Curse is something we all have to struggle with."
    "Pushing our bodies past their natural limits works only for so much time."
    scene black with Dissolve(1.0)
    "Some limits can never be crossed."
    scene black with Dissolve(5.0)
    stop music fadeout 3.5
    play music epic
    show camp:
        linear 120 zoom 1.5 xpos -1300
    with Dissolve(5.0)
    "I walk across the empty village. Towards the Enemy."
    "This is my first time fighting truly alone. I am sure Cody is watching me, but I don't turn around to confirm it."
    "This is his struggle now."
    "Mine is to fight for both of us."
    scene bridge:
        zoom 0.4
    with Dissolve(2.0)
    "The first step on the bridge."
    "The Colossus doesn't look down on me. But I know He knows I'm here."
    "He won't start attacking me until I reach about the first pillars."
    "So I just stroll there slowly, collecting my strength for this fight."
    scene black
    show titanus:
        xpos -1200 ypos -1200
    with Dissolve(2.0)
    show titanus:
        easein 50 ypos 0
    "That I cannot win."
    "Cody never won."
    "Even though he started training when he was a kid."
    "Even though he had me helping."
    "Even though he desired it more than anything else in the world."
    scene challenge with Dissolve(2.0)
    "And yet I must win."
    "Only I can now get both of us across."
    scene black
    "Why do you keep us out?"
    play sound swordclang
    pause 0.5
    show slash:
        zoom 0.8
    with Dissolve(0.1)
    pause 0.5
    hide slash
    play sound swordclang
    pause 0.5
    show slash2:
        zoom 0.8
    with Dissolve(0.25)
    pause 0.5
    hide slash2
    play sound swordclang
    pause 0.5
    show slash at left:
        xzoom -1 zoom 0.8
    with Dissolve(0.1)
    pause 0.5
    hide slash
    mc "Let me in!"
    pause 2.5
    "Why do you taunt us with your happiness?"
    play sound swordclang
    pause 0.5
    show slash:
        zoom 0.8
    with hpunch
    pause 0.5
    hide slash
    play sound swordclang
    pause 0.5
    show slash2:
        zoom 0.8
    with hpunch
    pause 0.5
    hide slash2
    play sound swordclang
    pause 0.5
    show slash at left:
        xzoom -1 zoom 0.8
    with hpunch
    pause 0.5
    hide slash
    mc "LET ME IN!"
    pause 2.5
    "If only we never knew you existed."
    play sound swordclang
    pause 0.5
    show slash:
        zoom 0.8
    with vpunch
    pause 0.5
    hide slash
    mc "LET.{w=1}{nw}"
    play sound swordclang
    pause 0.5
    show slash2:
        zoom 0.8
    with vpunch
    pause 0.5
    hide slash2
    mc "ME.{w=1}{nw}"
    play sound swordclang
    pause 0.5
    show slash at left:
        xzoom -1 zoom 0.8
    with hpunch
    pause 0.5
    hide slash
    mc "IN!"
    stop music fadeout 10.0
    pause 10
    centered "{size=120}THE END{/size}"
    play music xiangqi
    show credits with Dissolve(5.0)
    pause 5
    centered "{size=50}Written and developed{/size} \n \n by Loudo{w=5}{nw}"
    pause 2
    centered "{size=50}Main menu{/size} \n {size=50}Camp CG{/size} \n \n by Hugh{w=5}{nw}"
    pause 2
    centered "{size=50}Sprite assets{/size} \n \n by Cody{w=5}{nw}"
    pause 2
    centered "{size=50}Free picture assets{/size} \n \n Adam Derewecki \n Aleksandr Barsukov \n An Wang \n Ansaf Ahmad \n Bas Masseus \n Bruce \n Callum Hilton \n Dex Ezekiel \n Dn Milk \n Felix Mittermeier \n Harshal \n Jill J Jekins{w=8}{nw}"
    pause 2
    centered "Joe Kniesek \n Kaique Rocha \n Kevan Craft \n Love Art Live Art \n Luke Besley \n Marcos Miranda \n Mario \n Masud Rana \n Pars Sahin \n Peter H \n Pexels \n Pixxel Worx{w=8}{nw}"
    pause 2
    centered "Reimund Bertrams \n Robert Karkowski \n Robinsonk26 \n Romeo Varga \n Ryaszard Porzynski \n Samson Jay \n Scott Goodwill \n Sebastiaan Stam \n Stock Snap \n Theresa Schenk \n Vadim Sadovski \n Vovaas Montenegro{w=8}{nw}"
    pause 2
    centered "{size=50}Pictures edited{/size} \n \n by Loudo{w=5}{nw}"
    pause 2
    centered "{size=50}Music{/size} \n \n City Rap  Beat by Stankbeast \n {size=20}Attribution NonCommercial 4.0 License{/size}{w=5}{nw}"
    pause 2
    centered "BlackSnow by airtone \n {size=20}Creative Commons Attribution (3.0){/size}{w=5}{nw}"
    pause 2
    centered "precarity by airtone \n {size=20}Creative Commons Attribution Noncommercial (3.0){/size}{w=5}{nw}"
    pause 2
    centered "CRYSTAL by Apoxode \n {size=20}Creative Commons Attribution Noncommercial (3.0) \n Ft: airtone, GeeArtriasRose, Speck{/size}{w=5}{nw}"
    pause 2
    centered "Enchanted by Apoxode \n {size=20}Creative Commons Noncommercial Sampling Plus (3.0) \n Ft: Rewob{/size}{w=5}{nw}"
    pause 2
    centered "Wolf by Audiorezout \n {size=20}Attribution NonCommercial ShareAlike 4.0 International{/size}{w=5}{nw}"
    pause 2
    centered "Peace and Blessings by djalng59 \n {size=20}Creative Commons Attribution Noncommercial (3.0){/size}{w=5}{nw}"
    pause 2
    centered "With These Wings by essesq \n {size=20}Creative Commons Attribution Noncommercial (3.0){/size}{w=5}{nw}"
    pause 2
    centered "Resonance by acrylic bathhouse \n {size=20}Creative Commons Attribution Noncommercial (3.0){/size}{w=5}{nw}"
    pause 2
    centered "{size=50}Sound effects{/size} \n \n Motorcycle sound effect by Satoration \n {size=20}Attribution (4.0){/size}{w=5}{nw}"
    pause 2
    centered "Sword sound effect by thecrow \n {size=20}Creative Commons 0{/size}{w=5}{nw}"
    pause 2
    centered "Campfire sound effect by foleyhaven \n {size=20}Creative Commons 0{/size}{w=5}{nw}"
    pause 2
    centered "Birds sound effect by hargissssound \n {size=20}Creative Commons 0{/size}{w=5}{nw}"
    pause 2
    centered "Waves sound effect by pulswelle \n {size=20}Creative Commons 0{/size}{w=5}{nw}"
    pause 2
    centered "None of the people credited here were directly involved \n in the project except Loudo and Hugh{w=5}{nw}"
    pause 2
    centered "Thank you for playing{w=5}{nw}"
    pause 2
return
