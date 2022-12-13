# The script of the game goes in this file.

#define i = Character("Ina", color="#FFFF00") #, color=""#FFFF00", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define n = Character("Ina", color="#c0ffd5", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define m = Character("Mei", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define r = Character("Rika", color="#ffd5c0", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define a = Character("Abe", color="#FFFF00", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define k = Character("Karin", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ]) #098fc1 (previous shadow color)#086f95
define l = Character("Leopold", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define u = Character("Naomi", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define c = Character("Archivist", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define narrator = Character(None, what_outlines=[ (0, "#075c7c", 2, 2) ])  #098fc1
#define a = Character("Alice", color="#ffffff", who_outlines=[ (1, "#FF00FF") ], what_outlines=[ (1, "#FF00FF") ])

#### VARIABLES ########################################################

label start:

    $ ina_score = 0
    $ mei_score = 0
    $ rika_score = 0
    
    stop music fadeout 2.0


#### DEBUG MENU #######################################################

    #jump debugmenu      

#######################################################################
#### PART 1 ###########################################################
#######################################################################

label prologue:

    window hide    
    
    #############
    scene black with fade
    #pause(0.5)
    #play sound "audio/light3.ogg" fadein 1.0
    #scene leaves_logo with Dissolve(1.0)
    #pause(1)
    #stop sound fadeout 2.0
    scene instructions1_ea with fade
    pause
    scene black with fade
    scene instructions2_ea with fade
    pause
    play sound "audio/0searoarrain.ogg" loop fadein 30.0
    scene black with fade
    pause(2)

    ############
    #image mainstreet_animated:
    #    "backgrounds/villageroad_red.png" with Dissolve(0.6)
    #    pause 0.6
    #    "backgrounds/villageroad_blue.png" with Dissolve(0.6)
    #    pause 0.6
    #    repeat
    ############
    
    scene rika_cg_6 with Dissolve(3.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 50.0 xalign 1.0 yalign 0.0
        
    window show
    play music "audio/0luctum.ogg" loop fadein 8.0
    pause(1)
    "She appeared oblivious—"
    pause(1)
    "—to the roiling waves—"
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1)
    "—the incessant thunder—"

    pause(1)  
    
    "—the lashing rain, as it soaked her winding, obsidian hair—"
    
    pause(1)
    
    "—and she stared at me, with a fanatical gaze in her eyes." #intent, fanatical
    
    pause(1)
    
    "There was—"
    ############
    stop sound fadeout 0.4
    stop music fadeout 0.4
    play sound "<from 2.0>audio/busarriving.ogg" noloop
    scene black with vpunch
    scene black with vpunch
    
    "Suddenly, the lurch of a braking bus shook me from my dream."
    
    play music "audio/summernight.ogg" loop fadein 4.0
    
    "In a state of panic, I exited the vehicle—"
    
    scene schoolroad_twi with Dissolve(3.0)
    stop sound fadeout 2.0
    "—although it wasn't until it had disappeared into the distance, that I noticed I had gotten off one stop too soon."

    pause(1)    
    
    "And as the memories of my dream faded from my conscious mind, I immediately became preoccupied with worries more mundane in nature."
    
    pause(1)
    
    #"I got off the bus at the street corner, while an old saying rang trough my head — {i}anyone who lives within their means, suffers from a lack of imagination.{/i}" 

    "For I had wasted another weekend, fruitlessly inquiring local businesses for part-time employment." 

    "{i}You should have tried during harvest{/i} — they'd reply, regretfully. If they didn't just laugh in my face."
    
    pause(1)
    
    "I was beginning to run out of options."
    
    #pause(1)
    scene school_side_twi with Dissolve(2.0)
    #pause(2)
    pause(1)
    
    "Due to setbacks at my father's work — the same that had led him to slash my weekly allowance — we were forced to relocate to Abbotsford, an agricultural hub with low costs of living." 
    
    "To me it felt like the apocalypse. I had lost my home, my friends, my indulgent city life—"
    
    "—and now I couldn't even find a side job."
    
    pause(1)
    
    "But in retrospect, I'll admit these were peaceful days, where money was the greatest problem on my carefree mind."

    stop music fadeout 2.0   
    window hide
    scene school_side_nig with Dissolve(2.5)
    #play music "audio/crowfield.ogg" loop fadein 1.0
    pause(1)
    scene school_side with Dissolve(2.5)
    play audio "audio/schoolbell.ogg"    
    pause(2)      
    scene schoolstairs with Dissolve(1.0)
    play sound "audio/clock.ogg" loop
    window show
    pause(1)
    
    "That was before I realized I had a stalker."
    window hide
    pause(0.5)
    play audio "audio/swipe.ogg"
    show ina uni imperative day open big with Dissolve(0.5)
    pause(2)
    stop sound fadeout 0.1
    play music "audio/exelsisdeo.ogg" noloop fadein 10.0
    

label opening:

    scene white 
    show ina uni imperative day open big 
    with Dissolve(3.0)
    show ina uni imperative day closed big with Dissolve(0.2)
    show ina uni imperative day open big with Dissolve(0.2)
    pause(2)
        
    scene opening_park with Dissolve(2.0):
        subpixel True
        xalign 0.0 yalign 1.0
        linear 8.0 xalign 1.0 yalign 0.0 #ease, linear, easin, easeout   
    show opening_leaves with Dissolve(1.0)
    pause(1.0) 
    hide opening_leaves with Dissolve(1.0)
    pause(1)
    scene white with Dissolve(1.0) 
    
    scene opening_sky:
        subpixel True
        xalign 0.0 yalign 1.0
        linear 10.0 xalign 1.0 yalign 0.0 #ease, linear, easin, easeout
    show opening rika_sil
    with Dissolve(2.0)
    show opening rika with Dissolve(1.0)
    pause(4)
    
    scene opening_dunes with Dissolve(2.0):
        subpixel True
        xalign 0.0 yalign 0.0
        linear 8.0 xalign 1.0 yalign 1.0 #ease, linear, easin, easeout   
    pause(2)  
    scene white with Dissolve(1.0) 
    
    scene opening_sky:
        subpixel True
        xalign 1.0 yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    show opening mei_sil
    with Dissolve(2.0)
    show opening mei with Dissolve(1.0)
    pause(4)
    
    scene opening_road with Dissolve(2.0):
        subpixel True
        xalign 0.0 yalign 0.0
        linear 8.0 xalign 1.0 yalign 1.0 #ease, linear, easin, easeout   
    pause(1)  
    scene white with Dissolve(1.0) 
    
    scene opening_sky:
        subpixel True
        xalign 0.0 yalign 1.0
        linear 10.0 xalign 1.0 yalign 0.0 #ease, linear, easin, easeout
    show opening ina_sil
    with Dissolve(2.0)
    show opening ina with Dissolve(1.0)
    pause(4)
    
    scene opening_sky2:
        subpixel True
        xalign 0.0 yalign 1.0
        linear 11.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    with Dissolve(2.0)
    show opening_logo with Dissolve(2.0)
    pause(3)  
    scene white with Dissolve(2.0)
    
    scene opening_sky:
        subpixel True
        xalign 1.0 yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    show opening girls
    with Dissolve(2.0)

    pause(2.0)
    scene opening threnody with Dissolve(3.0)
    pause(4)
    stop music fadeout 12.0
    scene white with Dissolve(2.0)
    pause(1)
    #################################################################################################
    ##cut to same closeup of ina
    
    play sound "audio/clock.ogg" loop
    scene schoolstairs #with Dissolve(0.5)
    show ina uni imperative day open big 
    with Dissolve(2.0)
    pause(1)
    window show
    pause(2)
    n "I saw you loitering around the stores yesterday."
    n "You better admit it."
    
    show ina uni imperative day closed big with Dissolve(0.2)
    show ina uni imperative day open big with Dissolve(0.2)
    
    "Her name was Ina — a strange, determined girl."
    "Although she was in the same class as I, I wouldn't be able to say who her friends were."
    
    pause(1)
    
    a "I have no idea what you're talking about—"
    show ina uni imperative day closed big with Dissolve(0.2)
    show ina uni imperative day open big with Dissolve(0.2)
    n "They say a man is only as good as his labor. I've got just the thing for you."
    a "Eh—"
    n "Please follow me up to my office."
    
    pause(1)
    hide ina with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    play music "audio/deadprincess.ogg" loop fadein 3.0 
    play sound "audio/officesound.ogg" loop fadein 3.0
    scene white with Dissolve(3.0)
    pause(1)
    scene part1_title1 with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    

label p1c1:

    scene office with Dissolve(3.0)
    pause(1)
    show ina uni neutral day open at left with Dissolve(0.5)
    window show

    "I followed her into a small, cluttered room that was situated next to the teachers lounge."
    
    pause(1)
    
    n "It's so unbearably hot in here. Let me take off that horrible uniform."
    
    #hide ina with Dissolve(0.1)
    play audio "audio/clothesdrop.ogg"
    show ina shirt defiant day open at left with vpunch #Dissolve(0.5)    
    
    "Gracelessly she removed her vest and jersey, crumpling them into a ball which she dropped into a corner of the room."
        
    pause(1)
    
    n "I don't understand why they're making us wear {i}viscose{/i}. It's practically tropical outside."

    pause(1)
    
    "She turned to me."
    show ina shirt angry day open at left with Dissolve(0.5)
    
    n "You're anxious to get started, right? Let me explain what your duties will entail."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)
    n "I need someone to deliver a newspaper—"
    n "—don't worry, I can see a panic forming in your eyes. Brains, however, are entirely optional for this job."
    
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)
    
    a "I—"    
    "She cut me off."
    
    show ina shirt mirth day open at left with Dissolve(0.5)
    
    n "If there's one thing this village is famous for, it's the stellar quality of our newspaper, {i}The Sunday Abbot{/i}—"
    n "—or at least it is since {i}I{/i} took over as editor-in-chief."
    show ina shirt mirth day closed at left with Dissolve(0.2)
    show ina shirt mirth day open at left with Dissolve(0.2)
    n "The Abbot doesn't play games, you know? Fourth place in the national ranking of school papers; an honorable mention by {i}The Evening Mirror{/i}—"
    pause(0.5)
    a "I didn't know we had a school paper."
    
    show ina shirt angry day open at left with Dissolve(0.5)
    
    n "A {i}school{/i} paper? We're much more than that! Crime, corruption, unsolved mysteries — did you know we were the first to break news on the Sandford House affair?"
    n "And I have so much more up my sleeve."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)
    n "So what do you say?"
    pause(1)
    
    
    #### INA 1 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "Will you take the job?"

        "I had something more respectable in mind.":
            show ina shirt saddened day open at left with Dissolve(0.5)
            "Hmpf. Maybe this will pique your interest."

            
        "It's better than nothing. I'll take it.": 
            $ ina_score += 1
            show ina shirt interested day open at left with Dissolve(0.5)
            pause(1)
            "Great! Let me show you my mock-up for this week's issue."
    
    #######################################################################################################
    
    # TODO newspaper mockup
    show abbot one big with Dissolve(1.0)   
    #"She handed me a stencil."
    show ina shirt angry day open at left with Dissolve(0.5)    
    
    n "This week we're reporting on an interesting case. It's linked to a murder that happened about a year before you arrived here."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)
    n "Back then we brought the news of a seasonal worker who fell victim to a violent attack on one of the local farms." #reporting, case
    n "It was late at night, he was on his way to his sleeping quarters after his shift ended — when suddenly, he was struck from behind by an anonymous assailant."
    hide abbot with Dissolve(0.5)   
    "Ina, in her apparent excitement, had begun tapping her right hand against her skirt." #rhythmically 
    pause(1)
    n "His co-workers found him next morning — more dead than alive."
    n "By the time the ambulance arrived he'd already succumbed to his injuries."
    "Regretfully, he wasn't able to give a testimony before he died."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)
    a "Poor guy."
    pause(1)
    n "A full year has passed since that fateful night, so I decided to do due diligence."
    n "I went down to the police station to ask how the investigation into the attack was coming along. However, the receptionist told me the case had been closed. "
    scene inaoffice with Dissolve(0.5)

    n "{i}Case closed?{/i} — I asked her. {i}Then who was the culprit?{/i}"
    #show ina shirt saddened day open at left with Dissolve(0.5)      
    n "But she said the perpetrator had never been found."
    n "Then when I asked if I could see the case file — she just mumbled something and directed me towards the exit."
    
    "Ina sighed."
    
    scene office 
    show ina shirt saddened day open at left 
    with Dissolve(0.5)      
 
    
    n "I know exactly what goes on around here. They never {i}did{/i} a proper investigation."
    n "You know — the owner of the farm where it all happened. He has ties to the town mayor." #They're corrupt to the bone. Each and every one of them."
    n "This place is ruled by small caucus of cronies, that can do as they like as long as their powers go unchecked."
    show ina shirt saddened day closed at left with Dissolve(0.2)      
    show ina shirt saddened day open at left with Dissolve(0.2)    
    n "That's why we need a quality newspaper. To shine a light in the darkness."
    pause(1)
    "I could detect a tremble in her voice."
    pause(1)
    n "We {i}really{/i} need a paperboy."
    n "Do it for your community, Abe. Those poor wretches need you."
    
    show ina shirt saddened day closed at left with Dissolve(0.2)      
    show ina shirt saddened day open at left with Dissolve(0.2)     
    pause(1)
    "By that time I had already begun to notice the first signs of Ina's compelling presence, although I ascribed it to youthful eccentricity at the time — not paying it any further attention."
    "The afternoon was drawing to an end."
    pause(1)
    hide ina with Dissolve(1.0)  
    "Wordlessly we gathered our belongings and headed towards the stairs."
    
    pause(1)
    window hide
    stop music fadeout 1.0
    pause(1)
    stop sound fadeout 1.0
    scene school_front with fade
    play music "audio/crowfield.ogg" loop fadein 1.0
    pause(1)
    window show    
    show ina shirt angry day open at left with Dissolve(0.5)
    pause(1)
    
    n "Let's get down to business."
    n "We have just under 2000 subscribers. I'll pay you two cents per paper delivered. That should add up a decent salary for a morning's work."
    pause(1)
    n "Now remember — the printer will deliver tomorrow at five in the morning, so I want to see you here no later than 5:15 AM."
    pause(1)
    a "I'm not much of a morning person."
    #pause(1)
    n "See you then."

    stop music fadeout 1.0
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    scene blueroom_nig with fade
    play sound "audio/ventilator.ogg" loop fadein 3.0
    pause(1)
    window show
    pause(1)

    "That night I lay in turmoil, pondering whether I should even indulge Ina's ridiculous offer—"
    pause(1)
    "—while a neurotic, continuous tapping played through my head like a stenotype."
    
    pause(1)
    stop sound fadeout 4.0
    scene black with Dissolve(3.0)
    pause(1)
    window show
    pause(1)
    "Morning came all too soon."
    pause(1)



label p1c2:

    play sound "audio/crowfield.ogg" loop fadein 3.0
    scene school_side_nig with Dissolve(2.0)
    pause(1)
    #window show
    #pause(1)
    #"The next morning, the constant rhythm of overpowering fatigue still echoed through my cranium, consistently droning out my thoughts."
    play music "audio/0andante664.ogg" loop fadein 30.0
    show ina pink sincere nig hair at center with Dissolve(0.5)   
    pause(1)
    
    n "So you're finally there? The delivery guys left ages ago. I could have used some help with the boxes."
    "Ina didn't appear the least bit thrilled to see me."
    pause(1)
    n "Here's a list of all the addresses, sorted by proximity to the school. Please try not to get lost."
    n "I'm off now. I have a lot of reading to catch up on. You can call me when you're done. "
    #pause(1)
    show ina pink smile nig hair at center with Dissolve(0.5)  
    "She handed me a small business card with her number on it. {i}Chief Editor of The Sunday Abbot{/i} was printed below her name in tasteful lettering."
  
    pause(1)
    
    a "I have a question."    
    
    show ina pink dissapointed nig hair at center with Dissolve(0.5)   
   
    "Though she appeared anxious to leave, she turned around at the last moment."
    pause(1)
    n "What?"
    pause(1)
    a "S—so why is it called The {i}Sunday{/i} Abbot?"
    pause(1)
    n "What do you mean?"
    pause(1)
    a "That doesn't make sense, does it? If it's delivered on a {i}Saturday{/i}."
    pause(1)
    n "That's just the way it's always been. We deliver on Saturdays and people read it on Sundays."
    #TODO happy face
    n "Some of our subscribers are very old-fashioned, you know— They wouldn't want us working during sabbath."
    show ina pink smile nig hair at center with Dissolve(0.5)  
    n "Anyway, good luck with your first day on the job."
    
    pause(1)
    hide ina with Dissolve(0.5)
    stop music fadeout 3.0
    pause(1)
    
    window hide    
    stop sound fadeout 1.0
    scene black with Dissolve(1.0)
    scene villageroad with Dissolve(1.0)
    play sound "audio/edgemeadow.ogg" loop fadein 3.0
    pause(1)
    window show
    pause(1)
    
    "I resigned myself to the arduous labor. Even though it was October already, an unnatural, sticky heat permeated the air that made my work all the more unbearable."
    
    ##sfx of dog barking (in the distance)"
    play audio "audio/bark1.ogg"
    
    "How quickly my situation had taken a turn for the worse. No more than two months ago, I had been enjoying my life among the nation's elite — headed for a bright role on the world stage."

    scene postbox with Dissolve(0.5)
    pause(1)
    "I would be pained to see myself now, spreading gutter journalism for a slave's wage—"
    
    #"Quietly I corrected myself. Having established a reputation of the highest accuracy and conscientiousness, the postal employee is considered the cornerstone of the nation. I should be more proud of my newfound profession, at least it beats working on a farm—" #improve
    
    ##sfx of dog barking (loud this time)
    play music "audio/angrydog.ogg" loop fadein 0.5
    show phyrrus at right with Dissolve(0.3)
    
    "But then! Out of nowhere, a snapping shadow lunged towards me."
    "The street erupted in violent mayhem as I fought to keep the dog's razor sharp fangs away from my jugular — using my messenger bag to shield myself from its all-devouring clutches." #narrowly avoiding its clutches."
    "I was in a state of panic, frantically trying to block its strikes as I sought a path to safety."

    stop music fadeout 6.0
    play audio "audio/swipe.ogg"
    scene inahouse with vpunch #Dissolve(0.5)
    "And without further hesitation, I leapt over a garden wall, away from what I figured was the hound's territory."
    #first encounter with mei (maybe have wagner theme for her, like wintersturme)
    ## playground?
    pause(2)
    "{i}Sigurd!{/i}"
    stop sound fadeout 3.0
    pause(1)
    scene playground with Dissolve(0.5)
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    pause(1)
    
    "I must have ran at least four blocks, before collapsing onto a playground bench. I took some time to come to my senses — all the while cursing Ina for not disclosing the dangers of the job."
    
    pause(1)
    
    a "If I encounter one more dog today, I will definitely—"
    
    "{i}Sigurd!{/i}"
    pause(1)
    "Over the sound of my heavy breathing, I could discern a fragile voice calling out."
    
    pause(1)
    
    "{i}Sigurd!{/i}"
    pause(1)
    "{i}Please stop hiding! Sigurd!{/i}"
    
    pause(1)
    show mei dress happy day open at right with Dissolve(0.5)
    play music "audio/rheingold_meandering.ogg" noloop fadein 5.0
    pause(1)
    
    "A girl appeared — her eyes as bright as the summer sky."
    
    show mei dress happy day closed at right with Dissolve(0.2)      
    show mei dress happy day open at right with Dissolve(0.2) 
    
    m "Hi there! Are you delivering the mail?"
    
    "She seemed distracted by my sudden presence. No signs of her prior distress remained."
    
    show mei dress interested day open at right with Dissolve(0.5)    
    
    a "Calling it {i}mail{/i} may be an overstatement. It's just a weekly paper."
    show mei dress happy day closed at right with Dissolve(0.2)      
    show mei dress interested day open at right with Dissolve(0.2) 
    m "I'd love to work as a postman one day! The honor! The excitement!"
    m "To see the delight in people's eyes when they receive life-altering news!"
    #pause(1)
    "I let out a self-deprecating chuckle."
    
    a "I know someone you'd might like to meet—" #TODO, improve
    
    show mei dress surprised day open at right with Dissolve(0.5)
    
    m "SIGURD!!!"
    show mei dress happy day open at right with Dissolve(0.5)         
    "She was at it again — at the top of her lungs."
    
    show mei dress happy day closed at right with Dissolve(0.2)      
    show mei dress happy day open at right with Dissolve(0.2)   
    
    a "Are you looking for someone?"
    m "It's just my little brother. Sigurd."
    m "He loves playing hide-and-seek. He made me count to a hundred this time, but when I turned around he had disappeared without a trace."#, though usually he doesn't dwell far."
    show mei dress happy day closed at right with Dissolve(0.2)      
    show mei dress happy day open at right with Dissolve(0.2)   
    a "Isn't that the object of the game?"
    m "This was almost half an hour ago. Usually he doesn't stray so far."
    pause(1)
    a "Well I really hope you find him."
    a "I have to get going. They don't pay me by the hour."
    show mei dress happy day closed at right with Dissolve(0.2)      
    show mei dress happy day open at right with Dissolve(0.2)   
    m "Will you please look out for Sigurd? He's wearing a light red fleece."
    m "I told him it was far too warm for his winter clothes, but he never listens."
    
    #### MEI 1 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "Will you let me know if you see him?"
        
        "Sure thing. I'll keep my eyes wide open.":
            $ mei_score += 1
            show mei dress happy day closed at right with Dissolve(0.5)   
            m "You're the best! Please send him over here if you find him."
            
        "I really do have a lot of work to do.": 
            show mei dress fedup day open at right with Dissolve(0.5)   
            m "That's okay. I know mailmen have to focus on their duty."
            m "But if a little blond boy happens to cross your path, please tell him his sister Mei is looking for him."
    
    #######################################################################################################
    
    pause(1)
    hide mei with Dissolve(0.5)
    stop music fadeout 1.0
    pause(1)
    stop sound fadeout 1.0
    scene council with fade
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    pause(1)
    
    "Every mansions had a garden, and every garden had a gate, and every cursed garden gate added three more seconds to my seemingly endless route."
    
    #pause(1)
    #scene council with Dissolve(0.5)
    
    "I really didn't mind the apartment complexes, which had their letterboxes stacked conveniently together. But these gardens were {i}ruining{/i} my average."
    
    "And while I gradually began to come to the conclusion that Ina had played me for a fool, suddenly—"
    
    show phyrrus at right with easeinbottom
    play music "audio/angrydog.ogg" loop fadein 0.5
    
    "The infernal beast returned. Without abandon, it began furiously snapping at my leg."
    
    pause(1)
    show karin surprised at left with Dissolve(0.5)
    stop music fadeout 6.0
    
    k "There there, Phyrrus, the man's doing an important job."
    show karin serious at left with Dissolve(0.5)
    "Adeptly she wrangled the dog away from my quivering limbs."
    
    play audio "audio/panting.ogg" fadein 1.0
    show karin worried at left with Dissolve(0.5)
    play music "audio/buciumeana.ogg" noloop fadein 7.0
    
    k "I'm sorry! Phyrrus is usually very kind, but it takes him a while to get used to strangers."
    a "Your dog has been terrorizing me all morning, madam."
    
    pause(1)
    
    k "Oh Phyrrus isn't {i}my{/i} dog. He lives here. The community has adopted him."
    show karin happy at left with Dissolve(0.5)
    k "You must be new in town."
    k "I'm Karin, I work at the city council. Welcome to the beautiful municipality of Abbotsford!"
    pause(1)
    k "I'm so glad you're willing to do this job."
    k "I heard Ina had some unfortunate resignations as of late. But a small town like this really needs free press."
    pause(1)
    a "Ina mentioned something along those lines—"
    pause(1)
    "I handed her a paper — and as I was about to proceed on my route, her eyes fell on the headline."
    show karin worried at left
    hide phyrrus 
    with Dissolve(0.5)
    k "Wait a minute— This seems interesting."
    
    show karin serious at left with Dissolve(0.5)
    
    "As she skimmed over the front page, a grave expression came over her face." #frequent use of 'as'
    
    k "This is very interesting {i}indeed{/i} — what you've dug up here."
    pause(1)
    k "You should be careful though, this is a very small community."
    "She uttered the warning with concern in her voice."
    
    pause(1)
    a "I'm just the paperboy—"
    k "I know, I know. I apologize— This {i}really{/i} is very interesting."
    hide karin with Dissolve(1.0)
    "And with these words she proceeded to make her way back towards the council building — until I suddenly recalled Mei's words."
    
    a "Wait! Have you seen a little boy somewhere around here?"
    pause(1)
    show karin happy at left with Dissolve(0.5)
    "She turned around, a meaningful expression appearing on her face."
    
    #show karin happy at left with Dissolve(0.5)
    pause(1)    
    
    k "I figure you've run into Mei?"
    pause(1)
    k "Don't worry too much, little {i}Sigurd{/i} always shows up in the end."
    
    pause(1)
    stop music fadeout 3.0
    hide karin with Dissolve(0.5)           
    #evening gold
    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
    play sound "audio/summernight.ogg" loop fadein 2.0
    scene residential_eve with Dissolve(2.0)
    pause(1)
    window show
    pause(1)
    
    "Though the fortunate may be entitled to Saturdays off, my fate is governed by a crueler power."
    "If you want to experience hell on earth, I implore you to take on a paper round—"
    "—my hands lacerated, my legs buckling—"
    pause(1)
    "{i}Sigurd!{/i}"
    pause(1)
    "{i}Sigurd! Where are you Sigurd? Please come out!{/i}"
    "{i}Mom will be angry!{/i}"    
    pause(1)
    "Her voice was reduced to a feeble wail. I hurried in the direction of the sound."
    
    pause(1)
    scene villageroad_eve with Dissolve(0.5)
    pause(1)
    show mei dress crying nig open at right with Dissolve(0.5)
    pause(1)
    
    m "Sigurd still hasn't come back— He's never been away this long."
    "She was teary-eyed, shivering like a newborn calf."
    m "Please, Sigurd! Please!"
    m "Sigurd—"
    play music "audio/haunting.ogg" loop fadein 18.0 #"audio/haunting.ogg"
    "And as she pleaded, her voice grew fainter, as though the last of her strength was slipping away."
    
    show mei dress white nig open at right with Dissolve(1.0)
    
    "Until suddenly her eyes, which had been vibrant blue a heartbeat ago, turned an ashen white."
    
    pause(1)
    "A silent murmur escaped her lips."
    pause(1)
    m "{i}Sigurd . . . Please . . . Sigurd, no . . . {/i}"
    m "{i}He's only seven . . . Please don't take him . . .{/i}"
    
    pause(1)
    "Having lost all her prior vitality, Mei had become wholly possessed by a paralyzing entrancement."
    "Staring into her pale white eyes, I could determine her life essence was very frail at the time — a faint light in the distance, close to dying out."
    "A growing concern took hold of me."
    pause(1)
    
    a "Are you alright—?"
    a "Do you want me to call someone?"
    "But my words passed right through her."
    pause(1)
    m "{i}Please, I promise he'll be good— Please let him stay with me—{/i}"
    pause(1)
    m "{i}Sigurd!{/i}"
    
    stop music
    play audio "audio/swipe.ogg"
    scene villageroad_eve with vpunch
    
    "Her knees buckled. Had I not been fast enough to catch her, she would have plummeted to the ground."
    
    pause(1)
    
    "As I stood there, trying my best to keep her upright, I felt her strength gradually return."
    "As suddenly as it had appeared, the paralysis dissipated from her body."
    
    pause(1)
    stop music fadeout 2.0
    show mei dress fedup nig open at right with Dissolve(0.5)
    pause(1)    
    
    "She remained silent for a very long time."
    
    pause(2)
    
    m "I'm sorry."
    "Her voice was calm, almost devoid of emotion."
    pause(1)
    m "I'm sorry . . . I forgot. Sigurd isn't here anymore."
    m "I apologize for causing you trouble."
    
    pause(1)
    hide mei with Dissolve(1.0)
    pause(1)
    
    "And without any further clarification, she disappeared into the night."
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)


label p1c3:

    play sound "audio/clock.ogg" loop fadein 3.0
    play music "audio/phonecall.ogg" loop fadein 3.0
    scene blueroom_twi with Dissolve(2.0)
    pause(1)
    window show
    pause(1.0)
    "I picked up the phone."
    stop music fadeout 0.1
    pause(1)
    n "Where are you? What happened?!"
    "I flinched from the outrage in her voice."
    #pause(1)
    a "Nothing happened. I'm back home from a long day's work."
    n "But these boxes! There are still three boxes here! That means we have disappointed subscribers!"
    a "Ina. The job's killing me. I'll be contacting the civil labor board—"
    n "You better finish this {i}first{/i} thing in the morning. I swear if we even have {i}one{/i} canceled subscription over this I'll be docking your pay till Christmas."
    pause(1)
    a "Sure, Ina."
    pause(1)
    "The cataclysm of abuse had ended. She remained quiet for a while. Before resuming, in a more subdued voice."
    pause(1)
    n "Please be here early tomorrow morning. We need to deliver the remaining papers before the fundies get up for church."
    pause(1)
    a "Sure, Ina."
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 0.1
    scene black with Dissolve(3.0)
    pause(2)

label p1c4:

    play sound "audio/summermeadow.ogg" loop fadein 4.0
    scene school_side with Dissolve(2.0)
    pause(1)
    window show
    play audio "audio/schoolbell.ogg" 
    
    "When Monday finally came, it felt like a welcome respite."
    "I sat in class, dozing a little, plagued at times by flashbacks of rabid dogs."
    
    pause(1)
    stop sound fadeout 1.0
    scene schoolstairs with Dissolve(0.5)
    play sound "audio/clock.ogg" loop
    pause(1)
    
    "It was after classes ended, that a dark-haired girl approached me out of nowhere." #more info
    
    pause(1)
    play music "audio/prelude6.ogg" loop fadein 8.0
    show rika uni sad day closed at left with Dissolve(0.5)

    pause(1)
    
    r "I understand how summer's drawing late and that we're all young and in our best spirits—"
    "I stared at her uncomprehendingly."
    show rika uni sad day open at left with Dissolve(0.5)
    r "I'd just like you to know that Mei is {i}strictly{/i} off limits!"
    pause(1)
    "Alarm bells went off in my head."
    pause(1)
    
    #### RIKA 1 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "Please tell me what's going on."
        
        "I can assure you I only had the purest of intentions!": #Mei? You saw us on Saturday? But 
            $ rika_score += 1
            show rika uni sad day closed at left with Dissolve(0.5)
            r "Oh, I'm sure you did. And that you'll {i}continue{/i} to." 
            
        "I have no idea what you're talking about—": 
            show rika uni unhappy day open at left with Dissolve(0.5)
            r "You think you can lie yourself out of this one?"
    
    #####################################################################################################
    
    show rika uni sad day open at left with Dissolve(0.5)
    
    r "Just understand this is a small community. Rumors travel fast in a place like this."
    
    show rika uni sad day closed at left with Dissolve(0.2)
    show rika uni sad day open at left with Dissolve(0.2)    
    pause(1)
    scene rikalegs with Dissolve(0.5)
    #pause(1)
    "If only she realized that romance was the furthest thing from my mind at the time." #right now
    
    "She sighed."
    pause(1)    
    r "You may have noticed that Mei isn't exactly {i}like the other girls{/i}."
    
    "I nodded."
    pause(1)

    r "She has a learning disability — the school board is currently struggling to place her in suitable education." #"She explained to me that Mei had a learning disability — that the school board was having trouble placing her in suitable education."
    
    r "So for the time being she's being taught by a small group of church volunteers." #"For the time being, Mei was being taught by a small group of church volunteers."

    #it must be tough, in a small place like this

    pause(1)
    "Once she realized that I was sympathetic to the situation, her overall stance softened."
    
    "Together, we made our way to the main exit."
    
    #hide rika with Dissolve(0.5)
    pause(1)
    scene bluehall with Dissolve(0.5)
    #pause(1)
    show rika uni happy day closed at right 
    with Dissolve(0.5)
    pause(1)
        
    r "It's good to see a new face in school."
    r "So how are you enjoying the Isle of Abbot?"
    r "My name is Rika, by the way, Rika Kuyper. I apologize for not introducing myself sooner."
    a "Pleased to meet you. I'm Abe."
    
    show rika uni happy day open at right with Dissolve(0.5)
    
    r "Abe? Abe Janssen?"
    r "Oh I heard your father would be coming. It's good to know he finally arrived."
    r "He should know my dad — he's the pastor in town."
    show rika uni happy day closed at right with Dissolve(0.2)
    show rika uni happy day open at right with Dissolve(0.2)  
    a "I'm afraid we're not a very religious family."
    r "Oh he'll know my dad. I'm sure of it."
    
    show rika uni happy day closed at right with Dissolve(0.2)
    show rika uni happy day open at right with Dissolve(0.2)    
    pause(1)
    
    #### RIKA 2 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        "As she stood there, staring at me with a beaming smile, it was as if all her prior hostility had completely evaporated."
            
        "I wouldn't mind visiting your church some day.": 
            $ rika_score += 1
            show rika uni mischievous day closed at right with Dissolve(0.5)
            #pause(1)
            r "You'd be very welcome!"
            
        "I should probably be on my best behavior when dealing with the pastor's daughter ":
            show rika uni sad day closed at right with Dissolve(0.5)
            #pause(1)
            r "I've been teased about that more than enough."
    
    #####################################################################################################
    
    pause(1)
    r "Religion is a lot less intimidating when you grow up around it, you know?"
    r "Due to my father's status, people have always treated me like some kind of sacrosanct being—"
    r "—but to me the Bible is just a mysterious story book."
    
    show rika uni mischievous day open at right with Dissolve(0.5)  
    
    "A faraway glance appeared in her eyes."
    pause(1)
    r "I've always loved to read about the fantastic creatures, like the Behemoth and the Leviathan."
    r "Did you ever hear about the Leviathan?"
    
    "She began to recite."
    pause(1)
    r "{i}I have seen a great light in the sea.{/i}"
    r "{i}You may have seen the eyes of Leviathan, for his eyes are like the eyelids of the morning.{/i}"
    r "{i}When Leviathan is hungry he emits a fiery breath from his mouth, and causes the waters of the deep to boil.{/i}"
    show rika uni mischievous day closed at right with Dissolve(0.2)
    show rika uni mischievous day open at right with Dissolve(0.2)    
    "She let out a dignified squeal of delight."

    a "That would give me nightmares—" #bad
    r "Isn't it exciting? Oh I wonder how the Leviathan feels, submerged all alone in pitch black darkness—"
    
    "She ran her fingers tenderly through her flaxen hair."

    pause(1)
    play audio "audio/window.ogg"
    
    "And just then the quiet corridor erupted in vitriolic clamor."
    
    show ina shirt angry day open at left with Dissolve(0.5)   
    
    n "No loitering during club time! I need you in my office right now!"
    
    show rika uni happy day closed at right with Dissolve(0.5)
    
    r "Ina—?"
    r "Oh I'm so glad to hear you've found someone for the school paper."
    a "I'm not on the school paper—"
    show ina shirt surprized day open at left with Dissolve(0.5)   
    n "It's not a {i}school{/i} paper! It's an independent periodical with two-thousand paying subscribers!"
    show ina shirt angry day open at left with Dissolve(0.5)      
    n "Come Abe, follow me!"
    
    stop music fadeout 2.0
    hide ina with Dissolve(0.5)
    hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c5:

    play sound "audio/officesound.ogg" loop fadein 5.0 #we need more indoor sounds beside clock
    play music "audio/dormant.ogg" loop fadein 2.0 #was poucet
    scene office #with Dissolve(0.5)
    #pause(1)
    #window show
    show ina shirt angry book open at left 
    with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    "Afraid she may ignite in irate fury over my performance during the weekend, I timidly waited for her to begin speaking."
    "Her initial outburst, however, appeared to have been transient in nature. She was just sitting there, paging through a heavy book."
    
    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    
    "After what felt like an eternity, she began to talk."
    pause(2)
    n "Did you notice the crickets yesterday?"
    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    "I felt no answer was expected." #assumed
    
    show ina shirt saddened day open at left with Dissolve(0.5)#  
    pause(1)
    
    n "The crickets sing during July and August. It's a sound they make to attract potential mates." #But in September it usually tapers off."
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt saddened day open at left with Dissolve(0.2)#
    a "I think I heard them chirping last night—"
    n "This year, something isn't right."
    n "Their song tapered off a bit in September, but now they are out in full force again."
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt saddened day open at left with Dissolve(0.2)#
    n "I'm doing research on this phenomenon for an article. It's a chore — so I'm going to ask you to take over some of my other duties."
    a "Eh—"
    
    show ina shirt defiant day open at left with Dissolve(0.5)#
    n "I will need you to cover the {i}Weekly Progress{/i} section this week."
    a "The {i}what{/i} now?"
    n "The Weekly Progress, it's a recurring editorial in which we write something about a local event or inhabitant of the town."
    n "Sadly, I inherited it from the previous editor-in-chief. It's a community favorite, so I haven't been able to cut it yet."
    show ina shirt mirth day closed at left with Dissolve(0.2)#
    show ina shirt defiant day open at left with Dissolve(0.2)#
    n "But never mind. It's only three-hundred words. You can write about anything or anyone you see around town."
    n "Seems perfectly suited for you—"
    #pause(1)
    a "I haven't agreed to any of this."
    show ina shirt mirth day closed at left with Dissolve(0.2)#
    show ina shirt defiant day open at left with Dissolve(0.2)#    
    n "If you want to keep your job you'll have to be a {i}team player.{/i}"
    a "Does that mean I'll be paid for this?"
    show ina shirt angry day open at left with Dissolve(0.5)#
    n "Don't get any ideas."
    
    show ina shirt angry book open at left with Dissolve(1.0)#    show ina shirt angry book open at left with Dissolve(0.2)#
    
    "She returned to her book."
    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    "Assuming I was no longer needed, I excused myself—"
    "—but on my way to the door she called after me."
    
    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    
    n "Hey. That girl you were talking to."
    a "Rika. What about her?"
    n "What did she say to you?"
    "I was silent for a second."

    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    pause(1)
    a "Nothing much. She approached me in the hallway. "
    a "Apparently her family are involved with religion."
    pause(1)
    n "You can say that again."
    n "Her father is a powerful figure in town — the leader of the church of Abbotsford."
    pause(1)
    a "Whatever that means—"
    scene inaoffice with Dissolve(0.5)
  
    "Ina stared at me with an intent gaze."#"She stared at me with an intent gaze."
    
    pause(1)
    
    n "I want you to befriend Rika."
    n "If you get close to her, we'll be privy to a trove of information on the sordid power structures in the community."
    n "We'll have so many {i}exclusives{/i}—"
    pause(1)
    a "Wouldn't that be a rather underhanded reason to befriend someone?"
    n "You're a journalist now. You'll have to play the game in order to get to the bottom of things."
    
    scene office 
    show ina shirt angry day open at left 
    with Dissolve(0.5)
    #show ina shirt angry day open at left with Dissolve(0.5)#
    pause(1)
    
    #### INA 2 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "So will you do this for me?"
        
        "I thought I was just a paper boy.":
            $ ina_score += 1
            show ina shirt defiant day open at left with Dissolve(0.5)#
            n "And a {i}terrible{/i} one at that."
            pause(1)
            a "You know? I haven't been paid yet."
            #(1)
            "She ignored my remark."
            
        "Befriend Rika? I'd be glad to.": 
            show ina shirt saddened day closed at left with Dissolve(0.5)#
            n "Well well, look at how eager you've become now that a pretty girl is involved."
            "I ignored her unwarranted outburst."
    
    #######################################################################################################
    
    
    pause(1)
    #segue?
    a "There {i}was{/i} something strange Rika said—"
    show ina shirt angry day open at left with Dissolve(0.5)#
    a "I believe she called this place the {i}Isle of Abbot{/i}. Does that make sense to you?"
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt angry day open at left with Dissolve(0.2)#
    n "The Isle of Abbot? That's just a phrase the old people use."
    n "It's an interesting tale—" #scrap?
    n "Did you know this town was once surrounded by miles and miles of water?"
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt angry day open at left with Dissolve(0.2)#
    a "This place? You can't be serious—"
    a "—you couldn't be farther from the sea down here."
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt angry day open at left with Dissolve(0.2)#
    "She sighed." #TODO put away book???
    
    pause(1)
    
    n "You may have noticed how the village of Abbotsford lies slightly elevated above the surrounding fields."
    show ina shirt angry day closed at left with Dissolve(0.2)#
    show ina shirt angry day open at left with Dissolve(0.2)#
    a "Not really—"

    n "Well let me show you on the map."
    pause(1)
    "She browsed her phone for a while, before handing it to me. "
    
    show map polder with easeinbottom #Dissolve(1.0) #slide from bottom?
    
    n "Look. This is the situation as it is today."
    n "You can see the town of Abbotsford down there, surrounded by the sprawling farmland of the Marshpolder."
    pause(1)
    n "However, it didn't always look like this."
            
    n "The Marshpolder is an artificial island, constructed during the first half of the twentieth century. It was initially conceptualized as a way to meet the rising demand for housing and farmland."
    
    pause(1)
    
    n "The lake used to be an inland sea, but they built a great dam in the north, severing its connection to the ocean." #that lake
    
    n "These were times of unfettered progress. The national government didn't shy away from major developmental projects."
    
    n "They stemmed off a large area of water, before proceeding to pump it dry. That's how the stretch of land was formed that would become the Marshpolder."
 
    hide map with easeoutbottom
 
    "She took back her phone and called up different map."
    
    show map bay with easeinbottom
    pause(1)
    
    n "This is what it looked like before 1942."
    
    n "As you can see, there's no sign of the Marshpolder yet. The lake was still an inland sea."
    
    pause(1)
    
    a "And Abbotsford was an island—"
    
    n "It was indeed. A few graybeards around here might still recall the day — when the last of the water was pumped out and their homestead was an island no more. "
    
    pause(1)
    hide map with easeoutbottom
    pause(1)
    show ina shirt angry book open at left with Dissolve(0.5)
    
    "Ina put away her phone and returned to her book, softly muttering to herself."
    
    show ina shirt angry book closed at left with Dissolve(0.2)#
    show ina shirt angry book open at left with Dissolve(0.2)#
    
    n "That incessant chirping. I can hear it even here."
    n "I wonder if they've entered a second mating season."
    
    n "Maybe Spengler {i}was{/i} right."
    
    stop music fadeout 2.0
    #hide ina with Dissolve(1.0)
    pause(1)
    
    "I left the office quietly."
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 0.1
    scene black with fade
    pause(1)


label p1c6:

    ##walking back, still during daytime
    
    scene dunes with fade
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    window show
    pause(1)

    "As I walked back home, my mind explored all the different strategies I could employ to restore my cherished city life."
    
    "I could stay at my aunt's house, until I'd be able to finance a place of my own — that or I could find a comfortable bridge to sleep under."
    
    "I was so preoccupied with my thoughts that I didn't notice a familiar figure approaching."
    
    pause(1)
    show mei dress earnest day open at right with Dissolve(0.5)
    play music "audio/rheingold_buildup.ogg" loop fadein 4.0
    pause(1)
    
    m "Hi there! Come to the stones with me!"
    
    show mei dress estatic day closed at right with Dissolve(0.2)
    show mei dress earnest day open at right with Dissolve(0.2)
    
    "I leapt back when I realized who it was."
    
    pause(1)
    
    a "Sorry, I'm not allowed to talk to you."
    m "What?! Are you joking? Who said that?"
    a "That Kuyper girl cornered me after class—"
    "She let out a childish giggle."
    show mei dress estatic day closed at right with Dissolve(0.2)
    show mei dress earnest day open at right with Dissolve(0.2)
    m "Rika? Oh she's just teasing you." 
    
    #### MEI 2 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "Please come to the stones with me!"
        
        "No way. I'll definitely end with my head on a pike.":
            show mei dress obsessive day open at right with Dissolve(0.5)
            m "But you have a {i}reason{/i} to go to the stones—"
            m "—isn't that where you lost your bag?"
            play audio "audio/swipe.ogg"
            hide mei with vpunch
            "And in one fell swoop Mei had snatched my book bag from my shoulder and set off towards the edge of town."
            "As soon as I realized what had happened, I gave pursuit — but she had a sizable head start."
            pause(1)
            stop music fadeout 2.0
            stop sound fadeout 1.0
            scene townpark with Dissolve(0.5)
            play sound "audio/summermeadow.ogg" loop fadein 1.0            
            pause(1)
            "I chased Mei along a short country trail which led us to an opening in the trees."
            "In the center stood two massive megaliths, partly buried in the ground. The surroundings seemed well maintained."
            pause(1)
            scene stones with Dissolve(0.5) #TODO add in small notice.
            pause(1)
            show mei dress happy day open at right with Dissolve(0.5)
            play music "<from 22.0>audio/rheingold_opening.ogg" loop fadein 4.0
            pause(1)
            "After Mei relinquished my bag, I took a few seconds to catch my breath. She appeared to be reveling in mirth."
            show mei dress happy day closed at right with Dissolve(0.2)
            show mei dress happy day open at right with Dissolve(0.2)
            m "I'm so glad you found your books again. {i}Please{/i} try to be more responsible next time."        
            
        "If you're sure no one will catch us—": 
            $ mei_score += 1
            show mei dress estatic day closed at right with Dissolve(0.2)
            show mei dress earnest day open at right with Dissolve(0.2)
            m "We'll be fine! There's no one around at this time of day."
            pause(1)
            stop music fadeout 2.0
            stop sound fadeout 1.0
            scene townpark with Dissolve(0.5)      
            play sound "audio/summermeadow.ogg" loop fadein 1.0   
            pause(1)
            "I followed her along a short country trail which led us to an opening in the trees."
            "In the center stood two massive megaliths, partly buried in the ground. The surroundings seemed well maintained."
            pause(1)
            scene stones with Dissolve(0.5) #TODO add in small notice.
            #play sound "audio/summermeadow.ogg" loop fadein 1.0
            play music "<from 22.0>audio/rheingold_opening.ogg" loop fadein 4.0
            pause(1)
            show mei dress happy day open at right with Dissolve(0.5)

    
    #######################################################################################################
        
    pause(1)
    m "Do you see these giant stones? There are many of them scattered across the island."
    m "I like to come here whenever I'm sad. They warm me up inside."
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)
    "She was right. When I placed my hand on one of the rocks I could feel it emanate a radiating heat — though I figured this was likely due to their exposure to the mid-day sun."
    
    pause(1)
    
    a "So are you feeling sad right now?"
    show mei dress blushing day open at right with Dissolve(0.5)
    "She blushed." ##TODO blush
       
    m "No no no."     

    pause(1)
    
    m "To be honest, I come here every night. It's not far from the farm, you know?"
    
    pause(1)
    scene townpark with Dissolve(0.5)   
    #pause(1)
    
    "She gave me a tour of the archaeological site, leading me around the megaliths at least three times."
    "After she'd confirmed that we had studied the stones from every possible angle, she drew my attention to a small placard."
    
    pause(1)
    scene stones  
    show mei dress happy day open at right 
    with Dissolve(0.5)
    pause(1)
    
    m "S . . . s . . . s . . . "
   
    "She appeared to have difficulty deciphering the writing. She looked up at me."
    
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)
    
    m "Hey, what does that say?" #does she know his name?"
    
    "I bent over to look at the text, which appeared perfectly legible to me. I began to read."
    
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)
    
    a "{i}Swifterbant-culture . . .{/i}"
    
    "I decided to read on, not questioning her curious display of illiteracy."
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)
    
    a "It says here that these stones were erected by an ancient civilization. They used them as gravemounds and as a place to venerate chthonic deities."
    
    "She was staring at me with a captivated expression in her eyes." #TODO lots of staring here
    
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)
    
    m "Please, read more! Read more!"
    
    a "{i}The Swifterbant people lived here between 7500 and 5500 years ago, during the early neolithic. They were an early agrarian society that held livestock, but also resorted to hunting at times.{/i}"
    
    a "{i}The stones these megaliths were made from aren't native to the region, but were brought here from Scandinavia during the Ice Ages.{/i}"
    
    show mei dress fedup day open at right with Dissolve(0.5)
    
    a "That means they were carried here by large sheets of glacial ice."
    a "{i}When the Saale Ice Age ended, about 130,000 years ago, the rocks and debris that were caught in the ice stayed behind.{/i}"
    
    pause(1)
    
    "Mei was staring off into the distance, making me fear for a second that she would revert into a mysterious episode again, like on the night after I first met her."
    "But she remained fully aware."
    show mei dress obsessive day open at right with Dissolve(0.5)
    "And then she began to speak."
    
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress obsessive day open at right with Dissolve(0.2)
    
    m "Isn't that a {i}beautiful{/i} thought?"
    m "When the Swifterbant-people found these stones, they had been lying here for more than a hundred-thousand years."
    
    m "The centuries since then have passed in less than a \nheartbeat—" #for layout

    show mei dress estatic day closed at right with Dissolve(0.5)    
    "She erupted in a smile as bright as the setting sun."

    pause(1)
    
    m "It makes me so happy, to think that these stones will still be standing here in another hundred-thousand years."
    m "People will move and kingdoms will fall — but these stones will remain."
    
    show mei dress earnest day open at right with Dissolve(0.5) 
    
    m "It will be like nothing has really changed."
    
    pause(1)
    scene townpark with Dissolve(0.5) #evening version?

    pause(1)
    
    "I couldn't say it was a reassuring thought — though I welcomed it at the time, as it put my own growing problems somewhat into perspective."
    "These stones would remain here long after I'd recovered from bankruptcy; long after the burden of my part-time job had herniated my spine; long after I'd succumbed to lethargy in this godforsaken, backwater town—"
    "—where a couple of oversized rocks were considered, for some reason, a major tourist attraction."
    
    stop music fadeout 2.0
    pause(1)
    window hide
    stop sound fadeout 1.0
    pause(1)
    #scene black with fade
    scene viaductfields_nig with fade
    play sound "audio/summernight.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)
    
    "When night fell I brought Mei back to her parents' farm."
    "As we walked in silence, I clutched my book bag tightly under my arm."
    
    pause(1)
    
    "My gaze wandered off into the fields — these endless fields of impervious green that tapered off into nothingness."
    
    "And I thought to myself how straight they were."
    
    "Endued with a perfect geometric flatness, as though they had been carefully sleekened out by the trowel of an obsessive god."
    
    pause(0.5)
    window hide
    pause(1)
    stop sound fadeout 3.0
    scene black with Dissolve(3.0)
    pause(1)
    #####################################################################################################
    if rika_score > 1:
        show prog_rika p at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    elif rika_score ==1:
        show prog_rika n at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    else:
        show prog_rika d at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
        
    pause(0.25)
    
    if ina_score > 1:
        show prog_ina p at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
    elif ina_score ==1:
        show prog_ina n at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright  
    else:
        show prog_ina d at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
        
    pause(0.25)
    
    if mei_score > 1:
        show prog_mei p at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    elif mei_score ==1:    
        show prog_mei n at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    else:
        show prog_mei d at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    
    
    #####################################################################################################
    pause(2)
    hide prog_rika with easeoutleft
    pause(0.25)
    hide prog_ina with easeoutleft
    pause(0.25)
    hide prog_mei with easeoutleft
    
    
    pause(1)
    ##PART 1 - title
    #scene part2 with fade
    #pause(2)
    #scene black with fade
    play sound "audio/ventilator.ogg" loop fadein 1.0
    scene white with Dissolve(1.0)
    pause(1)
    scene part2_title1 with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    


###########################################################
#### PART 2 ###############################################
###########################################################

label p2c1:

    scene white
    play music "audio/doorbell.ogg" loop fadein 1.0
    pause(1)
    scene blueroom_twi with Dissolve(3.0)
    window show
    pause(1)
    
    "I awoke to the furious ringing of the doorbell."
    "As I hurried downstairs — haphazardly dressing myself en route — I wondered for a second why my father wasn't home. He was a notoriously light sleeper."
    
    pause(1)
    window hide
    #stop music fadeout 2.0
    scene black with fade
    play audio "audio/window.ogg"
    pause(1)
    scene residential 
    show ina pink sincere day open
    with Dissolve(1.0)
    play sound "audio/crowfield.ogg" loop fadein 1.0
    pause(1)
    window show 
    
    pause(1)
    
    "When I opened the door, I was greeted by a familiar face."
    "Ina appeared far too excited to take her finger from the bell."
    a "Please stop pressing that."
    
    stop music fadeout 0.5
    play music "audio/dormant.ogg" loop fadein 5.0 #was kamin
    show ina pink unhappy day open with Dissolve(0.5)
    
    n "The article! Have you done it? I want it at the publishers by tomorrow."
    
    "My semi-dormant mind was digging fruitlessly."
    
    show ina pink dissapointed day open with Dissolve(0.5)
    
    n "The {i}Weekly Progress{/i} article. Did you write it like I told you to?"
    "At the early hour, I didn't have the presence of mind to throw up a fight." #did this before
    pause(1)
    a "Tomorrow. I promise. Tomorrow."

    n "It better not be late."
    
    show ina pink smile day open with Dissolve(0.5)
    
    n "But never mind that. I just received notice that our cover article has set the city council alight!"
    
    n "It turns out that the farm assault wasn't an isolated incident."
    n "Mayor Van Linden had been receiving signals of worker mistreatment throughout the year leading up to the murder. But he failed to act in any meaningful way."
    n "Then last year the incident occurred—"
    
    show ina pink sympathetic day open with Dissolve(0.5)
    
    n "—and now that the police investigation has come up with nothing, council members are beginning to openly question the mayor's efficacy."
    n "Do you realize our publication could cost him his career?!"
    
    pause(1)
    "Most of her words flew straight by me, though I remember her eyes burned bright like meteorites on that pale Wednesday morning."
    pause(1)
    
    a "We should really be getting to school."
    
    hide ina with Dissolve(1.0)
    pause(1)
    scene mainstreet with Dissolve(0.5)
    pause(1)

    show ina pink smile day open at right with Dissolve(0.5)        
    "On our way to school, Ina wouldn't stop lecturing me on the various intricacies of the municipal government. The trip had never felt so long"
        
    n "Voices within the mayor's own party are pushing for him to step down. They consider this incident a telltale sign of his continuing incompetence."
    a "Members of his own party? Wouldn't that be counter-intuitive?"
    pause(1)
    n "Well, it's complicated—"
    n "Abbot Island Reformed — commonly referred to as A.I.R — is the largest party in the town council. Its electorate consists of farmers and members of the church."
    
    show ina pink neutral day open at right with Dissolve(0.5)
    
    n "But with its size comes inner division. Of the eight seats the party currently occupies, four are held by members that represent the agricultural sector."
    n "They generally come from agrarian families and serve as advocates for the local farms." #Traditionally the agrarians "
    
    stop sound fadeout 1.0
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene schoolroad #with Dissolve(1.0)

    #pause(1)
    show ina pink sincere day open at right 
    with Dissolve(1.0)
    
    n "The other four seats, however, are held by the Kuyper faction. These are members of the church — mainly descendants of the original inhabitants of the Island."
    n "The current leader of the Kuyper faction is John Kuyper, Rika's father."
    
    pause(1)
    a "What ever happened to the separation of church and state?"
    
    "Ina pressed on, ignoring my remark."
    
    n "Even though they're in the same party, there's tension between the Kuyper faction and the agrarians."
    n "The Kuyper faction has always tried to implement a strictly isolationist policy for the town, letting in as few outsiders as possible."
    
    n "The agrarians however rely on outside labor during harvest season, and are generally more welcoming towards newcomers."
    
    n "The current mayor of Abbotsford is an agrarian, so the Kuyper faction is weaponizing this incident in order to strengthen their position within the party."
    
    scene school_side with Dissolve(1.0)
    show ina pink smile day open at left with Dissolve(0.5)
    
    n "A.I.R. has always exerted undisputed influence over the town's administrative affairs. You can tell their power has never been contested by an actual free press."
    pause(1)
    n "I believe there's much more to be uncovered on this matter."
    pause(1)
    stop music
    n "I'd like you to ask Rika out on a date. "

    "Suddenly I was wide awake."
    
    pause(1)
    
    a "I have absolutely no intention of doing that."
    pause(1)
    n "We'll see."
    hide ina with Dissolve(1.0)
    pause(1)

label p2c2:


    scene school_front with Dissolve(1.0)
    show ina pink unhappy day open at center with Dissolve(0.5)
    
    "We arrived at school early."
    
    pause(1)
    
    n "I'm going to head up to the office to change into that terrible uniform. I'll see you in class—"
        
    play audio "audio/swipe.ogg"
    hide ina with Dissolve(0.2) #easeoutleft
    "Suddenly she dove behind me, as though she were hiding from something."
    "She began to speak in a hushed voice."
    
    n "Look who's here, of all people. There! Go talk to her!"
    #play audio "audio/swipe.ogg"
    "And with these words she slid into a nearby entrance way." #bad
    pause(1)
    ##Rika
    show rika uni happy day closed at center with Dissolve(0.5) 
    play music "audio/prelude1.ogg" loop fadein 15.0
    pause(1)
    
    r "Abe! What a pleasant surprise. I hope you've been settling in nicely."
    pause(1)
    a "I see you're part of the early bird club."
    show rika uni happy day open at center with Dissolve(0.5)
    r "We practice with the swimming team on Wednesday mornings. There's a big championship coming up soon."
    "She ran her fingers through her long black hair."
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)
    r "I'm so glad you're getting involved with the school paper. Personally I don't really read it, but my father was absolutely lyrical about that cover piece you ran in the last issue."
    r "He can't stop gushing about how much student journalism has improved over the last years."
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)
    "I laughed incredulously."
    a "All credit goes to Ina. I just see to an, eh— timely delivery."
    r "Well, he said your paper's an asset to the town." #Some of the things that Linden guy gets up to . . ."
    #a "Isn't your father close to him?"
    
    #"I was amazed by the candor with which Rika was opening up to me."
    
    show rika uni mischievous day open at center with Dissolve(0.5)    
    
    #r "You know . . . There's been some complaints about the mayor recently . . ."
    r "Come on, there's time left before classes start. Let's take a walk over the school grounds."
    
    hide rika with Dissolve(0.5)
    pause(1)
    scene schoolgrounds with Dissolve(0.5) 
    pause(1)
    show rika uni happy day open at left with Dissolve(0.5) 
    pause(1)
    r "So you know this place used to be an island, right?"
    a "I nodded."
    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2) 
    r "In the early eighteen hundreds it was home to a community of about 400 fishing families."
    r "Life was tough, but they made an honest living."
    
    r "Periodically storms would rage through Ala Bay. The islanders protected Abbot against the water, by erecting long barriers built out of wooden poles."
    r "But during storms the barriers suffered, and the islander would have to rely on donations from the mainland to restore them."

    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2)     
    
    r "In 1858, a highly turbulent year weather-wise, the Elisabeth flood swept over the low countries, leaving a wake of annihilation behind."
    r "Part of Abbot's fishing fleet was destroyed, most of the barrier washed away."
    r "Not much later, the government announced the full evacuation of island. The inhabitants were to be rehoused on the mainland."
    
    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2) 
    
    r "They said it was due to the increasing threat of storms and the infeasible costs of restoring the wooden barrier."
    show rika uni mischievous day closed at left with Dissolve(0.5) 
    r "However, some suspect that persistent poverty and inbreeding on Abbot played an equally important role in the decision to evacuate."
    
    "She smiled a mischievous smile."
    
    pause(1)
    
    a "So in the end the island was left deserted?"
    pause(1)    
    r "Not really."
    
    
    show rika uni mischievous day open at left with Dissolve(0.5) 
    
    r "A group of two hundred islanders stayed behind, all hardline members of a small reformatory congregation."
    
    show rika uni mischievous day closed at left with Dissolve(0.2) 
    show rika uni mischievous day open at left with Dissolve(0.2)  
    
    r "The Church of Abbot had recently been ejected from the mainstream branch of low country Protestantism."
    r "These were troubled times, theologically speaking, and church schisms were a common occurrence."
    
    show rika uni mischievous day closed at left with Dissolve(0.2) 
    show rika uni mischievous day open at left with Dissolve(0.2)    
    
    r "Anyway, the seceded congregation vowed to remain on the island — and the government did nothing to stop them."
    r "For close to a century they lived isolated lives, with very little contact with the outside world."
    
    show rika uni sad day open at left with Dissolve(0.5) 
    
    r "Until reclamation of the Marshpolder began."
    r "In the 1940s, Abbot suddenly found itself floating on a sea of fertile soil. Farmers from the mainland migrated here to cultivate the fields."
    
    show rika uni sad day closed at left with Dissolve(0.2) 
    show rika uni sad day open at left with Dissolve(0.2) 
    
    r "But the original inhabitants of Abbotsford — descendants of the islanders who had seceded in 1858 — observed the influx of newcomers with sorrow in their eyes."
    
    r "There has always been tension between the two groups."
    r "The farmers work hard — but they're blind to our heritage."
    

    show rika uni sad day closed at left with Dissolve(0.5) 
    "A grave expression appeared on her face."
    pause(1)
    
    r "The islanders are honest people. They'd never cover up a crime—"
    
    play audio "audio/schoolbell.ogg"
    pause(1)
    #"We headed back towards the school."
    

    hide rika with Dissolve(0.5)
    stop sound fadeout 1.0
    pause(1)
    scene schoolstairs with Dissolve(0.5) #TODO, replace with the stairs!!!
    play sound "audio/clock.ogg" loop 
    window show
    pause(1)
    "By the time we'd made it up the stairs, classes had already started."
    show rika uni happy day open at left with Dissolve(0.5) 

    "She turned to me."
    
    pause(1)

    r "Do you know what's interesting? "
    r "After the Elisabeth-flood, Abbot was never struck by a storm again. "
    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2) 
    a "So the entire evacuation had been for nothing?"
    pause(1)
    r "You could say so."

    #pause(1)
    scene rikalegs with Dissolve(0.5)
    pause(1)
    
    r "Some of the more self-righteous members of our congregation speculate that the floods were punishment by a higher power."
    r "That there was no more need for them, after all subversive elements had been extracted from the community." 
    pause(1)
    r "{i}The kingdom of heaven is like a net cast into the sea, that gathered fish of every kind.{/i}"
    r "{i}When it was full, the fishermen hauled it ashore.{/i}"
    r "{i}Then they sat down and gathered the good fish into vessels, but cast the bad away.{/i}"
    
    pause(1)
    #show rika uni happy day open at center with Dissolve(0.5) 
    
    r "Anyway, I have to go to class now."
    r "I absolutely loved talking to you."
    
    r "Also, I was wondering—"
    
    "She paused for a second, tenderly winding her hair around her finger."
    #show rika uni happy day closed at center with Dissolve(0.2) 
    #show rika uni happy day open at center with Dissolve(0.2) 
    pause(1)
    
    r "Would you mind going out for dinner this Saturday evening? My parents are attending a wedding, and I'd hate to eat alone."
    
    "I could detect a hint of anxiety in her voice."
    
    pause(1)
    scene schoolstairs 
    show rika uni happy day open at left 
    with Dissolve(0.5) 
    pause(1)
    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2)
    
    #### Rika 3 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "Will you join me?"
        
        "I'd be glad to — if I survive my paper round.":
            show rika uni mischievous day open at left with Dissolve(0.5) 
            $ rika_score += 1
            r "That's great, I'd love to learn more about you."                         
            
        "This town has restaurants?": 
            show rika uni sad day open at left with Dissolve(0.5) 
            n "I know a good one. It's run by people from our church."
    
    #####################################################################################################   
    
    show rika uni happy day open at left with Dissolve(0.5) 
    "I was struck by the candor of her sudden proposal — so struck that I had no choice but to accept, even though I realized I was playing directly into Ina's plans."
    
    show rika uni happy day closed at left with Dissolve(0.2) 
    show rika uni happy day open at left with Dissolve(0.2) 
    
    a "Then it's a date. See you next Saturday."
    
    pause(1)
    "With a nod of her head she said goodbye."
    
    stop music fadeout 3.0
    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    pause(1)


label p2c3:

    #scene bluehall with Dissolve(0.5) #improve classroom image
    scene office with Dissolve(0.5)
    play sound "audio/officesound.ogg" loop fadein 5.0
    window show
    pause(1)
    
    "Ina pulled me aside the moment classes ended. She seemed nervous."    

    pause(1)
    show ina shirt angry day open at left with Dissolve(0.5)#
    play music "audio/kamin.ogg" loop fadein 20.0 #should we cut in later??? "audio/dormant.ogg"
    #show ina shirt angry day closed at left with Dissolve(0.2)
    #show ina shirt angry day open at left with Dissolve(0.2) 

    pause(1)
    
    n "So?"
    
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    
    "I shook my head in ignorance."
    pause(1)

    
    #### Ina 3 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "What did you manage to get out of Rika?"

        "I didn't really {i}get{/i} anything out of Rika . . .":
            show ina shirt angry day closed at left with Dissolve(0.2)
            show ina shirt angry day open at left with Dissolve(0.2)  
            n "You didn't?"
            "I would've hated to admit I landed a date."
            
        "She complimented you on your journalism.": 
            $ ina_score += 1
            show ina shirt defiant day open at left with Dissolve(0.5)
            pause(1)
            n "Yeah she {i}would{/i}, wouldn't she."  
    
    #####################################################################################################   
    
    show ina shirt defiant day open at left with Dissolve(0.5)
    n "Just tell me what you guys discussed."
    pause(1)
    "Though I still had vivid recollections of Rika's coiling hair, I had to admit the details of our conversation this morning had long since faded to the back of my mind."
    
    pause(1)    
    a "We talked about the town for a bit."
    n "And?"
    "I thought for a second."
    pause(1)
    a "She said the Isle of Abbot was evacuated in the nineteenth century, due to inbreeding. Does that make sense to you?"
    n "Sure, they were ravaged by storms at the time. Only a small community remained, including the Kuyper family."
    a "Well then I don't think she told me anything of interest."
    
    show ina shirt angry day open at left with Dissolve(0.5)
    
    n "Hmpf. {i}I{/i} should be the judge of that."
    
    pause(1)
    "An awkward silence lingered. The newsroom was a mess — every inch of floor space was filled up with boxes, newspaper clippings, scattered clothing—"
    
    pause(1)
    
    a "So Ina, I was wondering—"
    n "What?"
    a "When will you introduce me to the {i}other{/i} editors on the staff?"
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    "She flinched."
    
    show ina shirt surprized day open at left with vpunch #Dissolve(0.2)
    
    n "I-it's not a school paper!"
    a "I never said it was."
    
    show ina shirt angry day open at left with Dissolve(0.5)  
    
    n "We {i}have{/i} got other editors, but they mostly work from home."
    n "It's not like I write everything myself."
    pause(1)
    "It appeared that I had hit a nerve, and I began to regret my line of questioning."
    "I dug through my memory for something that would cheer her up."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2) 
    a "You know what? There {i}was{/i} something strange Rika told me this morning."
    
    show ina shirt defiant day open at left with Dissolve(0.2)
    
    n "What?!"
    a "Something about a church schism, just before the island was evacuated."
    a "She was a little vague on the matter."
    "As expected, Ina appeared unnaturally interested."
    show ina shirt angry day open at left with Dissolve(0.5)    
    n "A schism, you say? In the Church of Abbot?"
    a "Rika said it was the reason some of the islanders stayed behind."
    "Ina had begun browsing her phone, while a soft murmur trickled from her lips."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)        
    n "A church schism . . . That seems highly unlikely . . . If only . . ."
    
    show ina shirt interested day open at left with Dissolve(0.5)    
    
    n "There! I've found something. It's called {i}Theological Inquiries into the Congregation of the Church of Abbot{/i}."
    
    pause(1)
    
    a "Is it relevant?"
    "Some more typing."
    show ina shirt angry day open at left with Dissolve(0.5) 
    
    n "I'm not sure. It could be."
    n "Inquiries were a big deal in the reformed church at the time. They could point towards corruption or severe theological divergencies."
    scene inaoffice with Dissolve(0.5)
    n "The thing is, the Church of Abbot and the Kuyper family have always held a pivotal position of power in this town."
    "Her eyes were glowing."
    n "Any dirt on them, old or new, will surely cause a stir — {i}much{/i} more than any aberrant migration pattern of insects ever will." #cause stir, turmoil, etc.
    "She turned her attention back to her phone."
    pause(1)#
    n "There it is! They have a copy in the municipal archive of Bremersberg. That's less than 20 minutes away by train. We'll go there on Friday."
    a "On Friday? Don't we have school on Friday?"
    n "Oh but this is much more important than school. "
    pause(1)
    n "And besides, we get allotted time off for mandatory club activities."
    
    pause(1)
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene schoolstairs with Dissolve(0.5)
    play sound "audio/clock.ogg" loop
    pause(1)
    
    "As we headed downstairs I noticed she was trembling with excitement."
    
    pause(1)
    stop sound fadeout 1.0
    scene school_front with Dissolve(0.5) 
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    show ina shirt angry day open at left with Dissolve(0.5)    
    pause(1)
    
    n "Lets head over to my house for now. I want to run some ideas by you—"
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    "I wasn't in the mood to protest." #TODO bad, used before tons of times???
    
    hide ina with Dissolve(0.5)
    window hide
    stop sound fadeout 2.0
    pause(1)
    scene black with fade
    pause(1)
    scene diningroom with fade
    pause(1)
    window show
    pause(1)
    ## living room
    play sound "audio/clock.ogg" loop #good indoor sfx
    "Her house had a well-kept, almost sterile appearance to it."
    pause(1)
    #show ina shirt saddened day open at left with Dissolve(0.5) 
    #pause(1)

    "As she led me into the living room, I noted a hint of sadness in her eyes."
    #pause(1)
    
    "After prying, she told me her mother was touring at the moment. She was a famous conductor, Mina Mengelberg, currently serving as the musical director of the Vienna Philharmonic Orchestra."
    
    "I mentioned I had seen her name on a playbill once. When I still lived in the city."
    
    hide ina with Dissolve(0.5) 
    
    pause(1)
    scene inabedroom_eve with Dissolve(0.5)
    pause(1)
    play music "audio/poucet.ogg" loop fadein 3.0
    show ina shirt angry day open at left with Dissolve(0.5) #TODO Maybe more obsessive expression
    
    n "So this is my room."
    n "I hate it, though. Empty houses give me the creeps."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    n "That's why I'm usually at the office."    
    
    show ina shirt angry book open at left with Dissolve(1.0)
    "She produced a large book from her bag — the same one I had seen her reading at school."
    
    pause(1)
    
    n "I'm reading Oswald Spengler at the moment. {i}Untergang des Abendlandes{/i}."
    n "I haven't made it past the second chapter."
    show ina shirt angry book open at left with Dissolve(0.5)
    "She folded it open to a page that she'd marked with a slip of paper."
    
    show ina shirt angry book closed at left with Dissolve(0.2)
    show ina shirt angry book open at left with Dissolve(0.2)    

    n "{i}A boundless mass of human being, flowing in a stream without banks, up-stream, a dark past wherein our time-sense loses all powers of definition and restless or uneasy fancy conjures up geological periods to hide away an eternally-unsolvable riddle—{/i}"
    n "{i}—down-stream, a future even so dark and timeless. Such is the groundwork of the Faustian picture of human history.{/i}"


    show ina shirt angry day open at left with Dissolve(1.0)
    "She closed the book and handed it to me." 

    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    n "Modern man's yearning for infinite progress is Faustian in nature. Spurned by his endless aspirations, humanity involuntarily seals its own fate."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)  
    n "We have left the natural state far behind. We couldn't return even if we wanted to."
    n "Being has been altered irredeemably."
    
    pause(2)
    
    n "I'm sorry I dragged you down here."    
    pause(1)
    n "I know you're not really interested in this newspaper business."
    show ina shirt saddened day open at left with Dissolve(0.5) 
    n "It's just—"
    pause(1)
    n "I talk in myself, if I don't have someone else to talk to. Whenever I'm catching onto something great."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt saddened day open at left with Dissolve(0.2)  
    n "It drives me insane."
    
    show ina shirt saddened day open at left with vpunch
    "I gave her a reassuring nudge."    
    a "I guess you know my predicament."
    #a "I guess you know what feels it feels like."

    show ina shirt interested day open at left with Dissolve(0.5) 
    
    pause(1)    
    "She smiled."
    n "You know—?"
    show ina shirt mirth day closed at left with Dissolve(0.2)
    show ina shirt interested day open at left with Dissolve(0.2)
    n "I have a feeling this church piece is going to be big. Bigger than anything we've done before."
    n "Bigger than the Sandford house affair—"
    pause(1)
    a "What's that Sandford house affair you keep talking about?"
    "It was out before I realized what I was doing."
    show ina shirt smiling day open at left with Dissolve(0.5) 
    
    n "Didn't I {i}tell{/i} you?"
    show ina shirt smiling day closed at left with Dissolve(0.2) 
    show ina shirt smiling day open at left with Dissolve(0.2) 
    n "Our exposé on the Sandford house affair was our finest hour — the scoop that truly put The Sunday Abbot on the map."
    pause(1)
    n "It was around this time last year when the {i}Evening Mirror{/i} — a smutty tabloid — published a series of compromising photographs of an influential Abbotsford politician."
    
    n "The photo's were taken inside a notorious Bremersberg cabaret club, where he was being courted by an, uh— {i}dancing{/i} girl."
    
    scene black 
    show ina shirt smiling day open at left
    with Dissolve(1.0)
    
    scene marquis 
    show ina shirt smiling day open at left
    with Dissolve(1.0)
    
    n "The politician in question is named Leopold. Leopold {i}marquis of Abbot{/i}, to be precise — a member of the nobility. He still holds a seat in the Abbotsford city council."
    n "Leopold hails from the old lineage of lords of the isle. He has quite a reputation as a party animal — and for that reason the incident initially blew over without much ado."
    
    show ina shirt smiling day closed at left with Dissolve(0.2) 
    show ina shirt smiling day open at left with Dissolve(0.2) 
    
    n "But four months later, we received an anonymous package at the office."
    
    show ina shirt smiling day closed at left with Dissolve(0.2) 
    show ina shirt smiling day open at left with Dissolve(0.2) 
    
    n "It was another set of photographs — placing marquis Leopold at a lavish party inside {i}Sandford House{/i}, one of the oldest mansions in Abbotsford."


    scene marquis_house 
    show ina shirt interested day open at left
    with Dissolve(1.0)
    
    n "There were more girls present during this occasion, and the marquis appeared to be fully inebriated. "
    
    n "In a note, the anonymous source explained that marquis Leopold had been carrying classified documents with him on the night he attended Sandford House."
    
    n "But after the hedonistic party — the source wrote — his briefcase and the documents it contained were nowhere to be found."
    
    show ina shirt angry day open at left with Dissolve(0.5) 
    
    n "We ran an absolute bombshell of an article. Apparently the marquis had indeed lost classified policy papers on that fateful night — and to make matters worse, he hadn't notified the council of their disappearance."
    
    scene inabedroom_eve
    show ina shirt angry day open at left 
    with Dissolve(1.0)
    
    n "It became a lot harder to forgive the marquis's decadent escapades when the political integrity of the community was at jeopardy."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)     
    n "The Kuyper faction initiated a charge, declaring that the marquis's conduct was unworthy of a christian political party."
    n "They had a field day with the whole affair."
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2)   
    a "So did Leopold lose his seat over this?"
    
    n "He didn't. He's an elected official — after all — and is therefore protected by the constitution. However his position within A.I.R. has become precarious since the affair."
    
    n "I doubt he'll return after the elections—"
    
    stop music fadeout 4.0
    show ina shirt angry day closed at left with Dissolve(0.2)
    show ina shirt angry day open at left with Dissolve(0.2) 
    
    "She stopped abruptly. Looking down — then up at me again."
    pause(1)
    
    n "I'm probably boring you."
    n "It's okay, you should be on your way home."
    pause(1)
    n "I'm going to read some more Spengler before bed."
   
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 1.0
    stop sound fadeout 0.1
    scene black with fade
    
        
label p2c4:
    
    scene black with fade
    pause(1)
    scene council with Dissolve(0.5)
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    window show
    pause(1)
    
    "I spent most of Thursday afternoon loitering around town, trying to find something or someone to write my Weekly Progress article on."
    "Sadly, as I searched in vain, it began to dawn on me why Ina had unloaded this piece on me. Abbotsford really didn't have {i}any{/i} progress to report—" 
    #pause(1)
    play audio "audio/swipe.ogg" 
    "Then, a flash, in the corner of my eye."
    play music "audio/angrydog.ogg" loop
    show phyrrus at right with Dissolve(0.3)
    
    "No! Move away! Hellhound! I'm not even working today!"
    
    pause(1)
    show karin surprised at left with Dissolve(0.5)
    pause(1)
    
    k "Phyrrus! Leave the man alone!"
    stop music fadeout 2.0
    pause(1)
    play audio "audio/panting.ogg"
    "As soon as miss Voorhees entered the scene, the dog became as docile as a lamb."
    pause(1)
    a "Hi Karin. Thanks for coming to my rescue again."
    
    show karin happy at left with Dissolve(0.5)

    
    k "I feel like he's warming up to you. He didn't even bite you this time. "
    k "So what brings you here today?"
    pause(1)
    a "Ina's making me write an article. It can be about any person or event in town."
    a "The thing is — it's due today."
    pause(1)
    k "You wouldn't be referring to {i}The Weekly Progress{/i}, would you? That's a local favorite!"
    k "Ina must have a lot of faith in you, to entrust you with such an important piece of journalism."
    
    "I could tell she was concealing an impish smile." #As she stood and pondered for a second, 
    
    show karin serious at left with Dissolve(0.5)

    
    k "Anyway, if you want you can interview me. It may help my re-election if I get some positive press out."
    hide phyrrus with Dissolve(0.5)
    a "Maybe you could write the whole thing for me?"
    
    show karin laughing at left with Dissolve(0.5)    
    "She burst out laughing."
    
    k "Come on, let's go someplace where we can talk. "
    
    stop music fadeout 1.0
    hide karin with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene ristorante with Dissolve(0.5)
    show karin worried at left with Dissolve(0.5)

    play music "<from 10.0>audio/cellosonata.ogg" loop fadein 4.0
    pause(1)
    "She let out a long sigh."
    pause(1)
    
    k "Small town politics can be a headache. "
    
    k "That piece you guys published last week, um—"
    k "—to be fair, it caused quite a bit of commotion."
    show karin serious at left with Dissolve (0.5)
    "She adopted a more serious demeanor." #TODO bad
    pause(1)
    k "Let me state first and foremost that our party has always been a proponent of the free exchange of labor."
    k "Abbotsford has some of the largest farms in the region, so come August there's always a huge demand for seasonal workers."
    
    a "What party are you in?" #do you represent
    
    k "Abbot Island Reformed. We're currently in charge—"
    
    pause(1)
    
    k "Laborers come here from all over the low countries — many even from further afield."
    k "The work offers them an escape from poverty. It's in our greatest interest that they're treated well."
    
    k "The thing is . . . Not everybody is as welcoming towards outsiders."
    k "Over the last years a new political movement had been growing in membership."
    k "Flock 05, they're called. They were founded in 2005. "
    
    
    k "Flock 05 takes a more cautious stance on labor migration. They claim that seasonal workers constitute an unnecessary burden on our local infrastructure. "
    
    k "There was a small incident — not long after their party was founded — in which a group of farm workers had been caught stealing food from local stores."
    
    k "It was just petty theft, but Flock really went to town with it, converting the incident into a large electoral windfall."
    
    #TODO expand a little, explain that he likes being an interviewer, write about Karin.
    pause(1)
    
    a "Do you think people from Flock 05 are behind the murder?"
    
    show karin worried at left with Dissolve(0.5)
    
    k "No. And I don't want you writing that."
    k "It's just that this subject matter is more complicated than it seems. "
    k "A.I.R. has always protected the rights of all farm workers, but the general attitude has been shifting lately—"
    pause(1)
    a "What about the Kuyper faction?"
    
    show karin surprised at left with Dissolve(0.5)    
    
    k "The Kuyper— what?"
    a "The Kuyper faction within your party, do they share your stance on labor migration?"
    k "I'm afraid you're misinformed. A.I.R. is one party. We don't have factions."
    
    show karin worried at left with Dissolve(0.5)
    "She began speaking in a hushed voice."
    pause(1)
    
    k "Look, I understand you guys feel involved."
    k "I'll tell you more, but you'll have to consider it {i}off the record{/i}."
    "I smiled."
    a "No problem, I have more than enough material as is."
    
    #She lowered her voice."
    show karin serious at left with Dissolve(0.5)  
    pause(1)
    k "This is a very painful incident for our mayor. The farm murder occurred on property that belonged to his brother."
    "I nodded."
    pause(1)
    k "Now several voices are implying that the police investigation into the abuse was intentionally halted by mayor Van Linden and the chief of police."
    pause(1)
    k "But I know the mayor. He wouldn't do such a thing."
    k "After the assault, the victim's co-workers returned to their hometowns. They weren't available for further questioning. The police closed the case because they really didn't have any more leads."
    pause(1)
    a "And the mayor's brother? What kind of person is he?"
    pause(1)
    k "I'm not sure."
    "She paused."
    
    pause(1)
    
    k "He works his people hard. A little too hard, at times. But he's not a sadist."
    k "He wouldn't do that to anyone—"
    
    #TODO write slightly more about the cafe/surroundings"
    #TODO make dialogues more fun in general, more stuff happening
    show karin worried at left with Dissolve(0.5)
    k "Anyway, I really need to get back to work."
    pause(1)
    k "If you guys want, you're welcome to come over to my place for coffee some time. I can imagine Ina would love to have a source inside the council."
    pause(1)
    hide karin with Dissolve(0.5)    
    pause(1)

    window hide
    stop music fadeout 4.0    
    pause(2)

    scene black with fade
    pause(1)
       
label p2c5:

    scene black with fade
    pause(1)
    scene train with Dissolve(0.5)
    window show
    pause(1)
    
    "On Friday, we snuck out of school during lunch break."
    "Outside of commuting hours, the train to Bremersberg only ran sporadically. We had to rush to make it in time."
    
    pause(1)
    window hide
    pause(1)
    play sound "audio/train.ogg" loop fadein 1.0
    scene viaduct with Dissolve(0.5)
    pause(2)
    scene trainin with Dissolve(0.5)
    pause(1)
    window show
    show ina pink neutral day open with Dissolve(0.5)
    #pause(1)
    show ina pink neutral day open with vpunch
    pause(1)
    n "I loved your article."

    "She appeared reluctant to admit it, like a child enjoying broccoli."
    
    show ina pink neutral day open with vpunch
    
    n "It had its flaws, of course. It's just . . . I'd never thought about using the Weekly Progress section that way. For actual journalism."
    show ina pink neutral day open with vpunch    
    a "I just happened to bump into Karin in the street."
    
    ## shots of train riding through fields"

    pause(1)    
    scene viaduct with Dissolve(0.5)
    
    "We shot past miles and miles of farmland. Ina had begun murmuring in herself."
    
    n "I haven't seen any bees this year. There were a few last year, but none this summer. It's just crickets now."
    n "You know they kept me up last night?"
    n "The crickets and their maddening song — like a thousand voices crying out in terror."
    n "As if they can sense their impending death once winter comes."
    pause(1)
    n "If winter ever comes."
    
    pause(1)
    scene trainin
    show ina pink sincere day open
    with Dissolve(0.5)
    show ina pink sincere day open with vpunch
    
    "I shrugged."
    
    show ina pink sincere day open with vpunch
    
    n "I spoke to the archivist on the phone — he confirmed that the publication should be there."
    n "It's part of a larger collection of church inquiries that were commissioned by the {i}Presbytery of the Low Countries{/i} after the secession of 1834."
    show ina pink sincere day open with vpunch
    n "The reformed church has always been prone to schisms. In 1834 however, three congregations seceded at once — out of dissatisfaction with liberal tendencies within reformed theology at the time."
    
    pause(1)
    
    n "During the subsequent decades many more churches followed in their wake, to the point where the remaining pastors felt the time had come to take action."
    
    show ina pink sincere day open with vpunch
    
    n "The reformed church isn't a centrally coordinated institution. Due to the particular state of affairs, however, the remaining pastors agreed to converge in what was named the {i}Presbytery of the Low Countries{/i}. "
    
    n "The presbytery resolved to rout out churches that appeared to stray from mainstream Protestant theology. By proactively excluding troublesome congregations, the church hoped to end the broader trend of insurgency once and for all."
    
    show ina pink sincere day open with vpunch
    
    n "The document we'll be consulting is a church inquiry, commissioned by this very presbytery."
    
    n "It pertains to the congregation on Abbot Island, led by the reverend Johan Kuyper."
    
    n "It would eventually lead to their expulsion from the Reformed Church. This all took place in 1857, not long before the evacuation of the island. "
    
    show ina pink sincere day open with vpunch
    
    a "Is Johan Kuyper—"
    
    show ina pink smile day open with Dissolve(0.5)
    
    n "Yes. Her great-great-great-great-grandfather. If I'm not mistaken."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    stop sound fadeout 3.0
    window hide
    pause(2)
    #scene underground with Dissolve(0.5)
    #pause(2)
    scene station with Dissolve(0.5)
    play sound "audio/citysounds.ogg" loop fadein 1.0
    window show
    pause(1)
    
    "We made our way towards the archives. The city was noisy as usual."
    
    scene bremersberg with Dissolve(0.5)
    pause(1)
    play music "audio/0adagio15.ogg" loop fadein 15.0
    show ina pink sincere day open with Dissolve(0.5)
    pause(1)
    
    n "So this is Bremersberg."
    
    n "I assume it's the first time you've been here."
    
    pause(1)
    
    n "It was built shortly after the war. Carefully planned to funtion as the metropolitan hub of the newly reclaimed land."
    
    show ina pink grave day open with Dissolve(0.5)
    
    n "How can something that's been thought out so meticulously, grow into such an abomination?"
    
    pause(1)
    
    n "In the past, cities arose out of the countryside, nourished lovingly by their surrounding communities."
    
    n "{i}But now the giant city sucks the country dry, insatiably and incessantly demanding and devouring fresh streams of men, till it wearies and dies in the midst of an almost uninhabited wasteland.{/i}"
    
    show ina pink unhappy day open with Dissolve(0.5)    
    
    n "Bremersberg has become a dismal necropolis, wrapped in the sounds of countless invisible cars — all attempting to find their way in its inorganic street plan."

    n "It appears completely amorphous to me, like a welded-together amalgamation of left over parts of other cities—"
    
    n "—lacking any differentiating feature."
    
    pause(1)
    stop music fadeout 6.0
    hide ina with Dissolve (0.5)
    pause(1)
    scene archives with Dissolve(0.5)
    pause(1)
    
    "The municipal archives were curated by the University of Bremersberg. We made our way through a few galleries of natural history exhibits until we reached the library."
    
    pause(1)
    stop sound fadeout 1.0
    scene archivesin with Dissolve(0.5) 
    play sound "audio/clock.ogg" loop
    pause(1)
    
    "Without as much as looking around, Ina went up to the archivist and asked him for the document she was looking for."
    
    "He eyed her up with a bemused glance in his eyes."
    
    pause(1)
    play music "audio/feerique.ogg" loop fadein 8.0
    show archivist at left with Dissolve(0.5)
    
    c "So you're the students that made a reservation for the {i}Theological Inquiries{/i}?"
    n "Sure. Is there a problem?"
    "He chuckled."
    c "Oh not at all. It's just that we don't get many requests for these dusty church annals."
    hide archivist with easeoutleft
    "He left briefly, to dig up an old book."
    show archivist at left with easeinleft
    pause(0.5)

    c "Here it is. It isn't available for loan — so you'll have to consult it at one of our reading tables."
    #hide archivist with Dissolve(0.5)
    pause(1)
    scene bookcase with Dissolve(0.5)
    pause(1)
    "We sat down."
    show ina pink neutral book open with Dissolve(0.5)

    pause(1)
    
    "From the moment Ina opened the heavy, leatherclad book, a musty fragrance poured forth from its yellow pages. In a hushed voice she began to read."
    #### Space for some reading.

    #"I sat silently while Ina read. After what felt like a century, she looked up at me."
    
    show ina pink sympathetic book open with Dissolve(0.5)
    
    ######################################################################################
    stop sound fadeout 1.0
    n "{i}Journal of the reverend Thomas W. H. H. Backer, inquirer for the Presbytery of the low countries.{/i}"
    
    play sound "audio/0sealapping.ogg" loop fadein 4.0
    scene lake
    show ina pink sympathetic book open
    with Dissolve(0.5)
    
    n "{i}Saturday, 19th of September 1856. We set sail early in the morning to favorable winds and quiet waters.{/i}"
    n "{i}Aboard were — the captain Jan H. M. Born and his two crew members, a traveling merchant, some islanders, and the gentleman Marcus P. Brasschaert who would be serving the island as a replacement schoolteacher—{/i}"
    
    pause(1)
    
    a "You're excused to read silently, if you'd like—"
    show ina pink grave book open with Dissolve(0.5)
    n "Hmpf. Let me skip ahead a bit."
    pause(1)
    
    n "{i}With the good south wind behind us, it took us less than half an hour to catch first sight of the isle in the distance.{/i}"
    stop sound fadeout 1.0
    pause(1)    
    play sound "audio/0searoar.ogg" loop fadein 6.0
    scene storm
    show ina pink grave book open
    with Dissolve(0.5)
    pause(1)    
    n "{i}But as we approached Abbot, we struck harsh and impetuous waves — and whitecaps formed around us.{/i}"
    n "{i}Within a matter of minutes, the formerly peaceful sea had erupted in a fierce tempest, rocking our ship to and fro.{/i}"
    
    n "{i}Though we as passengers were distraught by the sudden onset of the storm, our captain reassured us that sudden gales were not uncommon on this strait of Ala Bay.{/i}"
    n "{i}But as I lay cooped up in the ship's stern, I prayed fervorously for our safe voyage.{/i}"
    show ina pink neutral book open with Dissolve(0.5)
    
    n "{i}There appeared to be no end to the tempest. As I had a clear view of the firmament from my hiding place, I began to notice that this storm was imbued with a strange quality of sorts.{/i}"
    n "{i}For although the sea was in unruly turmoil, erupting in waves and eddies of violent fervor — the sky above remained blue and completely devoid of wind.{/i}"
    
    n "{i}It was as though not a gale, but a submarine vortex was kicking up these crashing waves.{/i}"
    n "{i}And when I gathered the courage to look overboard, I fancied at times, that I could see a thin black ripple, coiling through the waves, glistening — whenever it broke the surface — in the ever dazzling sun.{/i}"
    pause(1)
    n "{i}It took us the greater part of an hour to reach the harbor — and when the ship finally moored, the tempest abruptly came to a halt.{/i}"

    pause(1)
    stop sound fadeout 1.0
    scene sky_blue
    show ina pink neutral book open 
    with Dissolve(1.5)
    play sound "audio/summermeadow.ogg" loop fadein 2.0
    #pause(1)   
    
    n "{i}In a matter of minutes, the waves disappeared, and the sea returned to its original calm, as though no storm had ever laid hands upon it.{/i}"
    
    n "{i}Scores of islanders had spilled from their houses to congregate around the pier.{/i}"

    pause(1)    
    scene reverend
    show ina pink neutral book open 
    with Dissolve(2.0)    
    #pause(1)    

    n "{i}Immediately I could discern the tall figure of reverend Kuyper — with his chalky white hair, that appeared to glow against the black of his cassock — standing with outstretched arms, as if to consecrate the weatherbeaten ship.{/i}"
    
    stop sound fadeout 5.0
    pause(1)
    "She read silently for a while."
    pause(1)
    show ina pink sympathetic book open with Dissolve(0.5)
    
    n "Thomas stayed at the manse, where the Kuyper family provided him with food and dry clothing after his dire journey. He describes reverend Kuyper as a dignified gentleman."
    n "And he makes special note of Johan's daughter, Hendrika — a charming, though secretive young woman, with flowing black hair."
    pause(1)
    n "Then it skips over to Sunday morning, when Thomas will attend his first service on the island."
    
    show ina pink neutral book open with Dissolve(0.5)
    
    n "{i}I attended Sunday service next morning. Observance proceeded in great solemnity, in commemoration of to two fishermen who were lost to the sea last week.{/i}"
    
    n "{i}The sermon contained many nautical themes — alluding to both the calling of the fishers and the beast Leviathan. However, I believe this to be nothing out of the ordinary for seafaring communities.{/i}"
    
    pause(1)
    
    n "On Monday morning the two men conversed together, delving deep into Kuyper's religious teachings."
    n "Let me skim through this part quickly."
    pause(1)    
    "After what felt like a century, Ina looked up at me and began reciting."
    pause(1)
    
    n "{i}What I have come to learn is worrisome.{/i}"
    n "{i}I can only conclude that Kuyper's theology in its essence lacks the eschatological underpinnings of our shared faith, substituting these core tenets with a view on historical redemption that is cyclical in nature.{/i}"
    
    #n "{i}Fundamental church doctrines that have  apocalyptic, are reinterpreted by Kuyper to allude to a type of eternal recurrence.{/i}"
    
    n "{i}For Kuyper, the New Testament culminates seamlessly into the book of Job, leading all of biblical history — including the synoptic gospels and the New Covenant — to recur again and again ad infinitum.{/i}"
    
    n "{i}Based on our conversation, I am inclined to agree with the complainant that the creed that is proclaimed on this island is fundamentally alien to the doctrinal axioms as set forth in the Canons of Dordt and the Heidelberg Catechism.{/i}"
    
    n "{i}I am even inclined to doubt Kuyper's world-view is fully Trinitarian.{/i}"
    
    #pause(1)
    play sound "audio/0sealapping.ogg" loop fadein 3.0
    scene beach 
    show ina pink neutral book open    
    with Dissolve(2.5)
    #pause(1)
    
    n "{i}After luncheon I recused myself for an afternoon walk, in order to meditate on our conversation.{/i}" 


    pause(1)    
    n "{i}As I made my way across the perimeter of the isle, looking out unto a glittering, endless sea, I couldn't help but notice that I was being trailed by a dark figure.{/i}"  
    
    show ina pink sympathetic book open with Dissolve(0.5)
    
    n "{i}I turned around, just in time to catch a glimpse of Hendrika leaping behind one of the gargantuan stones that lie scattered across the isle.{/i}"
    n "{i}I called out, asking if she would care to join me, but she let out a shrill laugh and ran away, with her black hair tailing behind her.{/i}"
    
    show ina pink grave book open with Dissolve(0.5)
    
    "Ina pulled a concerned face."
    #pause(1)
    stop sound fadeout 1.0
    scene bookcase
    show ina pink grave book open 
    with Dissolve(2.5)
    #pause(1)    
    
    n "That's strange. There isn't much more to the report."
    n "He skips over a few days, and then recounts a last meeting the two men had on Friday evening."
    
    n "{i}I am now confident to write that the reverend Kuyper and I have reached a mutual degree of understanding.{/i}"
    
    n "{i}Kuyper has further clarified his theological positions to me, and I am fully confident now that his doctrines are wholly in accordance with the three forms of unity — in no way contradicting our shared reformed confession.{/i}"
    show ina pink neutral book open with Dissolve(0.5)
    
    n "{i}I believe Kuyper is a fine man, who operates as a good shepherd for his congregation.{/i}"
    n "{i}Our prior misunderstandings appear to have derived from my own ignorance of local culture and customs — not from any fundamental unorthodoxy within the religious teachings of the Church of Abbot itself.{/i}"
    
    n "{i}In conclusion I therefore recommend that no punitive or expulsory action is taken against the reverend Kuyper or his congregation.{/i}"
    
    pause(1)
    
    "She put down the book."
    show ina pink neutral day open with Dissolve(1.0)
    #TODO lay down the book
    "That's strange."
    pause(1)
    
    #### Ina 4 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "Did you notice anything?"
        
        "I'm sorry, I wasn't listening.":
            show ina pink unhappy day open with Dissolve(0.5)
            n "Hmpf."
            
        "Sounds pretty tame if they got in trouble for this.": 
            $ ina_score += 1
            show ina pink dissapointed day open with Dissolve(0.5)
            n "It does, doesn't it? And the sudden change of tone at the end . . ."
    
    #####################################################################################################   
    
    pause(1)
    n "I don't understand. The sources state that the reformed church of Abbot was ejected based on this report, however the conclusion doesn't point in that direction at all."
    n "I have no idea why this would be cause for Abbot to be cast out of the presbytery."
    pause(1)
    n "This trip appears to have been a waste of time. Let's head back to the station."
    
    pause(1)
    scene archivesin_twi with Dissolve(0.5)    
    pause(1)
    
    "Lethargically, Ina went to return the book."
    "We were on our way to the exit when a figure approached us."
    
    pause(1)
    #TODO show clerk
    show archivist at left with Dissolve(0.5)
    c "Hey, it's cool you guys've taken an interest in those old pieces of ecclesiastical bookkeeping. As I said, they haven't been requested in decades. You must be history buffs, right?" #improve
    "Ina eyed him up suspiciously."
    show ina pink neutral day open at right with Dissolve(0.5)
    n "We're conducting investigative journalism into the church of Abbot."
    c "Abbot?"
    "He went silent for a while, as though trying to remember something."
    pause(1)
    c "I guess the report on them is pretty boring. "
    show ina pink unhappy day open at right with Dissolve(0.5)
    n "You wouldn't say—"
    "She pulled me by the sleeve, signaling that we should leave."
    pause(1)
    
    c "I remember there was more to that story though . . ."
    c "There should be an addendum somewhere, some notes that were left out of the public report." 
    show ina pink sincere day open at right with Dissolve(0.5)    
    "With this he appeared to have caught Ina's attention."
    pause(1)
    
    c "They're pretty rare though, I believe only two copies were ever printed."
    
    show ina pink smile day open at right with Dissolve(0.5)     
    
    n "And where may we find these copies?"
    
    c "Good question."
    
    hide archivist with Dissolve(0.5) 
    
    "He headed back to his desk, where he spent some time browsing the catalogue."
    
    pause(1)
    show archivist at left with Dissolve(0.5)
    
    "One is in the private library of the Council of Reformed Churches. You could try to petition them, however—"
    show ina pink unhappy day open at right with Dissolve(0.5)     
    n "And the other?"
    
    pause(1)
    
    c "The other was sent to the Isle of Abbot in 1857."
    c "The town had the right to know why their church was being ejected from the presbytery."
    c "If it hasn't been pruned from the collection, it should still be in the town archives."
    show ina pink smile day open at right with Dissolve(0.5)  
    n "Well that's all we needed to know, dear man. You could have saved us a lot of time by telling us this up front."
    hide ina with Dissolve(0.5)    
    "And with these words she was out the door."
    "I thanked him briefly before running after her."
    
    pause(1)
    hide archivist with Dissolve(0.5)
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene club with Dissolve(0.5)
    play sound "audio/citysounds.ogg" loop fadein 1.0
    pause(1)
    
    "On our way back to the station, we passed a small, indistinct-looking theater. Ina nudged me."
    
    show ina pink smile twi open with Dissolve(0.5)
    pause(1)
    
    n "Look, this is the nightclub I told you about. The one where the marquis was spotted."
    pause(1)
    n "It looks as grimy as ever."
      
    hide ina with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene viaduct_twi with Dissolve(0.5)
    play sound "audio/train.ogg" loop fadein 1.0
    pause(1)
    
    "We were just in time to catch the six-o-clock train."
    pause(1)
        
    "Throughout our return voyage I could hear Ina mumbling to herself in excitement."

    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p2c6:

    scene black with fade
    pause(1)
    scene villageroad with Dissolve(0.5)
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    pause(1)
    window show
    pause(1)
    
    "Saturday came. I set to work. Everything went noticeably smoother than last time — and I was struck by the sad realization that I must be becoming an experienced paper boy."
    
    pause(1)
    stop sound fadeout 1.0
    scene sittingroom_eve with Dissolve(0.5)
    play sound "audio/clock.ogg" loop
    pause(1)
    
    "When my work day ended I returned home for a shower and a change of clothes, after which I briefly spoke with my dad."
    "I brought up how he hadn't been home much lately, but he told me not to exaggerate. That it was actually {i}I{/i} who was away all the time."
    "Though I doubted that was the case, I sensed there was little point in arguing."   

    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene restaurant with fade
    pause(1)
    window show
    play music "<from 40.0>audio/violinaminor.ogg" loop fadein 8.0 #is it ok?
    pause(1)
        
    "When I arrived at {i}Omophagia{/i} — one of the few licensed establishments in town — Rika sat waiting on me." #a small pseudo-Italian restaurant, 
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)
    ##start off with some small talk, maybe ansjovis, maybe leviathan
    ##TODO talk a bit about Mei!!!
    #pause(1)
    
    r "Are you hungry? We should order some side-dishes. The fresh anchovies here are excellent. "
    
    "I nodded in agreement."
    
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5) #TODO experiment with lowering sitting characters
    pause(1)    
    
    "As I settled in, Rika sat staring at me — beaming in playful anticipation. She let out a restrained cough."
    
    pause(1)
        
    r "So I heard you've been hanging out with Mei again."
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)    
    a "Your spies are doing excellent work."
    
    "She laughed."
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    r "Oh no, it's not like that this time. Mei told me herself — in fact, she hasn't stopped talking about you since last Tuesday."
    r "Your misadventures among the megaliths and such—"
    "Gently, she had begun brushing her fingers through her onyx hair — and the subtle, repetitive motions exuded a soothing calm, as though she were comforting a frightened creature."
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    r "—and, you know, I think that may not be so bad. It's good for her to have someone, to converse with on her level."
    
    a "What do you mean with {i}on her level{/i}?"
    "She giggled."
    r "Oh, don't take it the wrong way. It's just that Mei's always been a bit of a loner."
    r "Because she never attended regular school, she hasn't had the chance to make friends among her peers. "
    r "But for you, as an outsider, it should be the same."
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)    
    r "Just let me know if she becomes a burden, okay?"
    pause(1)
    "I nodded, not really sure if that point had already been reached."
    pause(1)
    
    r "But tell me, how did your work day go? No big headline this week?"
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    
    "I tried to feign offense at her statement."
    a "How dare you say such a thing?! Didn't you read our exclusive report on the {i}idiosyncratic{/i} migration patterns of the hairy hawker dragonfly?"
    r "I will, I will—"
    #change expression"
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)   
    
    "She turned her attention towards the laminated menu card, her bottom lip pouting in disinterest. The restaurant wasn't anything fancy. Italian in name only."
    show rika dress sad day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)   
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)       
    r "Don't think that headline will cause any trouble this time."
    "She looked up at me."
    
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)
    
    r "And that's good. We don't want trouble down here."
    
    pause(1)
    
    r "That girl Ina. She really attracts trouble, you know?"
    r "I feel like she seeks it out at times."
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    r "We have a gentleman in town who caused an embarrassment last year. Ina, of course, wrote all about it."
    
    "She flapped her hand rapidly, as if shaking off a disgusting substance."
    r "To think he considers himself {i}nobility{/i} . . ."
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)    
    a "Nobility?"
    a "You wouldn't be referring to the Marquis, would you?"
    
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)    
    
    r "Oh my, Ina has been mentoring you {i}very{/i} well."
    
    r "The current Lord of the Isle is quite the character indeed. Though I wouldn't say he deserves his title."
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    
    r "From the late middle ages onward his clan ruled the island."
    r "They owned most of the land over here, but only to collect taxes. They lived on the mainland, on a large estate near The Hague. "
    
    r "And to finance their lavish lifestyle among the nation's elite, they leeched on the poor fishers and clergymen of Abbot."
    r "But the lords never contributed anything of substance."
        
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)   
    "She smiled."
    
    r "You can imagine how distraught they were when the decision fell to evacuate in 1857. With the fishers leaving Abbot, there was no source of income left."
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)    
    "The waitress came to bring us our side dishes. "
    r "To stay out of poverty, the clan sold about half the island to the Church of Abbot — whose members would remain on the isle."
    r "Their glory days were indisputably over. They had to live frugally in their castle, which began to crumble from neglect— "

    
    #pause(1)
    scene restaurant_nig 
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) 
    with Dissolve(1.0)
    #pause(1)
    
    r "Things changed though, after the reclamation."
    
    show rika dress sad day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    pause(1)
    
    r "In 1947, when the Marshpolder fell dry, marquis Louis of Abbot was one of the first to return to Abbotsford — to lay claim on the part of the island that his family was still legally entitled to."
    
    r "Louis played an important role in developing Abbotsford in the twentieth century. It was in his interest that the housing prices rose, so that his family could collect rent again."
    
    r "He turned Abbotsford into a major agrarian hub, inviting farmers from all over the low countries to move here."
    r "He had a little boy with him at the time. Young Leopold. A spoiled brat, even at that age."
    
    "She paused for a second, to move the plate of fish in my direction."
    show rika dress sad day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    
    a "I can imagine the native population wasn't too happy with that—"
    
    r "They weren't. Initially there was lots of strife. As more and more farmers arrived, the newcomers began to outnumber the original islanders."
    
    show rika dress sad day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)
    
    r "Now politically, A.I.R had always maintained complete control of the town council. The islanders feared that the farmers would form their own political movement that would be able to seize power."
    
    pause(1)
    
    a "So how did that work out?"

    pause(1)
    
    r "Well, it wasn't all bad. Since the evacuation, the church was the second largest landowner on the isle. The inflated housing prices were good for us too."
    
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)   
    pause(1)
    
    r "In the end marquis Louis played an important role in reconciling the two sides. The agrarians were welcomed within A.I.R, as long as they agreed not to occupy more than half the seats in the council. "
    
    r "This meant the church would retain control on the state of affairs of the island, while the newcomers still felt represented."
    pause(1)
    a "So is that how the two factions within the town council arose?"
    
    r "A.I.R. doesn't have factions. All politicians operate in the best interest of the community."
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)   
    "She winked."
    r "Except for Leopold, of course. He's a blemish on our town." #TODO used this before!
    pause(1)
    r "I wouldn't mind you writing another article on him. Let me know if you need more information."
    show rika dress happy day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)      
    "I was beginning to realize that her loose tongue didn't necessarily stem from the wine or the amicable atmosphere."
    "It was as though the information she was disclosing was being carefully measured out."
    
    "We sat in silence, eating fish, while it gradually grew darker outside."
    "Then she gently wiped her mouth on her napkin and looked up at me."
    
    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)       
    pause(1)
    

        
    #### Rika 4 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "Is there anything else you'd like to know?"
        
        "Not really.":    
            show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)         
            "She chuckled."
            r "Why else would Ina send you on a date with me?"
            "I could feel the blood rush to my head."
            
        "Is there anything else you'd like to {i}tell{/i} me?": 
            $ rika_score += 1   
            show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5) 

            r "Oh plenty. It's just that I like to stay one step ahead of Ina's games."
            "While I was surprised at her sudden change in manner, I managed to remain collected."
    
    #####################################################################################################    
    
        
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.5)       
    pause(1)
    r "It's getting very late. I have to be in church tomorrow by 9 AM."
        
    "She smiled a faraway smile."
    pause(1)
    r "Can you imagine what it's like?"
    r "A reclamation like that? Can you imagine how it would feel?"
    r "You've been living your whole life on a secluded island — and then suddenly you witness the waters drop around you, until all that's left is an endless wasteland of stinking marshes."
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    
    r "The people here had spent their lives in the midst of a majestic sea. But in a period of less than a year, all of that was reduced to a swamp, strewn with decaying fish corpses."
    
    "I stared at her in silence."
    pause(1)
    r "There have always been higher powers that decided over the people of Abbot. Be it the lords, the national government, the presbytery of churches—"
    
    r "—but through their inhumane treatment of the islanders, they have sown the vines from which grapes of wrath would grow."
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    
    r "It left them feeling futile and angry. Helpless against the forces that be."
    pause(1)
    "She sighed."
    
    pause(1)
    
    r "For some reason it strengthened their faith. They realized they had to rely on a far higher power to deliver them from these tyrannical Pharaohs."
    
    r "The native inhabitants of Abbot truly feel they are God's people."
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2) 
    
    "Without asking, she impaled the last of the fish on her fork, bringing it to her mouth in one motion. After swallowing, she resumed her monologue."
    
    pause(1)
    
    r "During the reclamation, as the workmen built the long embankment that would keep the water out, incidentally strange reports would emerge."
    
    "I looked up from my drink."
    pause(1)
    
    r "The men would experience an impromptu storm, a sudden succession of roaring eddies that inhibited work for as long as they persisted."
    
    r "The thing was, these storms were highly localized. They would even occur on the most tranquil of days, when there wasn't a gust of wind in the air."
    
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    
    r "I think they ascribed the phenomenon to ocean currents, sent wayward by the altered flow of the great rivers."
    
    r "However, that doesn't sound at all like what these workmen described. They spoke about raging tempests and huge waves."
    
    "She took out her purse and placed a fifty on the table."
    show rika dress mischievous day closed at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)  
    show rika dress mischievous day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.55, yanchor=0.5) with Dissolve(0.2)      
    r "Anyway, I has a great time. Abe."
    
    r "I'd love to do this again."
    
    "I thanked her and told her I felt the same way. Then I reached for my wallet to pay for my share of the meal."
    
    r "Save your hard-earned money. My father said he'd cover the tab. "
    
    "I grumbled appreciatively."
    
    hide rika with Dissolve(1.0)
    
    pause(1)
    window hide
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p2c7:

    scene black with fade
    pause(1)
    play sound "audio/ventilator.ogg" loop fadein 1.0
    scene blueroom_nig with Dissolve(0.5) #maybe crop this image? set hands on the clock!
    play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)
    #TODO ticking sound?

    "I was awoken at nine by church bells, after which I fell back asleep until I was awoken for a second time by the bells for the noon service."
    pause(1)
    "For a brief moment my heart went out to Rika Kuyper — who was likely expected to be present and presentable for all of today's services — until I dozed off yet again, to be awoken, conclusively this time, by a mysterious ticking against my bedroom window."
    stop music fadeout 4.0
    pause(1)
    "When I made it out of bed to open the curtains, I could see Mei standing outside, dressed head to toe in immaculate black."
    
    pause(1)
    stop sound fadeout 1.0
    play music "audio/walkure_wintersturme.ogg" loop fadein 16.0
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene residential with Dissolve(0.5)
    pause(1)
    show mei black estatic day open at right with Dissolve(0.5)

    pause(1)
    #TODO add sound
    
    #could have her break a window for the lulz. #have her wear black shirt with waistcoat (or jersey)"
    m "She told me! Rika finally told me!"
    m "I poked and pestered her throughout the service, until she finally agreed to give me your address. I think she was embarrassed in front of the congregation."
    show mei black estatic day closed at right with Dissolve(0.2)
    show mei black estatic day open at right with Dissolve(0.2)
    m "You sure like to sleep late—"
    m "I tried throwing stones at each of the windows. Isn't your father home?"
    "I grumbled a reply, still half asleep."
    pause(1)
    
    m "Come on, it's Sunday afternoon! Let's go on an adventure!"
    m "Have you had lunch yet? Don't worry, I took some peppermints from church."
    show mei black estatic day closed at right with Dissolve(0.2)
    show mei black estatic day open at right with Dissolve(0.2)
    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    scene villageroad with Dissolve(0.5)
    pause(1)
    
    "In my groggy state I tailed Mei through deserted streets."
    pause(1)
    "From her determined gait, I could tell she was leading me somewhere — it wasn't long before we left our drab suburban estate behind to enter a patch of brushwood that bordered the village."
    
    pause(1)
    scene woods with Dissolve(0.5) 
    pause(1)
    show mei black understanding day open at right with Dissolve(0.5)
    
    "She stopped for a second to hand me some mints. They stood out chalky white against her jet-black dress."
    pause(1)   
    
    a "So what's with the depressing outfit? You had a funeral this morning?"
    
    show mei black understanding day closed at right with Dissolve(0.2)
    show mei black understanding day open at right with Dissolve(0.2)
    
    m "Oh no. We always dress in black for church. If there'd been a funeral, they'd make me wear a veil."
        
    "Giggling, she placed a mint in her mouth and took off again."
    
    hide mei with Dissolve(0.5)
    stop sound fadeout 1.0
    pause(1)
    scene sky_blue with Dissolve(0.5)
    play sound "audio/edgemeadow.ogg" loop fadein 3.0
    pause(1)
    
    "On the other side of the trees lay a rolling meadow."
    "It wasn't far beyond here that the landscape made a sudden, steep drop into the endless stretches of farmland formed by the remnants the former seabed."
    pause(1)
    
    m "Hurry up!"
    
    "I could barely make out her golden hair in the blinding autumn sun."
    
    "It wasn't much later that we reached what appeared to be the destination of our journey."
    
    pause(1)
    scene gravemound with Dissolve(0.5)
    pause(1)
    show mei black understanding day open at right with Dissolve(0.5)
    pause(1)
    
    a "You've led me to a pile of stones again."
    show mei black understanding day closed at right with Dissolve(0.2)
    show mei black understanding day open at right with Dissolve(0.2)
    
    m "Not just stones! A dolmen! Can't you tell by the way they're stacked?"
    "Though smaller than the megaliths she'd shown me last week, the stones had indeed been arranged to form a tiny abode."
  
    "Excitedly, she pulled my hand."
    show mei black surprised day open at right with Dissolve(0.5)     
    m "Look! S! An S!"
    show mei black understanding day open at right with Dissolve(0.5)    
    
    #### Mei 3 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        "She was pointing at a crude s-shaped pictogram, engraved into the surface of one of the rocks."
        
        "It {i}does{/i} look like an S.":
            $ mei_score += 1        
            show mei black happy day closed at right with Dissolve(0.5)
            m "Doesn't it?"
            
        "Abbotford's spelling ace is at it again.": 
            show mei black annoyed day closed at right with Dissolve(0.5)   
            m "Don't tease me like that."
    
    #####################################################################################################
    
    pause(1)
    show mei black happy day closed at right with Dissolve(0.5)      
    
    "Figuring Mei had brought me here as her personal translator, I walked over to the obligatory tourist sign that stood a few yards from the archaeological site."
    pause(1)
    
    a "{i}Dolmen M4, commonly referred to as the S Dolmen. Likely built as a megalithic tomb by members of the Swifterbant culture. Dated around 3500 BC.{/i}"
    
    "I skimmed over some further text." #TODO overused term?
    #pause(1)
    
    a "{i}A salient feature of M4 is the s-shaped petroglyph engraved on its southeastern side.{/i}"
    a "{i}Though resembling the letter s, it was carved long before the emergence of the proto-sinaitic alphabet. This rune likely depicts a house-mark, a type of symbol that was used to identify clans during the late neolithic.{/i}"
    a "{i}Though the discovery of petroglyphs inside megalithic tombs from this period is not uncommon, the prominent placement of this s-shaped rune on this dolmen's outer exterior is unique in the low countries.{/i}"
    
    pause(1)
    show mei black sad day open at right with Dissolve(0.5)       
    
    "Mei stood there, slinking down in disappointment."
    pause(1)
    
    m "So the S is not an S?"
    
    "I read on."
    pause(1)
    
    a "These stones stood quite close to the shore, when this was still an island."
    a "Did you know Abbotsford used to be an island?"
    stop music fadeout 3.0    
    m "No. "   
    "She was looking at me, all glassy-eyed."
    pause(1)
    
    a "You didn't know? What do these people teach you?"
    pause(1)
    m "No—"
    pause(1)
    
    m "Not an island— Abbot was connected to the mainland once—"

    "Her voice was no more than a whisper."

    a "Huh?"
    
    play music "audio/haunting.ogg" loop fadein 18.0 #"audio/haunting.ogg"
    show mei black white happy open at right with Dissolve(1.5) #TODO
    
    "And before I knew it, her eyes had turned a cloudy pearl."
    "She had drifted off, a faint smile lingering on her face."
    pause(1)
    
    m "{i}We were playing here on the beach, Sigurd and I.{/i}"
    pause(1)
    m "{i}I had four younger brothers, but three of them died in infancy.{/i}"
    m "{i}Sigurd survived, though.{/i}"
    m "{i}Sigurd was the strongest.{/i}"
    pause(1)
    m "{i}We dragged a fallen tree far into the water, that day, to pretend it was a sea-monster.{/i}"
    m "{i}I already knew he would be leaving soon.{/i}"
    pause(1)
    m "{i}I remember his hair, how it shone bright in the sun on that last summer day—{/i}"

    show mei black white sad open at right with Dissolve(0.5)  #TODO
    #TODO mei white eyes, frown
    pause(1)
    "Her expression darkened."
    pause(1)
    m "{i}Sigurd — I prayed so long for your return.{/i}"
    m "{i}I would pray here, by the stones—{/i}"
    m "{i}—I prayed to the chthonic gods, who dwell through the immeasurable depths of the earth—{/i}"
    m "{i}Sigurd was sent away to live with an allied tribe.{/i}"
    m "{i}It was a ritual we'd preform—{/i}"
    m "{i}—whenever an eldest son turned seven.{/i}"
    m "{i}It was meant to strengthen regional bonds, and to prevent—{/i}"
    pause(1)
    m "{i}—to prevent {/i}madness."
    show mei black white crying open at right with Dissolve(0.5)  #TODO
    #TODO mei white eyes, crying
    pause(1)
    
    m "{i}Sigurd—{/i}" 
    pause(1)
    
    "After that, Mei remained silent for a very long time. It wasn't until the sun began to set that the color in her eyes returned."
    
    stop music fadeout 6.0
    scene gravemound_twi #is mei ok color?
    show mei black crying twi open at right 
    with Dissolve(1.5)
    
    "During that moment she looked vulnerable, helpless, as though she couldn't begin to fathom the intricacies of the episode — that mysterious absence that had come over her."
    "I helped her to her feet, supporting her as we slowly, wordlessly, commenced our journey home."
    
    pause(1)
    hide mei with Dissolve(1.0)
    pause(1)
    scene woodpath_twi with Dissolve(0.5)
    pause(1)
    
    "Not looking to run into anyone in town, we took the long route back, around the perimeter of the former island."
    "After a while, I became aware of Mei's gentle humming in my ear, and by the time we had made it to her parents' farm, she appeared to have returned to good spirits."
    
    scene meifarm with Dissolve(0.5)
    pause(1)
    
    show mei black understanding twi closed at right with Dissolve(0.5)  #TODO#TODO, normal eye color, slow transition
    
    m "Thank you for bringing me home, Abe. I had a great time at the shore."
    
    "Though I was caught off guard, I was happy to see she had regained her former cheer."
    pause(1)
    
    m "Do you want to come to the lake with me some day? The water should still be warm. Like summer."
    
    "She appeared almost drunk with fatigue."

    show mei black understanding twi open at right with Dissolve(0.5)     
    m "Will you come with me?"
    m "Abe?"
    show mei black understanding twi closed at right with Dissolve(0.2)   
    show mei black understanding twi open at right with Dissolve(0.2) 
    m "The lake is so big, like an ocean almost."
    pause(1)
    
    #### Mei 4 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        "Will you come with me?"
        
        "I'd love to.":
            $ mei_score += 1        
            show mei black happy day closed at right with Dissolve(0.5)
            m "Thank you—"
            play audio "audio/1mysterychord2.ogg"
            #pause(1)
            m "—{i}Sigurd!{/i}"
    
        "It's really time to get you to bed.": 
            show mei black understanding day closed at right with Dissolve(0.5)
            "She smiled a drowsy smile."

    #####################################################################################################
    
    pause(1)
    "Cheerfully I bade her goodbye and headed back towards town."
    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    
    pause(1)

label p2c8:

    ##################################
    image mainstreet_animated:
        "backgrounds/villageroad_red.png" with Dissolve(0.6)
        pause 0.6
        "backgrounds/villageroad_blue.png" with Dissolve(0.6)
        pause 0.6
        repeat
    ##################################
    
    scene black with fade
    play sound "audio/firesirens.ogg" loop fadein 12.0
    window show
    pause(1)
    "Police sirens swelled in the distance as I drew closer to Abbotsford."
    pause(1)
    scene mainstreet_animated with Dissolve(2.0)
    pause(1)
    "I followed them into Main Street, where I was nearly knocked down by a small, dark figure."
    
    show ina pink sincere nig hair at center with Dissolve(0.5) 
    
    n "There you are! Finally! We need as many reporters at the scene as possible!"
    a "S-scene?"
    show ina pink dissapointed nig hair at center with Dissolve(0.5)     
    n "Didn't you read my messages? There's been an attack on Karin Voorhees!"
    pause(1)
    window hide
    stop sound fadeout 7.0
    scene black with Dissolve(1.0)
    pause(1)
    #####################################################################################################
    if rika_score > 2:
        show prog_rika p at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    elif rika_score == 2:
        show prog_rika n at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    else:
        show prog_rika d at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
        
    pause(0.25)
    
    if ina_score > 2:
        show prog_ina p at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
    elif ina_score == 2:
        show prog_ina n at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright  
    else:
        show prog_ina d at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
        
    pause(0.25)
    
    if mei_score > 2:
        show prog_mei p at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    elif mei_score == 2:    
        show prog_mei n at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    else:
        show prog_mei d at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    
    
    #####################################################################################################
    pause(2)
    hide prog_rika with easeoutleft
    pause(0.25)
    hide prog_ina with easeoutleft
    pause(0.25)
    hide prog_mei with easeoutleft
    
    
    pause(1)

###########################################################
#### PART 3 ###############################################
###########################################################


    pause(1)
    window hide
    stop music fadeout 1.0
    scene black with fade
    pause(1)

       
label p3c1:

    play sound "audio/officesound.ogg" loop fadein 1.0 #TODO, improve BGS?
    scene white with Dissolve(1.0)
    pause(1)
    scene part3_title1 with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)

    scene white with Dissolve(0.5)
    pause(1)
    play music "audio/0andantino20.ogg" loop fadein 16.0
    scene inabedroom_eve with Dissolve(1.0) #TODO is eve ok?

    pause(1)
    window show


    pause(1)

    a "Rise and shine!"
    pause(1)
    show ina cami neutral day open at center with Dissolve(0.5)
    pause(1)
    a "Have you slept at all tonight?"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    n "Hmpf."
    pause(1)

    
    "She looked exhausted."
    "I had spent the previous night by her side, assisting her as she darted around the police perimeter—"    
    "—snapping pictures and throwing questions at the forensic investigators that poured in and out of Karin's residence."    
    "The officers, however, were reluctant to discuss the case."
    "It wasn't until 2 AM — when most of the police had left the scene — that I could finally convince her to go home."
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    
    "But even there she remained restless, immediately setting to work on a laborious feature article covering the case."
    
    "And though {i}she{/i} appeared sharper than ever, tirelessly paging through her notebook, making phone calls, transcribing audio recordings she'd made—"
    "—I myself was fully depleted. Hence it wasn't long before I collapsed onto the couch."
    
    pause(1)    
    a "Well {i}I'm{/i} making eggs."
    a "I haven't had a solid meal in days."

    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    n "Do as you wish. I'm going to call the police station again."
    #pause(1)
    a "If you really think they'll answer—"
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    
    n "An attack on a politician — in Abbotsford, of all places." #a place like this
    #pause(1)
    n "It does make me wonder—"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    a "What?"
    #pause(1)
    n "—if this could be linked to the interview you conducted with Karin last week."
    a "Please don't bring {i}me{/i} into this."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)
    n "It's like someone wanted to silence her—"
    
    show ina cami astonished day open at center with Dissolve(0.5)

    n "We've been receiving warnings, you know?"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami astonished day open at center with Dissolve(0.2)
    a "We?"
    
    #pause(1)
    
    n "I have. The paper."
    n "I found one again, last week. After we reported on the farmhouse case."
    n "It was a very short message, sent from an anonymous e-mail address."
    
    n "{i}Sad to hear your office burned down{/i} — is what it said."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami astonished day open at center with Dissolve(0.2) 
    a "Did our office burn down?!"
    show ina cami neutral day open at center with Dissolve(0.5)
    n "No, you dimwit! It was a {i}threat!{/i}"
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    
    a "Why didn't you tell me before?"
    "For a second her eyes turned distant. She had begun fidgeting with the fabric of her bedsheets." #TODO effect?
    pause(1)
    n "I dismissed it as a prank at the time." 
    show ina cami smart day open at center with Dissolve(0.5) 
    n "I'm {i}still{/i} sure it's a prank, you know—"
    n "Don't worry."
    show ina cami smile day closed at center with Dissolve(0.2)
    show ina cami smart day open at center with Dissolve(0.2)  
    "Ina spoke with the resigned apathy of a war correspondent, who had stared into far greater peril."

       
    pause(1)
    #n "But let's get back to the matter at hand."
    #pause(1)
    a "So do you have {i}any{/i} idea who planned the attack on Karin?" #meh

    pause(1)
    "For a long time she was silent."
    pause(1)
    show ina cami smile day closed at center with Dissolve(0.2)
    show ina cami smart day open at center with Dissolve(0.2)      
    
    n "No, not really—"
    #pause(1)
    a "What about the mayor and his brother?"
    show ina cami neutral day open at center with Dissolve(0.5)   
    a "They've been brought up a few times—"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)       
    "An involuntary contraction flashed across her eyes."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)      
 
    
    n "The mayor's brother?"
    pause(1)
    n "There certainly have been rumors concerning him—"
    n "After our latest article resparked interest in the murder case, he was at the center of suspicion again."
    n "It's a small town, people gossip a lot."
    show ina cami neutral day open at center with hpunch
    
    "She shuddered."
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)   
    
    n "George Van Linden. A scary guy."
    pause(0.5)
    n "When we were younger, we'd tell stories about {i}Grumpy George{/i}."
    n "He was known for igniting in furious rage whenever someone came on his property."
    #Grouchy, Ghastly, Gruesome, Ghost, Godforsaken, Geriatric, Goony, Gangster, Gross, Gory, Grim, Gawky, Ghoulish, Glum, Gnarly, Grating, Grimy, Growling, Grotesque, Gruff, Grumbling, Grumpy, Grimy, Grueling, Grubby,
      
    n "There was even a time—"
    show ina cami astonished day open at center with Dissolve(0.2) 
    "She stopped abruptly, swallowing her words."
    pause(1)
    
    n "Never mind—"
    n "But I'm sure he's the kind op person that could coldly eliminate someone who got in his way."
    n "It chills me — that someone like him holds so much power in a town like this."
    show ina cami neutral day open at center with Dissolve(0.5)  
    n "The thing is, we don't have any {i}evidence{/i}—"    
    pause(0.5)
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)      
    
    n "George Van Linden. You should see him — there's a disquieting shimmer his eyes. "
    
    n "A slight squint that, though barely noticeable at first, somehow warps his entire face into an expression I could only describe as being— {i}detached{/i}."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)      
        
    n "It impacts his every feature. The curt, rude way in which he speaks. His disheveled movements. His acute outbursts of aggressive rage—"
    
    n "—but these are only the external symptoms of an underlying decay."
    
    n "The {i}true{/i} cause for his demeanor must come from a place far deeper inside. "
    

    "She paused, as though carefully measuring out the following sentence."
    
    pause(1)
    
    n "That strange look in his eyes, it's so unmistakably crucial to his whole persona—"
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    #that it goes beyond a mere isolated facial deformity. 
    n "—that it almost feels like it's a characteristic of a certain physiological type, that's slowly emerging from within him."
    
    "Ina was becoming increasingly grave, bringing down her voice to a level barely within the audible range."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)     
    
    n "That behavior. I don't think it can be explained as a primitive attribute of the uncivilized mind."
    n "No — quite the opposite."
    n "We can see his type all around — in our neighbors, in random passers-by. Even in politicians and world leaders—"
    
    "I could barely make out her tired whispers."
    pause(1)
    
    n "The short temper, the decadency — these are all qualities of the {i}future{/i} man."
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
       
    
    "She stared at me in silence, as though she had just divulged something of the greatest significance."
    "And though I didn't fully understand the thoughts Ina was trying to convey that morning — I was stricken by the seriousness that had come over her, as it was unlike anything she had previously subjected me to." #It was as though she were dictating a hermetic treatise." #revisit    
    
    pause(1)
    
    "Then she took out her phone."
    show ina cami pretty day open at center with Dissolve(0.5) 
    n "I'm sorry—"
    play audio "audio/dialing.ogg" fadein 6.0
    n "Go cook your eggs. I need to make a few calls."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    scene diningroom_day with Dissolve(1.0)    
    pause(1)
    
    "And as I switched on the stove, I could hear her calling out to me from the bedroom:"
    
    n "Oh and Abe! Please ask Rika to take you to the council library!"
    n "I'm still interested in that appendix document that they keep there!"


    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p3c2:

    scene black with fade
    pause(1)
    play sound "audio/officesound.ogg" loop fadein 3.0
    play audio "audio/schoolbell.ogg"
    scene bluehall with Dissolve(0.5)
    pause(1)
    window show
    pause(1)


    ## school hall? #rika in uniform

    "I went looking for Rika as soon as classes ended."
    
    "It didn't take me long to find her, hurrying through the hallway at a steady pace." 
    
    pause(1)
    play music "audio/0goldberg28.ogg" loop fadein 5.0
    show rika uni happy day closed at center with Dissolve(0.5) 
    pause(1)
    
    a "Hey Rika, {i}what's cookin'{/i}."
    
    "She chortled."
    pause(1)
        
    r "I'm on my way to the pool."
    r "We're running double training sessions up until the regional championships next month."
    show rika uni happy day open at center with Dissolve(0.2)  
    "She brushed aside her hair."
    show rika uni happy day closed at center with Dissolve(0.2)  
    show rika uni happy day open at center with Dissolve(0.2)     
    r "You can walk with me if you like." #I want to ask you something."
    #"Then her expression soured"
    
    show rika uni sad day open at center with Dissolve(0.5) 
    "And just as she was about to continue onwards, she faltered, as though she'd just remembered something."
    pause(1)
    
    r "So— You must be preparing for your big trip."

    "I stared at her in confusion."
    
    show rika uni sad day closed at center with Dissolve(0.2)  
    show rika uni sad day open at center with Dissolve(0.2)        
    
    r "Mei told me you'd be taking her to the beach sometime soon."
    r "You should have come to {i}me{/i} first."
    show rika uni sad day closed at center with Dissolve(0.2)  
    show rika uni sad day open at center with Dissolve(0.2)  
    
    #pause(1)
    
    #### Rika 5 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        "I thought back to Sunday evening — and the words Mei had drowsily muttered into my ear."
        
        "I don't see how this is any of your business.":                
            show rika uni unhappy day open at center with Dissolve(0.5) 
            r "I have a good mind to report you to the authorities."
            r "It speaks volumes of your character, this attempt to take advantage of a vulnerable young woman."
            
        "It was just a wild idea of hers—": 
            $ rika_score += 1  
            show rika uni sad day closed at center with Dissolve(0.2)  
            show rika uni sad day open at center with Dissolve(0.2)     
            r "I don't care."
    
    #####################################################################################################
       
    r "We've been very tolerant of your little outings with Mei up until now."
    r "But if you're going to take her out of town, I {i}insist{/i} she be accompanied by a chaperone—"
    "Her eyes were like hellfire."
    pause(1)
    
    a "I guess you have someone in mind?"
    r "—for an unwed girl, to go on private beach outings with a man."
    r "I have my reservations about the whole situation—"
    show rika uni sad day closed at center with Dissolve(0.2)  
    show rika uni sad day open at center with Dissolve(0.2) 
    a "I haven't promised her anything, we could just cancel—"
    show rika uni happy day closed at center with Dissolve(0.5)     
    r "—however, as I feel Mei is due for an excursion, and as I have some business of my own to attend to in Ryebury, I'm willing to accompany the two of you."
    a "{i}Accompany{/i} us?"
    show rika uni happy day open at center with Dissolve(0.5)      
    r "Sure. Or will my presence {i}ruin{/i} the little plan you had in mind?"
    a "Not at all—"

    show rika uni happy day closed at center with Dissolve(0.2)    
    show rika uni happy day open at center with Dissolve(0.2)    
    
    r "Fine then, I've already made arrangements."
    r "Classes end early this coming Thursday, so we can leave after school and be back before midnight."
    r "I'm sure we'll have a blast." 
    pause(1)
    
    hide rika with Dissolve(0.5)
    pause(1)
    scene pool with Dissolve(0.5)
    pause(1)
    
    
    ## at swimming pool
    "When we arrived at the pool, I was still somewhat taken aback by Rika's sudden takeover of the occasion."
    "But then I remembered my initial motivation for approaching her."
    
    pause(1)
    show rika uni happy day open at center with Dissolve(0.5)  
    pause(1)
    
    a "Hey Rika. Before I leave, I was wondering—"
    a "There's something I need from the town council library."
    
    show rika uni happy day closed at center with Dissolve(0.2)    
    show rika uni mischievous day open at center with Dissolve(0.2)      
    
    "She tilted her head, a curious expression forming on her face."
    
    r "From the council library? "
    a "Could you get me in? It isn't usually open to the public."
    show rika uni mischievous day closed at center with Dissolve(0.2)    
    show rika uni mischievous day open at center with Dissolve(0.2)       
    r "What would you {i}ever{/i} need from there."
    a "Oh, just some old records. It's something for a history assignment. "
    a "And I figure you owe me a favor, considering how I'm letting you come on this beach trip."
    
    show rika uni mischievous day closed at center with Dissolve(0.2)  
    
    r "Well I {i}could{/i} get you in, though we'd have to go soon. They are tightening security protocols after the whole attack on miss Voorhees."
    r "Did you hear about that?"
    a "I did."
    show rika uni mischievous day open at center with Dissolve(0.2)  
    r "We'll go this afternoon, after I'm done with my workout."
    r "Please meet me outside the council building in about an hour."
    
    pause(1)
    hide rika with Dissolve(0.5)
    stop music fadeout 4.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p3c3:

    scene black with fade
    pause(1)
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    scene council with Dissolve(0.5)
    pause(1)
    window show
    pause(1)


    ## Shot of City Council outside #Rika in blue/red dress.

    "I was met with the fresh scent of chlorine, emanating from her hair."
    pause(1)
    show rika uni happy day closed at center with Dissolve(0.5)  
    play music "audio/0goldberg15.ogg" loop fadein 2.0
    pause(1)
    r "There you are, let's get going."
    r "I have to be home in time for dinner."
    
    ## Shot of City Council entryway 
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)    
    scene council_entrance with Dissolve(0.5)
    stop sound fadeout 5.0
    pause(1)
    
    "The entrance to the council building was rather sophisticated for a country town. "
    "Rika immediately went over to the receptionist — with whom she seemed to be on friendly terms — and received a small copper key, which she pocketed quietly. "
    
    ## scene of backrooms two doors
    pause(1)
    scene council_hall with Dissolve(0.5)
    pause(1)
    
    "We were let through to the back rooms without issue. Wordlessly, Rika unlocked a nondescript door and led me in."
    
    ##In the City Council library, after Rika has left
    pause(1)
    scene council_library with fade
    pause(1)
    show rika uni happy day open at center with Dissolve(0.5)
    pause(1)
    
    r "Please don't get your hopes up. The municipal collection isn't actively curated."
    r "It's just a heap of whatever books the town gets their hands on."
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)      
    "I began to browse the shelves, which appeared to have been crammed full without any system or catalogue."
    pause(1)
    r "I'll help you. What title are you looking for?"
    
    "Though it was an obvious question, it caught me completely off guard. "
    
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)    
    
    a "Eh—"
    pause(1)
    r "Well?"
    r "Don't tell me you've forgotten? "
    a "Forgotten, yes, I mean—"
        
    #### Rika 6 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        "Can you at least tell me the name of the author?"
        
        "I'm sorry, I really have no clue.": 
            show rika uni unhappy day open at center with Dissolve(0.5)         
            "Considering the circumstances, I didn't want to reveal what book I was looking for."
            "Clearly, this was an unforeseen flaw in my plan."
            pause(1)
            r "You're looking for a book, of which you don't even know the name or author?"
            r "That's very foolish of you, Abe."
            show rika uni sad day open at center with Dissolve(0.5)
            r "Foolish— and a little {i}suspicious{/i}."
            pause(1)
            r "Anyway, thanks for wasting my time."
            r "I have to leave now, I'll tell the receptionist you'll be following shortly."    
            
            
        "I believe he was called, eh— Spangler?": 
            $ rika_score += 1  
                
            show rika uni happy day closed at center with Dissolve(0.2)
            show rika uni happy day open at center with Dissolve(0.2)  
            "I'd thrown out the first name that came to mind. But it seemed to appease Rika."   
            show rika uni happy day open at center with Dissolve(0.5)    
            r "{i}Spangler?{/i} Hmm."
            r "Never heard of him."

            hide rika with Dissolve(0.5)
            pause(1)    
            "We searched silently for a while."
            "I scanned the shelves one by one, paying special attention to any publication that appeared over a hundred years old. "
            
            ##maybe have Rika find something funny."
            "As time passed by, I could sense Rika growing increasingly restless."
            pause(1)
            r "{i}Zoning Restrictions on the Construction of Prefabricated Cupolas, Third Revision.{/i}"
            r "{i}Annual Report of Home-Owners Association \"The Gilded Bulrush\".{/i}"
            r "The amount of junk they keep here is appalling. They need someone to prune it all down."
            pause(1)
            r "{i}On the Reproductional Habits of Fruit Flies{/i}?!! — what kind of person holds on to this trash?!"
            pause(1)
            
            "After a further twenty minutes of pointless browsing — she'd finally had enough."
            
            show rika uni sad day open at center with Dissolve(0.5)
            
            r "That's it, Abe, I have to go home now. You can look further if you want." 
            r "Here's the key, I'll let the receptionist know that you're still in here."
            pause(1)
            a "Thanks Rika! Sorry for dragging you along for this."
            
            show rika uni happy day closed at center with Dissolve(0.5)    
            
            r "It's okay."
            
            "She was smiling again."
            
            r "Just make sure you're prepared for our big outing on Thursday. I've sent Mei a message already, she's delighted."
    
    #####################################################################################################    
    

    pause(1)
    "With a restrained wave of her hand she exited the room."
    
    play audio "audio/swipe.ogg"
    hide rika with Dissolve(0.5)
    pause(1)    
    "And I continued my hunt."
    pause(1)
    "After ascertaining I'd been through each and every bookcase, I started anew, just to be certain—"
    
    play audio "audio/window.ogg"
    
    "When suddenly, I heard a door open, followed by a loud shuffle."
    
    "Before I could even turn around, a booming voice rang out:"
    
    "{i}Great to see young people take an interest in the art of politics!{/i}"
    
    pause(1)
    show leo smile closed with Dissolve(0.5)
    pause(1)
    
    "I turned to see an older gentleman who — apart from the distinct fragrance of liquor that surrounded him — appeared impeccable." #appearance
    
    "And immediately I knew who I was dealing with."
    
    "It was as though he emanated a certain aura, that I could sense, even before he'd addressed me."
    
    "This must be him. The man of whom Ina had told me every rumor."
    
    "The illustrious Leopold marquis of Abbot."
    
    l "This library is the greatest resource we have. It's sad so very few people find their way here."
    l "Is there anything I can help you with?"
           
    "I saw no reason to lie to him at the time, as I knew he wasn't exactly partial to the church's dealings."
    pause(1)
    
    a "I'm looking for the appendix to the {i}Theological Inquiries into the Church of Abbot{/i}—"
    
    show leo neutral open with Dissolve(0.5)
    
    "Instantly, his demeanor changed."
    "He let out a short, throaty laugh. And I could detect a captivated twinkle appear in his eyes."
    pause(1)
    
    l "The Inquiries into the Church of Abbot, you say?"
    l "I believe I've heard that name before."
    
    show leo neutral closed with Dissolve(0.2)    
    show leo neutral open with Dissolve(0.2)    
    
    "He looked over his shoulder."
    l "I suggest we go for a drink, you and I. "
    l "Somewhere where we can talk in private."

    pause(1)
    hide leo with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 2.0
    scene black with fade
    pause(1)
       
label p3c4:

    scene black with fade
    pause(1)
    play music "audio/0impromptu.ogg" loop fadein 12.0
    scene ristorante with Dissolve(0.5)

    window show
    pause(1)
    show leo smile open with Dissolve(0.5)

    ##At the cafe, talking to Marquis

    l "So I saw you come in with Kuyper's daughter."
    l "She's a fine catch, that girl. "
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    l "Be wary of her father though."
    "He coughed out a dry chuckle."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    l "Oh, I remember what it was like to be young."
    l "Between the two of us — some say I haven't changed much since those days."
    "He scratched his beard with an agonized gesture."
    l "Pretty women will always be my achilles heel—"
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    
    a "So I've been told."
    
    #
    pause(1)
    "Leopold had chosen a table away from the other patrons."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)   
    l "You're eighteen, right?"
    a "I nodded."
    l "Let me order you a beer."
    "He signaled the bartender by holding up two fingers." #meh
    show leo angry open with Dissolve(0.5)
    l "Anyway, about that document you were looking for—"
    l "—I'm sorry to tell you, it's been lent out. You're wasting your time searching."
    
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)      
    
    a "Lent out?"
    l "That's right. {i}The appendix has been removed{/i} — as they say in medicine."
    l "But tell me, what were you planning on doing with that thing?"
    l "Give it to your girlfriend?"
    a "Not at all. I need it for a school project."
    show leo smile open with Dissolve(0.5)         
    l "Well that's a sign of great ingenuity."
    l "It's an interesting piece. It isn't requested much." #meh
    l "I'd say people had all but forgotten about it—"
    
    l "—but then {i}you{/i} came along."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)  
    a "You mentioned it had been lent out?"
    show leo neutral open with Dissolve(0.5)
    l "Lent out — yes."
    l "It has."
    "He let out a long sigh. "
    pause(1)
    l "It's been lent out to {i}me{/i}, to be precise—"#"And the one that borrowed it was me—" #It is. It's lent out — in my name. 
    show leo neutral closed with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2)      
    "I was overcome with confusion."
    a "To {i}you{/i}?!"
    pause(1)
    l "I figured your girlfriend would have known, considering her father's position."
    a "She's not my—"
    l "She really had you on a wild goose chase, looking for things that weren't there. "
    #pause(1)
    a "She didn't know what I was looking for."
    "This comment appeared to put him at ease."
    show leo smile open with Dissolve(0.5)    
    l "That's good. Very good. Stay vigil."
    l "You don't have to tell the ladies everything."
    l "Keep them guessing."
    show leo smile closed with Dissolve(0.5)     
    l "You're a stronger man than I."
    show leo angry open with Dissolve(0.5)       

    "Then he bent forward and lowered his voice discreetly." #something like this
    pause(1)    
    l "You must've heard the story, Abe. It was about a year ago."
    l "There was a guy we employed to do our garden, on Sundays — Jan was his name. "
    show leo neutral wink with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2)     
    l "Jan wasn't from here, you know. But more importantly, he was a cigar smoker."
    l "My wife doesn't let me smoke in the house anymore, so we'd often sit on the patio outside and smoke together."
    l "I don't work my people too hard. You need to take your time, enjoy life—" #smile here?
    show leo neutral wink with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2) 
    "He winked."
    pause(1)
    l "Anyway, I was having a lot of trouble with your father-in-law Kuyper back then."
    l "Sometimes I would vent about it against Jan — and that's when he told me about the church inquiry."
    l "He had been conducting some private research of his own, and he had reasons to believe that that document contained compromising information pertaining to the history of the church of Abbot."
    pause(1)

    l "Personally, I'm more of a worldly man. But Jan was very much into these theological matters. "
  
    l "He was a Catholic — like the priest of his group — so you can figure why he didn't like Kuyper too much."
    show leo neutral closed with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2)   
    l "As I had access to the council library, I promised I'd retrieve the appendix document for him."
    l "He suggested it contained enough information to cause a national scandal. That it would take down Kuyper for good."
    pause(1)
    a "But it didn't?"
    show leo smile open with Dissolve(0.5)   
    "A self-deprecating smile appeared on his face." #TODO, expression
    l "Well he's still here, isn't he?"
    
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2) 
    
    l "You should know—"
    show leo neutral open with Dissolve(0.2) 
    l "I'm a selfish man."
    pause(1)
    l "I went to the council, to retrieve the document. "
    l "But I declined to give it to Jan."
    l "I kept it in my briefcase, as I had my own plans with it. "
    l "And I had it with me when the whole Sandford house affair occurred."
    show leo neutral closed with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2) 
    a "You mean you {i}lost{/i} it?!"
    a "The document you lost at Sandford house was the appendix to the church inquiries?!"
    show leo angry open with Dissolve(0.2)  
    l "Shh! Quiet down."
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)     
    l "I never lost it. It was {i}stolen{/i}."
    l "It was all a ruse, conjured up by these church people."
    l "I may have been a bit loose-lipped, that day when I found the document."
    l "You know, after a long day at the council, I like to come down here to drink a few glasses. I may have boasted my find here and there."
    show leo neutral closed with Dissolve(0.2)
    show leo neutral open with Dissolve(0.2)      
    l "Not much later a call came in. That our party — A.I.R. — would be entertaining a wealthy donor that night. "
    l "Kuyper was happy to provide Sandford house — the most exquisite property in town — for the occasion."
    l "They wanted me to come right away."
    
    show leo angry open with Dissolve(0.5)
    
    l "I should have know better. But I was in the best of spirits, so of course I attended."
    l "And they knew all my preferences. There was liquor, and female entertainment — and somewhere during the night I must have blacked out."
    l "In Sandford house of all places! Beautiful, stately Sandford house."
    l "Did you know my clan used to own that manor?"
    l "It was residence to the lords of the isle, whenever we visited Abbot."
    l "But my great great grandfather sold it to the Kuyper family. Right after the evacuation."
    l "He was hoping the church would take good care of it, that they wouldn't let it fall to ruin."
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)        
    a "I figure he was right."
    l "Ever since the reclamation, we've been trying to buy it back — first my father, then me. But to no avail."
    l "That snake Kuyper knows how much we want it."
    l "And then he uses it in such a humiliating way — to orchestrate my downfall."
    pause(1)
    l "My position within A.I.R. has become precarious due to the whole affair."
    l "As a democratically elected representative they cannot remove me from my position right now. However I doubt they'll keep me in the party when elections come." #become fickle?
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)     
    
    a "And that Jan guy? What ever happened to him?"
    l "Jan? He left shortly thereafter."
    l "One of his friends had something terrible happen to him, you know? A guy named Michel. Got killed on one of the farms." #SFX??
    l "Most workers from his group returned to their hometowns after that incident, never to return. I reckon they'd seen enough of this place."
    
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)      
    
    l "Anyway, I never had the chance to look into that document. To be honest, I'd all but forgotten about it until I found you two snooping around the council library."
    l "Your safest bet is that Kuyper still has it — if he hasn't burnt it by now."
    l "You'll probably have to pry it from his cold, dead hands."
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)     
    l "I apologize. I'm a man of many flaws."
    l "I should have known women would spell my demise. Those {i}heavenly{/i} creatures—" #be my downfall
    
    show leo smile closed with Dissolve(0.5)
    
    l "Life's a feast. You should enjoy it while you're young."

    pause(1)
    hide leo with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p3c5:

    scene black with fade
    pause(1)
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene mainstreet with Dissolve(0.5) 
    window show
    pause(1)


    "On my way home I went by the town store to buy some salmon for dinner."
    "Although their selection of produce was predictably basic, they somehow managed to consistently maintain a quality supply of fresh fish."
    
    pause(1)

    stop sound fadeout 1.0
    scene blueroom with Dissolve(0.5) 
    play sound "audio/officesound.ogg" loop fadein 4.0
    pause(1)
    
    "After briskly searing the salmon in a pan, I headed up to my room, intending to finally enjoy a quiet evening."
    
    "But fate clearly had something different in mind." #head still heavy?? #
    
    pause(1)
    play music "audio/0adagio15.ogg" loop fadein 2.0
    show ina shirt defiant day open with Dissolve(0.5) 
    pause(1)
    a "Ina?"
    a "Who let you in?"
    show ina shirt mirth day closed with Dissolve(0.2) 
    show ina shirt defiant day open with Dissolve(0.2) 
    n "Your father did. He was on his way out when I got here — said I could wait until you were back."


    
    n "So how did the investigation go? You got the document?"
    show ina shirt mirth day closed with Dissolve(0.2) 
    show ina shirt defiant day open with Dissolve(0.2) 
    a "Have you been {i}spying{/i} on me?"
    pause(0.5)
    "I told her about my meeting with the marquis. How he had been notified of the appendix's existence — and how the church had conned him into losing both the document and his reputation."
    
    show ina shirt saddened day open with Dissolve(0.5) 
    
    "After I was done explaining, I caught Ina staring into the distance, as though a thousand cogs were turning in her brain." #meh
    pause(1)
    n "So Leopold's gardener — Jan — was a {i}friend{/i} of the worker that was killed?"
    #pause(1)
    a "Yes, a colleague."

    show ina shirt saddened day closed with Dissolve(0.2) 
    show ina shirt saddened day open with Dissolve(0.2) 
    
    n "I feel that may hold some significance."
    n "We'll have to try to get a hold of Jan. But before that, we should see if we can extract the appendix from John Kuyper."
    a "We— what? What makes you think Kuyper hasn't gotten rid of it by now?"
    
    show ina shirt interested day open with Dissolve(0.5)
    
    n "With Kuyper you can never be sure."
    "Her voice sounded strangely muffled, as though she were chewing gum."
    n "The document holds historical significance to him."
    n "If there's one thing the church is keen on — it's preservation."
    show ina shirt mirth day closed with Dissolve(0.2) 
    show ina shirt interested day open with Dissolve(0.2) 
    n "But in the end there's only one way to find out. We'll have to break in to the church offices to see if can find it."
    
    #### Ina 5 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "Do you have time this coming Thursday?"
        
        "No, I'm taking Rika and Mei to the shore after school.":                  
            show ina shirt saddened day open with Dissolve(0.5) 
            "I was so taken aback by the bluntness with which she proposed the felonious deed, that I was happy to have a valid excuse."
            n "You're going to the shore, with {i}two{/i} girls?"
            n "I figure inviting me along never even came to mind."
            a "Ina, I—"
            
        "I'm afraid I have a lot of studying to do—": 
            $ ina_score += 1  
            show ina shirt mirth day closed with Dissolve(0.2) 
            show ina shirt interested day open with Dissolve(0.2)       
            n "Studying? You?"
            "I nodded."
            n "Strange, you always struck me as the carefree type—"            
    
    #####################################################################################################    
        
    #show ina shirt mirth day closed with Dissolve(0.2) 
    #show ina shirt interested day open with Dissolve(0.2)       
    
    n "Hmpf. Then let's do Saturday."
    n "After you're done with work."
    show ina shirt mirth day closed with Dissolve(0.2) 
    show ina shirt interested day open with Dissolve(0.2)  
    n "Anyway, it's late and I'm dead tired."
    n "Thanks for dinner. You should know for next time that I'm not too fond of seafood."

    hide ina with Dissolve(0.5)
    pause(1)
    
    "She was already out of the door by the time I realized she'd finished more than two-thirds of my plate."
    
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p3c6:

    scene black with fade
    pause(1)
    play sound "audio/train.ogg" loop fadein 1.0
    scene trainin with Dissolve(0.5) #TODO more images?
    pause(1)
    window show
    pause(1)
  
    #TODO, insert shot of them in the train # few lines of dialogue??
    "The sun was blindingly bright that day. It shone its lazy beams into our carriage, which was empty save for the three of us." #improve
    
    pause(1)
    stop sound fadeout 1.0
    scene beach with Dissolve(0.5) #TODO more images?
    play sound "audio/0seawaves.ogg" loop fadein 4.0

    pause(1)
    "To get to the beach, we had to ascend a small flight of stairs — up over the concrete embankment that shielded the lower lying inlands from the waters of the lake." #hinterlands
    pause(1)
    
    show mei bikini enthusiastic day open at right with Dissolve(0.5)
    play music "audio/0goldberg24.ogg" loop fadein 10.0
    
    m "So what do you think?"
    m "Amazing, isn't it? It's so big you can't see the other side!"
    show mei bikini happy day closed at right with Dissolve(0.2)
    show mei bikini enthusiastic day open at right with Dissolve(0.2)
    m "Our very own sea!"
    
    show rika dress sad day open at left with Dissolve(0.5)
    
    "Rika sniffed."
    show rika dress sad day closed at left with Dissolve(0.2)    
    show rika dress sad day open at left with Dissolve(0.2)     
    r "A {i}sea{/i} you call it?"
    r "All I smell is rotten fish—"
    "I held my nose up to the air, but couldn't detect anything out of the ordinary."
    

    #TODO, some more beach banter??
    "Mei continued speaking, unfazed by Rika's snide remarks."
    show mei bikini intent day open at right with Dissolve(0.5)
        
    m "And isn't the sun nice?"
    m "It's as warm as a summer's day."
    m "Rika, can we have ice cream later?"
    show rika dress happy day open at left with Dissolve(0.5)
    r "I don't think there will be a vendor at this time of the year."
    r "But we can eat something in the village when the sun begins to set."
    
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini intent day open at right with Dissolve(0.2)      
    
    "Mei seemed entirely too excited to listen to her friend's words."
    "This outing to a neighboring town had sparked a childlike enthusiasm in her, the intensity of which made me wonder how often she had actually left the confines of Abbotsford."
    show rika dress happy day closed at left with Dissolve(0.2)    
    show rika dress happy day open at left with Dissolve(0.2)    
    r "So, first things first."
    r "The coach would only let me skip practice if I'd do a thirty minute workout down here. Anyone joining me?"

   
    show mei bikini reluctant day open at right with Dissolve(0.2) #too much
    
    "Mei began shuffling awkwardly."
    show rika dress happy day closed at left with Dissolve(0.2)
    show rika dress happy day open at left with Dissolve(0.2) 
    a "You're going swimming? In October?"
    a "I think I'll pass."
    r "Suit yourself."
    
    #pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    
    "Rika bounded towards the shoreline."
    "Then, in a graceful motion, she removed her dress — revealing a modest sports swimsuit below — before wading into the lake."
    "A perfect halo of ripples propagated out over its glasslike surface."
    
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini smart day open at right with Dissolve(0.2)    
    
    r "You should come in! The water's lovely! "
    r "You can take a shower afterwards to get the stench off you!"
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini smart day open at right with Dissolve(0.2) 
    m "I'd rather play on the beach!"
    
    "Rika waved one more time — and then she was gone, swimming parallel to the coastline in skilled butterfly technique."
    
    "Mei turned her attention to me."
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini smart day open at right with Dissolve(0.2) 
    m "I'm not much of a swimmer."
    m "They tried to teach me, when I was very young, but they say I never took to it—"
    pause(1)
    a "Were you afraid of water?"
    pause(1)
    m "I'm not sure."
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini smart day open at right with Dissolve(0.2) 
    m "Somewhere shallow is fine, like a swimming-pool. But I wouldn't want to swim anywhere where I couldn't see the bottom."
    
    #
    pause(1)
    scene lake with Dissolve(0.5)
    pause(1)
    
    "I looked over towards the water, where Rika was still tirelessly continuing her athletics."
    
    "There was a beautiful symmetry in her strokes. And the way her endless hair — which she had failed to tie into a bun — trailed behind her like a black veil, gave her an otherworldly appearance. "
    
    "I stood mesmerized by the sight, as it evoked images of mermaids and nymphlike beings."
    
    pause(1)
    
    scene beach 
    show mei bikini enthusiastic day open at right 
    with Dissolve(0.5)
    
    pause(1)    
    
    
    #### Mei 5 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "Rika's wonderful, isn't she?"
        
        "Such grace, I've never seen anything like it.":                 
            show mei bikini annoyed day open with Dissolve(0.5) 
            m "Well, her parents {i}did{/i} hire personal trainer for her, you know."
            m "Without that she'd probably be rubbish."
            "She sighed."
            pause(1)    
            
        "She's alright—": 
            $ mei_score += 1  
            show mei bikini happy day closed at right with Dissolve(0.2)
            show mei bikini enthusiastic day open at right with Dissolve(0.2)     
            #show mei bikini enthusiastic day open at right 
    
    #####################################################################################################     
    
       
    #show mei bikini enthusiastic day open at right 
    m "Rika's projected to take first place at the regional championships this winter."
    m "It's the nationals after that. The whole town will be cheering her on."
    

    
    "At that moment Rika dove down — continuing underwater for a good while — until she appeared again far out, waving at us, her head almost invisible against the indigo waters of the lake." #long sentence
    show mei bikini happy day closed at right with Dissolve(0.2)
    show mei bikini enthusiastic day open at right with Dissolve(0.2) 
    
    m "She can stay underwater for more than five minutes. Isn't that amazing? "
    m "I remember, when we were small — we would hold breath-holding contests."
    m "Rika would always beat me."

    show mei bikini annoyed day open at right with Dissolve(0.5) 
    
    m "At times she'd hold her breath for so long that I'd begin to panic, begging and pleading her to start breathing again."
    pause(1)
    a "She {i}does{/i} have a sophisticated sense of humor, doesn't she?"

    show mei bikini pretty day open at right with Dissolve(0.5) 
    
    "Mei giggled."
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini pretty day open at right with Dissolve(0.2)    
    m "Rika is the pride of the town, I'm delighted to be her friend."

    m "Most girls around here look up to Rika, though they don't always let it shine through—"
    
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini pretty day open at right with Dissolve(0.2)     
    
    m "Where is she, anyway?"
    "I had to admit that I hadn't been paying attention."
    pause(1)
    a "I'm not sure, probably still under water—"
    
    pause(1)
    stop music fadeout 3.0
    scene lake with Dissolve(0.5)
    pause(1)
    
    "We stood and looked out over the lake for what felt like an eternity, but the waters remained without a trace."
    pause(1)
    m "Rika!"
    a "Rika!"
    "If she truly had gone under, there was now only a narrow window of time before it was too late."
    a "Rika! Rika!"
    m "RIKA!"
    play music "audio/chaconne.ogg" fadein 12.0 loop
    pause(1)
    "But the lake lay deathlike before us."
    
    pause(1)
    scene beach 
    show mei bikini crying day open at right       
    with Dissolve(0.5)
    pause(1)
    
    a "She's been under for more than ten minutes. No one can survive that long—"
    m "Impossible — she's an excellent swimmer."
    #stop music fadeout 1.0 #music already stopped
    m "Rika! Stop playing games!"
    m "It's not funny anymore!"
    show mei bikini weeping day open at right with Dissolve(0.5)
    pause(1)
    "And that's when the gravity of the situation truly hit me — like a lead cylinder, impact with my stomach at twenty knots per hour."
    "If Rika truly had gone under, there was no hope she'd ever emerge again."
    pause(1)
    "It was over. Finished."
    "What was intended to have been a pleasurable beach trip, had turned into the darkest possible tragedy."
    
    
    #### Mei 6 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "What should we do? She isn't coming back—"
        
        "We'd better call the emergency services.":
            $ mei_score += 1
            show mei bikini crying day open at right  
            m "That's a great idea — quick!"
            "As I took out my phone to dial the emergency number, I noticed that my fingers had gone completely numb."
            
        "We need to dive in to look for her.": 
            show mei bikini crying2 day open at right  
            m "Dive in? I really can't—"
            "Faced with the impossible decision between her friend and her own well-being, an abstract terror was forming in Mei's eyes."
                
    #####################################################################################################    
    
    pause(1)
    "But then—"
    m "Look! In the distance!"
    "I saw it immediately — a black dot, clearly discernible far out in the lake. It was rapidly traveling in our direction."
    a "That's got to be her! How could we not—"
    show mei bikini intent day open at right with Dissolve(0.5)
    m "Rika! She's back!"
    
    stop music fadeout 4.0
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini intent day open at right with Dissolve(0.2)
    
    "Casually, a dark haired figure stepped out from the waves and slipped into her summer dress."
    
    show rika dress mischievous day closed at left with Dissolve(0.5)            
    
    m "Where were you, Rika? We thought you'd disappeared—"
    
    show rika dress mischievous day open at left with Dissolve(0.5)     
    
    r "Oh I apologize. There's an interesting geological feature out there in the water that I felt like examining."
    r "It's a black granite rock, hidden just beneath the surface."
    r "At times you can see little parts of it, sticking out from the waves."
    
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini pretty day open at right with Dissolve(0.2)
    
    m "A rock?"
    "Instantly Mei seemed to have forgotten about our recent crisis, completely captivated by Rika's new find."
    "I looked into the distance, but saw nothing."
    
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2)                
    
    r "There's lots of history surrounding that stone."
    r "It used to be a hazard for ships, back in the days when this was still a sea."
    r "If fishermen hit that rock it could sink their vessel."
    pause(1)
    r "Over the centuries it racked up quite a death count, and eventually it became so notorious that it was given a name — the {i}humming stone{/i}."
    r "It was said that strange creatures lived within the rock, who brought forth a mysterious, whirring sound."

    show mei bikini reluctant day open at right with Dissolve(0.2)

    r "They were dangerous too, as they feasted on the corpses of sailors that drowned there."
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2)       
    r "Ridiculous folk-beliefs, of course, but these things do amuse me. I wanted to ascertain if the stone was still there."
    pause(1)
    a "I'm glad you didn't get eaten."
    r "Oh how could you two {i}worry{/i} about me? Are you doubting your champion swimmer?"

    pause(1) #TODO, switch to lake image
    hide rika with Dissolve(0.5)
    hide mei with Dissolve(0.5)     
    pause(1)
    scene lake with Dissolve(0.5)
    pause(1)

    "Rika and I spent the rest of the afternoon lying in the sun, while Mei scoured the shoreline for pretty stones."

    scene lake_twi with Dissolve(2.0)

    "When the sun began to set, we headed up to the nearby town of Ryebury."

    pause(1)
    window hide
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p3c7:

    scene black with fade
    pause(1)
    play sound "audio/fridge.ogg" loop fadein 1.0
    scene cafeteria with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "Rika took us to a small cafeteria where they served locally produced fishcakes."

    show rika dress happy day closed at left 
    show fishcakes at Position(xpos=0.29, xanchor=0.5)
    with Dissolve(0.5)  
    show mei bikini reluctant day open at right with Dissolve(0.5)       
    play music "audio/0goldberg15.ogg" loop fadein 2.0
    
    r "You like them?"
    "I nodded eagerly."
    "Though fried in gratuitous batter, I could tell the fish was fresh and of excellent quality."
    "It had a delicate, flaky texture, signifying skilled preparation unusual for fast-food joints like this."
    
    show mei bikini sad day closed at right with Dissolve(0.2)
    show mei bikini reluctant day open at right with Dissolve(0.2)    
    
    "Mei sat chewing reluctantly on a piece of batter."
    
    m "They taste very, um— local—"
    
    show rika dress mischievous day open at left with Dissolve(0.5)                

    
    r "It's okay if you don't like them, Mei. I'll order you some potato fritters in a minute."
    
    show mei bikini pretty day open at right with Dissolve(0.2)      
    
    m "I like the sea, but I don't really care for what's inside." #like what's in it
    
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2)    
    
    r "These are made from saltwater cod, you know?"
    r "They have to sail all the way past the great floodgates to catch them."
    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini pretty day open at right with Dissolve(0.2)  
    a "Is there still a fishing community down here?"
    r "A very small one. The lake itself is mostly useless for fish, especially now with the quota on eels."
    r "But there are a few families that still sail up north."
     
    show rika dress happy day open at left with Dissolve(0.5) 
    
    r "It feels like a fools errand at times, but I guess it's what they do."
    r "To them it's a matter of pride."  

    show mei bikini smiling day closed at right with Dissolve(0.2)
    show mei bikini pretty day open at right with Dissolve(0.2)        
    
    "Rika ordered another round of fishcakes and a plate of fries for Mei." 
    
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2) 
    
    r "After you two finish your meal I want to show you something."
    "Her mouth curled into a promising grin as she held up an innocuous looking key." #meh
    r "You should know by now that I'm {i}very{/i} well connected."
    
    pause(1)
    hide rika 
    hide fishcakes
    with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene pumping_twi with Dissolve(0.5) #TODO day or twilight?
    play sound "audio/0seawaves.ogg" fadein 1.0 loop
    pause(1)
    
    "We followed Rika along the concrete embankment, into something that looked like an industrial estate."
    
    "She held still at one of the buildings, unlocking its heavy, metal door."
    
    pause(1)
    show black with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    
    "She switched on the lights."
    scene pumpingstation_hall with Dissolve(0.3)
    play sound "audio/extractor.ogg" fadein 1.0 loop
    pause(1)
    show rika dress happy day closed at left with Dissolve(0.5)  
    show mei dress happy day open at right with Dissolve(0.5)    
        
    m "Whoa, what is this place?"
    
    r "This is where the magic happens."
    r "{i}Ryebury pumping station.{/i}"
    pause(1)
    r "As the terrain of the Marshpolder lies below sea level, rainwater has nowhere to run off to and will inevitably flood the land."
            
    r "To prevent this from happening, all excess water is led to this station through an extensive system of drainage ditches."
    r "A hi-tech centrifugal pump lifts up the water and jettisons it out into the lake."
    pause(1)
    r "My father is deputy to the regional water board. That's how I have access to this place."
    show rika dress happy day closed at left with Dissolve(0.2)     
    show rika dress happy day open at left with Dissolve(0.2)    
    
    #main character likes exclusive nature
    
    "Though the hall was draughty and uncomfortable, I felt a tingling sense of privilege as I stood above these great machines."
    "This entire building was vital for the well-being of thousands of civilians, and we were fortunate enough to have unmitigated access." #improve, move to later???
    
    pause(1)
    
    a "I love it here. It's so big!"
    m "And a little scary."
    show mei dress happy day closed at right with Dissolve(0.2)
    show mei dress happy day open at right with Dissolve(0.2)       
    r "Look, this stairway leads down to the basement where the pumps are."
    r "They replaced the machinery just a few years ago. Each pump now has a capacity of 150 tonnes per minute, which should be plenty for the coming decades."
    
    show rika dress mischievous day open at left with Dissolve(0.5)     
    
    r "But still, you should realize that whenever you're behind the embankment, you're treading on a former sea bed."
    
    r "A small rupture in the concrete embankment would expand quickly, causing all the waters of the lake to flow back in."
    "She let out a compulsive giggle."
    r "Isn't that an {i}arousing{/i} thought?"
    
    show mei dress regret day open at right with Dissolve(0.5)     
    
    r "You're safe while you're on Abbot, of course. The island still lies higher than the surrounding farmlands."
    r "Though I don't know how long that will last. They say our town is slowly sinking down into the soil—"
    
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2) 
    
    r "This place has seen the birth of the Marshpolder. It was the first of these stations built, you know? It pumped out the lions share of the seawater."
    
    pause(1) #mei blink??
    stop sound fadeout 2.0
    
    r "After the land fell dry, it was a putrid mess. You wouldn't make it far before sinking away in the sludge."
    
    r "People had to wear boots with broadened soles — not unlike modern snowshoes — in order to make their way from town to town."
    
    show rika dress mischievous day closed at left with Dissolve(0.2)     
    show rika dress mischievous day open at left with Dissolve(0.2) 
    play sound "audio/0buzzingflies.ogg" loop fadein 15.0
    
    r "And it wasn't long before the flies came." #the soggy marshes began to attract countless flies
    #TODO fly sound
    r "Swarms of them — multiplying rapidly in the former seabed, where they feasted on seaweed and rotten fish."
    
    r "It was the birth of a whole new ecosystem, where the fly-population went unchecked."
    
    r "They had no natural enemies at the time."
       
    show rika dress mischievous day closed at left with Dissolve(0.5) 
        
    r "The poor inhabitants of Abbot were driven mad. Millions and millions of flies, descending upon their little town — buzzing through the houses, smashing themselves against the window panes."
    
    r "It didn't take long for the pavements and windowsills to fill up with piles of dead flies."
    
 
    
    r "My great aunt still tells tales about how the children would play games with their corpses — stuffing them into each others schoolbags, or crunching them up into balls with which they held morbid snowball fights—"
    show mei dress surprised day open at right with Dissolve(0.5)   
    
    m "That's disgusting—"

    stop music fadeout 2.5
    scene woods4_eve 
    show mei dress surprised day open at right #with Dissolve(0.5)      
    show rika dress mischievous day open at left 
    with Dissolve(2.5) 
    play music "audio/summernight.ogg" loop fadein 2.0
    
    r "But the seabed made for fertile ground. It didn't take long for all kinds of plants to sprout in the new-formed soil."
    r "And as their roots spread through the mud, the ground gradually grew steadier — to the point where you could traverse it normally on foot."

    r "Spiders spun their webs among the countless shrubs — and just as the insect population had initially exploded, now the spiders reigned supreme—"
    show mei dress regret day open at right with Dissolve(0.5)
    r "—engorging themselves upon the endless supply of flies, often catching more than they could eat in a single summer."
    
    show rika dress mischievous day closed at left with Dissolve(0.5)     
    
    "Rika was smiling with sadistic glee."
    stop sound fadeout 5.0
    play effects "audio/haunting.ogg" fadein 17.0 loop
    
    r "Many islanders welcomed the arrival of the spiders, as their presence would finally put an end to the nuisance of the flies."
    r "But for some — such as my great aunt, who was wary of all things creepy and crawly — the circumstances became all the more dire."

    show mei dress blushing day open at right with Dissolve(0.5) 
    
    "I noticed Mei was cowering silently."

    r "Due to the abundant prey, the spiders grew to unnatural sizes."
    r "Larger than a human hand, they would hang, legs outstretched, within their massive webs."
    
    show rika dress mischievous day open at left with Dissolve(0.5)       
    
    r "My aunt recounts one traumatizing afternoon — when she was sent down into the cellar to retrieve a bowl of cured herring."

    stop music fadeout 3.5
    scene black
    show mei dress blushing day open at right
    show rika dress mischievous day open at left 
    with Dissolve(2.0)   
    #play 
    r "It was dark down there, and she didn't have a light."
    pause(1)
    r "She carefully made her way to the large, brine-filled barrel that stood far in the back."
    
    show rika dress mischievous day closed at left with Dissolve(0.2)   
    show rika dress mischievous day open at left with Dissolve(0.2)   
    stop effects fadeout 0.5    
    r "And then, when she raised the lid—"

    pause(1)
    r "—out crept two humongous, hairy—" #TODO segue into SFX, something smashing? Mei knocks something over

    play audio "audio/1pot.ogg"
    scene pumpingstation_hall
    show rika dress mischievous day open at left    
    show mei dress surprised day open at right 
    with vpunch
    
    m "Ieeeeeeeeeeeee!"
    play sound "audio/extractor.ogg" fadein 10.0 loop
    "Mei stood petrified, her eyes open wide."
    show mei dress crying day open at right with Dissolve(0.5)     
    m "Please stop, Rika! You know these stories frighten me!"
    show rika dress sad day open at left with Dissolve(0.5)       
    r "I'm sorry Mei — I forgot how sensitive you are."
    show rika dress happy day open at left with Dissolve(0.5)  
    "Rika mumbled soothing words as she sat and comforted Mei — though I could tell she was concealing a silent mirth."
    
    pause(1)
    hide rika with Dissolve(0.5)
    hide mei with Dissolve(0.5)  
    pause(1) #maybe a break of some sorts TODO
        
    "We played a game of hide and seek and indulged ourselves on Mei's seemingly endless supply of peppermints. It wasn't long before it had turned completely dark outside."
    
    "Rika let out a theatrical yawn."
    
    
    show rika dress happy day open at center with Dissolve(0.2)   
    pause(1)    
    r "It's getting late. We should probably be heading home."
    pause(1)
    r "As I mentioned before, I have some private business to attend to in Ryebury. It will only take a minute."
    r "Could you two go on ahead to the railway station and wait for me there? I'll catch up with you in time for the ten o'clock train."
       
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene lake_eve with Dissolve(0.5)
    play sound "audio/0seabonfire.ogg" fadein 7.0 loop
    pause(1)
    
    "And as we walked over the embankment, back to the train station, it was as though I could detect a very slight fragrance of burning meat in the air."
    
    "I figured it must be beach-goers, who had lit a bonfire."
    
    "And as I looked over towards the water, I could indeed detect a small fire burning in the distance."

    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)
       
label p3c8:

    scene black with fade
    pause(1)
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    scene ichthys with Dissolve(0.5) 
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    ##outside church ##Ina wearing her kimono or pink outfit

    "On Saturday afternoon I met up with Ina outside of {i}Ichthys House of Prayer{/i}."
    
    show ina shirt interested day open at center with Dissolve(0.5)
    
    n "These are the Church of Abbot's headquarters. They host a worship center and an adjacent office complex."
    n "So the plan is — we head in, grab the appendix document, and then we're out again in less than ten minutes."
    
    show ina shirt mirth day closed at center with Dissolve(0.2)
    show ina shirt interested day open at center with Dissolve(0.2)
    
    
    #### Ina 6 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "Is everything clear?"
        
        "Sounds pretty foolproof to me.":  
            $ ina_score += 1    
            show ina shirt mirth day closed at center with Dissolve(0.2)
            show ina shirt interested day open at center with Dissolve(0.2)                
            n "Of course it isn't, but I've implemented some safeguards."
            
        "Wouldn't that constitute a felony?": 
            show ina shirt defiant day open at center with Dissolve(0.5) 
            n "Sure it does, but I've implemented some safeguards."
    
    #####################################################################################################    
    
        
    n "The church itself is open to visitors until 8:00 PM, so as long as we're just looking around we're not breaking any laws."
    show ina shirt angry day open at center with Dissolve(0.5) 
    n "However, they probably keep their valuable documents somewhere inside the administrative offices."
    n "As soon as we venture further we'll be engaging in {i}breaking and entering{/i}."
    show ina shirt angry day closed at center with Dissolve(0.2)  
    show ina shirt angry day open at center with Dissolve(0.2) 
    a "Which is a crime—"
    show ina shirt defiant day open at center with Dissolve(0.5)   
    n "Anyway, it's dinner time now. Most clergymen are at home with their families."
    
    show ina shirt mirth day closed at center with Dissolve(0.2)
    show ina shirt defiant day open at center with Dissolve(0.2)    
    
    a "And if we get caught?"
    n "If we get caught we'll tell them we're high school students who are searching for meaning in their lives."
    n "We may get scolded — but then again, they can't go too hard on repentant sinners."
    n "Come on, let's go!"
    show ina shirt mirth day closed at center with Dissolve(0.2)
    show ina shirt defiant day open at center with Dissolve(0.2)   
    n "Try to appear interested in seventeenth century religious architecture."
     
    pause(1)
    a "I'll try."
    
    ## in church
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene church with Dissolve(0.5)
    play music "audio/0toccata.ogg" fadein 5.0 loop
    pause(1)
    
    "On our way inside, we passed a small booth where a church warden sat. Ina placed some money in the glass donation box that had a prominent place near the entrance."
    "The man nodded at us."
    
    pause(1)
    
    #"We headed "
    "The church itself was deserted save for the organist, who was rehearsing for tomorrow's service."
    
    show ina shirt angry day open at center with Dissolve(0.5)  
    
    n "This is it, the devotional heart of our town."
    n "I'm afraid there isn't much to see in here, apart from the organ."#?
    n "The history of this place goes back a long time, you know? It used to be a Catholic church, with a far more ornate interior."
    n "But during the reformation, all the statues were smashed and the decorations were removed."
    
    show ina shirt angry day closed at center with Dissolve(0.2)  
    show ina shirt angry day open at center with Dissolve(0.2)      
    
    n "The people of Abbotsford practice an austere devotion, where large displays of ecclesiastical wealth are frowned upon."
    n "But that doesn't mean the church isn't wealthy, you know. They sure are, considering all the properties they own. "
    n "They just don't feel the need to {i}parade{/i} their riches."
    
    show ina shirt defiant day open at center with Dissolve(0.5)      
    
    n "Anyway, it's time for us to make our move. If we stay in here for too long the warden will grow suspicious."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    
    #show ina shirt mirth day closed at center with Dissolve(0.2)  
    #show ina shirt defiant day open at center with Dissolve(0.2)       
    
    "Ina grabbed my arm and led me towards an nondistinct wooden door, hidden away in the walls of the church."
    "From her pocket she produced an elongated iron wire, the end of which she had carefully bent into a small hook. Quietly she inserted it into the door's keyhole."
    pause(1)
    a "You—you appear to be a seasoned burglar."
    n "Not really, but I've been looking it up on the internet."
    n "These old locks should be so simple even a child can open them."
    play audio "audio/0lockpick.ogg"
    "With a muted click the door gave way." #SFX click
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    scene stairs with Dissolve(0.5)
    stop music fadeout 1.0
    play sound "audio/0toccatamute.ogg" fadein 1.0 loop
    pause(1)
    
    "The church annex was dimly lit. Attempting carefully not to make a sound, we descended the tall staircase. "
    pause(1)
    show ina shirt angry day open at center with Dissolve(0.5)  
    pause(1)
    n "Remember, we're just looking for a youth pastor to talk to. We're seeking inner enlightenment."
    a "Do wayward souls carry lock picks?"
    n "Let's just maintain the door was slightly ajar."
    show ina shirt angry day closed at center with Dissolve(0.2)  
    show ina shirt angry day open at center with Dissolve(0.2)   
    n "There should be two offices downstairs. "
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    scene catacombs with Dissolve(0.5)
    pause(1)
    
    "The stairs led into a dark hallway."
    
    a "Not the most cheerful work environment."
    
    "Ina pressed her ear up to one of the doors. After confirming it was empty, we entered the room."
    
    ##room
    pause(1)
    scene kuyperoffice with Dissolve(0.5)
    pause(1)
    show ina shirt angry nig open at center with Dissolve(0.5)  
    pause(1)
   
    n "Al these books, looks like we've struck gold!"
    n "This must be John Kuyper's study. "
    
    hide ina with Dissolve(0.5)
    pause(1)
    
    "Immediately, we started browsing through the piles of paperwork. As expected, Kuyper's library was mostly theological in nature. It was like searching for a needle in a needlestack."
    pause(1)
    
    n "{i}Church Dogmatics volume XII{/i}—"
    n "{i}Compendium of Theological Hermeneutics{/i}—"
    n "{i}The Belgic Confession{/i}—"
    n "Why is nothing kept in order? They should teach this man a system."
    pause(1)
    a "His daughter's pretty tidy, I'd say."
    n "I bet she takes after her mother."
    #pause(1)
    "We continued searching. Ina appeared to be growing more frantic by the minute."
    pause(1)
    n "Are you sure the marquis wasn't lying to you?"
    n "He doesn't have a good {i}reputation{/i}, you know? I bet he was drunk at the time."
    pause(1)
    a "I can't deny that."

    n "And even then, who says Kuyper didn't just burn the documents after he obtained them? There's no use keeping them around if they're so incriminating—"
    play music "audio/0gurglingmute.ogg" fadein 17.0 loop
    a "But {i}you{/i} said—"
        
    "I froze— for over Ina's frustrated whispers I suddenly detected a strange noise that was coming from the room next to ours."
    "It was a hesitant gurgling, that burbled just within the audible range."
    pause(1)
    "{i}Ghrhlghlbr— Ghrhlghlbr—{/i}"
    pause(1)
    "There was something distinctly guttural to it."
    "{i}Ghrhlghlbr—{/i}"
    pause(1)
    "I pressed my ear up against the wall, trying to get a better gauge of the sound, when suddenly—"
    
    show ina shirt surprized day open at center with Dissolve(0.5)  #TODO papers 
    
    n "There! I've got it! {i}Appendix to the Theological Inquiries!{/i}"
    
    n "Let's get out of here!"
    show ina shirt angry day open at center with Dissolve(0.5)  #TODO papers     (blushing)
    "She clasped her hand to her mouth — realizing suddenly how loud her voice had sounded in the deathly silent office."

    "Then she resumed, in a hushed tone:"
    
    show ina shirt mirth day open with Dissolve(0.5)
    n "It was in his desk drawer — which was childishly simple to break open."
    
    a "That's great, Ina—"
    a "—but listen, can you hear that sound?"
    stop sound fadeout 2.0
    show ina shirt saddened day closed at center with Dissolve(0.5)  #TODO papers     
    "She grew quiet."
    a "There, listen closely. It seems to be coming from the room next door."
    pause(1)
    n "Come on, let's check it out."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    scene catacombs with Dissolve(0.5)
    pause(1)
    
    "We exited the room."
    "On her tiptoes, Ina headed over towards the adjacent door."
    pause(1)
    n "There seems to be someone in there. I can hear a voice, though it sounds heavily distorted, as though in agony."
    a "Come on Ina, we should leave. We have what we came for."
    n "Just let me listen for a second longer. I'd love to get a recording—"
    
    scene catacombs_figure with Dissolve(0.5)
    play sound "audio/0panictheme.ogg" fadein 1.0 loop
    
    "{i}What do you think you're doing down here?!{/i}"
    
    "Ina jumped up, almost dropping her papers in the process. A figure had appeared at the end of the hallway and was angrily making it's way towards us. "
    "Almost mechanically, Ina called out her alibi—" 
    
    n "We're looking to speak to a youth pastor!"
    

    stop music fadeout 7.0
    scene stairs with Dissolve(0.5)

    
    "—but she'd already grabbed me by the arm, dragging me up the flight of stairs—"
    
    scene church with Dissolve(0.5)
    
    "—through the door that led to the main chapel—"
    
    scene ichthys with Dissolve(0.5)
    
    "—and we sped-walked past the warden, who — though clearly oblivious to the whole affair — stared after us in amazement as we set off over the town square at Olympic speeds."

    window hide
    stop music fadeout 1.0
    
    scene black with fade
    #pause(1)
       
label p3c9:

    scene black with fade
    #pause(1)
    play music "audio/summernight.ogg" loop fadein 1.0
    scene schoolroad with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    #pause(1)
    window show
    #pause(1)


    "Ina led me on detours, in order to shake off our imagined pursuers."
    
    scene school_side with Dissolve(0.5)
    
    "It took us more than half an hour to get to school."
    "We sped through alleyways, jumped a hedge, spent time hiding behind a dumpster, cut through the woods, until we eventually reached the school grounds via the east gate."
    
    scene school_front with Dissolve(0.5)
    
    "Once Ina had ascertained that we weren't being followed, we entered the building."
    
    pause(1)
    stop sound fadeout 7.0
    stop music fadeout 1.0
    scene office with Dissolve(0.5) #TODO twilight version? too hard?

    pause(1)
    
    "Though my newfound profession had measurably increased my general fitness over the past few weeks, I was unaccustomed to the sudden outburst of physical exercise that had just been demanded of me." #due to paper round
    play sound "audio/officesound.ogg" fadein 3.0 loop        
    "Fully at the end of my tether, I collapsed into a chair."

    pause(1)
    show ina shirt angry day open at center with Dissolve(0.5)
    play music "audio/0adagio15.ogg" fadein 23.0 loop 
    pause(1)
    n "They really had it out for us there."
    
   
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "They must have some hidden secrets — for them to be so weary of visitors."
    pause(1)
    a "Well, we {i}were{/i} trespassing—"
    
    pause(1)
    show document with Dissolve(0.5)
    
    "Ina — who appeared rather unfazed by our close escape — took out her captured documents and began paging through them intently."

    #"And it wasn't long before she began to read out loud." #unfazed
    
    show ina shirt smiling day open at center with Dissolve(0.5)
    
    n "{i}Addendum to the Journal of the Reverend Thomas W. H. H. Backer.{/i}"
        
    n "{i}Monday, 28th of September 1856.{/i}"
    scene sky_blue 
    show ina shirt smiling day open
    show document
    with Dissolve(2) 
    
    n "{i}Due to the extraordinary circumstances that have arisen during my inquiry into the proceedings of the Church of Abbot, which will be elucidated upon further herein—{/i}"
    n "{i}—these pages shall serve as an appendix to the journal that I have submitted prior to the Presbytery of the Low Countries.{/i}"
    show ina shirt smiling day closed at center with Dissolve(0.2)
    show ina shirt smiling day open at center with Dissolve(0.2)
    n "{i}Given my circumstances I did not feel at liberty — during my visit — to commit to paper those occurrences that I have witnessed upon the isle, the sheer distressing and even blasphemous nature of which will immediately become apparent to the reader.{/i}"
    
    show ina shirt saddened day open at center with Dissolve(0.5)    
    
    "Ina cleared her throat."

    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)

    
    n "{i}As described in the paragraphs previously divulged, my initial welcome and contact with the reverend John Kuyper was cordial and without notable event.{/i}" #The content of these meetings has been accurately described in in the paragraphs already put forth.{/i}"
    
    n "{i}It was not until the third day after my arrival, that I became aware of certain behavioral eccentricities within both the Kuyper family and the community of Abbot at large.{/i}"
    
    n "{i}Though not immediately apparent, this anomaly manifested itself as a creeping awareness, a palpable sensation, as though I was never fully alone during my stay on the isle.{/i}"
  
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    n "{i}Wherever I went, there was a mystifying presence that gradually grew more discernible.{/i}"
    
    n "{i}It could take the form of a muted giggle, or a glimpse of black hair, dashing away in my peripheral vision.{/i}"
    
    n "{i}But whenever I tried to confront Hendrika with her strange behavior, she would act coy, evasive even, avoiding my glances—{/i}"
    
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    
    n "{i}And there was more. Slightly alleviating the annoyance of the constant espionage — though nonetheless unsettling — there was a peculiar, habitual occurrence within the town that immediately drew my attention.{/i}"
   
    scene nightsky_dark 
    show ina shirt saddened day open
    show document
    with Dissolve(2.0) 
   
    n "{i}For every evening, after dinner, when I would retreat to my room for prayer and meditation, I noticed that the entirety of the island became shrouded in a deathly quiet — as though every living being had disappeared from the face of the earth.{/i}"
    n "{i}The streets below would be without stir, and even within the manse itself I could detect no trace of the Kuyper family.{/i}"
    
    n "{i}These absences would always start before seven, and never lasted for less than an hour.{/i}"
    
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    
    n "{i}After picking up on the regularity of these intervals, I would utilize them to embark upon walks around the desolate town — as even my dark-haired sentinel appeared to be absent during this period of time.{/i}"
    

    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    
    n "{i}It was on Wednesday evening, during one of these walks, that I first noticed a distinct fragrance of smoke coming from the dunes.{/i}"
    
    n "{i}With my interest piqued, I cautiously headed in the direction whence the scent came from. {/i}"
    n "{i}And as I drew closer, I ascertained that it originated not from the dunes themselves, but from the beach beyond — whereupon a great bonfire had been ignited.{/i}"
    
    stop sound fadeout 1.0
    play sound "audio/0seabonfire.ogg" fadein 40.0 loop
    
    n "{i}I had already entertained the notion that the inhabitants of Abbot held a covert observance in the evening hours — and my heart jumped as I finally beheld the large crowd of people that had gathered upon the shore.{/i}"
    
    n "{i}With the bright flames casting elongated shadows over the chalky sand, the assembly made for a haunting scene.{/i}"

    show ina shirt angry day open at center with Dissolve(0.5)
    
    n "{i}For upon the bonfire lay the carcass of a sheep. A sheep not raised above the flames, but placed directly upon them—{/i}"
    stop music fadeout 10.0
    n "{i}—so that a great fire emanated from its carcass, sending smoke and the stench of burning flesh up into the sky, to be swept away by the evening breeze.{/i}"
    

    n "{i}Taking shelter in the dunes, as not to be discovered, I continued to observe the haunting spectacle.{/i}"
    
    play music "audio/0kyrie.ogg" fadein 60.0 loop

    n "{i}Though most of the winds blew out over the sea, some of them blew over the land — and although these gusts were infrequent and far between, during those times I could clearly make out Kuyper's voice.{/i}"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "{i}He was preaching a sermon upon the shore—{/i}"
    n "{i}—his voice drenched in a fervor and devotion that had been absent during that observance I had attended on Sunday morning.{/i}"
    
    n "{i}And just as I arrived, the reverend led the congregation in prayer.{/i}"
    n "{i}And the people spoke — in unison, so that it was clear for me to hear — these words that are commonly referred to as the {/i}Song of the Sea:"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    #####################
    n "{i}The LORD is a man of war, the LORD is His name.{/i}"
    
    n "{i}Pharaoh's chariots and his host hath He cast into the sea. His chosen captains also are drowned in the Red sea.{/i}"
    
    n "{i}The depths have covered them, they sank to the bottom as a stone.{/i}"
    
    n "{i}And in the greatness of Thine excellency Thou hast overthrown them that rose up against Thee. Thou sentest forth Thy wrath, which consumed them as stubble.{/i}"
    
    n "{i}And with the blast of Thy nostrils the waters were gathered together, the floods stood upright as a heap, and the depths were congealed in the heart of the sea.{/i}"
    #####################

    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "{i}After this communal prayer the reverend resumed his sermon, and he spoke in enthused vehemence.{/i}"
    
    n "{i}What I could make out from his words alluded to the most ancient parts of the Pentateuch — and even to arcane Talmudic texts that are completely foreign to Christian scripture.{/i}"
    
    n "{i}And I heard him utter blasphemous monikers, such as these belonging to the great serpent Leviathan, and he spoke this name with such exalted reverence that it were as though he were heaping praise upon the beast. {/i}"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "{i}And he spoke more blasphemous and unholy names, many of which I had not seen in any text, religious or profane. And a name I distinctly recall crossing his lips was that of a certain {/i}Lotan{i}.{/i}"
    
    n "{i}And he described Lotan as infinite, as being without end.{/i}"
    
    n "{i}And during his sermon the carcass burnt, and it burnt fast and hot, for it had much fat in it.{/i}"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "{i}And when the carcass had been reduced to ashes, two members of the congregation came with shovels and swept the ashes in the direction of the sea. {/i}"
    
    n "{i}And as they swept the burnt remains towards the water, reverend Kuyper raised his hands — much like he had done on that tempestuous afternoon, when I arrived four days ago — and he spoke a blessing unto the waters.{/i}"
    
    n "{i}And it was at that moment that the sea rippled in fanatic rage, and a large wave rose up over the shore and swept away the remains of the charred carcass — which I deduce must have been a burnt offering, as was custom in Noah's days.{/i}"
    n "{i}And thus the beach was wholly clean again and there was no evidence for the morning tide to lay bare.{/i}"
    
    n "{i}The reverend led the crowd in a solemn chant:{/i}"
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    n "{i}He who coils through immeasurable depths;{/i}"
    n "{i}He who traverses impenetrable darkness;{/i}"    
    n "{i}Lotan! Lotan! Eel without end;{/i}"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    
    n "{i}And they repeated this incantation many times — but I had become nauseated to my stomach from the decadent display of depravity that I had witnessed upon the shore that night. Highly distraught I returned to the manse. {/i}"
    
    n "{i}And it was not until{/i}—{nw}"
    play audio "audio/0smash.ogg"
    stop music fadeout 0.1
    stop sound fadeout 0.1
    scene office_smashed
    show ina shirt angry day open
    show document
    with vpunch
    n "Wha!" #TODO ina surprized
    
    #TODO vpunch interjected in dialogue
    

    stop sound fadeout 0.5
    #scene office with Dissolve(0.5)
    play sound "audio/officesound.ogg" fadein 0.5 loop
    pause(1)
    
    "Suddenly we were shaken by the sound of breaking glass. A large stone had crashed through the window and came hurling onto the floor."
    
    "For a second Ina sat frozen, still clenching the document tightly in her fist. But then she stood up from her chair."
    
    play music "audio/0panictheme.ogg" fadein 5.0 loop
    show ina shirt surprized day open with Dissolve(0.5)
    
    n "It's the church! They're on to us!"
    n "Run!"
    
    hide ina 
    hide document
    with Dissolve(0.5)
    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    stop music fadeout 7.0
    
    pause(1)
    window hide
    scene black with Dissolve(3.0)
    pause(1)
    #####################################################################################################
    if rika_score > 3:
        show prog_rika p at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    elif rika_score == 3:
        show prog_rika n at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
    else:
        show prog_rika d at Position(xpos = 0.25, xanchor=0.25, ypos=0.25, yanchor=0.25) with easeinright
        
    pause(0.25)
    
    if ina_score > 3:
        show prog_ina p at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
    elif ina_score == 3:
        show prog_ina n at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright  
    else:
        show prog_ina d at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with easeinright
        
    pause(0.25)
    
    if mei_score > 3:
        show prog_mei p at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    elif mei_score == 3:    
        show prog_mei n at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    else:
        show prog_mei d at Position(xpos = 0.75, xanchor=0.75, ypos=0.75, yanchor=0.75) with easeinright
    
    
    #####################################################################################################
    pause(2)
    hide prog_rika with easeoutleft
    pause(0.25)
    hide prog_ina with easeoutleft
    pause(0.25)
    hide prog_mei with easeoutleft
    
    
    pause(1)

    
    
    ########################################################
    ################ PART 4 ################################
    ########################################################
       
label p4c1:

    
    scene white with Dissolve(1.0)
    pause(1)
    scene part4_title1 with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    pause(1)
    #play sound "audio/ventilator.ogg" loop fadein 1.0
    play music "<from 25.0>audio/0panictheme.ogg" fadein 5.0 loop
    scene schoolstairs with Dissolve(3.0)
    pause(1)
    window show
    pause(1)

    "We scrambled down the stairs and out through the fire escape."
    
    scene school_side_twi with Dissolve(0.5)
    
    "I hadn't fully recovered from our previous sprint, and began to lag behind — but Ina grabbed me by the arm, pulling me onwards through the streets." #stitches
    
    pause(1)
    stop music fadeout 3.0
    scene diningroom with Dissolve(0.5)
    #pause(1)
    
    "We made it to Ina's house."
    
    pause(1)
    scene inabedroom_eve with Dissolve(0.5)
    play sound "audio/ventilator.ogg" loop fadein 1.0
    pause(1)
    "As we entered her room she locked the door and hastily closed the curtains."
    
    pause(1)
    show ina shirt angry day open with Dissolve(0.5)
    pause(1)
    
    a "You think they'll find us here?"
    
    n "Oh they will — but I think they've stated their case."
    play music "audio/0andantino20.ogg" fadein 30.0 loop
    n "They're bound to leave us alone for now."
    a "I hope we don't end up like Karin—"
    
    show document with Dissolve(0.5)

    pause(1)
    "But Ina was already riffling through her papers, trying to find the passage where she had left off."
    #"Without wasting any time she resumed reading."
         
    
    n "{i}The next morning I spent indoors, resting my weary head. I had abstained from putting my recent discoveries to paper, as I was aware the family would habitually go through my belongings, whenever I was out.{/i}"
    #Though usually these intrusions seemed purely for domestic purposes, there was at least one time where I noticed that my papers had been disturbed."
    
    #For this reasons I began to keep a shadow journal, in which I wrote sundry observations, as to not raise any suspicions of my true inquiry into the idiosyncratic customs of the inhabitants of Abbot. "
    
    stop sound fadeout 1.0
    scene beach 
    show ina shirt saddened day open
    show document
    with Dissolve(2.0)
    play sound "audio/0searoar.ogg" loop fadein 15.0
    
    n "{i}When I returned to the beach, later that afternoon, all traces of yesterday's vigil had been erased by the morning tide.{/i}"
    n "{i}And it wasn't long before I caught Hendrika, sitting against a sand dune.{/i}"
    n "{i}She was quietly singing to herself, an old fishwives' tune.{/i}"
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    n "{i}Herring ashore, herring ashore—{/i}"
    n "{i}Put on yer boots, they'll be back with more—{/i}"
    n "{i}Herring ashore, herring ashore—{/i}"
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)    
    n "{i}She was no longer making any effort to conceal her perpetual surveillance of me.{/i}"
    pause(1)
    scene reverend 
    show ina shirt saddened day open
    show document   
    with Dissolve(2.0)
    
    n "{i}The following day I conversed with Kuyper. He appeared to have returned to his affable self, without any trace of the possessed fervor that I had witnessed in him two nights ago.{/i}"
    show ina shirt interested day open with Dissolve(0.5)    
    n "{i}I surmised to him that I had not found anything abrasive within his teachings — and that I would take the night ship in order to relay this message to the presbytery.{/i}"
    n "{i}Kuyper seemed pleased and thanked me heartily for my visit.{/i}"
    show ina shirt mirth day closed at center with Dissolve(0.2)
    show ina shirt interested day open at center with Dissolve(0.2)    
    n "{i}And to be honest, the man made such a wholesome impression on me that afternoon—{/i}"
    n "{i}—that I felt inclined, when the evening silence fell upon the town once more, to embark to the beach for one last time — just to confirm that my conclusions were truly correct, and as not to lay false judgment upon his character.{/i}"
    
    scene lake_nig 
    show ina shirt saddened day open
    show document      
    with Dissolve(2.0)
    
    n "{i}That night, as I headed through the dunes, I noticed that the air was devoid of smoke. And when I arrived at the place where the sermon had previously been held, I found it to be desolate.{/i}"
    
    n "{i}The tide was fully out that night — so that the island was at its largest — and I could walk out far over the moonlit beach.{/i}"
    
    n "{i}And that's when I saw it, far in the distance, at the northernmost tip of the isle, there shone a faint light.{/i}"
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)    
    n "{i}And as I hurried towards the light — under the cover of the dunes, so as not to fall prey to watching eyes — I saw that a large gathering of people had converged once again, and that some of them carried torches.{/i}"
    stop music fadeout 8.0
    n "{i}And Kuyper was speaking, leading the sinister ceremony in his animated manner.{/i}"
    
    n "{i}I took shelter behind a cluster of large stones, that stood close to the dunes. {/i}"
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    n "{i}But as the tide was out, and the congregation stood near the shoreline, I could not clearly make out the reverend's words.{/i}"
    
    n "{i}However, the torches and moonlight illuminated the nocturnal scene, and I had a clear line of sight of the spectacle which took place upon the shore.{/i}"

    show ina shirt angry day open at center with Dissolve(0.5)    
    n "{i}For more than and hour the reverend preached, and over time I grew aware of a certain visceral change in his gesticulations.{/i}"

    n "{i}It was as though the motions of his hands and his body became more erratic and disjointed in nature.{/i}"
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    n "{i}And simultaneous with this change, his voice grew louder, to the point that I could clearly make out the sounds he brought forth.{/i}"
    n "{i}But what reached my ears no longer resembled any human speech, for it had acquired a strange, guttural quality, that sounded wholly alien to me.{/i}"
    
    n "{i}In all his characteristics, Kuyper had become ailed with an unholy, demoniac possession that made me pray to any remaining forces of good on this forsaken isle. {/i}"
    #slightly more
    
    play music "audio/haunting.ogg" fadein 15.0 loop
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    n "{i}And after his sermon, the noise died down, and I could see a silhouette upon the shore which I recognized as the silhouette of a young woman—{/i}"
    n "{i}—and I could see that she was unclothed, her pale white skin reflecting the moonlight to the extent that it appeared to be glowing.{/i}"
    
    n "{i}And she had waving black hair that reached down to her thighs, and from that I could tell it was Hendrika, the pastor's daughter.{/i}"
    
    n "{i}And as she stepped forward and knelt down into the surf — with the eyes of the congregation upon her — I saw a ripple passing through the waters.{/i}"
    n "{i}And though it was a completely windless night, the sea erupted in sudden tempest.{/i}"

    n "{i}And in the pale light I fancied I saw a hundred thousand pitch black wires, coiling through the waves. {/i}"
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)    
    n "{i}And then something emerged from the waters.{/i}"
    
    n "{i}I deemed it to be a shadow, at first, as it was blacker than the dead of night. But as it rose higher I soon found it to be wholly opaque.{/i}"
    
    n "{i}A solid mass, pitch black, as though no light could ever escape from it.{/i}"
    #slightly more
    
    n "{i}And as it emerged, the crowd erupted in ecstasy — uttering words in heathen tongues and reciting the name of Lotan.{/i}"
    
    n "{i}The being crept onto the sand, and into the ring of bystanders. Slowly it drew towards the black haired girl.{/i}"
    
    n "{i}And I fear I have no other word for this wholly unspeakable act —{/i}"
    n "{i}But it {/i}knew{i} Hendrika. {/i}"
    n "{i}It knew her, there, before countless eyes, upon that moonlit shore.{/i}"
    
    show ina shirt angry day closed at center with Dissolve(0.2)
    show ina shirt angry day open at center with Dissolve(0.2)
    stop music fadeout 8.0
    n "{i}But already I was running, back through the dunes, down the entire stretch of fields that lay between me and the harbor.{/i}"
    n "{i}And I clambered up to my room  — gathering my clothes and papers haphazardly — before rushing towards the dock, where the mail boat lay that would leave for the mainland that night.{/i}"
    
    n "{i}And I sat there until it departed, all the while quivering, thinking of these things that exist beneath the waves, of which no good Christian man has any understanding.{/i}"
    stop sound fadeout 3.0
    #slightly more
    
    pause(1)


    scene inabedroom_eve 
    show ina shirt saddened day open
    show document
    with Dissolve(2.0)
    play sound "audio/ventilator.ogg" fadein 1.0 loop
    pause(1)
    
    "Ina sat there, reading the last pages in silence while she dragged her nails through the fabric of her skirt."
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    n "It ends with a long, technical appeal — in which he recommends expulsion of the Church of Abbot with the highest prejudice."
    
    pause(2)
    
    a "That was quite the story."
    

    
    "Ina nodded."
    
    "Suddenly she'd become languid, as though all the excitement of the past hours had instantly seeped out of her."
    
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    
    n "I have a lot to process—"
    
    "Her voice drawled."
    pause(1)
    
    n "I'm sorry. I really need to go to sleep—"
    n "—we can discuss our findings tomorrow."
    show ina shirt saddened day closed at center with Dissolve(0.2)
    show ina shirt saddened day open at center with Dissolve(0.2)
    n "If you want you can take the couch—"

    pause(1)
    hide ina 
    hide document
    with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p4c2:

    scene black with fade
    pause(1)
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    scene villageroad with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)
    #TODO explain that it's the next morning??

    "I paced through the desolate streets, an unsanitary sensation washing over me, as though everything had suddenly been tinted by the strange superstitions that the church document had laid bare."
    
    "Whatever it was that Ina had read to me yesterday evening, it appeared like something from a horror novel."
    
    "And the realization that the inhabitants of this town, Leopold, John Kuyper, Ina herself, had placed so much {i}weight{/i} on it—"
    
    "—showed just how underdeveloped their minds must have become."
    
    #TODO   
    "I've been callous. I've treated these people as my peers. But I should be careful—" #expand with his own thoughts on the document
        
    "Suddenly a voice rang out behind me."
    
    play music "audio/0goldberg22.ogg" fadein 30.0 loop
    
    r "Down in the dumps?"
    scene villageroad with vpunch    
    "I jumped." #TODO vpunch
    
    pause(1)
    show rika dress happy day open with Dissolve(0.5)
    pause(1)
    
    a "R—Rika, nice to see you."
    r "Looks like someone has a bad conscience."
    show rika dress mischievous day closed with Dissolve(0.5)
    "She smiled."
    pause(1)
    r "Anyway, how are you doing?"
    a "Oh, I'm okay. I had a rough night."
    
    r "I hope Ina hasn't been keeping you from your studies."
    show rika dress mischievous day open with Dissolve(0.5)    
    "She looked at me with all-knowing eyes, making me wonder how much exactly she had learnt about our brush-in with the clergy last night, and the mystifying document we had managed to capture."
    #TODO: this is suspicious
    
    #have rika say some things about their relationship. Maybe have there be a decision point.
    #they move somewhere else
    
    #"She smiled." #improve
    
    show rika dress happy day open with Dissolve(1.0)
    r "Say, I wanted to thank you again, for letting me join you on your beach trip last Wednesday."
    r "I realize I didn't leave you much of a choice, but I wanted you to know it meant a lot to me."
    r "I'm blessed to have you as my friend."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Sometimes I'm afraid to let myself go, you see?"
    r "I get caught up, in my workout schedule, in my church duties."
    
    r "But sometimes I forget to savor the moment. To make lasting memories—"
    r "—at the beach, with my friends."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)      
    r "Youth is far too short to waste—"
  
    r "I'd like to make more memories with you, Abe—"
    pause(1)
    "She spoke with such honest candor that I couldn't help but be touched by her words."
        
        
    "But then—"
    
    show rika dress mischievous day open with Dissolve(1.0)
    r "Before I go, I'm curious."
    r "Did you find it?"
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    a "What—"
    r "That book you were looking for, last Monday."
    "My heart skipped a beat."
    r "I forgot to ask if you managed to find it in the end."
    

    "Her eyes shot fire." #improve
    #pause(1)
    "I was unsure how to respond. It was clear that she knew more than she was letting on — the question was, how {i}much{/i}." #TODO improve
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)    
    a "I'm afraid I didn't find it—"
    r "You didn't?"
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)   
    "Her face warped into a menacing grimace."
    
    
    ##### Rika 7 ####################################################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "—{i}didn't{/i} you?" #place for a flash forward?"
    
        "I didn't, I swear.":
            show rika dress unhappy day open with Dissolve(0.5)  
            r "I apologize."
            #pause(1)
    
        "Will you please drop the charade?!":    
            $ rika_score += 1
            show rika dress happy day open with Dissolve(0.5) 
            stop music fadeout 3.0
            "Her soothing words, her voice, the mockery in her her smile — her entire presence ignited an explosive rage in me that burst out all at once." #at that moment into an explosive rage that burst out all at once." #slightly more, more drama, explanation etc."
    
            a "Just shut up!"
            a "I have nothing to say to you!"
    
            "Already regretting my sudden outburst, my anger was over the second it erupted." #I already regretted my sudden outburst."
    
            "Silenced, but further unfazed, Rika took a step backwards."
            show rika dress happy day closed with Dissolve(0.2)
            show rika dress happy day open with Dissolve(0.2)
            r "Wow Abe, please control yourself."
            
            r "But you're right, I apologize."
        
    #### CECK CHARACTER SCORE ###############################################################################################
    
    if rika_score < 4:

        r "I feel as though this conversation has drawn to an end. I have to go now, to prepare for the afternoon service."
        r "See you some other time."
        
        pause(1)
        hide rika with Dissolve(0.5)
        pause(1)
        window hide
        pause(1)
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with fade
        pause(1)
                
        #SCORE TOO LOW, MOVE ON        
        jump p4c4 
        
    else:
        show rika dress sad day open with Dissolve(0.5)     
        r "I will cease playing games."
        
    ##########################################################################################################################
    
    #something about the service, about retribution (bible quote about wrath)
    
    r "I've been keeping you in the dark about a lot of things."
    r "You must have many questions by now—"
    "Though she feigned remorse, the playful glare hadn't completely faded from her eyes. "
    
    r "I have to change for the afternoon service soon. Let's say you come over later tonight, then I can answer all your questions."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)    
    a "Later tonight? "
    a "Will your parents let you have a guy over on Sunday evening?"
    show rika dress mischievous day open with Dissolve(0.5) 
    #TODO closeup of black stockings
    r "Oh but I have something far better in mind."
    
    "She winked."
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)    
    r "Recall me telling you I was well connected?"
    pause(1)
    r "I have the keys to Sandford house."
    play music "audio/light3.ogg" loop fadein 4.0 
    
    scene white
    show rika dress mischievous day open
    with Dissolve(2.0)
    
    r "Let's say we meet there at 8 PM. I'll explain everything to you then. I promise."
    
    
    #### Rika Ending ##########################################################################################
    #TODO different sound
    menu:
        with Dissolve(1.0)
        r "So will you join me?"
        
        "Sure, see you at eight.":          
            show rika dress happy day open with Dissolve(0.5) 
            #### POSITIVE RESOLUTION    
            r "I'm so happy, Abe. I'm overflowing with joy."

            r "I promise, everything will be a lot clearer after tonight."
            show rika dress happy day closed with Dissolve(0.2)
            show rika dress happy day open with Dissolve(0.2)   
            r "Please excuse me for now. I have to look my best for the afternoon service."
            stop music fadeout 2.0
            scene villageroad
            show rika dress happy day open
            with Dissolve(1.5)
            r "See you later."
            
            pause(1)
            hide rika with Dissolve(0.5)
            pause(1)
            window hide
            pause(1)
            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene black with fade
            pause(1)
            
            jump p5Rc1
            # START RIKA'S ENDING
            
        "I'm afraid I have to pass on the offer.": 
            show rika dress unhappy day open with Dissolve(1.0) 
            #### NEGATIVE RESOLUTION  
       
            "Suddenly Rika grew cold."
            stop music fadeout 2.0
            scene villageroad
            show rika dress unhappy day open
            with Dissolve(2.0)
            r "I'm sorry Abe. I felt we were getting along so well."
            
    #r "I have great memories for now" #about trip, beach, etc."
    r "However, you leave me no choice than to respect your decision."
    show rika dress sad day open with Dissolve(1.0)       
    r "I believe for the coming future, we should observe some distance between the two of us." #TODO: make less harsh
    r "To protect both our feelings, if you understand."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)   
    r "We may run into one another sometime, Abe. But please keep your distance."
    
    r "{i}Guard your heart above all else, for it determines the course of your life.{/i}"
    
    r "A girl's heart is so easily broken—"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)    
    r "Please excuse me for now. I have to look my best for the afternoon service."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    
    "With these words she turned away, trotting off at a brisk pace."
    
    #####################################################################################################    
          
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p4c4:
    #### MEI's ROUTE
    scene black with fade
    pause(1)
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    scene dunes with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    #play music "audio/schoolbell.ogg"
    #Intending to make the most of my Sunday afternoon
    
    "Pushing the mystifying encounter with Rika to the back of my mind, I set off homeward through the sunlit streets which were alive with the gentle chirping of birds."
    
    play audio "audio/1leaves.ogg" fadein 6.0 #TODO improve
    pause(1)
    "Until I detected a suspicious movement in the bushes—"
    pause(1)
    "Reflexively I adopted a defensive position, throwing up my arms to shield my vital organs."
    
    play audio "audio/panting.ogg"
    show phyrrus with Dissolve(1.5)
    "And while I observed the figure that emerged from the shrubs, I readied myself to flee the scene as soon as the situation necessitated it."
    pause(1)
    
    "But the hound made an unusually calm impression."
    "Entirely devoid of the aggressive behavior I'd previously grown accustomed to, he stared at me with pleading eyes."
    pause(1)
    "Not intending to lower my guard, I slowly edged backwards."
    pause(1)
    
    a "Goood doggy—"
    a "You just stay there — no need to get physical with me."
    pause(1)    
    
    "But when Phyrrus saw me back away, he immediately leapt up at me—"
    play audio "audio/1bark.ogg"
    show phyrrus with vpunch    
    "—playfully sniffing my fingers before letting out a short, loud bark."
    
    
    "I almost jumped out of my skin."
    pause(1)
    "Eagerly he hopped down again, dashing back towards the bushes from whence he came."
    hide phyrrus with Dissolve(0.5)
    "And upon closer inspection, I saw they gave way to a forest trail."
    play audio "audio/bark1.ogg"
    "Phyrrus let out another bark."
    pause(1)
    "Y—you want me to follow you?"
    play audio "audio/bark2.ogg"
    "Again, a bark."
    pause(1)
    "I must remain wary. He could be attempting to lead me to a secondary location, where no one will find my mutilated corpse—"
    
    "But Phyrrus was already off, running up the forest trail a few yards, before{nw}"
    play audio "audio/bark2.ogg"
    extend " turning round and barking for me to follow him."
    
    "And driven by macabre curiosity — combined with a latent death wish — I followed the dog, to see where it would lead me."
    
    pause(1)     
    scene woods3_mor with Dissolve(0.5)
    pause(1)   
    
    "Phyrrus led me along the old perimeter of the island, past the dolmen Mei had shown me last week, and through the nearby woodland—"
    
    "—until we reached a patch of forest where the trees were bare and the ground was strewn with rocks."
    
    pause(1)  
    stop sound fadeout 7.0
    scene black with Dissolve(0.5)
    scene castlehall with Dissolve(1.5)
    play music "audio/rheingold_meandering2.ogg"   
    
    show phyrrus at right with Dissolve(0.5)
    
    "In the center stood a large headstone."

    pause(1)
    "{i}Phyrrus!{/i}"    

    pause(1)

    "{i}You brought him here so quickly!{/i}"
    
    pause(1)
    show mei garb happy day open at left with Dissolve(1.0)
    
    "The voice belonged to Mei, who was standing among the trees, dressed in archaic looking clothes."
    
    play audio "audio/bark1.ogg"
    show phyrrus at right with vpunch
    "Phyrrus appeared excited, leaping up at me expectantly."
    show mei garb happy day closed at left with Dissolve(0.2)
    show mei garb happy day open at left with Dissolve(0.2)    
    
    m "Poor dog, he's all worked up."
    m "I told him it was an emergency—"
    m "—that if he'd fetch you, you'd surely give him a treat. "
    m "You {i}did{/i} bring him something, didn't you?"
    show mei garb happy day closed at left with Dissolve(0.2)
    show mei garb happy day open at left with Dissolve(0.2)       
    a "Bring him something?"
    a "You made an empty promise—"
    play audio "audio/bark1.ogg"    #TODO whine sfx
    "Phyrrus whined in disappointment, and I saw some of his prior hostility return to his eyes." 
    a "You could offer him a peppermint."
    play audio "audio/1doggrowl.ogg"    #TODO whine sfx
    "My suggestion was met with an angry snarl."
    show mei garb happy day closed at left with Dissolve(0.2)
    show mei garb happy day open at left with Dissolve(0.2)       
    m "Please don't be sad, Phyrrus — you did great."
    m "I'll get you a marrow bone when we return to the farm."
    hide phyrrus with Dissolve(0.5)
    show mei at center with easeinright #TODO check
    
    a "So what {i}is{/i} the big emergency you called me for?"
    
    "She contemplated for a second."
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)       
    m "Oh yes, the emergency—"
    m "It's a secret."
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)      
    "She smiled at me self-consciously."
    pause(1)
    a "Well, if it's a {i}secret{/i} emergency, I don't see how I could be of any help—"
    m "Wait, I can tell you the secret!"
    "Again, she pondered."
    pause(0.5)
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)  
    m "{i}This{/i} is the secret! My secret hideout!"
    m "Nobody knows about the hidden clearance—"
    a "I highly doubt that—"
    m "It's true! {i}You{/i} didn't know about it, did you?"
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)  
    a "There's lots of things I don't know about—"
    show mei garb sad day open with Dissolve(1.0)      
    "She pouted."
    m "I didn't even want to show it to you at first, but decided I had to repay you—"
    a "Repay me? For what?"
    
    show mei garb sad day closed with Dissolve(0.2)
    show mei garb sad day open with Dissolve(0.2)  
    m "For taking me to the beach."
    m "I hadn't been down there since childhood."
    m "The church is really strict, you know—"
    m "Even when Rika goes for shopping trips in the city, she hardly ever lets me come—"
    show mei garb sad day closed with Dissolve(0.2)
    show mei garb sad day open with Dissolve(0.2)     
    a "So it's true, you never leave the island—"
    show mei garb smile day open with Dissolve(0.5)     
    m "Not an island! I thought I told you so."
    m "You're beginning to sound like Rika."
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)         
    m "But you're right, that was my first trip in years—"
    show mei at left with easeinright
    m "Anyway, there are enough pretty spots nearby."
    m "What do you think of this place?"
    m "The forest floor here is littered with rocks."
    m "Do you know why?"
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)   
    "I shook my head."
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2) 
    m "Well I know!"
    "She grinned triumphantly."
    m "The soil around this town is filled with all kinds of different stones, which have to be removed to turn it into suitable farmland."
    m "So for hundreds of years, farmers have dumped their unnecessary stones up here, in the woods."
    
    #TODO: have Mei repeat that Abbot wasn't an island. “Once, maybe, but only for a short time. I try to talk this out of Rika's head./You're beginning to sound like Rika.”
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)     
    m "It makes for a pretty sight, doesn't it?"
    m "Like a castle hall."
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)  
    m "{i}My{/i} castle hall."
    m "Bow to your queen, loyal subject!"
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)      
    "It was clear the excitement had risen to her head."
    pause(1)    
    m "You should know they crown me Queen of Abbotsford every spring."
    m "Do you like my royal attire?"
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)   
    m "As long as you're in my halls, you have to do exactly as I say."
    pause(1)
    a "That goes without question—"
    
    #Look, it's has also been used as a memorial site."
    "She pointed at the large gravestone behind her."
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2) 
    m "There, the tomb of my forefathers."
    m "Their names are etched into the stone."
    pause(1)
    
    
    #### Mei 7 ##########################################################################################
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "Please tell me who lie buried there—"
        
        "Let me take a careful look.":  
            $ mei_score += 1  
            show mei garb happy day open with Dissolve(0.5)      
    
        "Y—you don't even know your own ancestors—?":
            show mei garb blush day open with Dissolve(0.5)     
            "She blushed."
            m "Please don't tease me like that. Just obey me—"
            m "Help me read these letters. I can see an S, an E—"
            #pause(1)
            
    #####################################################################################################        
            
    "I crouched down to inspect the faded epitaph."
    pause(1)
    a "Hm—"    
    a "It says that this is a memorial to saint Wynfreth the missionary, who christianized the low countries."
    a "In the year 750 AD, Wynfreth was murdered by Germanic tribes at this site."
 
    a "That's all it says—"
    show mei garb happy day open with Dissolve(0.5)      
    m "Thank you, I've always thought as much, but I wanted to be certain."
    #"Her confidence couldn't conceal the transparent lie."
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)     
    m "Poor Wynfreth, the tribes mustn't have liked his teachings at the time."
    m "I guess, in the end, he did get his way—"
    pause(1)    
    "I glanced around the clearance."
    "The trees here were without leaves, as though they had died a long time ago, their austerity adding to the consecrated atmosphere of the place."    
    "And while I stained my eyes to make out my surroundings, I grew aware of a steady fatigue that had been creeping up on me unnoticedly."
    "The trees melded together in swaths of brown and gray." #TODO meh
    "After I caught my balance, I turned to Mei."
    
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)     
    a "I've had an eventful weekend."
    a "I'd like to go home now, to get some rest before school starts—"
    pause(1)
    
    
    #### CECK CHARACTER SCORE ###############################################################################################
    
    if mei_score < 4:

        m "That's okay Abe. I'm sorry for making you come all the way over here."
        m "Will you be able to find your own way back?"
        pause(1)
        "I nodded, and we parted ways."
        
        pause(1)
        hide mei with Dissolve(0.5)
        pause(1)
        window hide
        pause(1)
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with Dissolve(1.5)
        pause(1)
                
        #SCORE TOO LOW, MOVE ON        
        jump p4c6 
        
    else:
        show mei garb sad day open with Dissolve(0.5)      
        m "You're leaving — already?"
        
    ##########################################################################################################################
    
    
    

    show mei garb happy day open with Dissolve(0.5) 
    m "Come Abe, please stay for a little longer."
    m "I command you, as your queen."
    stop music fadeout 5.0
    a "I'm sorry—"
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2) 
    "She squinted at me tellingly."
    
    play music "audio/light3.ogg" loop fadein 5.0
    scene white 
    show mei garb happy day open at left
    with Dissolve(2.0) ###TODO piano piece
    pause(1)
    m "But Abe—"    
    pause(1)
    m "If you leave now, you won't find out my secret—"
    show mei garb happy day closed with Dissolve(0.2)
    show mei garb happy day open with Dissolve(0.2)    
    a "I thought you told me this place {i}was{/i} the secret—"
    m "This isn't a real secret. You said so yourself."
    show mei garb smile day closed with Dissolve(0.2)
    show mei garb smile day open with Dissolve(0.2)  
    "She giggled playfully."
    pause(1)   
    
    m "So do you want to know?"    
    pause(1)
    
    ### MEI DECISION ###
    menu:
        with Dissolve(1.0)
        m "I won't ask you again—"
        
        "Sure, I'm curious to find out—":          
            show mei garb smile day closed with Dissolve(0.2)
            show mei garb smile day open with Dissolve(0.2)  
            #### POSITIVE RESOLUTION   

            m "Thank you Abe, I knew you'd be willing to listen."
            m "But I have to admit, you do look tired."
            
            stop music fadeout 2.0
            scene castlehall
            show mei garb smile day open at left
            with Dissolve(1.5)
            
            m "Please come and visit me tomorrow evening, then I'll reveal my secret to you."
            m "But you have to promise me you won't tell anybody else."    

            pause(1)
            #stop music fadeout 1.5
            hide mei with Dissolve(0.5)
            pause(1)    
            play sound "audio/edgemeadow.ogg" loop fadein 1.0
            scene woodpath with Dissolve(0.5)
            pause(1)
            
            "I dropped Mei off at her farm on the way back to town."
            
            pause(1)

            scene meifarm_day with Dissolve(0.5)
            pause(1)
            show mei garb smile day open with Dissolve(0.5)  
            
            m "Don't forget, tomorrow evening."
            m "See you then—"
        
            pause(1)
            hide mei with Dissolve(0.5)
            pause(1)
            window hide
            pause(1)
            stop music fadeout 1.0
            stop sound fadeout 1.0
            scene white with Dissolve(2.0)
            pause(2) 
            jump p5M1
            
        "I'm tired, Mei. I really have to go home.":    
            show mei garb sad day open with Dissolve(0.5)        
            #### NEGATIVE RESOLUTION
            
            "Her lip curled down in apparent disappointment."
            stop music fadeout 2.0
            scene castlehall
            show mei garb sad day open at left
            with Dissolve(1.5)
            m "You're no fun—"
            m "—a terrible subject. You should do as your queen demands."
            show mei garb sad day closed with Dissolve(0.2)  
            show mei garb sad day open with Dissolve(0.2)              
            m "O-off with your head!"
            pause(1)
            
            "Cheerfully I bade her goodnight before heading back to town."
            ####

    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)  
    
label p4c6:
    
    #### INA's ROUTE
    scene black with fade
    pause(1)
    play audio "audio/schoolbell.ogg"
    play sound "audio/officesound.ogg" loop fadein 1.0
    scene school_front with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "Next day, Ina didn't show up for school."
    pause(1)
    "During lunch break I received a text message from her, asking me to check the office and to bring her the computer hard drive."
    "She didn't reply to any of my further inquiries into her situation."
    
    pause(1)
    scene office_smashed with Dissolve(0.5) #TODO broken glass
    pause(1)
    
    "The office was in the exact same state we'd left it Saturday afternoon. Apparently the damage to the window had gone completely unnoticed."    
    "I secured the computer's hard disk before informing the janitorial department about the broken glass."

    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p4c7:

    scene black with fade
    pause(1)
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene inahouse with Dissolve(0.5) 
    pause(1)
    ## START 1
    #"After school I headed straight to Ina's house."
  
    pause(1)
    stop sound fadeout 1.0  
    scene inabedroom_eve with Dissolve(1.0)
    play sound officesound loop fadein 1.0
    pause(1)
    window show
    pause(1)
    
    "I found Ina in her bedroom, in mostly the same state as I'd left her."
    "She appeared listless, hardly responding to my presence."
    
    play music "audio/0forgottendreams.ogg" fadein 12.0 loop
    show ina cami neutral day open at center with Dissolve(0.5)
    
    a "Ina, I brought you the hard drive you asked for."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    "She muttered a thank you."
    pause(1)
    a "Have you been eating?"
    n "I'm okay—"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    "I stood there for a while, not really knowing what to say."
    pause(1)
    a "Quite the story we read last night—" #what do you make of all of this?" #TODO, more precise
    pause(1)
    n "It was."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)    

    ##### Ina 7 ###########################################################################################################   
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        
        n "So what did {i}you{/i} make of it?"
        
        "Sounded like a load of nonsense to me.":
            show ina cami smart day open at center with Dissolve(0.5)   
            $ina_score += 1
            n "It did — didn't it?"
            n "Can't believe we wasted so much time hunting down that stupid document." #I'd say it's utter nonsense. 
            "A feeling of relief came over me. For a minute I feared that Ina would send me hunting for cosmic abominations next."
            pause(1)
            a "I'm glad you feel that way."

        "It has changed my very perception of reality—":
            show ina cami surprised day open at center with Dissolve(0.5)           
            "She looked at me with a stare of bemusement in her eyes."
            pause(1)
            n "You take that nonsense serious?" #TODO meh
            n "You're more gullible than I thought."
            
    ############################################################################################################################        
            

    pause(1)
    ## END 2
    ## START 3
           
    show ina cami neutral day open at center with Dissolve(0.5)   

    n "It makes me wonder, how a document like that could come into existence—"

    pause(1)
    n "A civilization that's in a state of decline will often fall back on beliefs from a simpler age."
    n "Like a senile old grandmother, singing nursery rhymes in her rocking chair."
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)    
        
    n "{i}Georgie Porgie, pudding and pie—{/i}"
    n "{i}Kissed the girls and made them cry—{/i}"
    
    n "For children, singing nursery rhymes is a happy pastime — as it contributes to the formation of a developed psyche."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)  
    n "But when a demented person sings them, there is always a sinister undertone—"
    n "—as they are signifiers of a great reversal taking place."
    #pause(1)
    n "These memories from childhood are all that remain to a worn-out, withered mind."
    
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    
    n "Our society is growing decadent. We're collectively sliding into a void of decay."
    n "And now that we're on our way out, we grow more and more receptive to pre-modern folk-tales."
    
    n "Such as that document — that dime-store horror tale we read last night."
    pause(1)
    a "So you're confident it was all made up?"
    #"She glared at me with a look of contempt."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    n "Pagan rituals by the sea shore?"
    n "It was one of the biggest farces I'd ever read."
    n "A witch hunt, no more no less. Who would've expected these kinds of hoaxes to persist into the nineteenth century?"
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)    
    n "It must be a symptom of corrupted enlightenment — for clergy to use superstitions of the distant past against communities they deemed spiritually backwards."
    n "The presbytery likely felt threatened by the upsurge of separatist congregations, to the extent that they made up allegations of witchcraft and idolatry against dissenting pastors—"

    show ina cami blue day open at center with Dissolve(0.2)
    
    n "And to think that marquis Leopold willingly participated in reviving these folk-beliefs in this day and age."
    n "He must be desperate — going to such lengths to paint the church in a negative light."
    
    show ina cami blue day closed at center with Dissolve(0.2)
    show ina cami blue day open at center with Dissolve(0.2)  
    
    n "These accusations, these lurid tales of horror and decadency — these prejudices aren't natural to man."
    n "But they're often born from fertile ground — from generations of sadism, inbreeding, and false piety."
    n "To think that these matters would take place, in a developed country—"
    
    show ina cami neutral day open at center with Dissolve(0.5) 
    
    n "You should know."
    n "Time isn't always simultaneous."

    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2) 
    
    n "The originating history of a modern nation always allows for pockets, where time runs at a crawl."
    n "Where practices and ideas remain. Conserved, sheltered perfectly from the winds of modernity that rage throughout."
    
    pause(1)
    ##########################
    "She sighed."
    show ina cami frown day closed at center with Dissolve(0.2)
    show ina cami neutral day open at center with Dissolve(0.2)     
    n "The irrationality of it all."
    #It's a recurring pattern."
    
    n "We went through so much trouble just to uncover that stupid document."
    n "I should have seen this coming—"
    #show ina cami sad day open at center with Dissolve(0.5)   
    n "I'm clearly not as perceptive as I thought I was—"
    
    ## END 3
    ## START 4
    pause(2)
    
    "In an attempt to cheer her up, I tried to change the subject."
    
    a "You know. I can hook up that hard drive for you, if you want."
    a "There are other things to write about—"
    a "We could start on next week's cover article."
    
    pause(1)
    
    n "Never mind—"
    n "I received word from the headmaster this morning. They're cutting our funding."
    show ina cami crying day open at center with Dissolve(0.5) 
    n "They said we've been reporting too little on school matters." #more emotional, crying
       
    "She was visibly distraught."
    pause(1)
    #show ina cami frown day closed at center with Dissolve(0.2)
    #show ina cami sad day open at center with Dissolve(0.2)     
    
    a "What? They can't do that!"
    pause(1)
    n "It's no use fighting it. The school board are all church members."
    
    #All that work gone to nothing. Terrible town, nothing good ever persists.    
    
    n "We won't be able to cover printing costs without additional funding. Let alone your salary."
    
    a "I haven't even been paid yet—"
    
    "She was too melancholy to acknowledge my comment."
    #"She began speaking in a hoarse voice." 
    pause(1)
    
    n "Do you realize how much work I've put into the Sunday Abbot?"
    
    n "All my spare time, for almost two years. All for nothing."
    a "It wasn't—"
    n "Oh it's my own fault, for trying to build something in a town like this."
    
    n "Nothing will grow in tainted soil. It will sprout, and rot, and fall to pieces—"
    
    #n "Nothing of value can ever persist."
    stop music fadeout 4.0
    show ina cami neutral day open at center with Dissolve(0.5) 
    
    n "My life's work, gone — all over a nineteenth century hoax."
    
    
    #### CECK CHARACTER SCORE ###############################################################################################
    
    if ina_score < 4:

        pause(1)
        r "Come on, Abe. You should probably be on your way home."
        r "We had a great time while it lasted."
        show ina cami frown day closed at center with Dissolve(0.2)
        show ina cami neutral day open at center with Dissolve(0.2)     
        #segue towards ina's bad ending
              
        pause(1)
        hide ina with Dissolve(1.0)
        pause(1)
        window hide
        stop music fadeout 1.0
        scene black with fade
        pause(1)
                
        jump iBad #BAD ENDING
        
    else:
        show ina cami frown day closed at center with Dissolve(0.2)
        show ina cami neutral day open at center with Dissolve(0.2) 
        
    ##########################################################################################################################
    
    
    
    ################# still no good segue ### TODO TODO TODO
    ## END 4
    ## START 5
    
    pause(1)
    #
    
    #n "Do you realize what we're dealing with? Such backwards superstition, in the current age—"
    #n "This is the face of sheer irrationality."
    #mankind is becoming susceptible to this nonsense"
    play music "audio/light3.ogg" loop fadein 4.0 
    scene white
    show ina cami neutral day open at center 
    with Dissolve(2.0) 
    #n "It's useless, nothing good can come from digging further."
    n "It's time to give up this pointless investigation."
    n "It's not like we have any other choice." #Now that the funding for the Sunday Abbot has been cut—"
    pause(1)
    #### Ina Ending ##########################################################################################
    #play audio "audio/decision.ogg" #different sound
    menu:
        with Dissolve(1.0)
        n "Let's call it quits—"
        
        #### INA NEGATIVE RESOLUTION
        "Well, if that's what you truly want—":          
            show ina cami frown day closed with Dissolve(0.2) 
            show ina cami crying day open with Dissolve(0.2)     
            n "It's okay, Abe, don't be sad. We've tried our hardest."
            n "Not every story can become a headline."
            
            stop music fadeout 3.0
            scene inabedroom_eve
            show ina cami crying day open at center 
            with Dissolve(2.0)
            
            "I need to be alone now."
            
            pause(1)
            hide ina with Dissolve(0.5)
            pause(1)
            window hide
            pause(1)
            jump iBad
     
        #### INA POSITIVE RESOLUTION
        "I can't agree with that.":
            show ina cami astonished day open at center with Dissolve(0.5)     
            n "You what—?"
        
    #########################################################################################################  
            
    a "I can't let you quit the Sunday Abbot."
    a "Even if the appendix document was a dead end, there's still so much work to do."
    a "Though I'll admit I was doubtful at first, over the past few weeks you've really won me over."
    pause(1)
    a "If you won't continue the paper, I will. Without you."
    show ina cami happy day open at center with Dissolve(0.5) 
    "For the first time since entering her room, I thought I noticed a faint light igniting in her eyes."
    stop music fadeout 3.0
    scene inabedroom_eve
    show ina cami happy day open at center 
    with Dissolve(2.0)

    n "You will?"
    show ina cami happy day closed at center with Dissolve(0.2) 
    show ina cami happy day open at center with Dissolve(0.2) 
    n "You really {i}do{/i} care, don't you?"
    pause(1)
    n "Come on Abe, let's get something to eat."
    
    ##END 5

    pause(1)
    hide ina with Dissolve(1.0)
    pause(1)
    window hide
    stop music fadeout 3.0
    scene black with fade
    pause(1)
       
label p4c8:

    scene black with fade
    pause(1)
    play sound "audio/phonecall.ogg" loop fadein 1.0
    play music "audio/officesound.ogg" loop fadein 3.0
    scene inabedroom_eve with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    "Next morning I awoke to my phone buzzing. While my eyes adjusted to the light, I could hear Ina answering the call."
    
    stop sound fadeout 0.5
    
    #  
    n "Really? That's a huge relief."
    n "We'll head down there immediately."
    n "Thank you for contacting us."
    pause(1)
    "She put away her phone and began dressing herself."
    show ina cami optimist day open at center with Dissolve(0.5)   
    n "That was Karin."
    n "She's making a steady recovery and says she wants to issue a statement to the press. "
    
    play audio "audio/clothesdrop.ogg"
    show ina shirt interested day open at center with vpunch     
    
    n "Let's head to the hospital right away."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene white with Dissolve(1.0)
    pause(1)
        
    
    ############################################################
    ########## PART 5 INA ######################################  
    ############################################################
         
label p5Ic1:

    scene white with Dissolve(1.0)
    pause(1)
    scene part5_ina with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    
    pause(2)
    play sound "audio/ventilator.ogg" loop fadein 1.0
    scene hospital with Dissolve(1.0) #TODO correct placement, pan?
    pause(1)
    window show
    pause(1)

    "We made our way to the front desk, where we were redirected towards the neurology ward."
    
    pause(1)
    scene hospital_corridor with Dissolve(0.5)
    pause(1)
    play music "<from 3.05>audio/0impromptu.ogg" loop fadein 5.0
 
    show karin happy at right with Dissolve(0.5)
    show ina shirt interested day open at left with Dissolve(0.5) 
    n "It's good to see you fine and well."
    

    
    "Karin was doing rehabilitation exercises — carefully pacing the hall like a bird that had forgotten how to fly."
    pause(1)
    
    k "A cerebral contusion."
    k "I was out for a solid minute. Couldn't hold in food for the first few days."
    k "The police came by my bed, but as expected they were completely useless—"
    show ina shirt mirth day closed at left with Dissolve(0.2)      
    show ina shirt interested day open at left with Dissolve(0.2)  
    n "Well they secured the crime scene all right — wouldn't even allow the press in."

    

    "Karin let out an exasperated chuckle."
    show karin worried at right with Dissolve(0.5)
    k "Come, let me sit on the bed."
    
    pause(1)
    hide ina
    hide karin
    with Dissolve(0.5)
    pause(1)
    scene hospital_room with Dissolve(0.5)
    pause(1)
    show karin worried at right    
    show ina shirt interested day open at left 
    with Dissolve(1.0) 
    pause(1)
    show ina shirt angry day open at left with Dissolve(0.5)   
    
    
    n "So, what can you remember of the night of the attack?"
    "Ina appeared anxious for answers."
    
    #TODO slightly more banter, describe the attack from k viewpoint    
    pause(1)#
    k "Hmm."
    pause(1)
    k "That night, when it happened—"
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    k "I had spent most of the day working in the garden, so the back door had been unlocked."
    pause(1)
    k "After it grew dark, I had dinner on the couch, while reading through some policy papers for the plenary meeting next morning."
    k "Then, as I got up to bring my dishes to the kitchen, I suddenly saw a shadow in the corner of my eye."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)      
    k "Everything went black. The last thing I remember was the sound of falling plates—"
    
    pause(1)
    
    k "The perpetrator must have snuck inside sometime during the day, lying in wait until sundown."
    #show ina shirt angry day closed at left with Dissolve(0.2)      
    #show ina shirt angry day open at left with Dissolve(0.2)  
    show ina shirt surprized day open at left with Dissolve(0.2)     
    n "And he just left you there?"
    n "You could have died! How did the emergency services find you?"
    show ina shirt angry day open at left #with Dissolve(0.5)      
    show karin happy at right 
    with Dissolve(0.5)    
    k "Well, I got lucky—"
    k "Phyrrus had been hanging around me all afternoon, digging up the garden and acting like an all-round nuisance."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    k "When the attack happened, he must have still been close by — close enough to be alerted by the noise."
    k "He'll have seen me lying out cold on the kitchen floor."
    k "The neighbor said Phyrrus began barking and whining, that he kept at it until she went out to take a look."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    k "He was my savior."
    k "According to the neurologists, I could have retained permanent brain damage if I'd been found any later."

    a "I figure every dog has its day—"
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  

        
    n "And do you have {i}any{/i} idea who did this to you?"
    "Karin sighed."
    show karin worried at right with Dissolve(0.5)    
    k "I never saw the face of my attacker."
    pause(1)
    k "But I have my suspicions."
    k "Are you guys up to date on local politics?"
    show ina shirt interested day open at left with Dissolve(0.5)      
    "Ina nodded eagerly."
    #show ina shirt angry day closed at left with Dissolve(0.2)      
    #show ina shirt interested day open at left with Dissolve(0.2)  
    k "Well Abe, you should know the Abbotsford town council holds a total of 14 seats."
    k "A party needs an eight seat majority to obtain the mayoral office."
    k "When the largest party doesn't secure eight seats during the elections, a coalition of two or more parties has to be formed to ensure majority rule."
    show ina shirt mirth day closed at left with Dissolve(0.2)      
    show ina shirt interested day open at left with Dissolve(0.2)      
    n "But that's unnecessary, as A.I.R. holds eight seats at the moment."
    pause(1)
    k "That's right. A.I.R. currently holds an absolute majority in the council."
    #
    show karin serious at right with Dissolve(0.5)    
    "An agonized expression drew over Karin's face."
    k "The problem is, A.I.R. isn't free of inner division."
    k "Our seats are evenly divided between agrarians, like me, on the one side, and church loyalists on the other."
    k "And now that I have been temporarily incapacitated, a stand-in has been appointed to take my seat in the council until I recover."
   
    show ina shirt saddened day open at left with Dissolve(0.5)  
    
    #k "My stand-in ."
    k "My replacement, the highest listed party member who does not yet occupy a seat, is a man named Robert Ligters, who is partial to the church."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt saddened day open at left with Dissolve(0.2)  
    n "I see, someone from the Kuyper faction."

    show karin happy at right with Dissolve(0.5)  

    k "If you want to say it like it is—"
    "Karin laughed wryly."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt saddened day open at left with Dissolve(0.2)     
    n "So, you're saying that due to your incapacitation, the Kuyper faction now controls five of A.I.R's eight seats?"
    show karin serious at right with Dissolve(0.5)    
    k "Yes — and this has greatly disturbed the balance of power."
    k "Together with Flock 05's three seats, the church now holds a political majority."
    k "They can bypass the three agrarian councilmen in our party, and implement new legislation with Flock's support."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt saddened day open at left with Dissolve(0.2)
    k "It's a de-facto coup."
    
    show ina shirt angry day open at left with Dissolve(0.5)  
    k "Leopold has been updating me on the most recent developments, and it's worse than I'd even imagined."
    k "The Kuyper faction and Flock are passing laws left and right — all under the very nose of our mayor, who is powerless to intervene."
           
    "Her voice was breaking. She paused for a moment."
    pause(1)
    
    show karin laughing at right with Dissolve(0.5)  
    k "Oh, these hospital dorms have turned me melancholy—"
    k "Maybe I wasn't suited for politics after all."
    pause(1)
    "A nurse came in, informing us that visiting hours were over."
    
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    
    a "So how long will it take for you to return to work?"

    show karin worried at right with Dissolve(0.5)      
    k "If I stick to my exercises, I should be able to leave the hospital in a few days."
    k "Though even then, it will take a while before I'll be able to return to my duties."
    "She shot us a nervous glance."
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    k "Please don't tell anyone. We don't want to elicit a second \n{i}incident{/i}—"
    show ina shirt angry day closed at left with Dissolve(0.2)      
    show ina shirt angry day open at left with Dissolve(0.2)  
    n "Are you sure you'll be safe at home?"
    
    show karin laughing at right with Dissolve(0.5)       
    k "Oh I'll manage. I'm planning to have Phyrrus stay at my apartment for protection."
    "She winked."
    pause(1)
    a "Villains beware."

    hide karin with Dissolve(0.5)  
    hide ina with Dissolve(0.5)    
    pause(1)
    scene hospital_corridor with Dissolve(0.5)
    pause(1)
    
    k "Good luck on your investigation. You can come visit me again when I'm out."


    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic2:

    scene black with fade
    pause(1)
    #play sound "audio/ventilator.ogg" loop fadein 1.0
    scene hospital with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)

    show ina shirt interested day open at left with Dissolve(0.5)  
    pause(1)
    "As we hung around in the lobby, deciding on what to do next, I suddenly heard a familiar voice."
    pause(1)
    l "So kids, have you delivered your fruit basket?"

    show leo neutral open at right #with Dissolve(0.5)
    show ina shirt angry day open at left 
    with Dissolve(0.5)   
    "I looked over to see Leopold, who had approached us from the side of the restaurant."
    pause(1)
    l "Same Abe, different girl."
    l "I really hope you've found what you were looking for, this time."
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    a "Hi Leopold."
    a "This is Ina, you may know her."
    "I gestured at Ina, who was eyeing the marquis suspiciously."
    
    show leo angry open at right with Dissolve(0.5)    
    "Leopold shot her a cold look."
    l "The town's star journalist." #Our star journalist.
    l "How are you?"
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    n "Fine."         
    "He returned his attention to me."
    l "I'm so glad you've been able to visit Karin. She's made an impressive recovery."
    l "I come here every day, to fill her in on council business. Has she told you what's going on down there?"
    l "It's atrocious, a regular mutiny."
    l "You kids should come along for a glass or two. I want to ask you something—"
    
    pause(1)
    hide leo
    hide ina 
    with Dissolve(0.5)
    pause(1)
    window hide
    stop sound fadeout 2.0
    pause(1)
    scene black with Dissolve(1.0)
    scene ristorante with Dissolve(1.0)

    pause(1)
    window show
    pause(1)
    play music "<from 70.0>audio/0fingal.ogg" loop fadein 30.0
    show leo angry open at right
    show ina shirt angry day open at left 
    with Dissolve(0.5)      
    pause(1)
    l "They're more than I signed up for, these events of late—"
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    l "The Kuyper faction and Flock have effectively hijacked our plenary sessions. All their motions are immediately put to the vote and approved with an eight to six majority."
    l "They have axed all summer labor programs. Blocked the construction of a gas station on the motorway."
    l "And they will be remediating all municipal tax deductions for the agricultural sector."
    show ina shirt interested day open at left with Dissolve(0.5)       
    n "Maybe that isn't so bad—"
    pause(0.5)
    l "Look, I'm no country boy myself — but the farms are our main source of income."
    show ina shirt angry day open at left with Dissolve(0.5)     
    l "However, the thing I'm most worried about is a new package of austerity measures regarding our municipal water management infrastructure."
    l "They're proposing a forty percent budget cut for all drainage and pumping systems"
    l "An incredibly foolish move if you ask me. We need to guard ourselves against the water. These systems are our life-line."
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    l "Please understand. The town in falling into the hands of zealots, without any regard for the public good."
    
    l "I'm a cosmopolitan man, you know. I don't want this place to go down the route of so many backwater towns."

    show leo neutral open at right with Dissolve(0.5)    
    l "You should know what I'm talking about, Abe. You dated that Kuyper girl for a while—"    
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2)     
    n "Excuse me?!"  #facial expression   
     
    a "I never—"
    l "—you know what they're like, these fundamentalists. So principled, so judgmental."
    l "It didn't take you long to trade her in."
    show leo smile open at right with Dissolve(0.5)    
    l "I figure Ina here doesn't make you wait—"
    show ina shirt surprized day open at left with Dissolve(0.5)      
    "Ina let out a disgruntled cough."
    show ina shirt angry day open at left with Dissolve(0.5)  
    pause(2)
    l "Oh, and I was wondering, Abe."
    l "Did saint Anthony show mercy upon your tainted soul?" #this time around? 
    a "What?"
    "He cackled mischievously."
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    l "{i}Anthony of Padua{/i} — the patron saint of lost things. "
    l "I recall you were searching for something — last time we met."
    l "And from John Kuypers' sour expression the following day, I was inclined to assume you may have {i}acquired{/i} it."
    #show ina shirt mirth day open at left with Dissolve(0.5) 
    "I saw a twinkle in his eye." #done before?
    a "Oh yes — um, we did. Most of it, at least."
    
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2)   #TODO maybe blush?  
    "Ina shot me a deathly glare."
    l "I'm impressed — never imagined you kids would pull it off."

    show leo angry open at right with Dissolve(0.5)      
    l "Now look, although I don't want to involve myself too deeply in these matters, I know a lot about the church. "
    
    show ina shirt interested day open at left with Dissolve(0.5)     
    l "I can help you with your investigation."
    l "Police records, council logs — you name it, I can get it."
    l "I could make your research go a lot easier."
    pause(1)
    l "But the thing is—"
    show leo neutral open at right with Dissolve(0.5)      
    l "I've told you, I am a selfish person—"
    pause(1)
    l "A man is nothing without a home — a dry leaf, floating on the wind."
    pause(1)
    n "What do you want?"
    pause(1)
    l "I would love to receive a copy of that appendix document—"
    show ina shirt angry day open at left with Dissolve(0.2)        
    n "That's out of the question!"
    
    show leo angry closed at right with Dissolve(0.5)  
    "For a second I thought Leopold would lose his cool, as he sat toiling under Ina's contemptuous glare."
    
    #tell more about Jan
    
    n "You can't have that document! It's filled with occult nonsense — but I'm sure you already know."
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2)        
    n "There's enough corruption and treachery in this town. We don't need to add a modern day witch trial."
    n "Although I realize that we're currently facing a crucible of journalistic integrity, I draw the line here. Do you {i}understand{/i}?" #???
    show leo neutral open at right with Dissolve(0.5) 
    "Leopold — who had initially endured Ina's exhortation meekly — had already began to regain some of his former cheer."
    pause(1)
     
    l "I apologize, Ina. I didn't realize it was all so bad. I was, regretfully, never in the position to read the text myself—"
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    n "We know."
    l "My gardener, Jan, who put me on the document's trail. He was a little rigorous at times."
    l "He was a Catholic, you see—"
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    l "Anyway, I'd still love to read it. If you ever change your mind, you'll know where to find me."
    "Ina grunted."
    
    show leo smile closed at right with Dissolve(0.5)      
    l "I'm serious."
    stop music fadeout 6.0
    show ina shirt angry day closed at left with Dissolve(0.2)          
    show ina shirt angry day open at left with Dissolve(0.2) 
    "We got up from our seats."
    "On our way out, I thanked the marquis jovially."

    pause(1)
    hide leo with Dissolve(0.5)
    pause(1)
    hide ina with Dissolve(0.5)

    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic3:

    scene black with fade
    pause(1)
    play sound "audio/ventilator.ogg" loop fadein 1.0
    scene diningroom_day with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)


    "After we returned to the house, Ina immediately retreated to her room to read."
    
    "For the rest of the day she remained somber, as though a gray shroud was weighing down upon her."
    "I mostly left her to her own devices, only checking up on her infrequently." #reading book
    pause(1)
    "At around one o' clock I knocked on her door to bring her some coffee. She invited me in."
    
    pause(1)
    stop sound fadeout 1.0
    scene inabedroom_eve with Dissolve(0.5) #day??
    play music "audio/0aase1.ogg" loop fadein 40.0
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    #TODO: maybe different music at first
    show ina cami neutral day open at center with Dissolve(0.5)     
    
    pause(1)
    
    #a "So what did you make of our conversation with the marquis?"
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)  
    n "Leopold is human filth."
    a "I won't deny that—"
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)      
    n "No really. I feel dirty, even talking to him. What a revolting man he is."
    
    "The curtains were drawn. A musty odor permeated the ill-ventilated room, though there was a sweet, tempting aroma hiding within."
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)      
    n "Leopold is clearly the end of his lineage. The dredges of centuries of degeneracy and spiritual failure that have slowly sunk to the bottom."
    
    n "The age of nobility is decisively over. The residue of once-esteemed classes has come to form a layer of filth, coating the sewers of our exhausted society."
    
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)     
    
    n "There's but one terminus to all of the decadency, and that is death. The death of bloodlines, of cultures—"
    a "Ina—"
    n "Although our own death still lies far ahead of us, somewhere in the murky darkness of the coming millennium."   
    a "Ina, please—"
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)         
    n "I'm sorry."
    n "Sometimes I get caught up in depressive thoughts — whenever I read too much."
    pause(1)
    
    "In an attempt to cheer her up, I tried to return her attention to the case."#more

    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2)   
    a "I was thinking about what the marquis told us, about his gardener Jan."
    a "Don't you think it could constitute a motive?"
    a "Clearly Jan was on to something — he knew about the damaging appendix document."
    a "What if it was the {i}church{/i} that tried to take him out — to silence him?"
    a "But then, when they perpetrated the murder, they accidentally killed the {i}wrong guy{/i}. Michel, a different farm worker."
    a "Sounds plausible, doesn't it?"
    
    show ina cami frown day closed at center with Dissolve(0.2)     
    show ina cami neutral day open at center with Dissolve(0.2) 
    
    a "When the body was found, Jan realized the attack was meant for him. So he fled to his hometown, never to return. "
    a "And subsequently the church — who were content, now that Jan was out of the picture — tried to frame the agrarians for the murder, thus expanding their political influence."
    a "Effectively killing two birds with one stone."
    "Though I could tell Ina was hesitant to talk about the matter, a grand apparatus had clearly begun churning inside her head."
    
    show ina cami optimist day open at center with Dissolve(0.5) 
    n "I'm impressed, Abe. You're deductive skills are clearly improving under my mentorship."
    n "To be fair, I've thought about this exact same scenario."
    "An apprehensive look was forming in her eyes."
    show ina cami smile day closed at center with Dissolve(0.2)     
    show ina cami optimist day open at center with Dissolve(0.2) 
    n "But it can't be—"
    "I was taken aback. Though I realized my theory was far from perfect, outright {i}rejection{/i} seemed harsh even for her standards."
    show ina cami smile day closed at center with Dissolve(0.2)     
    show ina cami optimist day open at center with Dissolve(0.2) 
    n "What about the police investigation?"
    n "The police is loyal to the mayor. Why didn't they find the culprit?"
    
    pause(1)
    a "I don't know."
    a "I mean, it's Abbotsford."
    a "Small town police forces are rife with incompetence."
    


    show ina cami smile day closed at center with Dissolve(0.2)     
    show ina cami optimist day open at center with Dissolve(0.2) 
    n "Still, it's impossible. It can't be—"
    
    
    a "If there's one thing we've learnt from the assault on Karin, it's that the church has its ways to deal with dissenters. "
    show ina cami neutral day open at center with Dissolve(0.5) 
    a "Now, I don't know if they used their own people, or if they hired thugs to commit the attacks. It's likely that they didn't even want to {i}kill{/i} their target."
    a "Maybe they just wanted to scare him a little — like they did to Karin — but then they struck too hard and he bled out—"
    a "I mean, judging from the fact that they didn't even get the right guy, we're clearly not dealing with professionals."
    
    "While I was speaking, a languid expression had formed in her eyes."
    pause(1)
    
    
    n "No— You don't understand—"
    show ina cami frown day closed at center with Dissolve(0.2) 
    show ina cami neutral day open at center with Dissolve(0.2)     
    n "It's impossible—"
    
    a "How is it impossible?!"
    
    "Involuntarily I had raised my voice, as I was growing impatient with Ina's complete disregard for my contributions."
    #look at him with pain, crying, more buildup

    #show ina cami crying day open at center with Dissolve(0.2)
    #show ina_cg_1 with Dissolve(0.5)
    scene ina_cg_1r with Dissolve(1.0):
        subpixel True
        xalign 1.0 yalign 1.0
        easein 30.0 xalign 0.0 yalign 0.0  
    "And then she threw herself onto the bed, hiding her face in the palm of her hand."
    #began to cry — very softly, turning away her face to hide the tears. " #"turning away her face, to hide her tears."

    n "I'm sorry, Abe."

    n "It's a good theory, but {i}it can't be.{/i} The mayor's brother, George— He {i}has{/i} to be the perpetrator."
    "She was speaking in a broken voice."
    n "He's a violent man — a very, {i}very{/i} violent man."
    a "Ina—"
    "She paused for a second, as not to let her emotions overpower her."
    pause(1)
    n "Please trust me, I know—"
    a "I'm sorry—"
    n "I know exactly how horrible and vile he is—"
    stop music fadeout 8.0
    pause(1)
    a "Ina, what happened?"
    "I could feel my voice trembling."
    pause(1)
    a "You can tell me—"
    play music "<from 1.0>audio/0aase2.ogg" loop fadein 25.0 
    "And at that moment, everything came to an abrupt halt."
    

    
    #TODO, sit down on bed, CG segment begins
    
    pause(1)
    #scene ina_cg_4 with Dissolve(0.5) #TODO ina crying CG Slight panning?
    scene ina_cg_4r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    pause(1)
    
    "While fighting back the tears, she began to speak."
    pause(1)
    n "{i}Georgie Porgie, pudding and pie—{/i}"
    pause(1)
    n "The age itself has turned irreversibly vulgar. Most people have no idea to what extent they've become tainted—" #expand
    

    n "Like me—"
    n "I've always been drifting—"
    n "From a young age onward — my mother was never there, to hold my hand."
    pause(1)
    n "And for that reason I was always drifting. Because there was no one to guide me."

    
    "She spoke the words in a monotone murmur, as though they had been repeated internally many times."
    

    pause(2)
    n "It happened two years ago, when I was sixteen. "
    n "Ever since elementary school, horseback riding has been my passion."
    n "I relished in the freedom of galloping through the fields — on Potato, my favorite horse. His long brown manes blowing in the wind."
    pause(1)    
    n "We were like nomads, he and I. Drifting together—"
    pause(1)
    n "I'd meet up at the equestrian center in town on Friday afternoons, with a small group of girls."
    n "I had a lot more friends back then. Though I realize now that these friendships were perpetually shallow."
    n "We'd groom and ride horses — talk about horse things."
    pause(1)
    "She exhaled loudly."
    pause(1)
    
    n "I had been warned about George van Linden. He owned the land on which the riding school was situated."
    n "Every kid knew a horror story about George."
    n "He hated children — and was prone to violent outbursts."
    pause(1)
    n "But the thing is — he never really had much to do with the riding school."
    n "It was run by an easy-going couple, and since we were teenagers by then we had a lot of freedom to ride the horses by ourselves."
    pause(2)
    n "Then one Friday, it was just me and my friend Ana. "
    n "We rode the old bridleway around the island."
    n "It was a beautiful summer night."
    n "We could see dragonflies soar among the reeds, and hear cicadas whisper."
    pause(1)
    n "But on our way back, Potato faltered. Likely due to a stone or a shard of glass stuck in his horseshoe."
    n "So I urged Ana to go on without me, as her parents held a strict curfew."
    pause(1)
    n "And I stayed behind, tending to Potato's wounded hoof."
    "I remember his patient warmth, as he let me carefully remove the dirt and stones from his shoe. "
    n "At that time, I felt that there was no one in the world who trusted me as much as he did."
    pause(1)
    n "By the time we returned, it had grown late. It was dark outside, and the town was without sound."
    n "I returned Potato to his stable, applying a thick layer of ointment to his hoof to prevent infection."
    
    #show ina_cg_2 with Dissolve(0.5)
    scene ina_cg_2r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    "By now, warm tears fell steadily from Ina's cheeks."
    #n ""
    pause(1)
    n "And then—"
    pause(1)
    n "I noticed a figure, standing in the doorway—" #more jerky
    pause(1)
    n "It was him."
    pause(1)
    n "I froze." 
    pause(1)
    n "He didn't seem menacing at all this time — as though he were forcefully putting on a display of kindness."
    #pause(1)
    n "He told me, it was getting late—"
    n "—that he would walk me home—"
    #pause(1)
    "Ina was quivering, pushing out the words in bursts of exasperation."
    pause(1)
    n "And I wanted to refuse! I did! But I was afraid to anger him—"
    n "So I meekly allowed him to lead the way—"
    "My whole skin tinged, in visceral reluctance to what was about to come next—"
    pause(1)
    n "But it was useless—"
    n "—of course it was useless—"
    pause(1)
    n "We were barely outside when he grabbed me by the arm—"
    "Her voice broke."

    #show ina_cg_5 with Dissolve(0.5)
    scene ina_cg_5r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
        
    n "He forced me—"
    n "—right there, on the cold, hard ground—"
    pause(1)
    n "He {i}forced{/i} me—"
    
    pause(1)
    
    "And Ina broke out in a flood of tears, as I embraced her silently, knowing there was nothing I could say that would be of any significance."
    pause(1)
    
    n "I showered for two days, trying to wash his disgusting presence off me. Then I locked myself in my room for about a week, as I mustered up enough courage to go to the police."
    n "But at the station they scolded me for not coming earlier — told me that without any witnesses or traces of evidence there wasn't {i}anything{/i} they could do."
    n "And they said that I should have {i}known{/i} about George's reputation."
    
    pause(1)
    
    n "Then I called my mother, who was on tour in Australia — and she sounded so annoyed that I would even call her about something like this."
    n "I don't really think she believed me at the time. Probably thought it was a ruse to make her come home."
    
    "She took a deep breath."
    pause(1)
    
    n "I completely gave up horse riding after that."
    n "I lost most of my friends, as we no longer had any shared interests."
    pause(1)
    n "And worst of all — I lost Potato."
    pause(1)
    
    n "I still turn my head, whenever I hear the sound of hooves in town. Just to see if I might be able to catch a glimpse of him—"
    
    #

    pause(2)
    n "Do you understand now?"
    n "Do you understand why it can only be {i}George{/i} who committed that murder?"
    
    pause(1)
    n "Now you know, what kind of miserable person I am."
    a "No—"
    n "Just say it. I'm a despicable human being — the lowest kind possible. "
    n "How can I call myself a journalist? If I can't even be unbiased in my research?!"
    
    n "I don't deserve to be editor-in-chief of {i}anything{/i}."
    n "I deserve all that has happened to me—"
    
    ##TODO: have her break out into short ideological monologue
    pause(1)
    
    n "A decaying society breeds empty shells of human beings — infantile, brutish, worn out."
    n "They think only in terms of dominance — dominance by the strong, dominance over the meek."
    n "Any true yearn for liberty has been decisively snuffed out—"
    n "—they remain gray, like machines, waiting to be used up."
    pause(1)
    
    n "We wander among the ruins of a greater age, only destined for despair—"
    pause(1)
    ################################################
    "She sighed."
    pause(1)
    n "I'm sorry Abe. I have no right to force all this upon you."
    n "You must hate me. You must feel like I've been leading you on."
    n "And you have the right to be angry—"
    n "I understand if you never want to see me again." 
    pause(1)
    
    ####################################################################################################################################
    
    menu:
        with Dissolve(1.0)
        n "Just tell me—"
    
        #### INA LAST DECISION ###################
        "It may be better if we took a break—":
            "After my curt rejection, her veil of self-loathing suddenly gave way to remorse."
            n "Abe, I'm sorry! I really enjoyed the time we spent together."
            n "I understand that you need your space, and I promise I'll make \namends—"
            n "—but please, could you give me {i}one{/i} last chance?"
            menu:
                with Dissolve(1.0)
                n "Just {i}one{/i}?"
                
                #### INA VERY LAST DECISION ###################
                "I'm sorry, Ina—":
                    #TODO, last remarks
                    pause(1)
                    "I understand."
                    #pause(1)
                    #hide ina with Dissolve(1.0)
                    pause(1)
                    window hide
                    stop music fadeout 6.0
                    pause(1)
                    scene black with Dissolve(4.0)
                    pause(1)
                    
                    jump iBad
                    
                "Okay. {i}One{/i} last chance.":
                    a "We have a murderer to catch, remember?"
                    "She smiled."
        
        "No Ina. That's out of the question.":
        ###
            a "We have a murderer to catch, remember?"
            
            #scene inabedroom_eve 
            #show ina cami optimist day open
            pause(1)
            
            
            "Through her tears I could see a thin smile appear."


    

    ####################################################################################################################################
    
    stop music fadeout 8.0
    scene black with Dissolve(8.0)
    #hide ina with Dissolve(0.5)
    pause(1)
    scene diningroom with Dissolve(2.0)
    pause(1)
    
    "That night I stayed with her and we slept until the late afternoon." #more dramatic


    pause(1)
    window hide
    stop sound fadeout 1.0
    pause(1)
    scene black with fade
    pause(1)
       
label p5Ic4:

    scene black with fade
    pause(1)
    play sound "<from 20.0>audio/summermeadow.ogg" loop fadein 20.0
    scene inahouse with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    "After we woke up, she accompanied me to the store to help me pick out dinner."
    
    #######################################
    
    "But she remained in a despondent mood."
    "We made our way along the pavement, Ina always lagging a few steps behind." #improve
    pause(1)
    "Until suddenly she stopped."
    pause(1)
    "I turned around."
    pause(1)
    show ina pink dissapointed day open at center with Dissolve(0.5)  
    play music "audio/dormant.ogg" fadein 50.0
    pause(1)
    n "Do you want to have children? Abe?"
    pause(1)
    a "E-excuse me?!"
    pause(1)
    n "Well? Do you?"
    n "Do you want to bring new life into this decaying world?"
    n "Could you even look them in the eye?"
    pause(1)
    a "I'm not ready to think about these things—"   
    pause(1)
    
    
    n "When a civilization enters a state of decline, it loses its essential life-force."
    n "That's when people stop caring about procreation."
    n "Having children becomes a fashion statement, something that no longer comes naturally, but has to be carefully measured out."
    pause(1)
    n "At the apex of the Roman imperium, scholars would publish long tracts about the immorality of procreation."
    "She moaned."
    show ina pink grave day open at center with Dissolve(0.5)     
    n "I couldn't imagine going through child-birth."
    n "Having my body subjected to something so {i}instinctive{/i}."
    

    pause(1)
    hide ina with Dissolve(0.5)
    stop sound fadeout 1.0
    pause(1)
    play sound "audio/0rainsoft.ogg" loop fadein 5.0
    scene ichthys_rai with Dissolve(0.5) 
    pause(1)
    
    "And as we walked further — a sticky, lukewarm precipitation began to rain down from the sky."
    
    "This immediately caught Ina's attention."
    pause(1)
    show ina pink smile day open at center with Dissolve(0.5)  
    pause(1)
    n "It's raining."

    "She looked up at me."
    pause(1)
    n "That's the first time, in a very long time—"
    #show ina pink smile day open at center with Dissolve(0.5)      
    "A thin smile had appeared on her lips. "
    pause(1)
    a "We should head back home to get an umbrella."
    n "Oh, who cares about umbrella's!"
    n "The rain is back."
    n "Can you smell nature's funeral bouquet? The fungi, the rotting leaves?"
    n "It's invigorating! "
    n "Maybe autumn will come after all."
    pause(1)
    n "Come on, let's go home. I want to make a newspaper!"
    pause(1)
    a "I thought we'd lost our funding."
    n "Oh, who cares about funding!" # Paper and ink is all we need!"
    
    pause(1)
    hide ina with Dissolve(0.5)
    stop music fadeout 2.0
    pause(1)
    stop sound fadeout 1.0
    scene diningroom with Dissolve(0.5) #or ina house at night rain?
    play sound "audio/0roomrain.ogg" loop fadein 1.0
    pause(1)
        
    "That night — to the constant noise of torrential rain beating against the window — we worked on our big feature article."
    
    "Slowly we assembled the puzzle pieces that we'd gathered over the last weeks."
    
    "Ina was the best mood I'd seen her since we broke into Kuyper's office." #since reading that weird document
    pause(1)
    
    "But in the end it turned out that there was still a lot missing. Too much to make up a convincing case."
    #TODO, little better explained
    pause(1)
    "Fully exhausted, we turned in for the night."


    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic5:

    scene black with fade
    pause(1)
    play sound "audio/0roomrain.ogg" loop fadein 1.0
    scene inabedroom_eve with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)


    "Next morning, Karin called to tell us that the Kuyper faction had used their new-gained political agency to obtain full executive control over the municipal water board, in an unprecedented display of power."
    
    "Though I couldn't fathom why such a bureaucratic victory was anything worth panicking about, Ina appeared highly alarmed by the whole situation."
    
    show ina cami astonished day open with Dissolve(0.5)  
    
    n "We're in trouble! If Kuyper controls the water, he controls the entire town!"
    
    show ina cami frown day closed at center with Dissolve(0.2) 
    show ina cami astonished day open at center with Dissolve(0.2) 
    
    n "There's a wholescale coup going on, and we don't even have a free press to report on it."
    
    "I shrugged and put my clothes on."
    
    show ina cami neutral day open at center with Dissolve(0.5)  
    
    n "Where do you think you're going?"

    show ina cami frown day closed at center with Dissolve(0.2) 
    show ina cami neutral day open at center with Dissolve(0.2)     
    
    a "To school."
    a "Unlike some, I still very much intend to graduate this year."
    a "We'll look into this later today."
    
    show ina cami astonished day open at center with Dissolve(0.5)     
    n "Hmpf."
    n "Please hurry back."
    #n "She's not a {i}friend{/i} — you know?"
    #pause(1)
    #n "I don't like being left alone."
    #a "It's worth a try. She's been very informative in the past."
    #a "She may be able to shine a light on all of this."
    
    #### Meet up with Mei (at Rika's house)
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    scene black with Dissolve(1.0)
    pause(1)
    scene pool with Dissolve(1.0)
    pause(1)
    window show
    pause(1)
    
    "I showed up early, heading down to the pool where I expected to find Rika."
    "The swimming team had just dried off from their morning workout, its members gradually emerging from the changing rooms."
    
    #TODO view of lockers??
    #name her ruth
    pause(1)
    play music "audio/0goldberg22.ogg" loop fadein 10.0
    
    show naomi cautious with Dissolve(0.5)
    pause(1)
    u "Excuse me, are you looking for someone?" #have her wear bikini?
    "A bespectacled girl had approached me — clearly distrustful of my intentions."
    a "Yeah— eh, Rika. Rika Kuyper. Is she still in there?"
    u "Trying to catch a glimpse of our star athlete?"
    u "Well I can inform you she hasn't shown up to practice since the weekend."
    u "I'm not sure what she's doing, but I suspect the coach has her on a private training schedule."
    u "He {i}always{/i} plays favorites."
    pause(1)
    a "That's okay, thank you. I'll go by her home."
    
    show naomi irked with Dissolve(0.5)
    u "Please respect her privacy!"
    pause(1)
    hide naomi with Dissolve(0.5)
    pause(1)
    stop music fadeout 2.0
    scene black with Dissolve(1.0)
    play audio "audio/schoolbell.ogg"
    scene woodhouse_rai with Dissolve(1.0) #rain?
    play sound "audio/0rainsoft.ogg" loop fadein 1.0
    pause(1)

    "Just as the bell rang for first term, I set off back towards town." #SFX
    
    pause(1)
    scene postbox_rai with Dissolve(0.5) #TODO rainy street
    pause(1)
    
    "The Kuyper family resided in a large manse that was centrally situated in an affluent neighborhood. "
    
    "As I approached the gate, I felt a certain reluctance take hold of me."
    "I dreaded that Rika's father would answer the door — that he'd maybe recognize me, from descriptions that had been passed around within the church."
    "And as the rain fell steadily, it occurred to me that it had been pouring incessantly ever since yesterday afternoon. As though the heavens had some catching up to do, for the drought of the past weeks."
    "Warnings had been coming in on the radio, about the adverse consequences of heavy precipitation after a period of drought."
    "The rain could erode the brittle soil, carrying away large amounts of earth through the waterways — eventually clogging the drainage systems downstream."
    
    pause(1)
    
    "When I arrived at the residence, I encountered a miserable-looking Mei."
    
    show mei dress regret day open at center with Dissolve(0.5) 
    play music "audio/walkure_gentle.ogg" loop fadein 20.0
    
    m "She's not home. She hasn't been home since Sunday. "
    show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret day open with Dissolve(0.2) 
    m "The maid said she was at a swimming camp. But I know that isn't true."
    m "Rika told me she was leaving for the pumping station in Ryebury. That she had some important maintenance work to do, now that there was a changing of the guard at the water board."

    #show mei dress regret day closed at center with Dissolve(0.2) 
    
    
    m "I was afraid she'd gone with you, Abe. Leaving me behind."
    show mei dress interested day open at center with Dissolve(0.5)     
    m "I'm glad to see you're looking for her too."
    
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress interested day open with Dissolve(0.2) 
    a "The pumping station? Did she tell you what she would be doing?"
    m "Oh no, she didn't. But she made it sound {i}very{/i} important."
    m "Important — and a bit mysterious."
    
    show mei dress earnest day open at center with Dissolve(0.5)     
    "Then Mei smiled."
    m "Oh well, we'll have to hang around till she returns."
    m "Let's go and explore. Granite becomes so {i}beautiful{/i} in rainy weather."
    a "I'm sorry Mei. We'll have to do this another time."
    a "I— uh, have to get back to school, before they notice I'm gone."
    show mei dress surprised day open at center with Dissolve(0.5)       
    m "Playing truant on a weekday?"
    show mei dress estatic day closed at center with Dissolve(0.5)
    m "You're a lost cause!"
    
    pause(1)
    hide mei with Dissolve(0.5)
    stop music fadeout 2.0
    pause(1)
    stop sound fadeout 1.0
    scene inahouse_rai with Dissolve(0.5) #rain
    play sound "audio/0rainsoft.ogg" fadein 1.0
    pause(1)
    
    "Not planning to return to school anytime soon, I went straight to Ina's house. "
    
    "The news of Rika's suspicious behavior activated her immediately." 
    
    "Together, we left for the station, hurriedly, as the next train was about to leave."


    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic6:

    scene black with fade
    pause(1)
    scene trainin_nig with Dissolve(0.5) 
    play sound "audio/train.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)
    "We took the train to Ryebury—"
    #TODO do something that suggests they traveled there
    pause(1)
    stop sound fadeout 1.0
    scene pumpingstation with Dissolve(1.0) #rain
    play sound "audio/0seawaves.ogg" loop fadein 1.0

    pause(1)
    "—after which I led Ina to the pumping station."
    pause(1)

    a "This is it, it looks deserted."
    "I felt the door, which didn't budge."
    pause(1)
    a "It's locked."
    pause(1)
    show ina shirt angry day open at center with Dissolve(0.5)    
    pause(1)
    n "It's {i}still{/i} locked — you mean. Please get out of the way."
    "After rummaging around in her handbag, Ina produced a small lock-picking set." 
    play audio "audio/0lockpick.ogg" 
    show ina shirt angry day closed at center with Dissolve(0.2) 
    show ina shirt angry day open at center with Dissolve(0.2)  

    
    pause(2)
    stop sound fadeout 1.0
    scene pumpingstation_hall with Dissolve(0.5) #SFX muted rain sounds
    play sound "audio/0roomrain.ogg" loop fadein 1.0 
    pause(1)
    
    "Two minutes later we were inside." #standing inside the building
    
    show ina shirt defiant day open at center with Dissolve(0.5) 
    n "Quiet now. Rika could be lying in ambush." #laying in ambush?
 
    pause(1)
 
    a "I don't think there's anyone here."
    
    "We searched the main floor of the deserted building, looking for signs of tampering. But to no avail."
    
    n "I'm going down to the basement, where the pumps are."
    
    show ina shirt mirth day closed at center with Dissolve(0.2) 
    show ina shirt defiant day open at center with Dissolve(0.2)    
    
    n "You stay up here to keep a look out. If you see the front door open, just hide and call my phone."
    "I nodded."
    
    hide ina with Dissolve(0.5)
    "As Ina descended the large spiral staircase, I stayed behind — watching the entrance with a hawk's eye."
    play music "audio/0gurglingmute.ogg" fadein 20.0
    "Up until now Ina's excursions had always felt like a game. A way to keep her overactive mind distracted from the myriad neuroses that lay behind her hazel eyes."
    "Even the break-in at the church had felt like a senior prank to me — no worse than the tricks we pulled back in high-school."
    "But now, as I stood here waiting, in this decrepit, moldy testament to 1950s water engineering — a creeping sensation began to take hold of me."
    "I hadn't expected I'd become so {i}involved{/i}—"
    
    play audio "audio/0attack.ogg"
    show pumpingstation_hall with vpunch
    
    
    "Suddenly an intense pain shot through me." 
    
    stop music fadeout 0.5
    play audio "audio/0attack.ogg"
    play music "audio/1pianoboss.ogg" loop fadein 2.0 #"audio/0panictheme.ogg"
    show pumpingstation_hall with vpunch
    
    r "So {i}there{/i} you are! Glad to see you've joined the cause."
    
    show rika dress unhappy day open at center
    show bible at center
    with Dissolve(0.5)     
    
    "Rika was wielding a heavy, leatherbound tome. She struck it at me again, twice, in rapid succession."
    play audio "audio/0attack.ogg"
    pause(0.3)
    play audio "audio/0attack.ogg"
    show redhaze with Dissolve(1.0)
    "My vision began to tinge a blood red, as I cowered under her assault." #TODO red filter

    r "I see you two've been playing detective again."
    r "I'm glad I stayed behind to keep an eye on things. Our church caretaker informed me about Ina's fine lockpicking-skills."
    
    a "Rika! What are you {i}doing{/i}?"
    
    show rika dress mischievous day open with Dissolve(1.0)
    
    r "{i}God is jealous, the LORD avenges;{/i}"
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    r "{i}The LORD avenges and is furious;{/i}"
    r "{i}The LORD will take vengeance on His adversaries;{/i}"
    
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
     
    r "{i}And He reserves wrath for His enemies;{/i}"
    r "{i}The LORD is slow to anger and great in power;{/i}"
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    r "{i}And will not at all acquit the wicked.{/i}"    
    
    pause(1)
    "Then suddenly, a furious voice rang out."
    #show rika dress unhappy day open with vpunch

    


    #show rika uni sad day closed at left with Dissolve(0.5)
    hide rika 
    hide bible
    with Dissolve(0.1)
    
    show rika dress unhappy day open at right behind redhaze
    show bible at Position(xpos = 0.9, xanchor=0.75) behind redhaze
    with vpunch
    show rika dress unhappy day open at right behind redhaze
    show bible at Position(xpos = 0.9, xanchor=0.75) behind redhaze
    with vpunch
    n "Rika!"
    "Ina had appeared from the stairwell — brandishing a glass bottle that appeared to contain a clear liquid. Rika leapt back in apparent shock." #FX: have rika vpunch to right
        
    show ina shirt pitiful day open at left behind rika with Dissolve(0.5) 
    n "Get away from him!"
    n "Get away go or I'll throw it!"
    show ina shirt angry day open at left with Dissolve(0.5) 
    n "What is it, anyway?"
    show ina shirt angry day closed at left with Dissolve(0.2) 
    show ina shirt angry day open at left with Dissolve(0.2)   
    n "I've seen your little setup down there."

    n "Is it acid? To eat away at the centrifugal pump?"
    
    #show rika uni sad day open at left with Dissolve(0.5) 
    r "Stop shaking that bottle! You harlot!"
    r "If you throw that, we'll all blow up!"
    "Ina remained disquietingly calm under the prospect." #ominously
    show ina shirt angry day closed at left with Dissolve(0.2) 
    show ina shirt angry day open at left with Dissolve(0.2)   
    n "Why are you doing this, Rika? Sabotaging the pumping station?"
    n "What's the point?"
    show rika dress mischievous day open with Dissolve(0.5)
    r "Oh Ina, you have {i}such{/i} an analytical mind."
    r "It's so sad we don't have a school paper anymore, for you to put these deductions into writing."
    "Ina snarled."
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    #r "The thing is, I hate irrigation systems. 
    r "Mankind has become so arrogant."
    r "Like gods, they deem themselves, creating land from water. With their miserable pumps and drainage systems."
    r "But what fun is it, to manipulate the water like that?" #meh
    show ina shirt angry day closed at left with Dissolve(0.2) 
    show ina shirt angry day open at left with Dissolve(0.2)   
    #show rika uni mischievous day open at left with Dissolve(0.5) 
    r "Wouldn't it be a lot more natural, to let everything follow its original course?"
    
    r "The rains will continue to fall over the next weeks, and the waters will converge and become far too much for an old, inefficient pumping station to handle."
    show ina shirt angry day closed at left with Dissolve(0.2) 
    show ina shirt angry day open at left with Dissolve(0.2)   
    r "A flood, a magnificent deluge, will wash away these idle contraptions of man."
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    r "Abbot will be an island again. A beautiful island, in the midst of a stormy sea."
    r "Don't worry, the school is built on high ground. We may even let you relaunch the Sunday Abbot again, if you promise to stop publishing these hateful lies."    
    n "Y-you're insane, Rika! Centuries of in-breeding have taken their toll on your family!" #bloodline
    show ina shirt angry day closed at left with Dissolve(0.2) 
    show ina shirt angry day open at left with Dissolve(0.2)   
    r "Oh, not at all! I have been authorized to preform this covert modification by the Abbotsford water board."
    r "It has all been ratified by the town council."
    r "But you should know all about—"
    
    play audio "audio/0attack.ogg"
    show pumpingstation_hall 
    hide ina Dissolve(0.5)  
    with vpunch
    show pumpingstation_hall 
    with vpunch
    
    "And suddenly — mid sentence — Rika swung her Bible at Ina, who was caught completely off-guard."

    "With a loud cry, Ina dropped the glass vessel into the stairwell, and as it shattered she had just enough time to dive in our direction before—"
    play audio "audio/explosion.ogg" #TODO interject in the text   
    stop music fadeout 1.0    
    show pumpingstation_hall with vpunch  
    hide rika 
    hide bible
    with vpunch
    scene pumpingstation_hall 
    show redhaze
    with vpunch    
    "—a loud explosion shook the building on its foundations."

    scene pumpingstation_hall 
    show redhaze
    with vpunch   

    play audio "audio/swipe.ogg"
    show ina shirt surprized day open at center with Dissolve(0.4) 
    n "Come on Abe, run!"
    hide ina with Dissolve(0.2)
    scene pumpingstation_hall 
    show redhaze
    with vpunch   
    stop sound fadeout 1.0
    scene pumpingstation with Dissolve(0.5)
    play sound "audio/0rainsoft.ogg" loop fadein 1.0
    
    "She grabbed me by the hand — and as we made our way out of the front door, I could hear Rika's maniacal laughter behind us."

    
    r "Thanks, Ina! This is the kind of sabotage I could only have dreamt of!"
    r "And to think that we have such a {i}convenient{/i} scapegoat now!"
    r "You're an asset to the cause!"

    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic7:

    scene black with fade
    pause(1)
    play sound "audio/train.ogg" loop fadein 1.0
    scene trainin_nig with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    
    "As the train rode through the murky fields, we were witness to the first effects of the persistent rainfall, which was submitting countless acres of arable land to a rapid process of paddyfication."
    
    "Ina had just made a phonecall to the police, to report the damage to the pumps."
    pause(1)
    show ina shirt angry day open with Dissolve(0.5) 
    pause(1)
    n "It's no use. They said they'd redirect our report to the municipal water board."
    n "But the church {i}controls{/i} the water board. They'll obstruct all efforts to restore the pumps."
    
    show ina shirt saddened day open with Dissolve(0.5) 
    n "All that water. It's slowly seeping in. "
    n "Just think about all the creatures that will drown."
    
    show ina shirt angry day closed with Dissolve(0.2) 
    show ina shirt saddened day open with Dissolve(0.2)     
    
    n "I can't believe they'd go this far—"
    
    #reflect on how crazy Rika is
    
    hide ina with Dissolve(0.5)
    
    pause(1)
    stop sound fadeout 1.0
    scene inabedroom_eve with Dissolve(1.0)
    play sound "audio/0roomrain.ogg" loop fadein 1.0 
    pause(1)
    
    #
    # Or try this:
    # Ina had gone back to reading in her room, and I wasn't even sure if my presence was still required at the house. (she's depressed.)
    # I knocked on the door.
    # Come in.
    # (Have her do some metaphysical sounding sentences, the start the dialogue.)
    
    "At home Ina remained restless, checking the news every other minute."
    
    #TODO: have her play an old record???
    pause(1)
    show ina cami neutral day open with Dissolve(0.5) 
    pause(1)
    
    n "The lower lying lands are flooding, thousands are going to be displaced."
    n "The water's reached the city, and the towns. Only Abbotsford will remain dry, due to its relative elevation."
    show ina cami frown day closed with Dissolve(0.2) 
    show ina cami neutral day open with Dissolve(0.2)   
    n "Thus ends the transient era of man."
    pause(1)
    a "What do you mean by that?"
    show ina cami optimist day open with Dissolve(0.5) 
    "Her lips curled into a bittersweet smile."
    show ina cami smile day closed with Dissolve(0.2) 
    show ina cami optimist day open with Dissolve(0.2)   
    n "Oh— I don't know. Don't you think there's a certain poetry to it all?"
    n "The sea avenging itself on a civilization that has reached too far—"
    pause(1)
    "I sighed."
    "There was something in the cavalier nonchalance with which she spoke the sentence, that rubbed me the wrong way."
    show ina cami smile day closed with Dissolve(0.2) 
    show ina cami optimist day open with Dissolve(0.2)
    a "Please stop, Ina—"
    a "Lives are in danger. You can't just make light of the situation—"
    
    pause(0.5)
    hide ina with Dissolve(0.5)
    
    "Wordlessly she walked over to her cabinet, where a small cd-player stood."
    "She took out a disk and placed into the drawer."
    pause(1)
    play music "audio/0credo.ogg" loop fadein 30.0
    n "Please listen to this."
    n "It's the Credo from {i}Victimae Paschali Laudes{/i}, composed by the renaissance composer Giovanni Animuccia."
    n "Music from a more vivacious age—"
    
    pause(1)
    "She threw herself on the bed."
    pause(1)
    #show ina_cg_3 with Dissolve(0.5)
    scene ina_cg_3r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0    
    pause(1)
    
    n "Do you know what it is, Abe?"
    n "I can't think. "
    
    pause(1)
    n "I'm sorry. I'm worthless."

    n "I can't think—"
    pause(1)
    n "I can only regurgitate—"
    #If there's one thing that has revealed itself to me now, it's how little of an original thinker I am."
    "She held silent for a moment, focusing intently on the music, as though she were deriving a sheltering comfort from the warming sounds."
    pause(1)
    n "My thoughts are led along a transfixed path, necessitated by the logic of time."
    n "I cannot go outside that path—"
    n "—at most I can dutifully laugh at the primitive mythologies of our forefathers."
    n "But to even grasp at the ideas that future man might hold—"
    
    "I stared at her, not fully understanding the significance of her words."
    pause(1)
    
    n "We uncover things. We demystify them. "
    n "Such is the plight of the fully enlightened mind. To shine a light into every dark corner of the modern world."
    pause(1)
    n "Do you believe in God? Or in the giant serpent?"
    "Before I could answer, she interrupted me."
    
    n "Of course not. Neither do I."
    n "To conjure up myths, to believe in Gods — surrendering to such childish fancies — has become entirely impossible to us."
    
    n "But that's just because we're forced along the timeline of history, to which all abstract thought acquiesces if it wishes to be taken seriously—" #genealogical 
    n "We have the outlook of cynical seniles."
    n "We can no longer fathom the youthful brilliance that springs from such intense religious devotion."
    n "We can only wait, bitterly, till the end."
    
    #pause(1)
    #scene ina_cg_2 with Dissolve(0.5) #TODO Ina crying
    scene ina_cg_2r with Dissolve(2.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0    
    #pause(1)
    
    n "You see, that's why I don't really care—"
    n "I don't care if Rika wins. If everything is swept away in a giant tidal wave."
    n "The world wouldn't be much worse of, would it?"
    pause(1)
    n "Just look at the squalor — it stretches in every direction."
    n "Look at what civilization has become."
    
    "Ina had become visibly emotional."
    pause(1)
    
    #nature suffers, agrarian revolution has become absolute"
    n "Cultivated land reaches as far as the eye can see. We control every aspect of our world. "
    n "We lace every square inch with gallons of ammonium nitrate, just so that mother earth can continue to exhaust her barren womb—"
    n "—and then we drench each of her fruits in pesticide, just in case the tiniest bug would dare venture near it."
    
    n "Nature shrivels beneath the absolute dominance of mankind. {i}Every{/i} aspect is out of sync."
    n "Bee populations decrease each year — butterflies emerge from their cocoons prematurely, horribly deformed, tricked by the false onset of spring."
    pause(1)
    n "And these crickets, these deafening crickets."
    n "I can hear them, even here. In the early morning, the dead of night."
    n "Their chilling death-wail resounds through my mind incessantly—"
    pause(1)
    n "It's the apotheosis of the agrarian revolution. No corner of the world remains untouched—"
    
    pause(1)
    
    n "And it's not just a societal transformation, it goes further — it changes the people {i}themselves{/i}."
    
    #tension between city and countryside
    n "The world is dotted with large metropoles, filled to the brim with parasitical city dwellers."
    n "They're cynical, traditionless, religionless, rational, clever, smug, polite. And all so highly contemptuous of the countryman."
    n "At times it is as though the cities meld together, to form one large, pulsating whole of limitless dystopia. "
    #new man?
    pause(1)
    n "The urbanite considers it a blemish on modernity — that isolated spots of rural elegance can still exist. "
    n "Places where life isn't governed by rosters and indicators and emancipated reason — but where customs prevail that are fundamentally {i}anti-modern{/i} in nature."
    n "In the name of reason, they foster an irrational hatred of all that they paradoxically deem irrational. "
    
    n "I am glad to see that there are still pockets of darkness left in this world."

    n "That I was wrong—"
    n "That there truly are entities hidden that would drive the rational mind far beyond the brink of insanity."
    pause(1)
    #
    #modernity is at it's end
    n "The modern world has become arrogant."
    n "It has uncovered the secrets of nature, of space, and it moves towards the future, relentlessly, ever forward — confident in its belief that a regression into a more primitive state is impossible."
    n "But can their civilization truly break free from the cosmic cycles of time? Can it truly keep moving, ever forward, without one day giving way to the greatest decline and fall of history?"
    n "When that eventually happens — there {i}will{/i} be a dark age upon us. Darker and more brutal than any precedent middle-age."
    pause(1)
    n "First, cultures are born—"
    n "—then they blossom—"
    n "—and then they fall. "
    n "No culture can escape that cycle of life, no matter how feverishly it reaches for the stars."
    
    n "And our civilization is about to tumble — even though it's too arrogant to realize it yet."
    n "It's still childishly staring upwards, into the cosmic expanses of future infinity — not acknowledging that it is crumbling at its foundations, that its children are dying from neglect and decadence."
    n "Its head is raised far too high, among the stars, which revolve to the soul-enchanting tones of Beethoven's Ninth—" #check if this is ok
    
    n "—these intoxicating tones!"
    pause(1)
    n "Do you know, many consider the classical symphony orchestra to be the highest manifestation of our culture? "
    n "The way these instruments converge, to form harmonies that sublimate, each individually, into something that is far greater than the sum of its individual parts."
    n "That is the dialectic of the Faustian spirit, condensed into a four-movement symphony."
    
    pause(1)
    scene ina_cg_5r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0      
    pause(1)
    
    n "That reminds me—"
    n "For my eighteenth birthday, last July— "
    n "My mother dedicated a concert to me."
    
    n "She arranged me to fly out to New York, where she was touring at the time with the {i}Royal House of Tudor Choir{/i}."
    pause(1)
    n "It wasn't even a specially organized concert — just one that was part of her tour. "
    n "But at the beginning, she acknowledged me in front of the audience — she had the choir humiliate me with a rendition of the birthday song."
    n "Who could have imagined a worse birthday? I was mortified, encumbered, jetlagged—"
    n "I even missed our printer's deadline due to the whole charade. "
    
    #start crying around here
    pause(1)
    "Ina looked at me with a look of sheer agony in her eyes."
    pause(1)
    
    n "And the thing is—"
    n "As grandiose as the whole gesture was — it wasn't really about {i}me{/i}. " #where to lay emphathis
    n "I was invisible in the crowd, all alone, looking up at my mother, as she preformed in all her majesty. Elevated, distant, exalted—"
    n "—as out of reach as ever. "
    
    pause(1)
    #expand
    n "They performed this piece."
    n "{i}This{/i} piece! My favorite!"
    n "But how dare she try to interpret something so pure?"
    n "How dare she place her contaminating hands on the artistic expressions of our civilization's youthful years?"
    pause(1)
    n "She can't pretend to know the suffering in our world, if she wasn't even present for her own daughter—"
    n "—in the very darkest time of her life." 
    #My mother! My very own mother! Who hadn't even been there to console me, on the very day my world shattered!"
    pause(1)
    #scene ina_cg_4 with Dissolve(0.5)
    scene ina_cg_4r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0      
    pause(1)
    
    n "And now—"
    n "—the symphony has reached its final movement."
    n "Modernity decays — having completely  lost all intuition and purpose."
    n "It's calling to be euthanized, to be shredded into the fertilizer for younger, more vigorous cultures to come—"
    n "—each filled with vibrant young people that forego thought in lieu of pure, unmitigated experience."
    pause(1)
    n "But for us, it's the end of the road—"
    n "—we might just as well—"
    stop music fadeout 8.0
    pause(1)    
    "I stopped her."
    pause(1)

    a "I can't listen to this any longer."
    
    "She looked up at me, glassy eyed."
    pause(1)
    a "Where do you keep the appendix document?"

    pause(1)
    n "It's on my desk. But why—"
    
    a "Ina—"
    a "If we give up now, we'll become just like the people you so \ndespise—"
    pause(1)
    n "It's no use, Abe—"
    "Her voice sounded exasperated."
    n "It's no use."
    n "You need to understand, it's not the {i}people{/i}—"
    pause(1)
    n "It's not like there's any honor left in anything—"
    
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Ic8:

    scene black with fade
    pause(1)
    play sound "audio/0rainsoft.ogg" loop fadein 1.0
    scene sandford_rain with Dissolve(0.5) 
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)
    play music "audio/0forgottendreams.ogg" loop fadein 12.0
    show leo neutral open with Dissolve(0.5)  
    pause(1)
    
    l "Quite the weather we're having."
    l "I've been dealing with reports of leaks and flooded basements all morning."

    l "I hate water. It gets everywhere—"
    
    show leo smile open with Dissolve(0.5)
    
    l "But I shouldn't complain. We're fortunate."
    l "You know this town is situated higher than the surrounding landscape? All the farmers have begun evacuating their livestock."
    #TODO livestock sounds??
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)   
    l "I figure you've brought the copies?"

    "Wordlessly I handed him a brown paper envelope."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)    
    l "I knew you kids would come to your senses. Politics is a game of give and take, you know."
    l "Sometimes you have to go against your beliefs — but it's the greater good that matters in the end."
    
    a "I hope you're right."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2) 
    l "I like you Abe, I really do."
    l "You remind me of my son sometimes. He's just a bit older than you, studying romantic theater in the city."
    l "But unlike you, he has no sense of politics at all." #He doesn't understand them—"
    l "With him it's all lofty principles — world peace and human rights and whatnot."
    l "He doesn't realize, that once you're in the political arena — your face marred with sweat and dust — that you sometimes need to make tough decisions to get your way."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)     
    l "You're a much more worldly man than he is. You understand, that no matter how good your intentions are, it's the {i}consequences{/i} that count, in the end."
    
    "Leopold was beginning to ramble. I had to cut him off."
    pause(1)
    a "So you think you can solve this mess?"
    show leo angry open with Dissolve(0.5)
    l "It'll be tough, I'll need to pull some strings."
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2) 
    l "Some {i}crossbow{/i} strings, if you know what I mean—"
    l "Do you know the current whereabouts of that Kuyper girl?"
    
    a "She's probably still in Ryebury."
    show leo angry closed with Dissolve(0.2)
    show leo angry open with Dissolve(0.2)     
    l "Then you go there — keep her busy, make sure she doesn't leave."
    l "I'll meet you at the shore in a few hours."
    
    show leo smile open with Dissolve(0.5)     
    l "Just look at it, beautiful Sandford house. The seat of my forefathers."
    l "I can't wait to walk through its halls again, restored to my rightful position as lord of the isle."
    
    pause(1)
    hide leo with Dissolve(0.5)
    stop music fadeout 5.0
    pause(1)
    window hide
    pause(1)

    scene black with fade
    pause(1)
       
label p5Ic9:

    scene black with fade
    pause(1)
    play sound "audio/train.ogg" loop fadein 1.0
    scene trainin_nig with Dissolve(0.5) 
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    #TODO mention how he's in the train, how it's busy at the station, trains are hardly able to operate

    "It took me a while to reach Ryebury."
    "Although the trains were still running, the station was packed with refugees who'd been streaming in from the surrounding villages."
    "The outbound train was completely empty."

    #Karin has retaken her seat, has initiated emergency override of council.
    #Leopold can show up with doggo.
    pause(1)
    stop sound fadeout 1.0
    scene lake_storm with Dissolve(1.0) 
    play sound "audio/0searoarrain.ogg" loop fadein 1.0
    pause(1)
    
    "When I arrived at the shore, I encountered Rika, staring intently at the turbulent waters of the lake."
    play audio "audio/0gurgling.ogg" fadein 10.0
    "And it was as I approached her, that I grew aware of a strange murmur emerging from her throat."
    "It was an unnatural, guttural sound, unlike any other human speech."
    
    pause(1)
    #scene rika_cg_3 with Dissolve(0.5)
    scene rika_cg_3r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0    

    pause(1)
    
    "As soon as she noticed me she turned around, a smile appearing on her lips."
    play music "audio/0gloria.ogg" fadein 30.0
    pause(1)
    r "Ever since I was a child I've dreamt of water."
    r "A breathing water, that permeates everything."
    r "Washing ashore. Rinsing away the stench."
    r "I've always hated that stench."
    r "The putrid pig excrement that the farmers throw on their fields—"
    
    pause(1)
    
    scene rika_cg_2r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 50.0 xalign 1.0 yalign 0.0
    
    pause(1)
    
    r "Oh Abraham, I'm so glad you've come to witness this moment of glorious retribution."
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)   
   
    
    r "It's no easy task, to identify when Abbot's misery began."
    r "For so many centuries, forces from outside have laid war upon us, on our traditions—"
    r "Violent missionaries, greedy lords — they tried to dominate the inhabitants of our isle, ever since their first ship arrived."
    r "And this subjugation was perpetuated, even after the world became enlightened."
    r "With the dawning of the modern age, their domineering interference never faltered—"
    r "—no, exactly the opposite was true."
    r "With emboldened zeal these rational, disenchanted men came for us — the last pocket of undiluted heritage within their modern world."
    r "And their methods of cruelty became all the more methodical. "
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)  
    
    r "How can a civilization become so overconfident? To deem itself worthy to meddle with God's creation in such a way that it becomes fundamentally degenerated in every sense?"
    r "How can you look upon such a society? That has completely poisoned the land and spews corruption from every orifice?"
    r "Can you truly look upon such a world? Without innately harboring the visceral urge to orchestrate its very obliteration?"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)  
    
    "A malevolent glare had appeared in Rika's eyes."
    
    #scene rika_cg_1 with Dissolve(0.5)
    scene rika_cg_1r with Dissolve(3.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    r "We are one. We and this forsaken isle."
    r "Our destinies are intertwined to such an extent, that disentwinement would entail a procedure akin to murder."
    r "How often have they tried to separate us? Through eviction, through coercive land-deals."
    r "But all is vanity, for Abbot and its inhabitants remain one — indivisible."
    r "We would not leave our homestead behind, not even in our darkest hour!"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)  
    
    "The storm grew stronger, and through my squinted eyes thought I saw a hypnotizing black ribbon, winding its way through the furious waves."
    
    pause(1)
    
    r "But now a new evil is upon us!"
    r "Every century it develops new schemes, new ploys to jeopardize our very existence."
    r "O Abraham, you have seen how it operates. How it attempts to demonize us, through its wicked and treacherous ways."
    r "Us, the original inhabitants of this land — as though we do not have the first right to live here!"
    r "We have waded through tides of darkness. Wandered in loneliness."
    r "So long have we witnessed death encroach upon our isle, standing powerless against forces that seemed far greater than ours."
    pause(1)
    r "I want to protect our world — this world, that is so fragile."
    r "So much injustice has come our way, over the course of centuries, hellbent on destroying that small flame of hope that remained."
    r "But there exist forces, that are not so easily silenced."
    r "That rest silent — in impenetrable depths of endless sea and under the soil of the land reclaimed."
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)  
    
    r "These forces cannot be banished by human acts, they cannot die."
    r "They lie silently in wait, slowly building up a bitter resentment against humanity—"
    
    pause(1)
    scene lake_storm with Dissolve(1.0) 
    pause(1)    
    
    "Suddenly a loud voice boomed out over the shore."
    pause(1)
    
    "{i}I stood upon the sand of the sea!{/i}"
    
    pause(1)
    show leo angry open at right with Dissolve(0.5)
    pause(1)
    
    l "{i}And I saw a beast rise up out of the sea, having seven heads and ten horns, and on his horns ten crowns, and on his heads a blasphemous name.{/i}"
    l "{i}And I saw and angel come down from heaven, having the key of the bottomless pit and a great chain in his hand.{/i}"
    l "{i}He laid hold of the dragon, that old serpent, who is the Devil and Satan, and bound him for a thousand years.{/i}"
    l "{i}And he cast him into the bottomless pit, and shut him up, and set a seal on him, so that he should deceive the nations no more till the thousand years were finished.{/i}"
    pause(1)
    "Leopold had appeared, the brown paper envelope clenched tightly in his fist."
    
    pause(1)
    show rika dress mischievous day open at left with Dissolve(1)
    pause(1)
    
    r "Well well, old man. You've been reading scripture? I didn't know they kept bibles in the type of hotels {i}you{/i} frequent."
    
    l "A typical Kuyper — always eager to cast the first stone."
    pause(1)
    l "I'm here to put an end to your little scheme."
    l "I always knew your clan practiced a depraved religion. That's why my family would try to keep their distance from your demonic cult."
    show rika dress unhappy day open at left with Dissolve(0.5)    
    r "And you should have kept it that way!"
    
    r "There's no end on the terrors I will unleash upon this land!"
    n "And you'll be the first to experience them, you pathetic excuse for a nobleman! What a blessing it will be, to have you cleansed off this earth."
    
    l "Oh, I've read all about your little sect."
    
    show rika dress sad day open at left with Dissolve(0.5)     
    "He opened up the envelope, revealing the pages within. A look of recognition flashed across Rika's eyes, and for a second she appeared to falter."
    pause(1)
    
    l "Do you recognize this document?"
    l "It recounts all the twisted dealings your church has been involved in."
    
    l "Twenty-four copies are with my people right now, ready to be sent out to news-outlets around the globe."
    
    l "Once the news gets out, hordes of tourists will descend upon Abbotsford, all dying to catch a glimpse of the monster."  
    show leo neutral open with Dissolve(1.0)
    l "People love a good horror story — especially one that features a pretty girl."
    l "Loch Ness will pale in comparison!"
    pause(1)
    l "Is that really what you want, Rika? For your church to become a cheap side-show attraction?"
    
    "For a second, Rika appeared to be pondering his words, a doubtful glance residing in her eyes. But then her victorious grin returned."
    
    show rika dress mischievous day open at left 
    hide leo
    with Dissolve(1.5)
    r "Do you really think that will stop me? Old man?"
    
    show rika dress mischievous day open at left with Dissolve(0.5)    
    r "Look behind me! Things have been set in motion, that are too great to be reverted! The pitiful era of man has come to an end!"
    
    pause(1)
    "But then another, much shriller voice rang out over the noise of the waves."
    
    n "It's over, Rika!"

    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0) 
    
    
    show ina shirt angry day open at right with Dissolve(0.5)
    "It was Ina, who stepped out from behind Leopold."
    "It was clear that she had come into action, after I'd left, in the systemic and meticulous way that I'd grown accustomed to."
    
    "I saw a determined gleam in her eyes, that I found attractive beyond measure."
    
    "And finally I realized that I was now at the center of time-defining events — here on this isolated, storm washed shore."
    
    show ina shirt angry day closed at right with Dissolve(0.2)
    show ina shirt angry day open at right with Dissolve(0.2)
    
    n "Karin has made a full recovery."
    
    n "She's reclaimed her chair in the town council, and an emergency coalition has been formed. All remaining parties have joined forces in order to regain control of the municipal water board."
    
    show rika dress sad day open at left with Dissolve(0.5)      
    
    n "And there's more — the central government has declared a national emergency!"
    
    n "Mobile pumping systems have been installed all around the Marshpolder, and digging crews are currently restoring the drainage canals, to redirect water to other pumping stations."
    
    show rika dress sad day closed at left with Dissolve(0.2)  
    show rika dress sad day open at left with Dissolve(0.2)  
    
    n "The water level is already receding. All land will be dry within a matter of days."
    
    show ina shirt angry day closed at right with Dissolve(0.2)
    show ina shirt angry day open at right with Dissolve(0.2)
    
    n "Please give up, Rika. There's still a way out of this!"
    
    show rika dress mischievous day open at left with Dissolve(0.5)     
    
    "But Rika had never seemed farther from giving up."
    "All trepidation had tracelessly evaporated from her being — in her eyes shone the look of a feral beast, backed into a corner."
       
    "An expression of fanatical desperation, of someone fully reconciled with the prospect of death."

    show rika dress mischievous day closed at left with Dissolve(0.2)  
    show rika dress mischievous day open at left with Dissolve(0.2)  
        
    r "You don't understand, Ina. If the pumps are restored, we'll just have to make a crack."
    
    r "How will you deal with a small, seven mile long, tear along the length of your embankment? Will your pumps truly be able to deal with the combined force of earth's gravity?"
    
    show rika dress mischievous day closed at left with Dissolve(0.2)  
    show rika dress mischievous day open at left with Dissolve(0.2)  
    
    "And then the lake erupted in roaring turmoil, as though the endless wire that coiled therein was preparing to strike."
    
    "But I was almost too transfixed to notice, as as all my attention was drawn by Rika's eyes, that were burning with a pure, irrational, madness—"
    
    "—the extreme devotion of an individual that had fully taken the leap of faith, and was now, eternally, departed from any conventional thought pattern."
    
    "And for a second, that burning fire in her eyes, appeared almost alluring."
    
    "When suddenly—"
    
    "A white flash!"
    
    play effects "audio/angrydog.ogg" loop
    show ina shirt surprized day open at right with Dissolve(0.5)
    show phyrrus with vpunch #TODO remove tail??
    
    hide rika 
    hide phyrrus
    with easeoutbottom
    
    n "Phyrrus!"
    
    show ina shirt defiant day open at left with easeinleft #Dissolve(0.5)
    
    "The dog had appeared out of nowhere, running up to Rika through the surf, and lodging its jaws firmly in her left thigh."
    
    "Rika let out a loud shriek, immediately losing all her former composure and collapsing to the ground, where she lay swinging frantically at the biting hound."
        
    "But Phyrrus wouldn't let go."
    
    show ina shirt mirth day closed at left with Dissolve(0.2)
    show ina shirt defiant day open at left with Dissolve(0.2)
    
    n "Can you believe it, Rika? That dog must have swam over twenty miles, just in order to {i}bite{/i} you!"
    
    pause(1)
    show leo neutral open at right with Dissolve(0.5)
    pause(1)
    
    l "How much I'd give to be in its place—"
    
    "And while Rika's wails of agony resounded out over the rainy shore, I could sense the large being in the lake growing quiet—"
    "—as the line of communication with its high priestess had clearly been severed." #expand a little
    
    pause(1)
    
    "And looking at Rika, how she lay there, writhing in pain, her thin summer dress drenched in brine and blood, I felt a wry sense of pity."
    
    "Because somewhere Ina's words had rang true with me — she was, in a sense, a dying breed."
    pause(1)
    show ina shirt mirth day closed at left with Dissolve(0.2)
    show ina shirt defiant day open at left with Dissolve(0.2)
    
    n "Let's get back to town. I think we're needed there."
    
    pause(1)
    
    n "It's okay, Phyrrus, you can let go of her now."
    stop effects fadeout 4.0
    
    n "We don't want you developing a taste for human flesh."

    pause(1)
    hide ina with Dissolve(0.5)
    hide leo with Dissolve(0.5)

    stop music fadeout 20.0
    pause(1)
    
    "And as we left, carrying Rika between the three of us, the lake gradually returned to its peaceful self."
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(4.0)
    pause(2)
       
label p5Ic10:

    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)

    pause(2)
    play sound "audio/0sealapping.ogg" loop fadein 1.0
    scene lake_twi with Dissolve(2.0)
    pause(1)
    window show
    pause(1)


    #### ending describes cleanup operations, fixing the pumping stations draining the water

    "{i}After a national state of emergency had been declared, extensive measures were undertaken to reclaim, once again, the portions of land that had been submerged by the flood.{/i}"
    
    "{i}While the maintenance crew worked day and night to restore the three centrifugal pumps that had been damaged by the explosion, additional ditches were dug to divert the excess water to pumping stations to the north and east of Abbotsford.{/i}"
    
    pause(1)
    
    "{i}Although the deluge had displaced many civilians and livestock, the overall number of casualties remained limited, due to the gradual nature in which the flooding had occurred.{/i}"

    pause(1)

    "{i}The exact cause of the disaster was never disclosed by the government, but most contemporary sources attribute the flood to a succession of extreme weather patterns that had been insufficiently planned for.{/i}"
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    scene office with Dissolve(0.5)
    play sound "audio/officesound.ogg" fadein 1.0
    pause(1)
    window show
    pause(1)
    play music "audio/1pianoending2.ogg" loop fadein 4.0
    show ina shirt interested day open at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.5)
    pause(1)
    
    n "Sounds like a decent cover-article."
    n "Let's publish it as soon as possible."
    show ina shirt mirth day closed at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    show ina shirt interested day open at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    n "Our subscriber-count has been increasing again. I'm sad we never could write anything on that old church inquiry. I feel like our readers deserve to know the truth."
    
    a "At least the school board has reinstated our funding."
    n "Oh definitely. Increased it, even."
    n "But don't get any ideas, Abe. This envelope includes your back pay for the previous month."
    n "I regret being unable to pay you sooner. However, you're probably aware money doesn't grow on trees."
    n "And the good news is, your paper round will be shortened from now on. We have a new man on the delivery team."
    
    show mei dress interested day open at Position(xpos = 0.8, xanchor=0.5, ypos=0.5, yanchor=0.5)  with Dissolve(0.5)
    
    m "A new {i}wo{/i}man, actually."
    n "Mei is happy to do the work. And she doesn't even require reimbursement."
    m "I'll do more houses if you let me!"
    a "Don't do it, Mei! Get out while you still can!"
    
    pause(1)
    play audio "audio/knock.ogg"
    "Suddenly there was a knock at the door." #TODO sfx
    
    #Rika asks if we can publish swimming results.
    pause(1)
    show rika dress happy day closed behind ina with Dissolve(0.5)
    pause(1)
    
    r "Hi! I have the results of the regional swimming championships."
    r "Please print them in your next issue — they should be fit for publication the way they are."
    show ina shirt mirth day closed at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    show ina shirt interested day open at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    n "Thanks Rika, we'll definitely include them."
    n "Naomi must be so happy with her medal. Now she'll have the chance to represent the province at nationals."
    "Rika smiled a sad smile."
    show rika dress happy day open behind ina with Dissolve(0.5)
    r "I'm so sorry I couldn't compete, with my leg wound and all—"
    r "I have to keep it dry until the stitches come out."
    show rika dress happy day closed behind ina with Dissolve(0.5)    
    a "I hope you don't end up catching that {i}hydrophobia{/i} they always talk about."
    
    show rika dress sad day closed behind ina with Dissolve(0.5)    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    
    "After Rika had left the office, Ina turned to me."
    show ina shirt mirth day closed at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    show ina shirt interested day open at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.2)
    
    n "Blaming it on her leg wound? Such a convenient excuse."
    a "I imagine she isn't ready to talk about the week she spent in {i}involuntary commitment.{/i}" #confinement??
    n "Hmpf, well you can't blame her."
    n "In orthodox religious communities, mental health issues are often stigmatized."
    n "It must be hard on her, to be the talk of the town—"
    
    play audio "audio/schoolbell.ogg"
    pause(1)
        
    "The bell rang and Mei hurried out, muttering something incomprehensible about alabaster formations."
    hide mei with Dissolve(0.5)
    pause(1)
    "As Ina and I gathered our bags, she shot me one last, meaningful glance—"
    "—and as I looked back into her burning eyes, I felt a warming comfort expand throughout my chest, reassuring me that no matter what the coming century had in store for us—"
    "—be it the crumbling of our biosphere, the degradation of mankind, or even the entire downfall of civilization—"
    "—there was no one more capable of chronicling the decline than the brown-haired girl standing there before me."
    
    pause(1)
    hide ina with Dissolve(0.5)
    stop music fadeout 5.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(1.5)
    pause(1)
    
    jump end
    
    ############################################################
    ########## PART 5 RIKA #####################################  
    ############################################################
       
label p5Rc1:


    scene white with Dissolve(1.5)
    pause(1)
    scene part5_rika with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    
    pause(2)
    play sound "audio/ventilator.ogg" loop fadein 1.0
    scene diningroom with Dissolve(0.5)
    window show
    pause(1)
    #TODO chapter title 

    #TODO, consider using CG instead of sprites
    "When I returned to Ina's house, I found her in the bedroom in mostly the same state as I had left her."
    
    pause(1)
    #scene ina_cg_1 with Dissolve(0.5)
    scene ina_cg_1r with Dissolve(1.0):
        subpixel True
        xalign 1.0 yalign 1.0
        easein 30.0 xalign 0.0 yalign 0.0      
    pause(1)
    
    play music "audio/0andantino20.ogg" loop fadein 30.0
    
    "She appeared listless, hardly responding to my presence."
    
    a "I ran into Rika, just a moment ago."
    a "I think she knows that we have the appendix document."
    
    "No reaction."
    
    a "But she didn't seem too upset about it. I figure the church is aware it's just a load of occult nonsense."
    "I let out a repressed chuckle."
    a "She even wants to talk to me, this evening."
    "Ina sat still for a while, staring at me."
    a "She says she'll explain everything, about the mysterious occurrences around town."
    "Then she stirred."    
    pause(1)
    a "I'm inclined to go."
    a "I mean, it's probably a good thing, right? To just talk to her, instead of all the covert spy business we've been doing lately."
    pause(1)
    scene inabedroom_eve with Dissolve(0.5)
    pause(1)
    show ina cami neutral day open with Dissolve(0.5)

    
    "She got out of bed."
    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2) 
    
    n "Sure. Go."
    n "Let me know what she says."
  
    "Ina appeared a deathly pale, as though she were coming down with a fever."
    a "Say, can I maybe make you some dinner? Heat up some noodles or something."
    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2)     
    n "No, it's okay. I'm not hungry."
    n "Just go. You need to prepare for your {i}date{/i} tonight."
    pause(1)
    "Realizing she'd rather be left alone, I gave her a quick nod before making my way to the door."
    
    "But as I was about to exit, she uttered one last sentence, in a clean voice."
    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2)     
    n "Please be careful tonight — that Kuyper girl can't be trusted."

    pause(1)
    hide ina with Dissolve(0.5)
    stop music fadeout 3.0
    pause(1)
    window hide

    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc2:

    scene black with fade
    pause(1)
    play sound "audio/summernight.ogg" loop fadein 1.0
    scene sandford_twi with Dissolve(0.5) 
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)

    show rika dress happy day closed at center with Dissolve(0.5)
    pause(1)
    r "Hi Abe! Let me restate how glad I am you chose to speak with me tonight."
    r "I've always believed that interpersonal differences stem from an inability to communicate. Don't you agree?"
    r "I'm sure that once we've openheartedly talked things through, it will not only take away any misgivings you may have about our church, but that it will also strengthen our relationship lastingly."
    
    show rika dress mischievous day open at center with Dissolve(0.5)    
    "She smiled."
    
    pause(1)
    hide rika with Dissolve(0.5)
    stop sound fadeout 1.0
    scene lobby with Dissolve(0.5)
    play music "audio/0goldberg22.ogg" loop fadein 5.0 
    pause(1)
    
    show rika dress happy day open at center with Dissolve(0.5)
    r "But please disregard my platitudes. Welcome to Sandford house, the most illustrious property on the island."
    r "This place isn't open to everyone, you know? The church only rents it out for high-profile occasions, such as weddings and conferences."
    r "Let me show you around the manor."
    
    hide rika with Dissolve(0.5)
    pause(1)
    scene statue with Dissolve(0.5)
    pause(1)
    show rika dress happy day open at center with Dissolve(0.5)

    
    r "The property has sixteen guest bedrooms."
    r "Did you know that the history of Sandford house dates back to the seventeenth century?"
    r "It once belonged to the lords of the isle."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)
    a "I believe someone may have mentioned that to me."
    
    show rika dress mischievous day closed at center with Dissolve(0.5)
    r "Anyway, as it's fundamentally a wooden structure, the property has underwent countless renovations over the ages."
    r "However, the spirits of the island's past haven't departed yet—"
    
    "She took me by the hand, leading me through the main hallway."
    hide rika with Dissolve(0.5)
    pause(1)
    scene doubleroom with Dissolve(0.5)
    pause(1)
    show rika dress happy day open at center with Dissolve(0.5)
    
    r "This is the master bedroom."
    r "After the evacuation of Abbot, the church acquired Sandford house."
    r "This was of immense symbolic importance to the islanders, as it solidified our restored sovereignty."
    r "Like conquering a tyrannical ruler's palace, we were finally autonomous over our homestead."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)    
    r "To this day, Sandford house remains property of the church. No matter how much that old letch Leopold offers us, we'll never relinquish it to him."
    
    pause(1)
    scene lobby with Dissolve(0.5)
    pause(1)
    
    "She led me through the ballroom and the library, until we had finished our tour."
    

    show rika dress mischievous day open at center with Dissolve(0.5)
    r "It's a great place, isn't it? And we have it all to ourselves tonight. "
    r "Let's hang out and talk in one of the bedrooms. That way I'll just have one room to tidy afterwards."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    scene doubleroom with Dissolve(0.5)
    pause(1)
    
    show rika dress happy day open at center with Dissolve(0.5)
    a "Do they compensate you for your work at the house?"
    r "Ha ha, I bet you're looking for something that pays better than your paper round?"
    #a "I didn't—"
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)
    r "They don't give me a formal paycheck. This is just one of the duties that comes with being the pastor's daughter."
    r "I've never really lacked anything material, though. You've probably realized by now that my family is rather wealthy." #had material needs
    r "The church makes tons in rent, and the members of our congregation tithe generously."
    pause(1)
    a "Oh yeah, how did your service go?"
    "She let out a contained laugh."
    r "Just the same old."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)
    r "I've listened to my father's preaching for so long now — you learn to zone out after a while."
    r "I know it's embarrassing for me to say — but dad's sermons have a tendency to go {i}on{/i} and {i}on{/i}."
    r "I usually go into my own private bubble."
    show rika dress mischievous day open at center with Dissolve(0.5)
    r "I pretend that I'm swimming — underwater, in an endless sea of blue."
    r "During those episodes, nothing gets through to me. "
    r "Not even Mei's excited whispers."
    show rika dress sad day open at center with Dissolve(0.5)      
    "Her face grew dark."
  
    r "It isn't always easy — you know?"
    r "As a pastor's daughter, the entire congregation looks up to you."
    r "Like living in a glass house, all your actions are magnified—"
    r "—and {i}judged{/i}."
    
    show rika dress happy day closed at center with Dissolve(0.5) #does this work?
    "She winked." #something , show smile
    r "Better make sure no one sees us together tonight."
    
    show rika dress sad day open at center with Dissolve(0.5)       
    r "Anyway, I wish my misery ended there."
    r "But while I'm placed upon a pedestal inside the church — outsiders regard me as a freak."
    r "They view my father as an eccentric witch-doctor, a relic from long forgotten times."
    
    show rika dress sad day closed at center with Dissolve(0.2)
    show rika dress sad day open at center with Dissolve(0.2)    
    r "I've always been given trouble at school. By farm girls, mainly."
    r "They'd try to ridicule me, drag me down."
    r "But I never let them." 
    show rika dress unhappy day open at center with Dissolve(0.5)
    r "You hear that? "
    "She was shaking with anger."
    r "As soon as you let them humiliate you, you become lower than them. An outcast in your own town."
    r "They'll always try to debase you. Those kind of people."
    r "Do you understand?"
    "Her voice became quiet."
    show rika dress sad day open at center with Dissolve(0.5)   
    r "It's just— This is exactly what they're trying to do in the council right now." #scrap council?
    
    pause(1)
    show rika dress happy day closed at center with Dissolve(0.5)     
    r "I apologize. "
    r "I became emotional. I don't want you to see me this way."
    pause(1)
    r "Just wait here for a minute, I'll get some drinks from the bar."
    hide rika with Dissolve(0.5)
    
    #TODO room for some reflection
    "And away she was."
    "I remained in the opulent room, which was adorned lavishly with statues and bas-reliefs — featuring figures I'd never read about in the Bible."
    pause(1)
    "A few minutes later, Rika returned with a bottle of wine and two glasses. "
    pause(1)
    show rika dress mischievous day closed at center with Dissolve(0.5) 
    
    
    r "You should try this, it's a {i}Château La Mission Haut-Brion.{/i}"
    "She poured a glass and handed it to me."
    
    show rika dress mischievous day open at center with Dissolve(0.5)     
    r "A great vintage. There's nothing sour about {i}these{/i} grapes." #blood of christ reference?"
    
    show rika dress mischievous day closed at center with Dissolve(0.2) 
    show rika dress mischievous day open at center with Dissolve(0.2)    
    r "But anyway, I've promised answers."
    
    pause(1)
    
    r "The largest farm in the region is owned by a man named George Van Linden. He has about 400 acres, which he tends to with a small group of farmhands."
    "The name immediately drew my attention."
    show rika dress sad day open at center with Dissolve(0.5)      
    r "When harvest comes, however, he employs a large team of seasonal workers to help him bring in the crops."

    r "These workers are paid a slave's wage. He provides accommodation for them on the farm — in a large barn that has been converted into makeshift sleeping quarters."
    r "His practices are undoubtedly in violation of the labor code. George, however, doesn't care. All that matters to him is his bottom line."
    r "And the workers don't complain, out of fear for their jobs."
    show rika dress sad day closed at center with Dissolve(0.2) 
    show rika dress sad day open at center with Dissolve(0.2)     
    
    r "As you've probably figured out, George's brother is the mayor of our town. He makes sure George stays out of trouble for the abysmal treatment of his employees."
        
    pause(1)
    "I took a sip from my wine, and was met with an intense, overpowering aroma of smoke and berries, that lingered in my mouth for a great while."
    show rika dress happy day open at center with Dissolve(0.5)  
    "Rika looked up at me, expectantly."
   
    r "Do you like it?"
    a "Sure. This isn't some ordinary wine."
    show rika dress mischievous day closed at center with Dissolve(0.5)
    "She smiled."
    r "Oh I just grabbed what we had back there."
    
    show rika dress sad day open at center with Dissolve(0.5)    
    r "Anyway, you should know George is an impulsive man."
    r "I remember once, when I was a kid, we'd pass by his orchards on our way to school. Even though we'd been taught to be weary of George, we sometimes picked up apples that had fallen by the wayside — figuring he wouldn't be able to sell them anyway." #(maybe start with this anecdote?)
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)        
    r "But one day, George was there."
    r "When my friend Naomi picked up an apple, George saw her, and immediately flew into a fit of unrestrained, maniacal rage."
    r "He dropped what he was doing, and came bounding at us, all the while snarling in an almost bestial display of fury."

    r "As soon as we noticed him coming in our direction, we fled towards the school, making it into the building just before he could catch us."
    
    pause(1)
    
    r "Remembering that look of pure, animalistic rage that I saw in his eyes that day, I realized right then that there was something fundamentally broken within that man. "
    
    r "I'm sure he would have inflicted seriously harm, if he'd been able to catch us that day. "
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)            
    
    #
    r "And this wasn't an isolated incident."
    r "George was a tyrant. He was known for acting out his anger on his employees."
    r "Whenever someone make a mistake, or went against his will, he'd make them {i}feel{/i} it."
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)       
    r "And of course, the seasonal workers — desperate to keep their jobs — were an easy target."
    r "More and more stories of worker abuse came out, so much that even the mayor had a hard time keeping the whole issue under wraps."
         
    a "So, are you saying?"
    
    stop music fadeout 5.0
    "She lowered her voice, even though there was no one there to overhear us."
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)   
    r "You must understand — what happened that night was an accumulation of coinciding factors."
    r "George's firm had been struck disproportionately hard by a series of tariffs on ammonium nitrate."
    r "Also, it was a bad year weather-wise, with extreme droughts plaguing the land."
    r "And then on top of that came the allegations of worker abuse, which were likely sparked by an anonymous source from among his own employees."
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2) 
    

    r "It all ignited on that fateful night."
    r "There had been a small confrontation earlier that day, between George and one of the laborers."
    r "When George became angry, the group of workers had formed a front, preventing George from lashing out against the insubordinate employee."
    a "Michel."
    r "George wasn't able to go up against them all, yet he also couldn't retaliate by firing them — as there was no time to hire replacements."
    r "Humiliated by his own subordinates, an intense rage ate at him from the inside."
    
    #TODO build up tension, spooky noise
    stop sound fadeout 1.0
    pause(1)
    play sound "audio/haunting.ogg" loop fadein 11.0    
    r "Later that night, when Michel came home, George was lying in waiting."
    
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)  
    "While speaking, Rika had wrapped her hair tightly around the palm of her hand, as though it were bandaged."
    "She appeared reluctant to describe what came next."
    
    show rika dress crying day open at center with Dissolve(0.5) 
    
    r "George must have dropped down from the granary. 200 pounds of concentrated fury—"
    
    r "—wielding a ten inch pruning knife."
    
    r "All was red before his eyes, all he could do was raise the blade and plunge it downward, again and again—" #meh
    stop sound fadeout 4.0     

    "She let out a loud, grief-stricken sob."
    pause(1)
    
    r "It's just, I can still see it perfectly in my mind—"
    r "—the anger in his eyes. From that day, as children, when we stole those apples."
    r "Something so irrational, so hellbent on revenge—"
    
    r "I could easily imagine him brutally take away another person's \nlife— "
    r "—with 87 stab wounds."
    show rika dress sad day closed at center with Dissolve(0.2)        
    show rika dress sad day open at center with Dissolve(0.2)   
    
    r "I apologize. The whole tale still brings tears to my eyes."

    #TODO, maybe a sentence?
    #show rika dress happy day open at center with Dissolve(0.5)      
    r "Come on, let's go outside."

    hide rika with Dissolve(0.5)
    
    pause(1)
    window hide
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc3:

    scene black with fade
    pause(1)
    play sound "audio/summernight.ogg" loop fadein 2.0
    scene sandford_nig with Dissolve(0.5)
    play music "audio/0goldberg1.ogg" loop fadein 40.0
    window show
    pause(1)

    "I poured a new glass and followed her through the art-nouveau conservatory."
    
    pause(1)
    show rika dress happy day open at center with Dissolve(0.5)
    pause(1)
    
    r "Sandford house lies on an elevation, it's higher than even the surrounding island."
    
    r "Quite suitable, isn't it?"
    
    r "Like a palace—"
    
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)   
    "And as we stood in the mild evening breeze, looking out over the distant lights of the town, a feeling of majesty gradually took possession of me."
    
    "Out here, in the shticks, simply spending time with Rika at this magnificent mansion instilled me with an air of importance."
    "Just walking through its halls, drinking wine in the courtyard—"
    
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)    
    
    r "Isn't it delightful — how warm it is?"
    
    
    r "I just adore coming out here for walks in the dark."
    r "I love how no one can see me. It's so exhilarating."
    show rika dress happy day open at center with vpunch
    "She spun around, giggling, sending wine spilling from her glass."
    r "Sometimes I just want to dance — to go out and dance, without anyone knowing."
    
    show rika dress mischievous day closed at center with Dissolve(0.5)
    "She took my hand in an attempt to initiate a waltz of sorts, but I was caught off guard by her sudden spontaneity, and remained rigid as she pulled me."
    pause(1)
    "Clumsily I followed her around the nocturnal yard."
    #extend?
    
    r "I'm sorry. I'm making you feel uncomfortable."
    #"Let's go inside again,
    
    show rika dress mischievous day open at center with Dissolve(0.5)
    r "Come on, I'll get us some more wine."
    
    "She led me back inside."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene lobby with Dissolve(0.5)
    pause(1)
    
    ## in the lounge
    show rika dress happy day open at center with Dissolve(0.5)
    r "Oh that evening air has done me well."
    r "Are there any more questions you'd like answered?"
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2) 
    "I though for a second."
    pause(1)
    a "Well, I spoke to Karin Voorhees, before she was attacked."
    a "She mentioned something about a group named Flock 05."
    pause(1)
    r "Karin? That's so typical of her."
    r "You should know — after the attack on his farm — it didn't take long for George to fall under suspicion."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)    
    
    r "On behest of the mayor, the police wasn't allocating many resources to the case."
    r "Still, rumors started to spread like wildfire."
    r "In an attempt to keep the accusations at bay, the mayor tried to shift the blame onto Flock 05."
    r "Their party harbors a long running grudge against all migrant workers. It sounded plausible, at the time, to assume they had orchestrated the gruesome murder."
    
    show rika dress sad day open at center with Dissolve(0.5)
    r "This, however, is where my father stepped in."
    r "There's a limit to the amount of evil that can fester within a community like ours."
    r "Our church may be regarded as close-minded by some — but we are still {i}Christians{/i}, and we will always stand up for the rights of the innocent and downtrodden."
    
    show rika dress happy day open at center with Dissolve(0.5)
    r "{i}Blessed is the man that endures temptation, for when he is tried, he shall receive the crown of life.{/i}"
    
    #Even though Flock 05's members can be crude or ignorant, there's no reason to frame them 
    
    r "Though my father understood he wouldn't be able to have George van Linden brought to justice, knowing the corruption that creeps within the police force—"
    r "—he did put his foot down when it came to framing an unrelated party for a crime they didn't commit."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)    
    
    r "This has caused something of a rift within A.I.R."
    pause(1)
    a "Would you say the party split into two separate factions?"
    
    show rika dress happy day closed at center with Dissolve(0.5)
    "She glared at me playfully."
    
    pause(1)
    
    #r "Come on, let's go someplace more comfortable."
    
    hide rika with Dissolve(0.5)
    pause(1)
    scene doubleroom with Dissolve(0.5)
    pause(1)
    
    
    "We returned to the bedroom, where we sat down upon the bed."
    "The lingering aroma of wine seemed to encompass everything, as though it had drifted from my taste buds and sailed out into the room."
    
    pause(1)
    scene statue with Dissolve(0.5)
    pause(1)
    show rika dress sad day open at center with Dissolve(0.5)
    pause(1)
    
    r "Karin has likely led you to believe that the church is against all forms of migrant labor. But that's a very one-sided representation of our point of view."
    pause(1)
    r "No farmer ever hires workers from afar without self serving reasons. Migrants are often cheap, and willing to work under appalling circumstances. "
    r "The agrarians like to paint themselves as regular philanthropists — but if you {i}knew{/i} what went down on their farms, you'd realize it's all a ruse—"
    show rika dress sad day closed at center with Dissolve(0.2)
    show rika dress sad day open at center with Dissolve(0.2)    
    
    "The sweet fragrance enveloped everything. My eyelids were gradually growing heavier, as though they were being borne down by the sticky, sugary wine."
    "I could barely make out Rika's delicate features, and began to curse myself for drinking so much."
    pause(1)
    r "—it's a disgusting trans-valuation of values."
    r "The slaveholder Pharaohs have deemed themselves as righteous God-kings, beyond all reproach—"
    
    show rika dress mischievous day closed at center with Dissolve(0.5)
    r "Watch out, Abe. Don't drop your glass."
    
    "Deep burgundy lines traversed my vision, slowly growing darker and fading into a thick, luscious black." #maybe pschedelic SFX
    "{i}Her hair, her black hair, coiling into infinity—{/i}"
    
    show rika dress mischievous day open at center with Dissolve(0.5)
    r "My parents always read to each other from the Bible, before going to bed. Wouldn't that be fun to do?"
    pause(1)
    a "Heh—"
    
    #make this more gradual, spread the explanation out over the evening/scenes
    #maybe blurry effect??
    
    pause(1)
    
    "{i}God is jealous, and the LORD avenges;{/i}"
    pause(1)
    "As my mind drifted off to distant shores—" #evaluates if this works, maybe move this
    pause(1)    
    "{i}The LORD avenges and is furious;{/i}"
    pause(1)    
    "{i}The LORD will take vengeance on His adversaries;{/i}"
    pause(1)    
    "—down into sunlit seas—"
        
    #"—and onwards, into azure depths—"
    
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)    
    
    "{i}And He reserves wrath for His enemies;{/i}"
    pause(1)    
    "{i}The LORD is slow to anger and great in power,{/i}"
    #"—an all-encompassing sea of blue—"
    pause(1)
    "{i}And will not at all acquit the wicked.{/i}"

    #hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 3.0
    pause(1)
    scene black with Dissolve(3.0)
    pause(1)
       
label p5Rc4:

    scene black with fade
    pause(1)
    play sound "audio/0gurgling.ogg" loop fadein 16.0
    scene black with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)
    "{i}Abe{/i}—"
    pause(1)
    scene monster2 with Dissolve(0.3)    
    scene black with Dissolve(0.3)
    pause(1)
    "{i}Good morning Abe.{/i}"
    pause(1)    
    scene monster2 with Dissolve(0.4) 
    scene black with Dissolve(0.4)
    pause(1)    
    "{i}You're such a sleepy-head.{/i}"
    "{i}Time to wake up{/i}—"      
    pause(1)   
    play music "audio/haunting.ogg" loop fadein 1.0    
    scene monster1 with Dissolve(0.1)    
    a "AAAAAAAAAAAAARGH—"
    
    ##scary face effect, with creepy sfx # Rika changes into blue dress"
    ##blurry frame? like opening eyes . . .
    #pause(1)
    scene black with Dissolve(0.1)
 #   pause(1)
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene monster3 with Dissolve(0.1)
    pause(1)
    "Suddenly I was wide awake. Rika sat crouching beside me, attempting to comfort me in my acute terror — her face completely normal in the pale morning light."
    
    r "Abe? Are you okay? You must have had a nightmare—"
    a "A nightmare— Yes—"
    pause(1)
    play music "audio/0canon.ogg" loop fadein 25.0
    
    scene statue with Dissolve(0.5)
    pause(1)
    show rika dress mischievous day closed at center with Dissolve(0.5) #maybe blushing    
    "She smiled at me."
    r "I apologize for yesterday evening."
    r "For how I behaved."

    show rika dress mischievous day open at center with Dissolve(0.5)    
    r "It's not in character for me, to let myself go like that. Especially not with a man present." #typical, characteristic
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)    
    a "It's okay, I had a great time."
    pause(1)
    a "I'm sorry for falling asleep on you."
    a "I don't want to be a burden. I'll help you clean — and then leave as soon as possible."
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)   
    r "Oh no, it's okay. Please take your time."

    r "We can leave in the afternoon."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    scene sandford_day with Dissolve(0.5) #TODO sandford house
    play sound "audio/edgemeadow.ogg" loop fadein 2.0
    pause(1)    
    
    "We had our breakfast of coffee and smoked salmon in the morning sun — after which Rika paced around the courtyard, brushing her hair slowly, counting every stroke."
    
    pause(1)
    
    a "Rika?"
    
    show rika dress mischievous day open at center with Dissolve(0.5)
    
    r "{i}—twenty two, twenty three, twenty four—{/i}"
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)
    r "Yes?"

    
    a "I was thinking about what you were telling me last night."
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)   
    r "{i}Twenty six, twenty seven—{/i}"
    
    a "I think everything makes a lot more sense now."
    a "I was just wondering—"
    pause(1)
    r "{i}Twenty nine—{/i}"
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)
    r "What?"
    
    a "That whole affair about the marquis. And the secret document that got lost." 
    a "Who was behind that?"
    
    show rika dress sad day open at center with Dissolve(0.5)    
    
    r "Ah—"
    "She put down her brush."
    
    r "You mean the document that was stolen from my father's office on Saturday night?"
    "I could feel the blood rushing to my head."
    pause(1)
    a "Yes—"
    "She stared at me with piercing eyes."
    a "Though that's not the first time it's been stolen, right?"
    show rika dress sad day closed at center with Dissolve(0.2)
    show rika dress sad day open at center with Dissolve(0.2)  
    r "Well I'm very sure you've familiarized yourself with its contents."
    r "So what did you make of it?"
    
    "She looked eager to hear my response, as though a lot depended on it."
    pause(1)
    a "Ehm—"
    a "They seemed like implausible fabrications—"
    show rika dress sad day closed at center with Dissolve(0.2)
    show rika dress sad day open at center with Dissolve(0.2)  
    r "Hm, perhaps."
    show rika dress mischievous day closed at center with Dissolve(0.5) 
    "She giggled."
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)    
    r "I guess you can imagine why Leopold wanted to get his hands on them."
    r "He's such a disgrace. "
    r "It's one thing that these sadistic remnants of outsider-persecution persisted into the nineteenth century, but to think that people are still trying to reinvigorate them in this day and age—"
    r "—only to demonize our church."
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)       
    r "That bears witness to an immense bias — a destructive bigotry that has been held against the inhabitants of these lands throughout history."
    
    r "What kind of nonsense do these papers contain? That we obey a demonic sea god? That we sacrifice new-born infants to the roaring waves?"
    
    r "Did Leopold really think he'd be taken serious, with these kinds of allegations? "
    
    show rika dress mischievous day closed at center with Dissolve(0.5)    
    "Nonchalantly, she resumed brushing her hair."
    
    r "I admit, we did take the appendix off him." 
    r "But not through any of scheme or trickery."
    r "It was late, Leopold was being entertained by a troupe of harlots that he himself had invited over — disgracing the halls of our illustrious house."
    r "My father just happened to stumble upon the papers, crumpled, sticking out of his briefcase."
    r "They're very rare manuscripts, only one other copy exists."
    r "And John's something of a conservator, you know? "

    r "Anyway, he took them, right there and then. To save the marquis the embarrassment of trying to use them for fruitless blackmail."

    show rika dress mischievous day open at center with Dissolve(0.5)    
    r "Then word got out about Leopold's behavior. We still have no idea who took these photographs."
    r "They were damaging for my father too, you see — considering how the whole affair took place on his property."
    
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)   
    
    r "There wasn't any {i}malice{/i} involved."
    r "My father is a man of love. He loves his enemies."
    
    show rika dress sad day open at center with Dissolve(0.5)    
    r "Sometimes a little too much — I'd say."
    
    r "I think, with a town like this — the murder, deceit and corruption that goes on."
    r "Forgiveness and love can only bring you so far."
    show rika dress happy day open at center with Dissolve(0.5)    
    r "A place like this needs cleansing."
    
    show rika dress happy day closed at center with Dissolve(0.5)    
    "She smiled a telling smile."
    
    r "{i}When the earth was corrupt and full of violence.{/i}"
    r "{i}God looked upon the earth and saw how degenerate the earth had become, for all flesh on earth had corrupted their ways.{/i} "
    r "{i}And God said to Noah, I am going to put an end to all flesh, for the earth is filled with violence because of them.{/i} "
    r "{i}I am surely going to destroy both them and the earth.{/i} "
    r "{i}Go make yourself an ark of gopher wood—{/i}"
    
    pause(1)
    
    show rika dress happy day open at center with Dissolve(0.5)
    r "Sometimes you can't get by on forgiveness alone. When evil is ubiquitous, when mankind is immutable in its ways—"
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)     
    r "The farmers, the surrounding lands — they are new lands, recently reclaimed from the sea."
    r "Just like when the earth was new, in Noah's days. Sometimes you need to push the reset button."
 

    scene comerredeluge #TODO best place???
    show rika dress happy day open at center 
    with Dissolve(2.0)
    
    
    r "{i}And it came to pass, after seven days, that the waters of the flood were upon the earth.{/i}"
    r "{i}On the seventeenth day of the second month, the fountains of the great deep broke apart and the windows of heaven opened.{/i}"
    r "{i}And the rain was upon the earth for forty days and forty nights.{/i}"
    
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)    
    r "A flood, wouldn't that be beautiful?"
    r "A nourishing, all-consuming flood, that sweeps away all the fields and farms, and washes the putrid excrement from our beautiful sea bed?"
    
    r "We'd be safe up here — this island still lies above sea level. It will shelter us against the waters like a wooden ark. "
    
    show rika dress mischievous day open at center with Dissolve(0.5)    
    "She stared at me, with mesmerizing eyes."
    
    r "I know it's a horrible thought, Abe, but it excites me to the fullest."
    r "For we truly are protected by a powerful God, a God that can wipe away the foolish constructions of man with only the flick of His finger." # wave of His hand
    
    r "I feel so good about you, Abe. I want to take you, through town, up to the shore. I want to show you so many things—"
    
    r "It may frighten you a little. But you need to trust me—"
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)
    #expand a little
    r "You need to trust me — that I can show you a true path to righteousness. "
    r "Will you join me on my path, Abe?"
    

    ####################################################################################################################################
    
    menu:
        with Dissolve(1.0)
        r "Do you trust me?"
    
        #### RIKA LAST DECISION
        "I trust you.":
            #### RIKA POSITIVE
            show rika dress mischievous day closed at center with Dissolve(0.5)
            r "I'm so happy, Abe."
            show rika dress mischievous day closed at center with Dissolve(0.2)
            show rika dress mischievous day open at center with Dissolve(0.2)
            r "So indescribably happy."
            scene sandford_day
            show rika dress mischievous day open at center 
            with Dissolve(1.0)
            r "Come on, we have no time to lose. There are so many things I want to show you—"
        
        "I do not trust you.":
            #### RIKA NEGATIVE 
            show rika dress sad day open at center with Dissolve(0.5)
            "Instantly, the excitement dissipated from her eyes"
            r "Abe—"
            r "Do you not see the injustices?"
            r "We could build a better world together—"
            r "I'm imploring you, Abe, please—"
            show rika dress sad day closed at center with Dissolve(0.2)
            show rika dress sad day open at center with Dissolve(0.2)
            menu:
                with Dissolve(1.0)
                r "— will you join me?"
                
                    #### RIKA VERY LAST DECISION                
                "Okay, I will.":
                    show rika dress mischievous day closed at center with Dissolve(0.5)
                    r "I'm so happy, Abe."
                    show rika dress mischievous day closed at center with Dissolve(0.2)
                    show rika dress mischievous day open at center with Dissolve(0.2)
                    r "So indescribably happy."
                    scene sandford_day
                    show rika dress mischievous day open at center 
                    with Dissolve(1.0)                    
                    r "Come on, we have no time to lose. There are so many things I want to show you—"   
                    
                "I can't.":
                    show rika dress sad day closed at center with Dissolve(0.2)
                    show rika dress sad day open at center with Dissolve(0.2)
                    r "That's clear."
                    show rika dress crying day open at center with Dissolve(1.0)
                    r "I'm afraid I overestimated our relationship."
                    r "I apologize for getting carried away."
                    scene sandford_day
                    show rika dress crying day open at center 
                    with Dissolve(1.0)
                    r "Now please have the decency to leave me to my melancholy."
                    r "You must realize that your presence is currently too much for me to handle."
                    
                    hide rika with Dissolve(0.5)
                    pause(1)
                    window hide
                    stop music fadeout 1.0
                    stop sound fadeout 1.0
                    scene black with fade
                    pause(1)
                    
                    jump rBad
    
    ####################################################################################################################################

    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 6.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc5:

    scene black with fade
    pause(1)
    #play sound "audio/ventilator.ogg" loop fadein 1.0
    scene doubleroom with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    "In a swift and practiced manner, Rika changed the bedding in the room that we had occupied, while I gave my best shot at vacuuming the carpet."
    
    pause(1)
    scene villageroad with Dissolve(0.5)
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    play music "audio/0goldberg28.ogg" loop fadein 5.0
    pause(1)
    
    "After that, she took me by the hand, leading me along the road that led to town. "
    "And as we ran, the glowing warmth of the midday sun, and Rika's sweet, invigorating fragrance, made it feel like the first day of spring." #was already here
    
    show rika dress sad day closed at center with Dissolve(0.5)
    r "Oh once beautiful Abbot, to see what they have done to you."
    r "The quaint streets and fishermen's houses of old, have been replaced with driveways and prefabricated mansions."
    r "To think that this place was once alive with the chatter of fishwives, the sound of roiling waves, the fresh sea air—"
    pause(1)
    r "All the toil and suffering — to think that it was all for naught."
    show rika dress happy day closed at center with Dissolve(0.5)
    r "I truly long for the day, when everything returns to how it once was."
    
    hide rika with Dissolve(0.5)
    pause(1)
    stop sound fadeout 5.0
    scene canal with Dissolve(0.5) #TODO not twilight
    stop music fadeout 8.0
    pause(1)
    
    show rika dress sad day open at center with Dissolve(0.5)
    r "Look, this is one of the drainage canals I told you about."
    r "Though the Marshpolder doesn't appear so different from the main land at first sight, it relies on a highly sophisticated apparatus to keep it from sinking back into the sea."
    show rika dress sad day closed at center with Dissolve(0.2)
    show rika dress sad day open at center with Dissolve(0.2)  
    play music "audio/0goldberg15.ogg" loop fadein 20.0
    r "Via these ditches, all the residual water and rainfall flows towards Ryebury pumping station, from where it is discharged into the lake."
    
    #have them move on to a next location"
    pause(1)
    
    "I felt a drop on my right hand."
    
    "The skies had become clouded, and an oppressive tension hung in the air as though a great thunderstorm could erupt at any second." #effect, make it rain?
    pause(1)    
    
    a "I think it's about to start raining."
    play sound "audio/0rainheavy.ogg" loop fadein 30.0
    
    show rika dress mischievous day closed at center with Dissolve(0.5)
    r "It is, isn't it? Well, that's formidable."
    r "Everything's proceeding as planned."
    r "It hasn't rained for weeks, you know? The farmers were beginning to complain."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    scene postbox_rai with Dissolve(0.5) #abrupt cut in dialogue??
    pause(1)
    show rika dress happy day open at center with Dissolve(0.5)
    
    r "Maybe if they had prayed more, they wouldn't be so prone to irregular weather." #cursive
    "She giggled."
    r "That's what they'd say in the past. Among fishers, when storms would plague the isle."
    r "If only they had prayed more."
    r "But they found out soon enough, that God no longer listened to their prayers."
    r "God had become an intellectual God — sitting safely in his heaven like a conceited watchmaker."
    r "He no longer dealt with our everyday qualms, engaging only in abstract theorisation."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)  
    r "Good and evil, eternal salvation — the God of the new covenant was tied up with matters that stood far away from our day to day lives."
    
    r "It's very different from Noah's time, when God still interacted with his people. "
    r "When God was still responsive to sacrifice—"
    pause(1)
    r "{i}Noah built an altar to the LORD, and offered burnt offerings on it from every clean animal and every clean fowl.{/i}" #no cursive this time
    r "{i}And when the LORD smelled the sweet savor, he said in his heart, \"I will never again curse the land for man's sake — even though his inclinations remain evil from youth — nor will I smite every living thing ever again, as I've done.\"{/i}"
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)      
    r "That is what the people of Abbot needed. A deity that stood close by us, that rewarded our devotion by safeguarding us from harm and misfortune."
    
    r "When you're on a cutter-boat, putting your life at risk in the open sea, braving the elements — you need a power close by."
    
    
    "I was overcome by an unsettling sensation." #evaluate
    pause(1)
    a "Did the people of Abbot turn away from God?"
    show rika dress sad day closed at center with Dissolve(0.5)
    r "Oh how {i}dare{/i} you suggest such a thing?! We are good Christians, you know that. We do as the Bible says—"
    r "{i}For the LORD is good, and greatly to be praised. He is to be feared above all gods!{/i}" #cursive or not?
    r "Even the ten commandments teach us—"
    r "{i}Thou shalt have no other gods {/i}before{i} Me{/i}!"
    
    r "We remain first and foremost devoted to the LORD, consulting him for all metaphysical matters. For there is no {i}other{/i} god as powerful as He."
    
    r "But there is a realm beneath the waves— Oh I can't wait to show you—"
    show rika dress sad day open at center with Dissolve(0.5)    
    r "Although first we need to collect something."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    #stop sound fadeout 1.0
    stop music fadeout 4.0
    scene ichthys_rai with Dissolve(0.5) #TODO church exterior raining
    #play sound "audio/0rainheavy.ogg" loop fadein 1.0
    pause(1)
    
    "She led me to the Ichthys building, where the church warden seemed stunned to see me in good grace with Kuyper's daughter."
    
    pause(1)
    stop sound fadeout 1.0
    scene catacombs with Dissolve(0.5)
    play music "audio/0toccatamute.ogg" loop fadein 2.0
    pause(1)
    
    "We entered the annex and descended down the stairs, into the basement where Ina and I had carried out our covert operation."
    "Leaving me out in the hallway, Rika slipped into the room that was adjacent to John's office — the one from which we had heard that mysterious, gurgling sound."
    "But the noise was entirely absent now, and whatever I could see of the interior of the room appeared bare and sterile, almost like a laboratory." #no gurgling
    
    show rika dress mischievous day open at center with Dissolve(0.5)    
    "Rika exited the room holding three glass bottles that were filled with a clear liquid. She put them into a bag, which she handed to me."
    r "I implore you to do a gentleman's duty."
    "I took it without complaint."
    show rika dress mischievous day closed at center with Dissolve(0.2)
    show rika dress mischievous day open at center with Dissolve(0.2)    
    
    r "Now let's head for the station, there's a train leaving in ten minutes."

    pause(1)
    window hide
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc6:

    scene black with fade
    pause(1)
    play sound "audio/train.ogg" loop fadein 1.0
    scene trainin_nig with Dissolve(0.5) #TODO rain fields???
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)

    ## at the shoreline

    "During the train ride, the rain outside swelled into a torrential downpour. "
    
    pause(1)
    stop sound fadeout 2.0
    scene lake_storm with Dissolve(2.0)
    play sound "audio/0searoarrain.ogg" loop fadein 5.0
    pause(1)

    show rika dress mischievous day closed at center with Dissolve(0.5)  # TODO darker RIka
    
    r "Ryebury beach! Did you expect to be back so soon?"
    
    "Gargantuan waves washed over the shore, whilst lukewarm water thrashed down in buckets from a caliginous sky. "
    "I could feel sand and surf lashing against my exposed flesh. Rika, however, appeared unnaturally calm under the extreme weather conditions."
    
    play music "audio/0luctum.ogg" loop fadein 40.0 #bad quality
    
    show rika dress happy day open at center with Dissolve(0.5)      
    r "The windows of heaven have opened!"
    r "Everything is coming together right now."
    #pause(1)
    #scene rika_cg_3 with Dissolve(2.0) #TODO make lighter?
    scene rika_cg_3r with Dissolve(3.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0    
    #pause(1)
    r "A large high-pressure area has been building up over the last months, causing unnatural temperatures and weather patterns to sustain into late autumn."
    r "Not many people seem to have noticed though, not even after Ina wrote an article on it."
    pause(1)
    "Fortunately it wasn't cold, but the damp was rapidly penetrating my clothes."
    "Although I admired Rika's sturdy constitution, I privately longed for the consoling comfort of Sandford house."
    pause(1)
    #TODO insert a detail image from your CG, just the legs
    
    r "Since today that high-pressure area has slowly begun shifting. It'll soon give way to a stationary front that will form directly over Abbot."
    r "Isn't it mysterious, how these meteorological phenomena occur?"
    r "A stationary front like this can persist for months — hanging in perfect stasis, and causing all kinds of extreme weather effects."
    r "For forty days and forty nights it will rain. A perpetual deluge will cover the land! "
    
    scene lake_storm 
    show rika dress mischievous day open at center    
    with Dissolve(2.0)
    
    r "The windows of heaven have opened!"
    r "The highest sheds its countless tears for the fate of our beloved isle!"
    
    show rika dress mischievous day closed at center with Dissolve(0.2)  
    show rika dress mischievous day open at center with Dissolve(0.2)      
    
    "A large wave swept up over the beach, drenching my already-wet shoes."
    
    r "Come on! There 'll be plenty of chances to soak up the rain. Let's go inside! "

    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc7:

    scene black with fade
    pause(1)
    #play sound "audio/0roomrain.ogg" loop fadein 1.0 #TODO rumble?
    play sound "audio/extractor.ogg" loop fadein 1.0 #TODO rumble?
    scene pumpingstation_hall with Dissolve(0.5)
    pause(1)
    window show
    pause(1)
    #TODO explain what's happening
    
    "A soft rumble emanated from the machine room below." #filled the pumping station
    #TODO sound of machinering
    ## inside the pumping station
    pause(1)
    show rika dress happy day open at center with Dissolve(0.5)  
    play music "audio/0goldberg15.ogg" loop fadein 20.0
    pause(1)
    r "Listen, the pumps are running at full capacity. But with so much rainfall, it's almost like carrying water to the sea."
    r "I wonder how much longer they will hold."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)      
    r "Mankind has always worked so hard. Look at all it has built."
    r "Creating land out of sea — you wouldn't imagine such a thing to survive."
    r "But humanity builds its clever contraptions. A pumping station, to keep the water out."
    
    r "Creating land out of sea—"
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    
    r "{i}And God said: \"Let the waters under the heavens be gathered together into one place, and let the dry land appear.\"{/i}"
    r "{i}And it was so.{/i}"
    r "{i}And God called the dry land Earth, and the gathering together of the waters he called Seas.{/i}"
    
    show rika dress sad day open at center with Dissolve(0.5)      
    r "But isn't it inconvenient to have seas? When humanity needs fertile farmland to devour?"
    r "Let's take that useless, unpredictable water, and subject it to the arrogant, profane ways of man!"
    
    pause(1)
    r "I wonder how clever these contraptions really are—"
    
    show rika dress happy day open at center with Dissolve(0.5)  
    "She shifted into a more casual tone of voice."
    pause(1)
    r "A superintendent comes by to inspect the pumps several times a week. "
    r "If we were to outright sabotage the machinery, he'd be notified immediately. Even a slight fall in the RPM would be cause to summon a repair crew."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    
    r "Therefore, we must leave the machines themselves untouched."
    
    r "Nevertheless, to effectively slow down the pumping capacity, we can limit the throughput of water."
    
    r "Some day to day blocking of the pump is natural to occur, and due to frequent blocking and unblocking of the pipes, the throughput of water isn't monitored as strictly as RPM."
    r "If the superintendent notices that throughput is down, he will likely attempt to remove any mud and branches blocking the pipes — thus causing flow to rise again."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    r "However if we systematically limit flow by about twenty percent, it will take him weeks to notice the root cause."

    r "With the amounts of rainfall that are predicted, that's more than enough time. Once the soil is saturated with water, there will be no stopping the flood. "
    r "The embankments, that had already been cracking under the extended period of drought, will engorge themselves with the overabundance of water — eroding under the slightest pressure."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    
    "I was so unprepared for this unexpected outpour of technical detail, that I remained unaware of the ominous implications it spelled." #outpour
    
    "She opened my bag and produced the three glass bottles, each containing a colorless liquid."
    
    show rika dress mischievous day open at center with Dissolve(0.5)  
    r "We have to be careful now, the perchloric acid inside these bottles is known to be highly volatile when disturbed."
    
    a "Hey! I've been carrying these things for the past hour—"
    
    pause(1)
    scene centrifugal
    show rika dress mischievous day open at center 
    with Dissolve(1.0)  
    pause(1)
    
    r "This building houses three large centrifugal pumps."
    r "I will install these bottles to slowly release their contents into the suction side of the installation, giving the water that leads through the pumps highly corrosive properties."
    
    show rika dress mischievous day closed at center with Dissolve(0.2)  
    show rika dress mischievous day open at center with Dissolve(0.2)  
    
    r "At the pressure with which the water is pumped through the machines, the acid will gradually eat away at the metal wear rings that prevent backflow of water, thus creating a tiny clearance."
    r "And in an installation like this, a clearance of even a fraction of a millimeter will significantly decrease pump efficiency."
    pause(1)
    r "It will be like years of wear, all happening within the span of one night. No one will suspect the rings until it's too late."
    r "And replacing the rings is a complicated process that will cause further days of downtime."
    
    pause(1)
    scene pumpingstation_hall
    show rika dress mischievous day open at center 
    with Dissolve(1.0)  
    pause(1) 
    
    r "Please hold guard here, while I head down to the basement to install the bottles."
    r "If anyone shows up you'll have to tell them that we're using this place for a {i}romantic{/i} encounter."
    show rika dress mischievous day closed at center with Dissolve(0.2)  
    show rika dress mischievous day open at center with Dissolve(0.2)    
    #"She winked."

    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc8:

    scene black with fade
    pause(1)
    #play sound "audio/ventilator.ogg" loop fadein 1.0
    scene pumping_twi with Dissolve(0.5)
    play sound "audio/0rainsoft.ogg" loop fadein 1.0 
    window show
    pause(1)


    ## at the shore again

    "As the rains continued, we sheltered at the pumping station, letting our clothes dry on the warm exterior of the engines. "
    
    "Towards the late afternoon the storm subsided a little, and under a veil of perpetual drizzle — that instantly undid the drying of our clothes — we returned to the shore."
    stop sound fadeout 1.5
    pause(1)
    scene lake_twi with Dissolve(0.5)
    play sound "audio/0sealapping.ogg" loop fadein 1.0 
    pause(1)
    
    play music "audio/0goldberg32.ogg" loop fadein 10.0 #maybe no music

    show rika dress happy day open at center with Dissolve(0.5)      
    r "Isn't the water beautiful?"
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    r "You should know, there's a whole world beneath the waves."
    r "A whole realm, uncharted by mankind—"
    "She looked me straight in the eyes."
    pause(2)
    r "I know you like me, Abe."
    
    "I nodded."
    
    show rika dress sad day open at center with Dissolve(0.5)      
    r "The thing is, I want you to {i}understand{/i} me."
    show rika dress sad day closed at center with Dissolve(0.2)  
    show rika dress sad day open at center with Dissolve(0.2)  
    r "To {i}really{/i} understand me—"
    r "I want you to like me, even if everything you've previously known about me turned out to be untrue."
    a "I—"
    
    show rika dress sad day closed at center with Dissolve(0.2)  
    show rika dress sad day open at center with Dissolve(0.2)  
    "She cast her attention back towards the water."
    "As she stared into the sea, she seemed entirely unresponsive — though after a while I noticed a low whisper emanating from her mouth."
    
    play audio "audio/0gurglingmute.ogg" fadein 16.0 #too loud?
    
    "It was a deep throaty sound, barely discernible — and though I initially mistook it for a long, drawn-out cough, there was something deliberate in its phrasing, that made it sound undeniably speech-like."
    
    show rika dress sad day closed at center with Dissolve(0.2)  
    show rika dress sad day open at center with Dissolve(0.2)  
    
    "Rika was casting a spell upon the former sea."
    pause(1)
        
    "She stood there for what felt like an eternity, before suddenly coming back to life."
    pause(1)
    a "Rika—"
    
    show rika dress happy day open at center with Dissolve(0.5)    
    r "It's okay—"
    
    "A sense of relief shone through her tired whispers."
    
    r "Tomorrow we'll have to head back to the pumping house, to retrieve the bottles."
    r "Come on, let's go to the inn. It's growing late."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)     
    "I was about to say something."
    
    r "It's okay, Abe. Our work for today is done."
    show rika dress happy day closed at center with Dissolve(0.2)  
    show rika dress happy day open at center with Dissolve(0.2)  
    r "Reinforcements are underway."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    "And just as I turned to follow her, in the corner of my eye, it was as though I could detect a sudden tremor in the surface of the lake."
    #show lake_twi with hpunch
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc9:

    scene black with fade
    pause(1)
    play sound "audio/0roomrain.ogg" loop fadein 5.0
    scene twinroom with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)


    "Rika went out to buy some fishcakes at the cafeteria — and we sat together in our hotel room eating them in silence, as the rain pattered reassuringly against the window panes."
    
    #We listened to the patter of the rain against the window, a reassuring sound — as it .  
    
    "I was still numb, under the spell of the illicit act we had just so casually committed. "
    "The events of the past days had felt monumental to me, as though I was living in biblical times."
    
    
    "Notwithstanding our humble surroundings, I truly felt that our movements and actions at the time were embodied by a new grandeur. "
    "And the natural self confidence with which Rika spurned me to these deeds, made me feel even more attracted to her. "
    "She had changed so much from the uptight church girl that had introduced herself to me, no more than a month ago. I could truly tell that this was her, in her element."
    "It made me want to see it through with her, to the very end."
    
    pause(1)
    
    "After we'd finished our meal she turned to me."
    
    play music "audio/prelude1.ogg" loop fadein 20.0
    pause(1)
    show rika dress mischievous day closed at center with Dissolve(0.5)   
    pause(1)
    r "I see such a wonderful future for the two of us."
    r "We could become the town's foremost couple, once it has been rid of all unwanted elements. "
    r "You'd have to take on my surname — which isn't exactly tradition in our community, though as a metropolitan man, you surely mustn't mind. "
    r "{i}Abraham and Hendrika Kuyper{/i}. I like the way it sounds. It has a certain {i}ring{/i} to it."
    pause(1)
    r "The island may be lonely at first. "
    r "But I'm sure our unification will be exceedingly fruitful."
    
    show rika dress mischievous day open at center with Dissolve(0.5)     
    r "Abe, the ties between our families go back longer than you may be aware of."
    r "On Abbot we found out the hard way that it was necessary to have a firm grasp on national politics in order to persevere as a community."
    show rika dress mischievous day closed at center with Dissolve(0.2)   
    show rika dress mischievous day open at center with Dissolve(0.2)      
    #For zoning laws, housing legislation. Without a representative in The Hague, "
    r "Your father was one of our most loyal allies. Unscrupulous and loyal. He would do anything for the right price — lobby, pressure, bribe."
    
    show rika dress sad day open at center with Dissolve(0.5)     
    r "I'm so sorry he had to take a fall. I heard it messed up his reputation for good."
    r "But we were happy to provide his family with a rent-free place to live."
    r "Even on Abbot there is plenty of use for his talent of persuasion."
    
    show rika dress sad day closed at center with Dissolve(0.2)   
    show rika dress sad day open at center with Dissolve(0.2)    
    
    r "I heard Karin will be out of hospital soon—"
    
    "The weight of her last words didn't truly sink in. I was too busy working out her previous remarks in my head."
    pause(2)
    "I was never really sure what kind of work my father did."
    "He'd refer to himself a consultant — or a business man — though I was kept in the dark about his day-to-day activities."
    "We were wealthy, had a nice house close to the beach. I never had any material needs — before we came here."
    
    show rika dress sad day closed at center with Dissolve(0.2)   
    show rika dress sad day open at center with Dissolve(0.2)
    
    "Then the headlines appeared — sweeping accusations of corruption — suggesting ties to notorious figures in the underworld."
    "My entire world unraveled."
    "Classmates would call after me. Yelling that my dad was certified mafia—"
    "And my mother moved out — to stay with her sister Maren for a while."
    show rika dress sad day closed at center with Dissolve(0.2)   
    show rika dress sad day open at center with Dissolve(0.2)
    "I asked my father what was going on, but he explained it all away, saying that it was just an unfortunate sequence of misunderstandings."
    "That his reputation would soon be cleared — we'd simply have to escape from the limelight for a while." #mention the Hague?
    pause(1)
    "That's when he devised the plan to move to Abbotsford."
    
    show rika dress sad day closed at center with Dissolve(0.2)   
    show rika dress sad day open at center with Dissolve(0.2)
    "In a sense I was comforted by Rika's praise of his character."
    "Although I always wondered, in the back of my mind, if there wasn't any truth to the allegations — I figured that if my father had done good work for the church—"
    "That it hadn't all been for nothing." #he must at least have done {i}something{/i} worthwhile."
    "That his legacy wasn't wholly tarnished."
    
    #I feel the breath of life is within you."
    #Less abstract gods, unlike JWHW who just sat in his heaven, but real deities that were still responsitive to sacrifice and prayer. Entered symbiosis with these creatures.
    
    
    ## closeup of only her face (partial?) with black background, like in Saya no Uta
    
    
    pause(2)
    
    #TODO: comment on breeding

    a "Rika?"
    pause(1)
    r "What is it?"
    pause(1)
    a "I have one more question, about the church document—"
    show rika dress happy day open at center with Dissolve(0.2)
    r "I was expecting that."
    show rika dress happy day closed at center with Dissolve(0.2)   
    show rika dress happy day open at center with Dissolve(0.2)    
    a "I mean, you've been hinting at things — it makes me wonder."
    a "How much of Thomas Backer's account was truly a fabrication?"
    pause(1)
    r "Oh, Abe—"
    show rika dress happy day closed at center with Dissolve(0.2)   
    show rika dress happy day open at center with Dissolve(0.2)  
    r "You're right. I may as well come clean."

    show rika dress mischievous day open at center with Dissolve(0.5)     
    
    r "You should know—"
    r "They've always been with us."
    pause(1)
    r "The relationships we've fostered with them may wax or wane depending on the times — but they never disappear."
    show rika dress mischievous day closed at center with Dissolve(0.2)   
    show rika dress mischievous day open at center with Dissolve(0.2)      
    r "Like something hidden in the corner of your eye—"
    pause(1)
    r "During the early middle ages, before the low countries were christened, we worshiped them like deities."
    r "There was a fertile magic that sprang from the sea." #they embodied a fertile magic
    show rika dress mischievous day closed at center with Dissolve(0.2)   
    show rika dress mischievous day open at center with Dissolve(0.2) 
    r "But after the missionaries came and forced us to accept Christ as one of our gods — our only god — our adherence to them was forced underground."
    
    r "The more Christianity came to dominate the land, the less people performed the ancient rites. And our distance to them grew." #fix
    
    r "We could no longer communicate out in the open — although they still played a significant role in our lives. Like remnants of an innocent folk-belief."
    r "We'd thank them whenever the catch was bountiful, or scorn them when a ship was lost."
    
    r "And this wasn't just ordinary superstition — for in secret, they continued to accept our prayers and sacrifice. "
    pause(2)    
    r "Oh the world under the waves is enormous—"
    r "—it encompasses far more than the ordinary mind could even fathom."
    r "All of human civilization equates to no more than a thin dusting of mold on the earth, in comparison to the gargantuan edifices they have brought forth."
    show rika dress mischievous day closed at center with Dissolve(0.2)   
    show rika dress mischievous day open at center with Dissolve(0.2)       
   
    #r "During the eighteenth century "
    r "During the seventeenth century, the low countries became a place of unparalleled religious freedom, and it wasn't difficult to mask our polytheistic adherences in a veil of eccentric Protestantism."
    r "And thus the bonds between our worlds grew stronger — we began to reforge our old alliances."
    
    r "It wasn't until 1856 — when that {i}inquisitor{/i} came by — that there came a pushback from the central church."
    
    r "We were cast out, and our island was cut off from mainstream society."
    show rika dress mischievous day closed at center with Dissolve(0.5)     
    r "But to be honest, that suited us quite well."
    
    r "For we do not require the primitive distractions of modernity."
    
    show rika dress happy day closed at center with Dissolve(0.5)  

    r "The bottom of the ocean is as dark and uncharted as outer space. Only dimly illuminated by countless clionidae, that drift omnipresent." #float omnipresent
    
    r "Witnessing only a tiny fraction of the expanse below could drive the uninitiated mind beyond the brink of insanity."
    
    show rika dress happy day open at center with Dissolve(0.5)     
    r "And {i}he{/i} permeates all."
    r "Without beginning and without end — he coils through immeasurable depths, traversing impenetrable darkness."
    #Imagine giant fish gods, jellyfish with enormous craniums."
    # Empathize how different of a world the bottom of the ocean is. "
    # Sea is untainted by original sin. Cleansing properties of the sea."
    # Sea adhered to a different order. Never fell under dominion of God or man."
    #Lotan, the Eel With no End. He coils through immeasurable depths. He permeates impenetrable darkness. "
    # She tells about her dream of an enormous flood that washes away all sin, etc."
    
    #
    pause(1)
    stop music fadeout 20.0
    hide rika with Dissolve(0.5)
    pause(1)
    
    "We crept into bed — and though I was fatigued from the day's events, my head was far too preoccupied to fully come to rest."
    
    scene black with Dissolve(4.0)
    
    "A storm swept through my mind, a limitless gyre of coursing waves that stretched out into the deepest crevices of my soul. "
    
    "It felt like a thousand lifetimes drifted by — as the blanket of darkness shrouded us. Even after I had drifted off into sleep, it wasn't long before I was wide awake again."
    
    pause(2)
    
    "The room was black. My senses dull."
    "All that came to me was her odor, the sweet scent of her youthful pheromones, laying thick in my nostrils, my tastebuds, surrounding, entangling me—"
    "—and I felt ensnared in the pitch black, as though her hair had grown to inconceivable lengths, extending into each and every nook and cranny of the room, stuffing my every orifice, suffocating me—"
    
    #flashback, Rika was swimming here as a child. Pulled under, caught glimpse of world beneath the waves. Got saved at last moment. Allude to this in earlier beach scene."
    
    # she asks him if he will join her, even if they fail"
    
    # Hints at repopulation. (Abraham and Hendrika Kuyper, most powerful couple.)"

    pause(1)
    window hide
    stop sound fadeout 1.0
    scene black with fade
    pause(1)
       
label p5Rc10:

    scene black with fade
    pause(1)
    play sound "audio/0roomrain.ogg" loop fadein 1.0
    scene twinroom with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)

    "We stayed in bed until the early afternoon, before leaving for the pumping station."
    
    pause(1)
    stop sound fadeout 1.0
    scene pumpingstation with Dissolve(2.0)
    play sound "audio/0rainsoft.ogg" loop fadein 1.0
    pause(1)
    
    "Rika had calculated that the acid must have dispersed by now — that enough damage had been done to the internals of the machinery to account for a notable decrease in throughput."
    "We would now dispose of all evidence of our sabotage."
    
    pause(1)
    scene pumpingstation_hall with Dissolve(0.5)
    play sound "audio/0roomrain.ogg" loop fadein 1.0
    pause(1)
    
    "Like before, Rika descended the spiral staircase, whilst I stayed on the lookout for prying eyes."
    "I must confess I wasn't at my sharpest. "
    "It had been a restless night for me, and due to Rika's demanding presence I hadn't been able catch up sleep in the morning. Safe to say, I wasn't at my most vigilant—"
  
    play audio "audio/swipe.ogg"
    show ina shirt surprized day open at left with Dissolve(0.5)      
    play music "audio/0panictheme.ogg" loop fadein 1.0
    n "Abe!"

    n "I knew you two were up to something!"
    show ina shirt angry day open at left with Dissolve(0.5)  
    n "Tell me, where is Rika— "
    n "You need to tell me right now, Abe—"
    #She struck at me a second time. I was in agony, frantically holding on to the banister to prevent myself from breaking down."
    n "Abe, you've been gone for {i}two nights{/i}!"
    show ina shirt angry day closed at left with Dissolve(0.2)  
    show ina shirt angry day open at left with Dissolve(0.2)    
    
    a "Ina — how did you even get in?"
    n "Hah. Do you think there's a lock that {i}I{/i} can't open? It was child's play."
    a "You should probably leave—"
    show ina shirt angry day closed at left with Dissolve(0.2)  
    show ina shirt angry day open at left with Dissolve(0.2)
    n "Leave?! No! Abe, I have it all figured out. The murder, the attack on Karin Voorhees. The church was behind it all!"
    n "And now Rika's trying to disrupt part of the municipal water management system."
    show ina shirt angry day closed at left with Dissolve(0.2)  
    show ina shirt angry day open at left with Dissolve(0.2)      
    n "This is an act of domestic terrorism, Abe. You could go to prison for this—"

    #TODO turns into more pleading, some reflection
    
    play audio "audio/0smash.ogg"    
    #TODO visual vpunch effect
    show ina shirt surprized day open at left with vpunch
    show ina shirt saddened day closed at left with Dissolve(0.2)
    #hide ina with Dissolve(0.2)
    "Suddenly a loud crash resounded through the building, ricocheting of the bare walls and metal machinery. "
    "An empty glass bottle had connected with Ina's pale cheekbone, shattering on impact and sending shards of glass flying in every direction. "
    
    show rika dress mischievous day open at right with Dissolve(0.5)      
    r "Ina! What brings you here?!"
    r "I don't recall sending out a press release!"
    
    "It was Rika, who had reappeared from the basement, holding another bottle casually in her right hand. "
    
    show ina shirt saddened day open at left with Dissolve(0.5) #TODO, new sprite   
    #ina gathered herself
    "Ina stood unevenly, clearly in agony from the blow, frantically holding on to a banister to prevent herself from collapsing."
    
    # some explanation
    
    show rika dress mischievous day closed at right with Dissolve(0.2)       
    show rika dress mischievous day open at right with Dissolve(0.2)      
    r "Your little paper has served us excellently. We'd only have to send you anonymous messages, and you'd publish them without question's asked."
    r "However, I feel that your use has come to an end."
    n "That's not true!"
    "Though Ina's voice was weakened, it still contained a tone of dignified conviction."
    show ina shirt saddened day closed at left with Dissolve(0.2)  
    show ina shirt saddened day open at left with Dissolve(0.2) 
    n "The Sunday Abbot always checks its sources!"
    show rika dress mischievous day closed at right with Dissolve(0.2)       
    show rika dress mischievous day open at right with Dissolve(0.2) 
    r "{i}Checked{/i} their sources, you must mean."
    r "Didn't you receive notification that the school board ended your funding?"
    show ina shirt angry day open at left with Dissolve(0.5)     
    "Ina stared at her contemptuously."
    pause(1)
    #
    n "Abe, look at her! There is madness in her eyes!"
    n "Centuries of inbreeding must have taken their toll."
    pause(1)
    "But when I looked at Rika I saw no madness—"
    "—I saw only glory."
    
    #
    
    hide ina with Dissolve(0.5) #slide down?
    "Ina sunk down, quivering. I could see a thin trickle of blood running down the side of her neck."
    
    n "Abe, please. It's all so {i}irrational{/i}—"
    
    show rika dress mischievous day closed at right with Dissolve(0.5)      
    r "Come Abe, I believe we should leave miss Mengelberg to her own devices."

    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    pause(1)
       
label p5Rc11:

    scene black with fade
    play sound "audio/0searoarrain.ogg" loop fadein 6.0
    pause(2)
    #scene rika_cg_3 with Dissolve(2.0)
    scene rika_cg_3r with Dissolve(3.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    #scene lake_storm with Dissolve(2.0)
    window show
    pause(1)

    "As I followed Rika out to the shore, a sustained current of anticipation surged through me, electrifying my every nerve."    
    
    pause(1)
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)   
    play music "audio/0gloria.ogg" loop fadein 30.0   
    
    r "Can you hear the roaring waves?"
    r "Can you hear their sound — almost like a wailing dirge?"
    r "They are singing their elegy for Abbot's fate."   
    r "The centuries of scorn and humiliation—"
    
    pause(1)
    #scene rika_cg_2 with Dissolve(1.0)    
    #pause(1)
    scene rika_cg_2r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    "Rika stood defiant, her bare feet planted in the ashlike sand and her face twisted into an expression of utter ecstasy."
    pause(1)
  
    #### 0. Start with a history.
     
    r "It is no easy task, to identify the point in time when our misery began—"
    r "—for so many centuries, forces from outside have waged war upon our people, our traditions."
    pause(1)
    r "Was it truly so impossible, for interfering powers, to simply let us be?"
    r "To leave us to our own devices, our own beliefs and patterns of meaning?"
     
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)    
     
    r "No. Violent missionaries, greedy lords — they intruded upon the worldly and spiritual life of our isle, ever since their first ships arrived."
    r "Forcing us to submit to their dominance, until they had extracted our every last morsel."
       
     
    r "Because for these men, these heralds of Moloch, there exists nothing which is unto itself — all is instrumental for the advancement of their kind."
    r "They left us barren, depleted both physically and mentally."
    
    #pause(1)
    #scene rika_cg_1 with Dissolve(1.0) 
    scene rika_cg_1r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    r "And even as the world became enlightened — with the dawning of the modern age — their interference never faltered."
    r "No, exactly the opposite was true."
    r "With emboldened zeal these rational, disenchanted men came for us—"
    r "—this last pocket of untainted culture within their wasteland of a modern world."
    pause(1)
    r "But their systems of suppression had become all the more methodical. Cutting us off, first from mainland society, and then from our beloved sea."
          
    r "How can a civilization become so overconfident? To deem itself worthy to meddle with God's creation in such a way — that it becomes fundamentally degenerated in every sense?"
     
    r "How can you look upon such a civilization? That has completely poisoned the land, and breeds corruption from every orifice?"
    
    r "How can you look upon such a world? Without innately feeling the visceral urge to orchestrate its very obliteration?"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0) 
        
    "Rika held her hand outstretched, as if she were addressing a massive crowd — even though the only ones present on the storm washed beach were myself and a quivering, deathly pale Ina."
     
    "The indulgent beauty of her female form, the natural charisma and the preacherly eloquence with which she spoke her iambic verses, captivated me wholeheartedly." 

    #### 1. The first thing he would do is point out the commonality of the people gathered in the crowd so that he could instantly unify the group. 
    pause(1)
    r "You, Abraham. You belong among us."
    r "Already, you have aided our community so well, even though you have only resided in our midst for a brief period of time."
    
    r "Maybe I should have told you sooner, but this morning I was awakened by a titillating nausea—"
    #r "I feel our destinies have already fused — that it will not be long before I bear your fruit."
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0) 
    
    r "We are one. We and this forsaken isle."
    r "Our destinies are intertwined to such an extent, that disentwinement would be a procedure akin to murder."
    pause(1)
    r "How often have they tried to separate us?"
    r "Through eviction, through coercive land-deals."
    r "Yet Abbot and its inhabitants remain one, indivisible."
    r "We would not leave our homestead behind, not even in our darkest hour!"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0)  
        
    #### 2. The next step would be to identify a threat to that commonality to put the group on edge, and stir up the emotions of fear and anger. 
    
    r "And yet again, a new evil is upon us."
    r "Every century its malice grows, developing new schemes, new ploys to jeopardize our very existence."
    r "O Abraham, you have seen how it operates. How it attempts to demonize us, through its wicked and treacherous ways."
    r "Us, the original inhabitants of this isle—"
    r "—as though we do not have the first right to live here."
    
    scene rika_cg_5r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    r "We have waded through tides of darkness. Wandered in loneliness."
    r "For so long we have witnessed death encroach upon our home, standing powerless against forces that seemed far greater than ourselves."
    r "So much injustice has come our way, over the course of the centuries, hellbent on quashing that small flame of hope that remained."
    r "I want to protect this world, {i}our{/i} world — that is so fragile."
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1.0) 
    #### 3. The third and most important step was to invoke a higher power, and appoint himself as an agent of that higher power. "
    
    #r "How foolish they are. These enlightened men. For in their overbearing arrogance, they disregard the monadic principles that are wholly unfathomable to their rational endeavors."
    
    r "We must turn our hope towards forces that are not so easily silenced."
    r "That hide quietly, in impenetrable depths of endless sea — and under the soil of the land reclaimed."
     
    r "These forces cannot be banished by human measures. They cannot die."
     
    r "They lie silently in wait, slowly building up a bitter resentment against the humans that have buried them."
    r "Waiting for a moment to strike!"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1)  
    
    "At that moment a great thunder cracked the sky and the waves swelled in tumultuous crescendo."
    
    pause(1)
    
    r "When I was little—"
    r "—the waters of the lake would ripple, whenever I came near."
    pause(1)
    r "They say I have a special bond, with those that live below — a special bond that heralds back to my great-great-great grandmother, after whom I was named."
     
    r "I am envoy of resting powers. Only I can restore them to their former glory."
     
    #### 4. give the higher power's “solution” to that threat to the commonality,
    
    r "Can you smell it, Abraham, the hint of brine in the air?"
    r "It's arousing to my nostrils — excites me through and through."
    r "Oh Abraham, the sensations that are currently thrashing though my body, are impossible to describe — for I realize that even currently, as we speak, salt water is slowly flowing back into the lake again."
    
    r "The great purification is commencing as planned."
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1)  
        
    "The intensity of the storm increased — and though it was difficult to make out, among the waves, that were roiling with unmatched fervor, I swore I could discern a glistening, black ribbon winding through the waters."
    
    "And that ribbon, that hypnotizing, serpentine shape, was not just limited to one location—"
    "—no, its unending, ever coiling form appeared to fill all of the sea before me, and maybe a thousand seas beyond."
    pause(1)
    r "Finally! We will be able to break through our veil of despair, and become once again the proud people we were!"
    r "I believe our fated justice is finally ready to break into a brand-new future!"
    
    scene rika_cg_1r with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0
    
    r "Oh a flood will come!"
    r "A powerful, all-encompassing deluge, that will sweep away every morsel of this wicked land!"

    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1)  
    
    #### 5. Q&A: list of criticisms and answer them 
    
    #### 6. and proclaim that carrying out the solution would be a victory for both the commonality and the higher power.
    
    r "Rise high, Lotan! Eel without end!"
    r "Who coils through immeasurable depths!"
    r "Who makes the waters churn!"  
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    pause(1)      
    
    r "The time has finally come to brandish our courage. To reclaim each and every inch of man-made land, once and for all."

    r "The grapes of wrath have fully ripened — their vines bring forth an intoxicating fruit!"

    r "Rise high, Lotan! Eel without end! Let us proclaim this new gospel of revenant hope!"
    r "Let us build a safe world that is illuminated in the shining light of our shared righteousness!"
    r "Come, Abe! To the ark!"
    
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    stop music fadeout 30.0
    pause(2)  

    window hide
    pause(8)
    pause(0.1)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    show white with Dissolve(0.03)
    hide white with Dissolve(0.03)
    pause(0.1)
    play audio "audio/0thunder.ogg" 
    stop sound fadeout 15.0 

    scene black with Dissolve(15.0)
    pause(4)
       
label p5Rc12:

    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)
    
    pause(2)
    play sound "audio/0seawaves.ogg" loop fadein 1.0
    scene lake_twi with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    pause(1)
    window show
    pause(1)
    
    
    #### POSTSCRIPT

    "And for forty days and forty nights the waters of heaven rained down upon the earth—"
    "—and an unstoppable flood stretched out from the lake, taking down houses and villages in its wake."
    
    "And even after the rains dried up, the waters remained upon the land for a further hundred and forty days, and many more days after that."
    
    pause(1)
    
    "And from the waters emerged abominations, more horrid than the world had ever known — for they came from a realm of unspeakable depth."  #
    
    "But these beings did not venture upon the land — for the sea is theirs, just as the land is ours."
    
    pause(1)
    
    "And among these washing waters Abbot arose, an island once more — lonely, defiant, as it had always been."
    
    "And Abbot was spared by the great flood due to the unbreakable bond that had existed between its people and the lords of the deep."
    
    #Dialogue at school, after the town has become an island again
    
    #THen monologue about his love for RIka. (Summarize main philosophy.)
    stop sound fadeout 5.0
    pause(1)
    window hide
    pause(1)

    scene black with Dissolve(1.0)
    pause(1)
       
label p5Rc13:

    scene black with fade
    pause(1)
    play sound "audio/officesound.ogg" loop fadein 1.0
    scene schoolstairs with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1)   
    
    "One month later."
    
    "After the afternoon observance, we headed up to the office to discuss next weeks publication."
    
    pause(1)
    scene office with Dissolve(0.5)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    play music "audio/0canon.ogg" loop fadein 8.0
    show rika uni happy day closed at right with Dissolve(0.5)
    pause(1)
    
    r "Welcome to the second {i}postdiluvian{/i} staff meeting of the Restored Sunday Abbot."
    r "Vice-editor-in-chief Ina, will you please introduce the agenda for today?"
    
    pause(1)
    show ina uni neutral day open at left with Dissolve(0.5)   
    pause(1)
    
    n "There's not much to discuss—"
    n "Our cover article on the remodeling of the Ichthys building should be available for review tomorrow."
    n "Oh, and your father is late in submitting his copy for the {i}Letter from the Reverend{/i} periodical."
    n "Please ask him to hand it in, or we {i}will{/i} go to press without it."
    "Rika giggled playfully."
    show rika uni happy day open at right with Dissolve(0.5)
    r "Please let {i}me{/i} be the judge on that."
    show rika uni happy day closed at right with Dissolve(0.2)
    show rika uni happy day open at right with Dissolve(0.2)    
    n "Anyway, I have to go now. I've promised to pick up the updated roster of school services at the chapel at six."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    
    "As Ina left the room, I could hear her introverted murmuring."
    "The recent changing of the guard at the Sunday Abbot had clearly taken its toll on her."
    
    pause(1)
    
    r "Ina — she's a stubborn one."
    r "How do you think she's reacting to the change?"
    pause(1)
    a "Oh, I'm sure she'll manage."
    a "She seems determined to make the school paper a success."
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene schoolroad_rai with Dissolve(1)
    play sound "audio/0rainsoft.ogg" loop fadein 1.0
    pause(1)
    show rika uni happy day open at right with Dissolve(0.5)
    pause(1)
    
    "We embarked into the mid-day streets, impervious to the drizzling rain, that endured, perpetually, as though it had existed since the birth of time—"
    show rika uni happy day closed at right with Dissolve(0.2)
    show rika uni happy day open at right with Dissolve(0.2)   
    "—and I imagined it could sustain for a thousand years more, indefinitely, into the endless bounds of the future."
    pause(1)
    "I felt, as I looked into Rika's eyes, more blessed than I ever had."
    show rika uni happy day closed at right with Dissolve(0.2)
    show rika uni happy day open at right with Dissolve(0.2)   
    #r "Come on, we have to prepare for tonight."
    #r "It's the first time our parents will be meeting—"
    #r "—that is, with us present, of course."
    
    #r "Come on, I want to take you outside. "
    
    #about father???
    
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop music fadeout 9.0
    #TODO
    
    #### TODO ENDING SCENE
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(3.0)
    pause(4)
    
    jump end
    
        
    ############################################################
    ########## PART 5 MEI ###################################### 
    ############################################################


label p5M1:

    scene white with Dissolve(1.0)
    pause(1)
    play sound "audio/cricketsafternoon.ogg" loop fadein 3.0
    scene part5_mei with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)
    pause(2)
    #scene black with fade
    #pause(1)

    scene residential with Dissolve(2.5)
    pause(1)
    window show
    pause(1)

    "On Monday, when I returned home from school, I encountered an unlikely visitor waiting outside the house."
    
    pause(1)   
    play music "audio/0goldberg1.ogg" loop fadein 5.0  
    scene residential with Dissolve(0.5)
    show rika uni sad day open with Dissolve(0.5)
    pause(1)
    
    "An apprehensive uncertainty had taken over her usually so lofty attitude. It was clear that she'd been dreading this conversation."
    pause(1)
    a "Rika—"
    a "I thought we were through—"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Please don't make this any harder than necessary."

    r "I realize I may have been a little harsh, yesterday."
    r "But try to understand, this isn't about me, or you—"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "At times we must put aside our differences, to protect those who are dear to us."
    pause(1)
    r "In this case — Mei."#"We need to talk about Mei."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    #"My face must have given away my surprise."
    a "Mei—?"
    pause(1)
    r "Over the past month, her condition has been rapidly deteriorating."

    r "She's been displaying increasingly aberrant behavior. Even out in public."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "People are beginning to talk—"
    a "B—behavior? What kind of behavior?"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Mei hasn't been herself recently." #been, been, been, lots of been
    r "Last Saturday she was nearly hit by a tractor, as she fled from some kind of unseen hallucination."
    
    r "She's always been an imaginative girl — but this is giving way to {i}delusion{/i}."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    r "And do you know what I think?"
    "Not much of Rika's initial trepidation remained."    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "I think it's the excitement!"
    r "The exploits among the gravemounds, the trip to the beach—"
    r "It's all too much for her."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "And at times I feel like you don't really care."
    r "That she's just another trophy to you—"
    
    r "But you can't treat Mei like the other girls."
    r "She's too fragile—"
    a "But she—"
    r "Oh I wish I'd put my foot down sooner."
    
    "Rika's tone softened."    
    show rika uni happy day open with Dissolve(0.5)    
    r "I apologize—"
    r "It's not your fault, Abe."
    r "As long as Mei moves freely in this world, she'll meet people who will influence her."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    r "She's nineteen now, a legal adult — there's not much we can do to protect her."
    r "In a sense, your interaction with her has served as a trial, to see how she would fare under new social relationships."
    pause(1)
    r "Relationships we cannot {i}protect{/i} her from."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    r "The thing is—"
    r "Mei's mental issues, they stem from deeper psychological trauma."
    r "At times, she has difficulty distinguishing between what {i}is{/i} and {i}isn't{/i} real."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "The reason she never fared well in school—"
    r "—she would be out causing commotion all day, chasing her imagined fancies."
    
    #"Sadly, there are people for whom there isn't any place in the world. That deviate too far from the norm—"
    a "Isn't she receiving therapy?"
    show rika uni sad day open with Dissolve(1.0)  
    r "She is — and she's made great progress."
    
    r "But now that she's outgrown the programs instituted for children with psychiatric needs, she runs the risk of falling into a dark hole."
    
    r "The adult world preys of fragile minds. We need to protect and prepare Mei as well as we can."
    r "Though I'm not sure if we can offer her the right help."
    "She sighed."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    
    r "Oh I apologize for moaning."
    r "There's been a lot on my mind lately, with the indoor sports exhibition coming up next Friday."
    r "I have no business meddling in other people's affairs. And I won't obstruct you any longer."
    r "But please promise me you'll keep an eye on her."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "If you witness more unusual behavior, you must inform me in a timely manner."
    #show rika uni sad day open with Dissolve(0.5)    
    r "Mei's a highly vulnerable young woman. If her episodes become any worse, she'll be in acute danger."
    
    #"Rika "
    #TODO, have Rika complain about the sports event that is coming up
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   

label p5M2:

    scene black with fade
    pause(1)
    play sound "audio/officesound.ogg" loop fadein 1.0
    scene inahouse with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "Later that afternoon I went to check up on Ina."
    
    "I found her in her room, wholly intrepid."
    "And as she still seemed unwilling to discuss our investigation any further, I decided to ask her what she knew about Mei."
    
    pause(1)   
 
    scene inabedroom_day with Dissolve(0.5)
    pause(1)
    "She stirred."
    play music "audio/0andante664.ogg" loop fadein 15.0  
    show ina cami astonished day open with Dissolve(0.5)
    pause(1)
    
    n "Mei—?"
    n "You mean the slow minded girl?"
    
    show ina cami surprised day open with Dissolve(0.5)
    
    "She cast me a bemused glance."
    
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami surprised day open with Dissolve(0.2)
    
    n "Everyone down here has a story about her."
    n "I let her corner me once, when I was heading back home from school. I must have been in eight grade."
    n "She started spouting a whole story about a family of rock-rabbits who were all friends with her."
    
    n "It took me a while to tear myself loose—"
    n "—without being {i}mean{/i}, you know?"
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami surprised day open with Dissolve(0.2)
    n "You could say she has a vivid imagination." #had it all fleshed out."
    n "I believe she's mostly harmless though—"
    
    n "And the town loves her."
    n "Each year, on the first of May, they crown her May Queen and parade her through the streets on a decorated wagon."
    n "And then the villagers dance around the maypole, while Mei oversees the spectacle from her throne."
    n "The church really abhors this tradition, you'll probably understand why."
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami surprised day open with Dissolve(0.2)
    n "But aside from that, she mainly just loiters around town. You get used to her, after a while."
    show ina cami neutral day open with Dissolve(0.5)    
    "A wrinkle appeared on her forehead."

    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2)
    
    n "But why do you ask?"
    n "I can confirm she's single, if that's what you're after—"
    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2)
    
    a "I've been talking to her, lately."
    show ina cami smart day open with Dissolve(0.5)      
    "Ina smirked."
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami smart day open with Dissolve(0.2)  
    n "If you show even the least bit of interest she'll never let you go."
    
    a "I've noticed—"
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami smart day open with Dissolve(0.2)
    n "Sounds like she's found a willing victim."
    pause(1) #maybe a break?
    a "Mei seems very interested in the geological features of the area."
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami smart day open with Dissolve(0.2)
    n "Sure. Old stones, right?"
    n "They're an obsession of hers." #fixations."
    n "She has one or two things that she really fixates on — and rocks are always one of them."
    show ina cami smile day closed with Dissolve(0.2)
    show ina cami smart day open with Dissolve(0.2)
    n "If I ever get my newspaper back, we could ask her to write a weekly geology report—" #the abbot is canceled
    a "I don't think writing is really her strong point."
    pause(1)
    a "But speaking of geology—"
    a "Mei has stated, a few times now, that Abbot never was a real island."
    a "That it used to be connected to the mainland, somehow. I guess like a peninsula—"
    
    a "Can you make any sense of that?"
    show ina cami neutral day open with Dissolve(0.2)    
    "Ina thought long and hard."
    pause(0.5)
    show ina cami frown day closed with Dissolve(0.2)
    show ina cami neutral day open with Dissolve(0.2)
    n "Not really—"
    
    n "I told you, she has a lively imagination."
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M3:

    scene black with fade
    pause(1)

    play sound "audio/summernight.ogg" loop fadein 1.0
    scene woodpath_twi with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "Even though Mei's farm was just a short distance away, a sticky heat lingered in the evening air that made it an unpleasant journey."
    
    #pause(1)
    play music "audio/walkure_climax.ogg" loop fadein 18.0   
    scene meifarm with Dissolve(1)
    pause(1)
    show mei dress happy day open with Dissolve(0.5)
    pause(1)
    
    "I arrived to find her standing outside. It was clear she'd been waiting for me."
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2)
    
    m "I'm so glad you made it!"

    show mei dress regret day open with Dissolve(0.5)
    "A concerned look formed in her eyes as she inspected my worn out appearance."
    show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret day open with Dissolve(0.2)
    m "I'm sorry for acting so childish yesterday."
    m "But I really am glad you came—"
    show mei dress happy day open with Dissolve(1.5)    
    m "It's still early. Do you want me to show you around the farm?"
    
    m "It's nothing special, you know—"
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2)    
    m "My parents run it by themselves, and I help them as much as possible."
    pause(1)
    m "That's a the cow shed over there."
    "She gestured towards a large, concrete barn that stood adjacent to the house. It appeared to have been erected during simpler times."
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2)
    m "We deliver milk to the village store, and we make our own cheese."
    
    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    scene chickencoop with Dissolve(0.5) #TODO, chicken coop
    pause(1)  
    "She took me down a small country trail, into a clearance between the trees, where an old henhouse stood."
    pause(1)
    show mei dress interested day open at right with Dissolve(0.5)
    pause(1)    
    

    m "This is where we normally keep the chickens. "
    m "Sadly they've all been transferred to a hospital for the time being, due to the recent avid flu outbreak." #hospital
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress interested day open with Dissolve(0.2)
    m "I'll introduce you to them when they're back safely in their coop."
    pause(1)
    "I was impressed by the level of responsibility Mei displayed, now that she was in a familiar environment."
    pause(1)
    
    a "You seem to really know your way around this place."
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress interested day open with Dissolve(0.2)
    m "I do."
    m "My parents are very old, you see?"
    m "They know their way around the farm, but they haven't really kept up with the times."
    show mei dress earnest day open with Dissolve(1.0)    
    "She smiled."
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)
    m "I try to help as much as possible, but it's hard. I don't know for how long we'll be able to stay in business."
    
    #"But we'll work hard till the end."
    pause(1)
    stop sound fadeout 2.0
    hide mei with Dissolve(0.5)

    pause(1)
    scene meiroom with Dissolve(0.5)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)  
    
    "I followed her up to her room."
    
    pause(1)  
    show mei dress happy day open with Dissolve(0.5)
    pause(1)    
    
    m "This is my room."
    
    "She cast me an apologetic smile."
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2)
    m "Not really a place fit for a queen—"
    show mei dress fedup day open with Dissolve(1.0)
    m "It feels more like a prison at times."
    m "A lonely dungeon tower—"
    m "—where I suffer the same torture, every night."
    show mei dress regret day open with Dissolve(0.5)
    "She looked me straight in the eyes."
    show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret day open with Dissolve(0.2)
    m "Have you ever had the same dream—"
    m "—over and over again?"
    pause(1)    
    a "What do you mean?"
    show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret day open with Dissolve(0.2)
    m "Have you? "
    m "A dream that repeats itself — night after night — to the point you wake up screaming?"
    
    #"I've been having that—"
    #Heh, let me think. Maybe one, where's I'm eating oysters at the Hotel Des Indes—"
    #—the same dream, over and over again—"
    #—too many oysters, until I'm nauseous."
    #I'm not sure exactly when they began, as I'd forget them again right after waking up."
    #They'd be hazy, like a blur."
    #They'd feel even more real than the waking world. "
    pause(0.5)
    show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret day open with Dissolve(0.2)
    m "At first it was hazy, like a fog—"
    stop sound fadeout 4.0
    pause(1)

    m "But every time the dream returned, it became clearer and clearer."
    play sound "audio/0seabonfire.ogg" loop fadein 30.0
    show mei dress fedup day closed with Dissolve(0.5)
    m "To the point where I could smell the smoke of the fire, feel the warm stone beneath my feet, hear the lapping of waves and the distant yell of the night-watchmen—"
    
    scene gravemound_nig 
    show mei dress fedup nig closed
    with Dissolve(2.0)
    
    m "—as though I were really there."
    pause(1)

    
    #"Mei's speech pattern was ondergone a grave transformation, rapidly foregoing its youthful playfulness for a sincere monotony as though she were reading from a book."
    
    #"Mei's voice attained the distant quality that it had during her earlier episodes, however her eyes remained unchanged as she recounted the dream."
    #show mei dress fedup day closed with Dissolve(1.0)
    #show mei dress regret day open with Dissolve(0.2)    
    m "I can even hear the tortured breath—"
    show sigurd at right behind mei with Dissolve(1.0)
    m "—of the man—"
    m "—standing before me. Wounded and weary."

    "Mei had closed her eyes, recounting the dream frame by frame from memory, in a grave, monotonous voice that had lost all its prior playfulness."

    #TODO comment on more mature sounding voice
    #show mei dress fedup day closed with Dissolve(0.2)
    #show mei dress regret day open with Dissolve(0.2)      
    pause(1)
    m "Tonight marks thirteen years since Sigurd was taken away."
    
    m "I'm still unwed — though likely not for much longer — and I go up to the dolmen every night, by myself, to pray to the all-mother for Sigurd's return."
    #show mei dress fedup day closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.5)     
    m "But this time I'm not alone."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)       
    m "A man has appeared out from shadows, heavily weakened, spear in hand."
    #"I always dream it this way. Every night."
    
    m "He says he's looking for shelter."
    m "That he was sent away by the night watch — but that he saw a light burning nearby."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)       
    m "And now he's asking for solace and a place to rest his head."
        
    "Mei stared at me intently, as though pleading me to make sense of her words."
    pause(1)
    "But all I could do was stare back in silence."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)       
    
    m "Although I distrust the man, I bandage and feed him."
    m "His naked body appears valiant underneath his wounds—"
    m "—and his eyes radiate a transparent blue."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)           
    
    m "And as he rests, I inquire further into his past."
    stop sound fadeout 6.0
    play effects "audio/0seawaves.ogg" loop fadein 6.0
    m "He tells me enemies hunt him, that they have taken all but his spear."

    scene gravemound_mor
    show mei dress regret nig open  
    show sigurd at right behind mei
    with Dissolve(2.0)
    
    m "The fire has died down, and is slowly replaced by a faint morning light."
    pause(1)
    m "I ask him his name, but he laughs at the question."
    m "Tells me {i}woe is him{/i}. That I can refer to him that way."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)
    m "And the way he laughs, that boyish giggle—"
    m "—not at all woeful—"
    m "—reminds me of a time—"
    m "—long, long ago—"
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)    
    m "—when we played by the sea—"
    
    stop effects fadeout 1.0
    play audio "audio/1pot.ogg"
    scene meiroom
    show mei dress regret day open  
    with Dissolve(0.5)
    
    "Suddenly I heard a crack, as a spontaneous fracture appeared in one of Mei's plant pots."
    "But before I could stand up to inspect the damage — Mei had already resumed speaking, her voice sounding more frantic than before."
    
    play sound "audio/0seawaves.ogg" loop fadein 2.0
    scene gravemound_mor
    show mei dress regret nig open  
    show sigurd at right behind mei
    with Dissolve(2.0)    
    play effects "audio/1battle.ogg" loop fadein 60.0
    #show mei dress fedup day closed with Dissolve(0.2)
    #show mei dress regret day open with Dissolve(0.2)     
    m "We're shaken by the sound of voices and the clatter of steel, coming from the village below."
    m "The enemy has appeared at the gate, laying war upon our homestead for harboring a fugitive."
    show mei dress fedup nig closed with Dissolve(0.2)
    show mei dress regret nig open with Dissolve(0.2)  
    m "I can tell he is in anguish."
    pause(1)
    m "{i}I must leave soon!{/i} he says."
    m "{i}My pursuers will burn down the village if they find out who you are hiding.{/i}"
    
    m "But I beg him to stay. To at least tell me his name."
    m "{i}Please tell me,{/i} I cry. {i}I need to know.{/i}"
    
    stop sound fadeout 2.0
    stop effects fadeout 2.0
    scene meiroom
    show mei dress crying day open 
    with Dissolve(2.0)    
    
    "Mei let out a bitter sigh."
    pause(1)
    m "This is where the dream ends."
    m "The moment when the world becomes intrusive, and the morning sun awakens me"
    
    m "Do you understand my torture now?"
    m "Of dreaming the same dream, again and again."
    pause(1)
    m "Never knowing." #how it ends
    show mei dress white day open with Dissolve(0.1)
    #pause(0.1)
    show mei dress crying day open with Dissolve(0.1)     
    "Her eyes flickered."
    show mei dress happy day closed with Dissolve(1.0) 
    m "Saturday night, I taped cardboard all over the window. So that no light or sound could penetrate my room."
    pause(1)
    m "I know now—"
    show mei dress happy day open with Dissolve(0.5)   
    m "—how the dream goes on."
    
    play sound "audio/0seawaves.ogg" loop fadein 2.0
    scene gravemound_mor
    show mei dress happy nig open 
    show sigurd at right behind mei #with Dissolve(1.0)
    with Dissolve(2.0) 
    m "Amidst the sound of spreading violence I asked him, once more, his name."
    m "Although I knew the answer inside my heart."
    m "And as he held me, he smiled, his eyes radiating in childlike brilliance—"
    
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2) 
    m "{i}Do you not recognize me?{/i}"
    m "—those eyes, that I had cherished—"
    pause(0.5)
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2) 
    m "{i}Do you not recognize me—{/i}"
    m "—during those sun-filled, youthful days."
    m "—{i}now that I have returned—{/i}"
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2) 
    m "—{i}my sister?{/i}"
    show mei dress earnest day open with Dissolve(1.0)
    
    stop sound fadeout 6.0
    scene meiroom
    show mei dress earnest day open 
    with Dissolve(2.0)
    
    "Mei grasped my arm."
    #white eyes
    #show mei dress white day open with Dissolve(0.5)      
    
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)
    m "Is it you?"
    m "Is it really you?"
    pause(1)
    m "Sigurd? My little brother?"
    pause(0.5)
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)
    m "For who I have waited these countless years?"
    
    "She was staring at me as though {i}I{/i} were the apparition from her dream, begging me with pale eyes."
    pause(0.5)
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)
    m "Sigurd."
    m "It really {i}is{/i} you."
    m "I knew all along—"
    pause(0.5)
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)
    m "Please do not leave without me. I will follow you to the edge of night."
    
    pause(1)
    stop sound fadeout 1.0
    scene meifarm_nig with Dissolve(1.0) #farm outside at night
    play sound "audio/summernight.ogg" loop fadein 1.0
    pause(1)  
    
    "She embraced me with an iron grip, not letting go until she was fast asleep."
    #"In the dead of night, I silently exit her room."
    
    stop music fadeout 6.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)   


label p5M4:

    scene black with fade
    pause(1)
    play sound "audio/crowfield.ogg" loop fadein 1.0
    scene school_side with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "It was nearing the end of the year. The school was alive with the carefree bustle of holiday preparations and communal events."
    stop sound fadeout 2.0
    pause(1)
    scene basketball with Dissolve(1.0)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    "But my own mind was occupied with other matters, like the case of the fair-haired girl that had recounted me her dreams the previous night—" #meh
    
    "—and it was with these thoughts in mind that I was approached by Rika, who was laying the last preparations for the indoor sports festival that would be held this coming Friday."    
    
    pause(1)
    play music "audio/0goldberg24.ogg" loop fadein 8.0
    show rika uni sad day open with Dissolve(0.5)
    pause(1)
    
    r "Abe—"
    r "Could you please help me?"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "The basketball team is so irresponsible. They never have their preparations done in time—"
    
    r "They consider themselves star athletes, too good for manual labor."
    r "But who's ever heard of Abbotford's achievements in {i}basketball?{/i} "
    
    "She cast her eyes over the deserted sports hall, which looked no different from usual."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "If it were up to me, I'd discontinue the whole program. We should focus on our strong points—"
    r "Like competitive swimming."
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    "I helped Rika with a few menial task, such as mopping the floor and positioning the bleachers."
    "Then we adjusted the height of the nets to conform with national standards."
    pause(1)
    show rika uni happy day open with Dissolve(0.5)
    #pause(1)
    r "It isn't much, but it'll have to do."
    r "I don't expect many people to show up anyway."
    
    "She turned her attention away from the court."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "Are you coming to cheer for me, this coming Friday?"
    r "We're holding a demonstration tournament at the Olympic pool."
    r "I'd like it if you took my picture — while I'm standing on the podium."
    
    a "You seem pretty confident of victory—"
    show rika uni sad day open with Dissolve(0.5)
    r "Oh I apologize for sounding so self-absorbed. It's just that it's important to create memories."
    r "Especially when it comes to matters as transient as sports achievements—"
    pause(1)
    "I promised Rika I'd be there."
    show rika uni happy day open with Dissolve(0.5)
    #But in the meantime, I was pondering whether I should tell her about the mysterious episode from last night. "
    # TODO, later Abe should feel guilty
    "And before we said goodbye, I decided I wanted to share some of last night's events with her."
    "As she seemed like the only one who was aware of Mei's disposition."
    
    pause(1)
    
    a "I saw Mei again — last night."

    show rika uni sad day open with Dissolve(0.5)
    "An expression of both condemnation and curiosity flashed over her face."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "There, there—"
    r "How was she?"
    
    "I hesitated."
    #"Though I had promised to keep Mei's secret, I felt obliged to report yesterday's episode to Rika, for the sake of her mental health."
    #"I would try to convey the essence of her condition, without going into any detail—"
    pause(1)
    a "She appeared anxious—"
    a "She's been having recurring nightmares—"
    pause(1)
    a "—all centering on her little brother."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    stop music fadeout 4.0
    "Instantly Rika took me by the hand, leading me to the adjacent locker rooms, where we could speak in private."
    hide rika with Dissolve(0.5)
    pause(1)
    scene lockers with Dissolve(0.5) #school lockers
    pause(1)
    play music "audio/0goldberg21.ogg" loop fadein 6.0
    show rika uni sad day open with Dissolve(0.5)    
    pause(1)
    
    r "Her little brother—"
    r "Her {i}long-lost{/i} little brother, right?"
    pause(1)
    a "Yes—"
    "She sighed."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    r "I was afraid of that—"
    r "You should know — Mei doesn't {i}have{/i} a little brother."
    "I nodded."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    #r "Um—"
    r "How should I put this—"
    pause(1)
    r "It's important to keep in mind that not everyone has been as fortunate in life as you and I."
    r "{i}The Lord's ways are as mysterious as the pathway of the wind.{/i}"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Poor girl—"
    r "We've all been condemned to suffer on this world."
    r "But for some the suffering is made {i}so{/i} much more unbearable—" #unbearably much worse
    
    "She cleared her throat, to keep her voice from breaking."
    pause(0.5)
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    r "It all happened about one year before I was born."
    #Mei came to us in spring, about one year before I was born. "

    r "On Sunday morning, the church warden gets up at 5AM to prepare for the Sunday service. "
    
    r "It was spring, but a biting chill still lingered in the fresh morning air."
    r "As the warden unlocked the wooden doors that lead to the main chapel, he heard a faint, exasperated wail."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)  
    r "{i}Many things have changed since the days of arks of bulrushes—{/i}"    
    pause(1)
    r "Mei had been left on the front porch, in the early hours of the morning, wrapped in a blanket and a plastic shopping bag."
    r "There wasn't even a note."   
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)  

    r "If she had been found any later, she may not even have made it."
    "Rika cleared her throat."
    pause(1)
    r "There exists a longstanding custom of leaving foundlings on church steps. "
    r "In the middle ages there would even be a hatch near the entrance of the church, where desperate mothers could safely abandon their unwanted child."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)      
    r "But during the twentieth century, as the standard of living improved, the hatch fell in disuse and was bolted shut."
    r "Mei was the first foundling to turn up in Abbot since the war."
    pause(1)
    r "Poor girl— "
    r "What a miserable start in life she had, to be abandoned by the very people who were chosen to protect her."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2) 
    r "For the first few weeks, she was in and out of hospital, receiving treatment against the effects of undernourishment and hypothermia."
    r "Then she stayed with my parents for a while."
    show rika uni happy day open with Dissolve(0.5)
    r "But little Mei made an impressive recovery — and by the time she was about three months old, she was placed with the Wahlsing couple."
 
    r "They're good people. Somewhat simple minded, but I truly believe they have Mei's best interest in mind."
    r "They were never able to have children of their own, you see? "
    r "So you'll understand how overjoyed they were to welcome the baby in their midst."
    show rika uni sad day open with Dissolve(0.5) 
    r "But there was a rough road ahead."
    r "The first months of an infant's life make up the most crucial part of its formative years."
    r "Mei hadn't received the undivided motherly love, that is so essential for the development of a person's cognitive abilities."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)     
    r "As a child, Mei would always lag behind."
    r "She worked so hard, but still—" 
    pause(1)
    r "When I was three, and she was four, Mei was already like a little sister to me."
    
    r "She was the kindest child I ever knew — with such an {i}active{/i} imagination."
    r "But her speech remained baby-like. She never figured out the alphabet, or how to count."
    r "And it wasn't like she didn't try, it was just that it was all so hard for her."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)     
    r "{i}So{/i} hard—"
    #pause(1)
    r "Like something was in the way, inside her mind."
    r "Something so brilliant, so beautiful, that it drowned out her understanding of the world around her—"
    r "—at times it was as though we lived in different worlds."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)     
    r "Mei entered elementary school one year late, so that we were in the same class."
    r "But even there she struggled."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2) 
    r "The staff, the children — they didn't understand Mei."
    r "All the teachers saw, was her weird behavior and the developmental milestones she kept missing."
    r "And the children took advantage of her kind-hearted nature, by bullying her."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2) 
    r "And though I tried to protect her, I was only small."
    
    r "She simply couldn't go on this way—"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2) 
    r "At the start of our second year, they chose to put her into a separate program."
    
    r "All social services in the town are coordinated by the church — including special education."
    r "We couldn't do much, but at least we could protect her."
    r "Protect her innocent, kind-spirited nature."
    r "I would have hated to see her go through the regular school system."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2) 
    r "The savagery—"
   
    "Rika had clenched her fist tightly around a strand of her ink black hair."
    pause(1)
    r "Mei has been with us for nineteen years now."
    r "The church's protection is coming to an end."
    r "She's not a child anymore. We need to find a place for her where she can learn real-world skills in a sheltered environment."
    pause(1)
    a "Do you have a place in mind?"
    
    "Rika swallowed."
    show rika uni happy day open with Dissolve(0.5) 
    r "We do."
    r "A boarding school, just over the border, in Germany."
    "I was seized by a paralyzing terror."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "They are fully equipped to deal with Mei's mental challenges—"
    
    #"A paralyzing terror seized my heart."
    #I had betrayed Mei's trust , only for her to be sent away to an institution."
    pause(0.5)
    a "You—you're sending her away?"
    r "It's not—"
    a "But she loves it here!"
    show rika uni sad day open with Dissolve(0.5) 
    r "I know, Abe—"
    r "It's just that we can't offer her the care she truly needs."
    r "The recent episodes you speak of, they've only been growing stronger—"
    r "After a while, Mei may no longer be able to distinguish her fantasies from reality."    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    #explain how she may unravel, fall apart."
    r "Don't you see?"
    r "There is something so large, so splendid inside of her—" #TODO beatiful
    r "—as though she isn't truly of this earth."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "But with a mind as beautiful and unique as hers, there always lurks an immanent danger."
    r "If the figments of her mind aren't accurately tempered — she could lose her connection to this world."
    r "And then she may fall victim—"
    r "—to herself." #TODO improve
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    #"We need dedicated professionals to look after her, who have experience with cases like hers."
    
    "I sunk down, defeated."
    pause(1)
    a "Are you sure it's a good place?"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "The very best."
    r "{i}Heilanstalt Uelsenkirchen{/i}, is what it's called."
    r "My father maintains a professional relation with their chaplain."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    #"I'm absolutely positive this is what's best for her."
    r "I promise we'll go visit her. Every month. "
    #"It's just a one-hour drive—"
    
    
    #"For some reason I could feel tears welling up in my eyes."
    "During the moments I'd spent with her, Mei always seemed so bright and easy-going."
    "Though she acted childlike at times, and displayed a stupefying fascination with minerals — I realized I had no idea of the deeper lying issues that surrounded the young woman."
    
    "And though Rika's plan of deporting Mei to a faceless facility filled me with an incumbent dread, I had to admit the church had spent inexhaustible effort towards Mei's wellbeing."
    "An effort that was entirely unthinkable to me."
    "And this realization made the situation so equivocal, that I was unable to think of anything more to say."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "I know it's a hard choice, Abe."
    r "Even for me."
    r "But we need to do what's best for Mei."
    r "I'm absolutely positive this is what's best for her—"
    show rika uni happy day open with Dissolve(0.5)
    r "Over the next days, I want you to spend as much time with her as you can."
    r "To make her time here worthwhile."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "But please don't tell her anything about our plans."
    r "If she catches wind of her upcoming relocation, before being in the right care, it may trigger an intense episode of delirium."
    r "She could harm herself. Or others—"

    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M5:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    play sound "audio/officesound.ogg" loop fadein 1.0
    play music "audio/0andantino20.ogg" loop fadein 8.0
    
    scene diningroom 
    show ina shirt interested day open
    with Dissolve(0.5) #TODO, do kitchen
    #pause(1)
    window show
    pause(1)

    #show ina shirt angry day open with Dissolve(0.5)
    #pause(1)

    #a "Mei will be leaving us soon."
    #show ina shirt angry day closed with Dissolve(0.2)
    #show ina shirt angry day open with Dissolve(0.2)
    n "Mei—?"
    #pause(1)
    a "Rika told me they're moving her to a special facility." #omewhere in the near future?
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
    n "Really? Mei—?"
    n "But she's an integral part of our town."
    n "I couldn't imagine not having her around, roaming the streets—"
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
    n "—harassing people."
    show ina shirt angry day open with Dissolve(1.0)    
    "She turned more serious."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "Was this her parents' decision? To send her there?"
    n "Or is the church behind this?"
    #pause(1)
    a "The church. Her parents aren't even her real parents—"
    n "Hmpf."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "Where are they sending her?"
    a "A place in Germany, in Uelsenkirchen."
    n "Hm—"
    "She took out her phone."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "I think I've read about that place."
    pause(1)
    a "Rika says they're optimally equipped to handle people struggling with her condition—"

    n "Still, I don't like it—"
    n "These types of places are often run by fundamentalists."
    n "They don't hold a rational view on psychiatric care, but consider mental disease a symptom of spiritual impurity."
    n "They have a bad record of dealing with their clients."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "Take a look at this inspection report."
    "She handed me her phone."
    pause(0.5)
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "It speaks of an unsafe environment and unsanitary living conditions."
    n "I've also found a lawsuit that's currently running against the institution, accusing personnel of false imprisonment and physical abuse. "
    pause(1)
    n "This isn't a place where they'll {i}help{/i} Mei."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)    
    n "They're locking her away in a private prison — maybe for good."
    show ina shirt saddened day open with Dissolve(0.5)    
    "I saw a panic forming in Ina's eyes."

    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt saddened day open with Dissolve(0.2)  
    n "You need to {i}warn{/i} her, Abe."
    n "Now! "
    a "Wa— Me? Why me?"
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt saddened day open with Dissolve(0.2)    
    n "You're friends with her. She trusts you."
    pause(1)
    a "I'll try to think of something—"
    
    "I was about to leave, when Ina stopped me."
    
    #What do you expect me to do?"
    #The least thing you can do is tell her. At least then she can choose for herself."
    
    #TODO: Mei repeats that Abbot wasn't Island. Tells it to Ina, but she denies. Later Ina confirms.
    
    
    
    #"Could that make sense at all?"
    #"Not really—"
    #"Sounds like one of her fabrications."
    #"Ina furrowed her brow, and began looking something up on her phone."
    show ina shirt interested day open with Dissolve(0.5)
    
    n "Hey—"
    n "Do you remember the conversation we had the other day?"
    n "About how Mei told you Abbot was never an island."
    
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
        
    n "I looked it up on the heritage website — and I'm afraid I stand somewhat corrected."
    
    n "This area has underwent a lot of geological changes over the centuries—"
    n "The Isle of Abbot was created by a terminal moraine — an elongated accumulation of stones and debris that was left by the glaciers of the late ice age."
    n "It used to stretch out long enough to reach the main land, but due to rising waters it became an island around the year 1400."
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)

    n "So in a sense she {i}was{/i} right, even through she probably just made it up."
    n "I mean we haven't even covered this in high school—"
    pause(1)
    a "I wonder—"
    pause(1)
    a "It would be like Mei, to know these things."
    
    #"She isn't dumb, you know? When it comes to {i}these{/i} things— "
    pause(1)
    a "When she talks about the past—"
    
    "I hesitated."
    pause(1)
    
    a "Never mind."

    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M6:

    scene black with fade
    pause(1)
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene canal_twi with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "I spent the following day restlessly contemplating my next move, while the uncertainty of Mei's approaching fate hung above me like a bronze sword."
    #pause(1)
    "I asked myself if it would be better to follow Ina's advice and warn her of her impending move."
    #pause(1)
    "Maybe Mei wouldn't even mind the prospect — it would be a change of environment for her, a chance to meet new people."
    "I thought back at how much she had enjoyed our trip to Ryebury beach. How much good the new surroundings had done her at the time—"
    
    pause(1)
    stop sound fadeout 1.0
    scene meifarm with Dissolve(0.5) #school gym
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    pause(1)
    play audio "audio/1stone.ogg"
    
    "And lured by these optimistic thoughts, I found myself casting stones at her bedroom window."
    play audio "audio/1stone.ogg"
    "It wasn't long before she emerged from the adjacent workshop."
    
    pause(1)
    show mei blue sad day open with Dissolve(0.5)
    pause(1)
    play music "audio/rheingold_opening.ogg" loop fadein 1.0
    
    m "Careful with those stones! You could break something!"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    a "I thought it was custom around these parts—"
    show mei blue happy day open with Dissolve(0.5)    
    "She giggled."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "We have single glazing, which makes it impossible to get insurance."
    #"Her answer surpized me. Though I had only come to know Mei's carefree side, I was growing aware that Mei was involved in a lot of dealings around the farm."
    
    m "Come on, let's go to my room."
    
    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene meiroom with Dissolve(1.0)
    play sound "audio/officesound.ogg" loop fadein 1.0    
    pause(1)    
        
    "She closed the door behind her."
    
    pause(1)
    show mei blue happy day open with Dissolve(0.5) 
    pause(1)
    
    m "My parents are growing old and forgetful. I have to help them with a lot of things."
    m "Especially since I'm an only child."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)        
    m "I often wonder what will happen when they're no longer here."
    m "If I'll live here by myself, to continue the farm—"
    pause(1)
    a "Do you want to—?"
    "She thought for a while."

    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "I like it here. It's so close to the woods—"
    m "Although the farm work is demanding at times."
    m "I don't know if I'd be able to carry on—"
    
    stop music fadeout 4.0
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "Still, I feel a very strong connection to this place—"
  
    "And when I saw the delighted glimmer in her eyes, I just couldn't put it off any longer."

    pause(1)
    a "Mei — I've come to tell you something."
    a "Rika told me, that the church wants to transfer you to a new school—"
    a "—in Germany." 
    show mei blue sad day open with Dissolve(0.5)  
    "Mei stared at me uncomprehendingly."
    play effects "audio/1pianoending.ogg" loop fadein 40.0  
    pause(1)
    a "She said it would be a place where you'd be able to learn many new things—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "Rika—?"
    m "Did Rika really say that?"
    a "I'm not sure if {i}she{/i} came up with the idea, but she was the one who told me."

    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "I don't understand—"
    m "I {i}have{/i} to stay here. My parents need me."
    
    m "I don't want to be transferred—"
    #a "Yes—"
    
    "A faraway shimmer was forming in her eyes."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)    
    m "I know I said the farm work was hard at times—"
    #a "I believe you if you say you want to stay."
    show mei blue crying day open with Dissolve(0.5)  
    m "—like the chickens—"
    m "—I know they aren't really brought to a hospital."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)  
    m "They get killed, all of them, when a pandemic breaks out."
    m "Not just the hens, but the little chicks too—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)     
    m "It doesn't matter if they're infected or not. It's just a preventive measure—"
    m "Papa would always tell me they were moved to a hospital, just so that I wouldn't cry—"
    m "But now that I'm older, I'm the one who oversees the process—"
    m "—and it doesn't change a thing—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)     
    m "—I still cry."

    pause(1.0)
    m "Do you understand how hard it is?"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2) 
    m "I want to stay here. I want to go to the dolmen with you."

    m "Why didn't Rika tell me—?"
    
    play audio "audio/knocksoft.ogg"

    show mei blue crying day open with vpunch
    "There was a knock at the outside door. Mei leapt up, letting out a muffled scream in the process."
    "We hurried to the window. And in the faint light we saw a black Mercedes-Benz, parked in the driveway."
    "At the gate stood two dark-clothed figures, led by a handsome looking man who appeared to be in his early forties."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)     
    m "That's John, Rika's father!"
    play audio "audio/knocksoft.ogg"
    "Another knock, louder this time."
    pause(1)
    m "Mama is home, she'll answer to the door soon."
    "Mei's voice was trembling with fear."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2) 
    m "Are they coming to {i}transfer{/i} me—?"
    "Not wanting to lie to her, I just stared at her wordlessly."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)    
    m "I don't want to go—"

    m "Why didn't Rika discuss this with me?"
    pause(1)
    m "Rika—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    m "I really don't want to—"    
    m "No—"
    pause(1)
    m "No—!"
    #"An acute panic had taken control of her."
    "Her breath intensified. An abstract terror had formed in her eyes."
    
    "Then she addressed me, clearer and more coherent than ever."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    m "I {i}can't{/i} leave!"
    m "I like it here. I like you, and Rika, and even the church!"
    m "I have to stay here, in Abbotsford, with the stones."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)    
    stop effects fadeout 20.0
    m "I promise I won't cause any trouble. I will stay inside. I will try harder!"
    m "Tell Rika to let me stay. Please let me stay here!"
    "Tears were rolling down her cheeks."
    
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    m "I need to stay here, to wait for him. I need to be {i}here!{/i}"
    
    "In the meantime, I could hear Mrs. Wahlsing answer the door and conversing with John Kuyper. "
    #"She appeared to have a resigned air about her, and"
    "She sounded unfazed by the nocturnal visit, and it struck me that, like myself, she must have been informed beforehand. "
    "It wouldn't be long before she'd let the men in."
    pause(1)
    play music "audio/siegfried_opening.ogg" loop fadein 15.0
    "Mei had sunk to her knees, paralyzed with fear."
    "The intensity of the moment weighed down on me. And I suddenly grew aware that, right now, we stood before a gambit that would irreversibly change both of our futures."
    "I looked her in the eyes."
    "Her quivering form appeared so far removed from the cheerful girl I had come to know — that I suddenly felt a rare courage take hold of me." #make less cliché"
    pause(1)
    a "Mei—"
    a "We could, {i}escape{/i}."
    "And the second that last word passed my lips—"
    show mei blue happy day closed with Dissolve(1.0)
    "—she grew calm."

    m "Escape—"
    m "We have to escape—"
    m "—again."
    pause(1)
    m "I'm not afraid—"
    m "—as long as I'm with you."
    show mei blue white day smile with Dissolve(0.5) #white eyes
    m "Sigurd—"
    play effects "audio/winds.ogg" loop
    "At that moment a tropical wind spread through the tiny bedroom, blowing back her golden hair, and revealing the pale, spotless white of her mesmerized eyes."
    m "I'm not afraid—"
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue white day smile with Dissolve(0.2)
    m "I trust you—"
    m "—if it's really you—" 
    m "Sigurd—"
    play audio "audio/1approachingsteps.ogg"
    "Heavy footsteps on the stairs." #sfx

    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue white day smile with Dissolve(0.2)
    m "Is it really you—?"
    
    #######################################################################################################################
    
    menu:
        with Dissolve(1.0)
        m "Is it really you—?"
    
        #### MEI LAST DECISION
        "It is me.":
            #### MEI POSITIVE
            show mei blue sincere day open with Dissolve(1.0)
            "A relieved smile crossed her face."
            pause(1)
            m "I knew it was you. "
    
        "It isn't.":
            #### MEI NEGATIVE
            #show mei blue sad day closed with Dissolve(0.2)    
            show mei blue white day frown with Dissolve(0.5)
            "But—"
            pause(1)
            "The dream—"
            pause(1)
            
            menu:
                with Dissolve(1.0)
                m "It must be you—"
        
                #### MEI VERY LAST DECISION    
                "I'm sorry. Mei—":
                    #### MEI NEGATIVE
                    stop effects fadeout 3.0

                    show mei blue sad day open with Dissolve(0.5)
                    "Immediately her eyes went back to normal."
                    pause(1)
                    m "You're right."
                    m "I'm sorry — I'm not myself at the moment."
                    m "I'm sorry for causing you so much trouble."
                    play audio "audio/knock.ogg"
                    "There was a loud knock at the door."
                    "She straightened her summer dress."
                    show mei blue sad day closed with Dissolve(0.2)    
                    show mei blue sad day open with Dissolve(0.2)
                    m "Please visit me often, while I'm away."
                    m "And don't worry about me—"

                    stop music fadeout 15.0

                    
                    pause(1)
                    hide mei with Dissolve(0.5)
                    pause(1)
                    "She got up and opened the door."
                    pause(1)
                    window hide
                    pause(1)

                    stop sound fadeout 1.0
                    scene white with Dissolve(2.0)
                    pause(3)  
                    jump mBad
                    
                "I need more time to remember.":
                    #### MEI POSITIVE
                    show mei blue sincere day open with Dissolve(1.0)
                    "A relieved smile crossed her face."
    
    ####
    
    #"A relieved smile crossed her face."

    show mei blue sincere day closed with Dissolve(0.2)    
    show mei blue sincere day open with Dissolve(0.2)     
    m "I'm so happy—"
    play audio "audio/knock.ogg"
    #"They were standing in the hall."
    #"There was a louder knock at the door of her room."
    a "Come, to the window!" #sfx window opening
    hide mei with Dissolve(0.5)
    play audio "audio/window.ogg"
        
    "The drop wasn't more than a few meters. "
    
    #pause(1)
    #hide mei with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    stop effects fadeout 3.0
    play audio "audio/swipe.ogg"
    scene meifarm_nig with vpunch
    scene meifarm_nig with vpunch
    play sound "audio/summernight.ogg" loop fadein 1.0
    #pause(1)
    
    "I leapt down first. As I caught Mei, who was a lot heavier than I'd imagined, I heard the door to her room open."
    
    #pause(1)
    scene chickencoop_nig with Dissolve(0.5) #chickencoop night
    #pause(1)    
    
    "But Mei took me by the hand and led me out over the yard and into the nearby undergrowth."
    scene woods2_nig with Dissolve(0.5) #chickencoop night
    
    "And I followed her, her golden hair guiding me through the pale moonlight."

    pause(1)
    window hide
    pause(1)
    #stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M7:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    play sound "audio/summernight.ogg" loop fadein 1.0
    scene woods2_nig with Dissolve(0.5)
    #pause(1)
    window show
    #pause(1)

    "The first minutes were hectic. We crawled through the thick bushes, gradually growing aware of the frantic shouts and heavy footsteps that emerged from the house behind us."
    "But by the time Kuyper and his henchmen had made their way outside, we had left them far behind."
    "Our progress was slow. We tried to stay away from the major footpaths and roads, taking detours whenever our path led us over exposed terrain. "
    "But the woodlands surrounding Abbotsford were wild and expansive enough to disappear into—"
    "—and so we did, for a good three hours, until it was completely dark outside and even Mei was uncertain of our current whereabouts."
    
    "She looked exhausted—"
    pause(1)
    m "What do we do?"
    m "Where do we go—?"
    pause(1)
    a "I was hoping {i}you{/i} would answer that question—"
    
    pause(1)
    scene trail_nig with Dissolve(0.5)
    pause(1)
    
    "Slowly we made our way through an opening in the trees that lead to a narrow trail."
    "Mei looked around, trying to discern our location."
    "Then she let out a sigh of relief."
    show mei blue happy nig open at right with Dissolve(0.5)
    m "I know this trail — it leads to the stones."
    "I gestured her to lower her voice."
    a "Are you sure it's safe?"
    show mei blue sad nig open with Dissolve(0.5)   
    "She looked up at me drowsily, her eyes almost falling shut. I could tell she wouldn't make it much further."
 
    m "Let's go—"
    #pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    scene townpark_nig with Dissolve(0.5)
    pause(1)
    
    "In the dead of night we arrived at the archaeological site."
    "We settled down in an alcove between the two megaliths, where we were invisible from the road."
    
    pause(1)
    scene stones_nig with Dissolve(0.5) #TODO see if ok, maybe scrap
    pause(1)
    show mei blue happy nig open with Dissolve(0.5)
    pause(1)
    #"Feel them—"
    m "They feel warm, don't they?"
    m "We're safe here—"
    #pause(1)
    hide mei with Dissolve(0.5)    
    stop music fadeout 5.0
    "Before I could even say a word, she had drifted off into sleep."
    "And though I'd made a resolve to hold watch all night, it wasn't long before I joined her—"
    
    #### break 
    scene black with Dissolve(2.0)
    pause(1)
    play effects "audio/1leaves.ogg" loop #fadein 2.0

    pause(0.5)
    play audio "audio/bark1.ogg"    
    play music "audio/0panictheme.ogg" loop fadein 1.0
    pause(0.5)
    scene nightsky_dark with Dissolve(0.2)  
    scene black with Dissolve(0.2)
    scene nightsky_dark with Dissolve(0.2)  
    scene black with Dissolve(0.2)
    pause(1)
    scene nightsky_dark with Dissolve(0.2)    

    "Aggressive shouting, footsteps. I found myself wide awake, tugging at Mei's sluggish body—"
    
    "Her eyes shot open."
    m "D—danger!"
    a "They're on to us! We need to move fast!"
    a "I think they have a hound!"
    "In the corner of my eye I saw two of Kuyper's men making their way in our direction."

    #pause(1)
    scene townpark_nig with Dissolve(0.5) #TODO night version
    #pause(1)
    
    "Then a white bolt split the sky."
    play audio "audio/angrydog.ogg" fadein 2.0
    "I saw one of the thugs rolling on the grass, clutching his leg in agony. "
    
    pause(1)
    show mei blue sincere nig open with Dissolve(0.5)
    pause(1)
    
    m "It's Phyrrus!"
    "Mei had scrambled to her feet."
    m "Come on, run!"
    stop effects fadeout 3.0
    hide mei with Dissolve(0.5)
    stop music fadeout 6.0
    
    "While Phyrrus kept our assailants at bay, we bolted over the lawn, into the dense forest that led northward."
    
    pause(1)
    play effects "audio/walkure_climax.ogg" loop fadein 30.0
    scene woods4_nig with Dissolve(0.5)
    pause(1)
    
    "Mei seemed sharper now, rejuvenated by the few hours of undisturbed sleep."
    "We traveled where the woods were at their darkest — so that we had to find our way by touch."
    "And though we kept moving,{nw}"
    play audio "audio/1leaves.ogg" fadein 1.0
    extend " it wasn't long before we grew aware of an ominous rustling of the bushes behind us." #staying out of the open field like we previously had,
    pause(1)
    "I froze."
    "Mei cowered beside me." #meh
    "The rustling intensified. The bushes opened."
    
    pause(1)
    show phyrrus_r nig at left with Dissolve(0.5)
    
    "And out leapt Phyrrus — our silent protector."
    
    pause(1)
    show mei blue happy nig open at right behind phyrrus with Dissolve(0.5)    
        
    m "Phyrrus—!"
    "Mei spoke in excited whispers."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2) 
    m "Thank you for helping us back there—"
    m "—they didn't hurt you, did they?"
    play audio "audio/panting.ogg" fadein 2.0
    "Phyrrus sat panting quietly."
    
    "Though I urged Mei to head on further, she remained concentrated on the dog."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2) 
    m "Phyrrus—"
    m "Can you help us with one more thing—?"
    m "We want to go to the castle hall. "
    m "You remember? The place in the woods where the floor is covered in stone."
    "The dog stared at her with a playful look in its eyes. There was no indication that it had understood her request."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2) 
    m "Could you lead us there? I promise there will be a real treat this time."
    "The dog turned its head."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2) 
    m "Thank you."
    pause(1)
    hide phyrrus_r with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    pause(1)
    stop effects fadeout 8.0
    scene forest2_nig with Dissolve(1.0)
    pause(1)
    
    "And through the thick undergrowth we continued, slowly but steadily, never resting for longer than a minute."
    "At times Phyrrus led the way, but he would also lag behind, seemingly oblivious to his surroundings. "
    "But from the highly inconsistent moss-patterns on the trees, I could tell were roughly traveling northward."

    pause(1)
    window hide
    pause(1)

    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M8:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    play sound "audio/crowfield.ogg" loop fadein 1.0
    scene castlehall_mor with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "The morning light had grown in intensity and was now tentatively making its way through the blanket of misty trees." #improve slightly
    "I felt tired to the point that I cursed myself for ever embarking on this pointless journey."

    #pause(1)
    scene mei_cg_3 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    #pause(1)
    "Mei however, had grown unusually quiet."
    "Carefully she made her way around the clearance, muttering softly to herself and casting anxious glances through the trees."
    play music "audio/siegfried_climax.ogg" fadein 20.0           
    "Then she turned to me."
        

    pause(2)

    m "We're fleeing again—"
    
    #m "We're safe here, we can rest for a while—"
    #and judging from Mei's facial expression, she was feeling not much different." #change
    
    #"We're fleeing again—"

    # We can rest inside the dolmen, if you want. It goes very deep, you know— "#?
    
    #"Her voice trailed off."   

    pause(1)
    m "Always fleeing—"
    #m "Always fleeing—"
    m "Just like back then—"
    pause(1)
    m "We traveled for months through inhospitable terrain."
    m "But no matter how dangerous our journey was, I basked in a consoling bliss."
    m "For I had reunited with Sigurd. My little brother."
    m "And my happiness drove away the fear."
    pause(1)

    m "The terrain was made up of treacherous marshes, intersected by patches of pine-wood."

    m "Over the past centuries, the seas had slowly encroached upon our settlements, gradually turning the arable pastures into basins of brackish swampland."
    m "Food became scarce — and many of the tribes that had been allied in the past, resorted to warfare over the dwindling resources."
    #pause(1)
    stop sound fadeout 5.0
    m "Wherever we went, we were met with distrust and hostility."
    play sound "audio/1flowing.ogg" loop fadein 6.0
    m "Traveling outcasts, left to fend for ourselves — with only Sigurd's spear for protection."
    
    #"And though it felt lonely at times, ever since the first day of our journey—"
    #"—I was growing aware of the hidden presence trailing us."
    #"No more than a dark shadow at first, always remaining at a safe distance."
    #"But we knew in our hearts that it was a force of good—"
    
    scene mei_cg_4 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    
    pause(1)
    m "Then one day, when crossing a woodland fen — {nw}"
    play effects "audio/1serpent.ogg" loop
    extend " a large\nappendage lashed out from the shallow waters!" #sfx splash
    m "It wrapped itself around Sigurd's waist — evading the blows of his spear, preparing to strike with its large, toothed maw."
    
    m "When suddenly—"
    play audio "audio/1wolfgrowl.ogg"
    m "—out from the shadow leapt a great, gray wolf. And the creature lunged it fangs deep into the snake's flank, lacerating its scaly armor."
    stop effects fadeout 4.0    
    m "The serpent shrieked out in pain, dropping Sigurd as it turned its attention towards its canine assailant."
    m "It coiled itself around the wolf,{nw}"    
    play audio "audio/1dogwhine.ogg"
    extend " trying to squeeze out\nits very life."
    m "But the wolf was strong — much stronger than any mortal beast — and it resisted the serpent's strangling grip."
    
    m "Long enough for Sigurd,{nw}"
    play audio "audio/0attack.ogg"
    extend " to thrust his spear into the monster's gaping maw, impaling it in the mud."
    
    pause(1)

    m "Slowly the wolf rose to its feet. Shaking out its drenched fur."
    m "Beifre — the all-mother, ancestor to our tribe — is capable of taking many forms."

    pause(1)
    stop sound fadeout 5.0
    m "Although the serpent was defeated — we realized he was a herald of an encroaching kind."
    m "As the sea spread out through our domains, nautical deities became gradually more dominant—"
    
    m "—pushing back our traditional chthonic gods into the depths of the underworld."
    
    scene mei_cg_2 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    
    pause(1)
    m "Summer turned to autumn. "
    play sound "audio/1winter.ogg" loop fadein 3.0
    m "Autumn turned to winter. "
    m "Nature died."
    pause(1)
    m "Now that the marshes had frozen over, serpents stood at bay."
    
    m "And we built a shelter, in the forest, against the winter storms."
    m "But we couldn't stay in the same place for long, as food was always scarce."
    m "And I was five months pregnant at the time, I couldn't travel fast—"
    
    pause(1)
    
    m "During the coldest nights, Beifre would enter our camp. Sleeping between the two of us."
    m "And her radiating warmth would drive away the freezing cold faster than any furnace."
    pause(1)
    stop music fadeout 8.0
    m "Beifre, the great wolf, our mother. Always watching over us—"

    pause(2)
    window hide
    stop sound fadeout 4.0
    pause(2)
    scene black with fade
    pause(2)   


label p5M9:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    #play sound "audio/.ogg" loop fadein 1.0
    scene castlehall with Dissolve(0.5)
    pause(1)
    window show
    pause(1)
    
    #show mei blue sad day open with Dissolve(0.5)

    "We rested for a while in the castle hall, but the ground was cold and barren."
    
    pause(1)
    scene gravemound with Dissolve(1.0)
    play sound "<from 10.0>audio/crowfield.ogg" loop fadein 1.0    
    pause(1)
    play music "audio/walkure_gentle.ogg" loop fadein 20.0
    "And urged forward instinctively by our fatigue, we made our way to the S-dolmen, which stood nearby."
        
    pause(1)
    stop sound fadeout 1.0
    scene dolmenint with Dissolve(0.5)

    pause(1)
    
    "Inside its earthen interior — which turned out to be quite spacious — we constructed a comfortable burrow from moss and fallen leaves, while Phyrrus camped outside to defend us against potential threats."
    pause(1)
    show mei blue sad nig open with Dissolve(0.5)
    pause(1)
    a "This used to be a gravemound, right? "
    a "What a morbid place to hide in."
    show mei blue sad nig closed with Dissolve(0.2)    
    show mei blue sad nig open with Dissolve(0.2)
    m "A gravemound, indeed—"
    m "—but it was far {i}more{/i} than that."
    m "A place of worship, an assembly hall—"
    "Her voice was beginning to drawl."  
    show mei blue happy nig open with Dissolve(0.5)
    m "We lived together with the dead back then, our ancestors—"
    m "Nothing to be afraid of—"
    
    #"But she had already drifted away— "
    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    stop sound fadeout 2.0
    stop music fadeout 4.0
    scene black with Dissolve(2.5)
    pause(1)
    
    "We slept all morning and most of the afternoon."
     
    pause(1)
    window hide
    pause(1)
#    stop music fadeout 1.0

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    play sound "<from 15.0>audio/crowfield.ogg" loop fadein 1.0
    scene dolmenint with Dissolve(2.5)
    pause(1)
    window show
    pause(1)
    play music "<from 53.0>audio/walkure_gentle.ogg" loop fadein 30.0
    "I awoke completely disoriented — more fatigued than before I fell asleep. "
    
    pause(1)
    
    #"As my memories of the past days returned to me, I was overcome by pressing sense of panic. "
    "The adrenaline that had fueled my previous actions had dwindled, making place for an intangible dread."
    
    "When I looked on my phone I saw a few missed calls from Ina.{nw}"
    play audio "audio/dialing.ogg" fadein 0.5
    extend " I dialed her number immediately."
    pause(1)
    
    a "Ina—"
    pause(1)
    n "Abe, I've been trying to call you all day!"
    n "What {i}have{/i} you two been up to?!"
    "Her voice sounded unwaveringly curious."
    pause(1)
    a "I did what you told me to. I warned her—"
    "I provided Ina a summary of last night's escape."
    pause(1)
    a "Has the town reacted to our disappearance yet?"
    n "Hm—"
    n "I heard some shouting coming from central square this morning—"
    n "—but I'm not aware of any large scale search operations."
    n "The church probably wants to keep Mei's escape under wraps for now — as not to fall under scrutiny for their actions."
    #"Mei's a well-known appearance around town. Though quirky, most people do feel a certain fondness towards her—"
    
    #"While I waited for Ina to come, Mei slowly awoke."
    
    n "Anyway, what's your current whereabouts?"
    pause(1)
    stop music fadeout 4.0
    a "Dolmen M4, near the northeastern slope."
    n "Please wait, I'll head down immediately."
    pause(1)
    a "Make sure no one follows you."
    
    #I'll come down with groceries and sleeping bags. Please wait for me."
    
    pause(1)
    scene gravemound with Dissolve(1.0)
    pause(1)
    show phyrrus at right with Dissolve(0.5)
    play audio "audio/bark1.ogg"
    pause(1)

    "It wasn't long before we were alerted by Phyrrus' muted barking."
    
    pause(1)
    #show mei dress earnest day open at right with Dissolve(0.5)
    play music "audio/0adagio15.ogg" loop fadein 15.0
    show ina shirt angry day open at left with Dissolve(0.5)

    pause(1)
    
    n "There, there, Phyrrus. I brought you some sausages. Please be quiet."
    pause(1)
    a "Ina, I'm glad you could make it."
    hide phyrrus with Dissolve(1.0)


    n "I've brought groceries, for lunch and dinner, and tomorrow's breakfast."
    show mei blue sincere day open at right with Dissolve(1.0)
    n "You probably haven't eaten for days—"
    show mei blue sincere day closed with Dissolve(0.2)    
    show mei blue sincere day open with Dissolve(0.2)  
    "Mei cast Ina a ravenous glance."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "I also brought you some sleeping bags, as you'll probably have to stay here for at least another night."
    n "I'll start looking for better options this evening." 
    show mei blue sad day open with Dissolve(0.5)  
    m "I don't understand—"
    m "Why did Rika do this to me?"
    show ina shirt smiling day open with Dissolve(0.5)    
    "Ina gave Mei a comforting nudge."
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)    
    n "Don't worry, we'll find a solution."
    n "I promise."
    n "But let's eat first."
    
    pause(1)
    hide ina with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    pause(1)
    stop sound fadeout 2.0
    play effects "audio/summernight.ogg" loop fadein 2.0
    scene gravemound_twi with Dissolve(2.0)

    pause(1)
    
    "Under the setting sun, we feasted on the bread and canned goods that Ina had brought us."
    "After our meal, Ina, who still had a lot of research to do, got ready to leave."
    "And while Mei stashed our newgained supplies inside of our burrow, Ina took me aside for a second."
    
    pause(1)
    show ina shirt angry twi open at center with Dissolve(0.5)
    pause(1)
    
    n "I want to get Mei some clean underwear — the poor girl must be suffering."
    "I felt the blood rush to my head."
    show ina shirt angry twi closed with Dissolve(0.2)
    show ina shirt angry twi open with Dissolve(0.2)
    n "Would you happen to know her, um—"
    n "—sizes?"
    pause(1)
    a "Her {i}sizes{/i}—"
    show ina shirt angry twi closed with Dissolve(0.2)
    show ina shirt angry twi open with Dissolve(0.2)
    n "Well—?"
    a "W—why don't you ask {i}her{/i}?"
    show ina shirt blushing twi open with Dissolve(0.5)
    "She blushed."
    show ina shirt blushing twi closed with Dissolve(0.2)
    show ina shirt blushing twi open with Dissolve(0.2)
    n "I don't know — it's embarrassing."
    n "I mean, I thought {i}you{/i} might know—"
    
    a "I definitely don't—"
    "She pouted."
    show ina shirt blushing twi closed with Dissolve(0.2)
    show ina shirt blushing twi open with Dissolve(0.2)
    n "Well, I think she's larger than me. But not by much."
    pause(1)
    n "Now that I think of it. The clothing store is owned by church people."
    n "They may become suspicious if I suddenly start buying larger sizes."
    show ina shirt blushing twi closed with Dissolve(0.2)
    show ina shirt blushing twi open with Dissolve(0.2)
    a "You could tell them you've increased your dairy intake—"
    
    #"They may just think you had a growth spurt."
    "Ina glared at me."
    show ina shirt blushing twi closed with Dissolve(0.2)
    show ina shirt blushing twi open with Dissolve(0.2)
    n "She'll just have to do with some of my spares—"
    
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    stop music fadeout 5.0
    stop sound fadeout 1.0
    scene dolmenint with Dissolve(0.5)
    play sound "<from 10.0>audio/crowfield.ogg" loop fadein 1.0
    pause(1)
    
    "Ina went home, and Mei and I turned in early."
    show mei blue sad nig closed with Dissolve(0.5)
    "And while I fell into a restless, fragmented sleep—"
    "—Mei remained sitting upright, whispering long stories to herself."
    "And sometimes it was as though I felt a quiet rumble passing through the stones below us."

    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop effects fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)   


label p5M10:

    scene black with fade
    pause(1)

    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    scene gravemound with Dissolve(0.5)
    pause(1)
    window show
    pause(1)

    "After breakfast, Ina returned, carrying clean clothing for Mei and additional supplies." #She had brought with her a visitor.
    
    pause(1)
    play music "audio/0andante664.ogg" loop fadein 10.0
    show ina shirt angry day open at left with Dissolve(0.5)   
    show mei blue sincere day open at right with Dissolve(0.5)  
    pause(1)
    
    a "I could do with some boxer shorts, you know—"
    n "Oh please, I'm not your mother."
    
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "I've been working tirelessly all night, just to get the two of you out of this sticky situation."
    n "I've scheduled a call with a representative of the women's shelter in Bremersberg this coming Thursday. Mei may be able to stay with them for a while."
    n "The church won't be able to find her there."
    pause(1)
    a "Have you looked into places for {i}me{/i} to stay?"
    n "Hmpf — not really."
    n "But you'll have a roof above your head once they lock you away for kidnapping a mentally impaired individual—"
    show mei blue sad day open with Dissolve(0.5)
    m "Hey—!"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "I'm not mentally impaired!"
    "Mei glared at Ina disapointedly."

    show ina shirt interested day open with Dissolve(0.5)
    n "I'm sorry, I must have had the two of you mixed up for a second. "
    
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
    
    n "Anyway Mei, I brought you something else—"
    "Ina reached into her bag and produced a large book."
    "{i}Illustrated Geological Lexicon{/i}, was written on its cover."
    "Mei eyed it apprehensively."
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
    n "I though it might provide you with some distraction. While you're keeping a low profile—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "Thank you, Ina."
    m "It's just—"
    m "I'm not a very good reader—"
    
    "Ina smirked."
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)
    n "Are you sure about that?"
    n "Come on, let's take a look at this together."
    n "I'd love to find out how bad your reading {i}truly{/i} is."
    show mei blue happy day open with Dissolve(0.5)
    n "Even Abe here can read. Can't you, Abe?"
    
    "The two girls giggled, as they seated themselves against the base of the dolmen. "
    
    pause(1)
    hide ina with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    pause(1)
    
    "And as soon as Ina opened the book to reveal the illustrations inside, Mei's initial hesitation turned into pure delight."
    pause(1)
    m "Oh look! That's Limestone—"
    m "—and Hematite!"
    
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause(0.5)
    play sound "audio/edgemeadow.ogg" loop fadein 2.0
    scene gravemound with Dissolve(0.5)
    pause(1)
    #At midday, I was shaken up by a strange crackling in the undergrowth."
    #Out crept Ina who had gone back to the town for a brief moment, to get groceries."
    
    "Around noon, Ina got up to help me prepare lunch, while Mei remained fully engorged in her book."
    
    pause(1)
    show ina shirt interested day open at center with Dissolve(0.5)
    pause(1)
    
    a "So, how's she doing?"
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)    
    n "Hm—"
    n "Slow but steady—"
    n "Mei didn't even know all the letters of the alphabet, you know? Just her name, and the letter s—"
    n "The church has been actively keeping her away from books, convincing her she was incapable of reading."
    pause(1)
    a "That's terrible—"
    show ina shirt angry day open with Dissolve(0.5)
    n "And nonsense—"
    n "After just a few hours of practice, she's already reading words and short phrases."
    show ina shirt interested day open with Dissolve(0.5)        
    n "The human ability to read has evolved a relatively short time ago, and is not ingrained too deeply in the structure of our brains."
    n "An adult can overcome illiteracy quite rapidly with the right training."
    n "Other functions, such as speech, which need certain synaptic networks to develop — they cannot be learned at a later stage."
    
    # Ina warns that church is setting up a large-scale man hunt with their members."
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)  
    
    
    n "Also, you may be interested to know."
    n "Karin called this morning."
    #pause(1)
    a "That's great. Is she making a steady recovery?"
    show ina shirt mirth day closed with Dissolve(0.2)
    show ina shirt interested day open with Dissolve(0.2)  
    n "Gradually—"
    n "She suffered a cerebral contusion, which will take a while to fully heal."
    n "But she'll be able to leave the hospital soon."
    show ina shirt angry day closed with Dissolve(0.2)
    n "I took the liberty to tell her about Mei."
    "I jumped."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "Don't worry. I haven't told her your whereabouts."
    n "And besides, she seemed sympathetic to our cause."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "Karin told me, how the mental health service is organized in this town."
    n "It's the council's responsibility to allocate accurate care to their beneficiaries."
    
    n "In Abbotsford, however, we only have one mental health care institute."
    show ina shirt angry day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "It's called the {i}Lazarus Foundation{/i}, and is run by the church."
    n "Due to Kuyper's influence in the town council, all underage patients with psychiatric needs are automatically redirected to Lazarus."
    n "There's no viable alternative—"
    pause(1)
    a "That's bad—"

    show ina shirt smiling day open with Dissolve(0.5)
    n "Probably. But now that Mei is of age, we have the agency to change that."
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)
    n "If her legal custodian states a case against the council, she may be able to have her funds redirected to a proper mental health organization."
    n "One that actually works for her, instead of doing everything within its power to keep her in the system."
    
    n "Unfortunately her current custodianship lies with her parents, who are loyal to the church—"
    #"They aren't even her real—"
    
    n "Which means that, once they find her, the Lazarus foundation will ship Mei off to Germany, never to be heard from again—"
    
    "I sighed."
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)
    n "Also, there's one more interesting detail Karin let loose."
    a "Which is—?"
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)
    n "The Lazarus Foundation celebrates their fifteenth anniversary this year."
    pause(1)
    a "Well, that's good for them—"
    n "No. Think about it. Fifteen years."
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)
    n "It's fifteen years ago, that Mei was taken out of the regular school system, and placed under the auspices of the church."
    n "Before that, mental health cases were handled by a regional healthcare provider."
    n "Lazarus was founded to harbor Mei."
    n "{i}Specifically{/i} for that purpose—"
    stop music fadeout 5.0
    show ina shirt saddened day open with Dissolve(1.0)
    n "What kind of disturbance could that girl have caused — for an entire institute to be established solely for her cause?"
    
    #TODO: GOUDA scene? is it too much???
    
    pause(1)
    hide ina with Dissolve(0.5)

    stop sound fadeout 1.0
    pause(1)
    play sound "audio/summernight.ogg" loop fadein 3.0
    scene gravemound_twi with Dissolve(3.0)

    pause(1)
    
    "When evening fell, Ina returned home, and Mei and I returned to our sleeping bags inside the Mesolithic tomb."
    
    pause(1)
    scene dolmenint with Dissolve(1.5)
    pause(1)   
    show mei blue sad day open with Dissolve(0.5)
    pause(1)
    
    m "How long do you think we'll need to stay here?"
    a "Just a short while longer—"
    a "Ina says she has a plan—"
    show mei blue happy nig open with Dissolve(1.0)
    m "It's okay."
    m "I could stay here forever if we had to."
    m "I sleep much better here than at home."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2)
    m "And do you know—?"
    m "The nightmares have stopped."
    m "They've disappeared, ever since we ran away."
    show mei blue happy nig closed with Dissolve(0.2)    
    show mei blue happy nig open with Dissolve(0.2)    
    m "Almost as though they were {i}urging{/i} me to flee—"
    m "—to move out over the indomitable marshes—"

    pause(1)
    hide mei with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    pause(1)   


label p5M11:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    scene dolmenint with Dissolve(2.5)
    pause(1)
    window show
    pause(1)
    
    "Inch by inch, the sun painted the walls of our burrow with its morning rays."
    #"We stayed in bed for most of the morning, as it took the sun's rays a long time to make their way into the dark interior of our hiding place."
    
    pause(1)
    scene gravemound with Dissolve(0.5)
    pause(1)
    
    "And after breakfast Mei returned to her geology book, in which she progressed at an accelerating speed—"
    "—while I just basked in the midday sun, paging through the increasing list of missed calls on my phone — some which were from Rika, some from school, but none, unsurprisingly, from my father."
    
    pause(1)
    
    "Suddenly Mei called me over."
    
    pause(1)
    play music "audio/siegfried_opening.ogg" loop fadein 10.0
    show mei blue sincere day open at right with Dissolve(0.5)
    pause(1)    
    
    m "Come, look at these marks."
    "She was pointing at one of the stones, trailing her finger along a series of perpendicular grooves that ran along its side. "
    show mei blue sincere day closed with Dissolve(0.2)    
    show mei blue sincere day open with Dissolve(0.2)
    m "This is called {i}glacial str—striation{/i}."
    m "It's formed by the wear the stone suffered when it traveled inside the great glacier."
    m "It runs lengthwise along the face of the rock, as that's the direction that causes the least friction—"
    
    pause(1)
    show phyrrus_r at left with Dissolve(0.5)
    play audio "audio/bark2.ogg"
    pause(1)       
    
    "While she was speaking, Phyrrus suddenly came up to us — visibly alarmed."  
    show mei blue sad day open with Dissolve(0.5)
    "And when I listened, I detected the faint sound of footsteps and voices, coming from the forest trail."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "Do you hear that?! They're coming!"
    hide phyrrus_r with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    "She closed her book — and hurriedly we gathered our belongings, stashing our sleeping bags and food far inside the dolmen, hidden from outside view."
    #show mei blue sad day closed with Dissolve(0.2)    
    #show mei blue sad day open with Dissolve(0.2)
    m "Come, this way!"
    
    pause(1)
    #hide mei with Dissolve(0.5)
    scene woods4_eve with Dissolve(1.0)
    pause(1)    
    
    "Mei took me by the hand, leading me in the opposite direction as where the sounds came from, while Phyrrus stayed nearby."
    
    pause(1)
    stop sound fadeout 5.0
    scene castlehall with Dissolve(1.5)
    pause(1)
    
    #soliloquiy at the sanctuary
    
    "Soon the chirping of birds and rustling of leaves had all but disappeared."
    "Due to the lack of foliage the castle hall was engulfed in a deathlike silence that was only sporadically interrupted by the muted sound of a branch cracking underfoot."
    
    #"It was clear where she was taking me— "
    
    pause(1)
    stop music fadeout 10.0  
    #show mei blue happy day open with Dissolve(0.5)
    pause(1)    
    
    a "What could that have been—?"
    a "A search party maybe—?"
    a "Do you think they're looking for us—?"
    #show mei blue happy day closed with Dissolve(0.2)    
    #show mei blue happy day open with Dissolve(0.2)    
    
    pause(1)
    
    m "It's okay."
    #"It's our own fault, for staying in the same place for so long—"

    m "Just listen to the silence—"    
    pause(1)    
    m "We'll be able to hear them from miles away."

    
    pause(1)
    play sound "audio/1winter.ogg" loop fadein 8.0
    m "All is covered in snow—"

    #pause(0.5)
    #show mei blue happy day closed with Dissolve(0.2)    
    #show mei blue happy day open with Dissolve(0.2)      
    #m "I remember the silence—"
    #m "We must keep moving, our tracks will soon be erased—"
    #m "—by the white snow."
    

    play music "audio/siegfried_climax.ogg" loop fadein 10.0
    pause(1)    
    scene mei_cg_4 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    pause(1)
    


    m "I was heavy, almost too heavy to move, as I protected the tiny life inside of me."
    m "Which felt close to dying out—"
    pause(1)
    m "Sigurd would go out to hunt, bringing the catch to our hiding place."
    
    m "But winter was harsh — harsher than the winters before — and it spread its frosted fingers across the land so that we found no refuge."
    m "We had no choice other than to return to the village, the secluded hamlet from which we'd fled the previous summer—"
    m "There we would plead for shelter and heat, until our child was born."
    m "Even though there was little chance they'd welcome us."
    
    scene mei_cg_3 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    
    pause(1)
    m "And so — with the reluctance of captives — we embarked upon the journey home."
    pause(1)
    m "Many times I was so slow that we moved at a crawl—"
    m "Many times we had to interrupt our voyage, to hide from the perpetual winter storms. "
    pause(1)
    m "How often was I close to giving up? Fearing the little fire inside me would extinguish, if I even set one step further."
    m "But Sigurd comforted me, telling me to have courage—"
    m "For he believed a great fate rested on the birth of our child—"
    m "—a fate connected to the very survival of our kind."
    pause(1)
    m "And Beifre, the all-mother, watched over us throughout. "
    m "Chasing away foes, bringing us small prey."
    m "And in her trail I knew we followed an illuminated path—"
    pause(1)
    scene mei_cg_2 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
    
    pause(1)
    m "After thirteen days of travel, we reached our destination."
    #"The ."
    m "That secluded crest — setting of my tormented youth — under which our village lay."
    
    m "Covered in snow, wrapped in silence—"
    m "Such absolute, penetrating silence — as though all life had vanished for miles around."
    pause(1)
    m "And as we descended the ridge, we found the root of the silence—"
    pause(1)
    m "Under the snow lay buried an atrocity."
    m "Burnt down houses, blooded corpses of men, women, children—"
    pause(1)
    m "The war had raged throughout our homestead. "
    m "Leaving no soul alive, no hearthstone unshattered—"
    pause(1)
    m "Our entire clan, from which we had fled after our reunification, had been routed out from the hillside for good."
    
    stop music fadeout 5.0
    m "Of our village, only the great dolmen remained — as an unmovable testament to the perseverance of our ancestors. We took refuge between its solid walls."
    "Mei looked up at me with saddened eyes."    
    pause(1)
    m "Just like {i}we{/i} do now—"
    stop sound fadeout 3.0
    pause(1)
    play music "audio/walkure_wintersturme.ogg" loop fadein 10.0
    scene mei_cg_5 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 30.0 xalign 1.0 yalign 0.0 
        
    pause(1)
    play sound "audio/summermeadow.ogg" loop fadein 12.0
    m "And while we sheltered, paralyzed by listlessness — a spring broke through."
    m "A soothing, delightful, warming spring, that chased away the winter storms."
    pause(1)
    m "And amidst the glow of that beautiful, heartwarming spring, I finally found the strength to give birth."
    m "Under the comforting care of Sigurd, my own brother and husband. With Beifre protecting us from harm—"
    m "—I gave birth—"
    pause(1)
    m "—to twins. "
    pause(1)
    m "For two flames had burned in me all that time."
    #Sigfrid and Sigfreya."
    pause(1)
    m "Beautiful, strong infants."
    m "Boy and girl."
    pause(1)
    m "The presence of the all-mother ran strong in our bloodline."
    #"I could see the vibrant form of the all-mother reflecting out from their features."
    m "And for that blessed morning we were happy, as we bathed and fed our newborn children."
    pause(1)    
    stop music fadeout 8.0
    play effects "audio/haunting.ogg" loop fadein 30.0 

    m "But with great joy came inconsolable grief—"
    pause(1)
    m "I was weak, Sigurd—"
    m "The journey, the exposure to the cold, the grueling delivery — they left me wholly depleted."
    m "It was as though, in keeping these two tiny beings safe, my own fire had given its final flame."
    pause(1)
    stop sound fadeout 5.0  
    m "I was weak—"
    m "I could feel my fire dying out—"
    m "All I saw was Sigurd, holding our beautiful children—"
    pause(1)
    a "Mei—"
    a "Mei—"
    pause(1)
    m ". . ."
    pause(1)
    m "S—"
    m "S—"
    pause(1)
    m "Sigurd—"

    pause(2)
    window hide
    pause(2)
    stop music fadeout 1.0

    scene black with Dissolve(3.0)
    pause(1)   
    
    
label p5M12:

    scene black with fade
    pause(1)
    #play music "audio/schoolbell.ogg"
    #play sound "audio/officesound.ogg" loop fadein 1.0
    #scene castlehall
    #show mei blue sad day closed
    scene mei_cg_5 with Dissolve(2.0):
        xalign 1.0 yalign 0.0 
    pause(1)
    window show
    pause(1)
    stop effects fadeout 10.0
        
    "Mei had become a deathly pale, as though she were close to passing out." #meh
    
    "In silence we sat and waited, unsure of our next move."
    "And when two hours had passed without any suspicious sound, we reluctantly set off to pack our belongings."
    
    pause(1)
    play sound "audio/summermeadow.ogg" loop fadein 15.0
    scene gravemound with Dissolve(1.0)
    pause(1)    
    
    "At the dolmen it was so peaceful, that I began to wonder if the voices in the woods had been no more than figments of our imagination—"
    pause(1)
    play music "audio/1pianoboss.ogg" loop fadein 1.0
    "—until a dark haired figure emerged from the opening between the stones."

    show rika dress unhappy day open at left
    show bible at Position(xpos = 0.42, xanchor=0.75) #Position(xpos = 0.9, xanchor=0.75)
    with Dissolve(0.5)  
    
    "And before I even realized what was happening, she had struck me in the head—"
    play audio "audio/0attack.ogg"
    show rika dress unhappy day open at left with vpunch
    "—with the large, leatherclad tome that she held in her right hand, so that I was knocked backwards by the blow."
    
    pause(1)    
    show mei blue sad day open at right with Dissolve(0.5)
    #pause(1)
    
    m "Rika!"
    "Mei stood paralyzed."
    pause(1)
    r "There you are!"
    
    hide bible with Dissolve(0.5)
    
    r "Come now, Abraham. We knew you had your eyes set on miss Wahlsing all along. "

    r "But to imagine that you'd go as far as to kidnap her—"
    "Rika took out her phone."
    show rika dress happy day open with Dissolve(0.5)
    r "The fugitives have been located. At the same place where you found the sleeping bags."
    r "Come over right now!"
    
    "I wanted to grab Mei, to make a run for it, but I still found myself disoriented by Rika's blow. "
    "A thin trickle of blood was making its way down the side of my neck, steadily staining my shirt a deep burgundy."
    
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    
    r "Oh poor boy. Did I strike you too hard?"
    r "I keep forgetting how heavy these old Bibles are."
    r "They really don't make them like they used to—"
    "Her lips curled into a foreboding grin."
    show rika dress mischievous day open with Dissolve(0.5)    
    r "If you can stay conscious for a little while longer—"
    r "—they'll have excellent healthcare available for you at the municipal jail."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2) 
    m "R-Rika, that's so mean!"
    show rika dress sad day open with Dissolve(0.5)    
    r "Hold your tongue!"
    r "You're in some deep trouble too!" #young lady
    r "How {i}dare{/i} you run away from us!"
    
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)    
    "Mei whimpered, overwhelmed by the spontaneous outburst of rage her one-time friend had unleashed on her."
    #"Mei quivered under her friend's outburst."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)   
    r "Our church has always looked after you, Mei."
    r "We cared for you, when no one else would—"
    r "—not even your own parents."
    "Mei let out an agonizing wail."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)   
    r "We housed you, fed you, gave you an education."#provided you with education."
    
    a "Education? What {i}kind{/i} of education?"
    r "A special education, tailored exactly for—"
    a "You taught her nothing! Not even how to read and write!"
    
    "Rika grew quiet — her explosive fury making place for a severe, more articulate anger."
    show rika dress unhappy day open with Dissolve(1.0)   
    r "No, Abe."
    r "You don't understand."
    pause(1)
    r "It's what she {i}needed{/i}."
    
    "Rika shot a spiteful glance at Mei, who was sobbing silently."
    pause(1)
    r "She's an {i}abomination{/i}—"
    
    a "Rika—!"
    
    #
    #TODO, make prettier and more mysterious"
  
    show rika dress sad day open with Dissolve(0.5)  
    r "Ever since she was young, Mei has displayed a certain trait."
    r "That was always there, hiding in her eyes—"
    r "—like an unsettling presence."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)  
    r "We realized her early life had been eventful, and hoped it would pass with the years. "#hen she grew older."
    
    r "But it worsened the moment she entered elementary school, as she began learning how to read and write."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)      
    r "Mei's classmates would come home fatigued, whenever they spent too much time in her presence."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    r "And even worse — things would {i}break{/i} in her vicinity."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)  
    r "One day — when she'd been put in detention, for driving a classmate to tears — her teacher found her inside a storage room, surrounded by shattered school supplies."
    r "And Mei just sat there, staring at her, a blank look in her eyes." #TODO improve.
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)      
    r "I have vague recollections of these disturbing events."
    #"I was one year younger than Mei, you know?"

    r "For us it was heartbreaking. To see a young, innocent child, be consumed by these powerful demons."
    
    r "The things her biological parents must have {i}done{/i} to her — to create such a horror. Truly bloodcurdling."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    r "Gradually, older kids began to pick up on Mei's weird behavior." #TODO foreshadow during Rika's earlier conversations."
    r "She was bullied. Mercilessly. To the extent that they had to take her out of school."
    r "But the thing was, while the Lazarus Foundation worked on creating a private curriculum for her, we noticed that Mei began to fare much better—"
    r "—unchallenged by social and cognitive stimuli."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)     
    r "It was clearly the stress of mainstream education that brought out the worst in her. And without these outside influences, she returned to her good behavior."
    r "After we confined her to a sober regimen of solitary play and coloring books, the chilling glare slowly disappeared from her eyes."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2) 
    r "And the mysterious occurrences ceased happening."
    
    pause(1)
    "Just then, two figures appeared, taking position behind us. Rika gestured for them to stand by."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2) 
    
    r "While Mei was under auspices of the church, my parents instructed me to keep an eye on her."
    r "To be her friend, even though I didn't want to."
    r "To be honest, I was rather afraid of her—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    "Mei stirred."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2) 
    r "I hated it, being paired up with the retarded kid. "
    r "But it was my duty, as the pastor's daughter."
    r "To act as a caretaker—"
    a "Rika—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    "Mei had begun shaking."
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)     
    r "I hated it so much that I'd even play mean pranks on her."
    r "But Mei didn't mind, as I was her only friend."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue crying day open with Dissolve(0.2)
    m "Rika, you—"
    
    r "Mei was doing so well."
    r "Her behavior grew stable, under our unwavering care—"
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2)     
    r "But look what {i}you{/i}'ve done to her!"

    r "Camping trips?"
    r "Books?!"
       
    r "Mei can't have that kind of stimulation!"
    r "You're undoing all that we have worked so hard for!"
    r "I can see it in her eyes already, the growing madness—"
    show rika dress sad day closed with Dissolve(0.2)   
    show rika dress sad day open with Dissolve(0.2) 
    r "Go! Seize her! "
    stop music fadeout 10.0
    stop sound fadeout 10.0
    r "Take her to the car! The police will deal with the boy."

    play effects "<from 60.0>audio/1covid.ogg" loop fadein 15.0
    show white behind mei, rika with Dissolve(0.5):
        alpha 0.0
        easein 25.0 alpha 1.0
    
    "But as the men enclosed on the trembling, forlorn figure of Mei, a white light began to shine."
    show mei blue white day frown with Dissolve(1.0) 
    "It was a calming light, that enveloped the entire scene, drowning out all the noise and violence."
    "And it appeared to be emanating from Mei."    
    pause(1)
    "At that moment I began to wonder, if maybe Rika {i}was{/i} right, if maybe the overpowering mixture of excitement and emotion had awoken a certain attribute in the girl—"
    "—a unique trait, wholly inconceivable by human understanding."
    
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue white day frown with Dissolve(0.2)
    m "Rika—"
    show white2 with Dissolve(0.5):
        alpha 0.0
        easein 15.0 alpha 1.0
    m "Rika, what is happening to me—?"
    m "I feel heavy."
    pause(1)
    #"And at that instant a strange glow began to emanate from Mei, enveloping the scene in a growing white light."

    pause(1)
    "And as I strained my eyes, which had almost succumbed to the overpowering luminescence, I realized that the light didn't come directly from her—"
    "—but that it originated from the dolmen behind her, on which the S-glyph had begun glowing mysteriously."
    
    scene white with Dissolve(1.0)
    
    "And then I was blind."
    pause(2)
    #2# Metaphorical allusion to cyclical theory
    # recurrence, poetic, philosphical
    # apple grows into tree, bears fruit — mother childbirth
        
    show meibig_closed with Dissolve(0.5):
        alpha 0.0
        easein 15.0 alpha 1.0
    pause(2)
    "All breaks down into cycles."
    pause(1.0)
    "What exists is fated to return upon itself — again and again, until the end of times."
    pause(1.0)
    "The apple seed sprouts into a sapling, then grows into a tree, until one day it itself is ready to bear fruit."
    pause(1.0)
    "And thus it repeats."
    pause(1.0)
    "Does that sound like the greatest torture to you—?"
    pause(1.0)
    "Reliving your life, every second of it, over and over again—"
    "—into eternity?"
    pause(1.0)
    "We are condemned to recurrence."
    "Growing through infancy, childhood, parenthood — before in turn giving birth to new life."
    pause(1.0)
    scene meibig_open with Dissolve(0.5)
    pause(1.0)
    #, as certain as the succession of the seasons, like mother and child.
    
    
    #3# Hinting at mitochondrial eve, recurrence of progenital event, power that accumulates
    # allude mitochondrial eve — all mother
    # essence = all, bond that remains.
    # Glowing life born from anguish and despair.
    # Originating history, the escape recurs, again and again. Life imitates the progenital event. The fated unification from which all is born.
    # Stored potential only increases, each time the history is relived.
    
    "How far can we trace back the lineage?"
    pause(1)
    "Through history, the great civilizations, the vast seas of dark that lay in between—"
    pause(1)
    "It all returns to that progenital event. That initial completion of the cycle, that all of existence ripples out from."
    pause(1)
    "Each iteration of the cycle is bonded to that progenital event—"
    "—all of life is steeped in its uniting essence."
    pause(1)
    "The essence of {i}all{/i}—"
    pause(1)    
    "Beifre—"
    pause(1)    
    "Life today mirrors history, born from anguish and despair—"
    
    "—the reunification, the escape, the birth, the death—"
    
    "—it recurs again and again, like an originating myth to which all of existence must atone."
    pause(1)
    "Each cycle attempts to come to completion, in the same way it did on that spring day—"
    pause(1)    
    "Each of our actions are steeped into the essence of {i}all{/i}, carrying the limitless potential of the first iteration."
    pause(1)
    "And each time the cycle repeats, the potential accumulates, steadily growing."
    

    
    #4# Blast, Rika has religious crisis
    #warm cyclone shoots past, flash, blast
    #Rika falls to ground, clothes torn to shreds. Religious crisis, afraid of true revelation. She fights it.
    #Above the transient gods. 
    # The influence of the all-mother is distant now. Nobody knows her hidden rites.
    stop effects fadeout 2.0
    play audio "audio/explosion.ogg" fadein 0.1
    play music "audio/winds.ogg" loop
    scene white with vpunch
    "Suddenly, an enormous blast resonated through the forest, as a force like a tropical cyclone blew us to the ground."
    pause(1)
    "And beside me I saw Rika, who appeared to be in anguish, her clothes having been torn to shreds by the blast."
    pause(1)
    "Above the sound of the winds, I could hear her praying furiously, as though her faith was being tried to the fullest extent."
    pause(1)
    r "{i}She does great wonders, making fire come down from heaven upon the earth within the sight of men.{/i}"
    
    r "{i}And she deceives those that dwell on the earth by means of these miracles, which she performs on behalf of the beast.{/i}"
    stop music fadeout 4.0
    pause(1)
    "Gradually all returned to silence."
    

    play effects "<from 280.0>audio/walkure_climax.ogg" loop fadein 20.0
    scene meibig_open with Dissolve(2.0)    
    pause(1)
    "The presence of the all-mother is distant now."
    
    "No longer do we perform the forgotten rites."
    pause(1)      
    "Many transient gods have since been bestowed the allegiance of men."
    
    "For short periods only, for these younger Gods are constructed in a fashion that is bound by linear time. "
    pause(2)      
    
    #5# Basks in Mei's glow
    #Feels that white light is familiar, as though it has always been inside of him. As though he knows Mei from before birth."
    
    "And as the white light continued outward, I noticed that its beams did not hurt me at all."
    "They simply went through me, filling me with a comforting sensation of immaculate bliss."
    pause(1)      
    "For it felt as though I recognized the light, its powerful, warming touch."
    "As though it had been with me, even from before the time I was born."
    pause(1)      
    "And as the beam grew stronger, I further surrendered to its glow, until I could no longer determine where the boundary between it and myself lay."
    pause(1)    
    "That is when I saw how the tale ended—"
    
    pause(1.0)
    show gravemound with Dissolve(0.5):
        alpha 0.0
        easein 35.0 alpha 1.0
    pause(1.0)
    
    "Inconsolable grief gave birth to the greatest happiness."
    
    #"And inconsolable grief gave birth to the greatest hope. "
    
    pause(1)   
    "Our new family, already without a mother, looked out over a ravaged world."
    "Death echoed at us from all sides, as though taunting the last of the living to join its ranks. "#A small flame of life within a wasteland of death.
    pause(1)    
    "While Beifre nursed the twins, I laid my sister to rest inside the gravemound."
    "Her, their mother."
    "The last of our tribe to be entombed therein."
    pause(1)    
    "And while we remained there, mourning for seven moons—"
    "—I etched the sigil of our clan into the dolmen's exterior wall."
    pause(1)
    "S."
    "Sign of the river—"
    "—flowing eternally, fruitfully, into the estuaries of time."
    pause(2)    
    "{i}So flourish then, blood of Wahlsing.{/i}"
    stop effects fadeout 10.0

    pause(2)
    window hide
    pause(2)
    stop music fadeout 1.0
    stop sound fadeout 1.0
    
    scene white with Dissolve(3.0)
    pause(2)       
    
    
label p5M13:

    #scene black with fade
    #pause(1)
    ##play music "audio/schoolbell.ogg"
    #play sound "audio/officesound.ogg" loop fadein 1.0
    #scene school_front with Dissolve(0.5)
    #pause(1)
    #window show
    #pause(1)
    #
    #
    #
    #pause(1)
    #window hide
    #pause(1)
    #stop music fadeout 1.0
    #stop sound fadeout 1.0
    #scene black with fade
    #pause(1)       
    
label p5M14:

    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)
    pause(1)
    play music "audio/1pianoending.ogg" loop fadein 20.0
    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    scene school_front with Dissolve(2.0)
    pause(1)
    window show
    pause(1)

    "It was about a week later that I received a message from Ina, summoning me to her office."
    
    pause(1)
    stop sound fadeout 1.0
    scene office with Dissolve(1.0)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    show ina shirt smiling day open at Position(xpos = 0.2, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.5)
    pause(1)
    
    n "So, are you ready to get back to work this coming Saturday?"

    a "Work? I thought we'd been shut down."
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)    
    n "I thought so too—"
    n "Until I received a highly apologetic letter from the school board, notifying me of the immediate reinstatement of our monthly funding."
    
    a "And their reason—?"
    show ina shirt smiling day closed with Dissolve(0.2)
    show ina shirt smiling day open with Dissolve(0.2)
    n "No reason stated."
    n "I think we may have a hidden benefactor, pulling strings somewhere."
    
    play audio "audio/window.ogg"
    
    "The door opened and two visitors entered the room."
    
    pause(1)
    show mei dress interested day open at Position(xpos = 0.8, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(0.5)
    show karin happy at center behind ina with Dissolve(0.5)
    pause(1)    
    
    n "Mei, Karin — thank you for joining us. You're just in time."
    
    n "From now on, Mei will be writing our weekly {i}Rock Solid Advice{/i} section, in which she answers geology related questions."
    
    n "As a managing editor, Mei will be positioned above you, Abe. So please make sure her every need is met."
    
    a "Sounds great. Does that mean she was able to enroll in high school?"
    
    
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress interested day open with Dissolve(0.2)
    m "I have! I need to take remedial classes until the end of the year, but after that I can enter tenth grade." #I want to be a geologist when I grow up!"
    
    show karin laughing with Dissolve(0.5)
    "Karin laughed."
    
    k "Mei has been settling in just fine. She's a great help around the garden. We're almost done decorating her room."
    
    
    show ina shirt angry day open with Dissolve(0.5)
    n "Didn't the church give you any trouble?"
    show karin serious with Dissolve(0.5)    
    k "Well, they were apprehensive at first, but I noticed your little um— {i}confrontation{/i} has definitely struck some fear into them. "
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress interested day open with Dissolve(0.2)    
    k "And also, I've been doing some digging—"
    
    k "I looked into the financial administration of the Lazarus Foundation, and found out they've been misappropriating community funds ever since their inception."
    
    k "It was one big mess of shady bookkeeping, missing receipts, unjustified payments to offshore accounts."
    
    k "Once I hinted at these matters, Kuyper became docile as a lamb."
    k "Suddenly, the transfer of legal custodianship was completed in a day. They even helped me move Mei's belongings."
    
    k "And all operations of the Lazarus Foundation have been suspended indefinitely."
    k "If they ever start up again, it will take only one call to the inspection board to have them shut down."
    show ina shirt smiling day open with Dissolve(0.5)
    n "Come on Karin, let's head down to the cafeteria. I want to interview you before next year's electoral campaign kicks off."
    
    #pause(1)
    hide ina with Dissolve(0.5)
    hide karin with Dissolve(0.5)    
    "The two women exited the room."
    
    show mei dress happy day open at center with easeinright
    
    "Mei turned towards me, smiling self-consciously."
    show mei dress happy day closed with Dissolve(0.2)
    show mei dress happy day open with Dissolve(0.2)
    m "I really like staying with Karin."
    m "This is the first time I've lived in a town, you know that?"
    m "But she's helping me fit in. I'm even allowed to set up a chicken coop in the garden."
    a "Those poor neighbors—"
    show mei dress estatic day closed with Dissolve(0.5)
    "She giggled."

    "And in her sweet, unencumbered smile I saw the will to life of a hundred-thousand generations reflecting back at me."
    stop music fadeout 9.0
    show mei dress estatic day closed with Dissolve(0.2)
    show mei dress earnest day open with Dissolve(0.2)    
    m "Hey, please come to the stones with me."
    m "I want to show you something—"
    
    
    #TODO ending scentence
    
    pause(1)
    hide mei with Dissolve(1.0)
    pause(1)
    window hide
    pause(1)

    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)           
    
    jump end
    
    ############################################################
    ########## BAD ENDING - INA ################################  
    ############################################################

label iBad:

    scene black with Dissolve(1.0)
    pause(1)
    pause(2)
    play sound "audio/summernight.ogg" loop fadein 1.0
    scene villageroad_nig with Dissolve(0.5)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    play music "audio/1pianoending2.ogg" loop fadein 30.0
    pause(1)
    window show
    pause(1) 
       
    "Three more months and then I'm done with it all."
    
    #"I have my eyes set on a university, far away from here. "
    
    "I've never been much of an honors student. But recently I've changed my ways—"
    
    "—each day, after school, I study for two hours. And then more after dinner, into the early hours of the night."
    
    "I only have three more months to increase my grade-point average — but if I succeed, all of Europe will open up to me."
    
    "London, Berlin, even the US—"
    
    "For each man, a moment comes, where he has to lay out his own destiny."
    
    "I can remain here in smalltown Abbotsford, on the outskirts of the modern world."
    
    "Or grasp this moment to spread my wings and head for greater skies."
    
    pause(2)

    "I don't really mind the studying, as it helps divert my thoughts—"
    
    "—away from the unrest and the violence. The local nonsense surrounding this town, that has left such a strange taste in my mouth."
    #starts focusing on graduation, wants to go to university
    pause(1)
    "Three more months and then I'm done—"
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)
    
    pause(1)
    #play sound "audio/summermeadow.ogg" loop fadein 2.0
    scene school_side with Dissolve(0.5)
    pause(1)
    window show
    pause(1)
    
    "Ever since our falling out, Ina had been ignoring me in class."
    
    "And not just me, but the other students as well."
    
    "At times it was as though she had become invisible."
    
    pause(1)
    
    "After graduation, I figured I'd never see her again."
    
    pause(1)
    scene schoolroad with Dissolve(0.5)
    pause(1)
    
    "However, there was one last occasion, where we both found ourselves waiting on the same bus."
    
    "Though I had resigned myself to standing with her in awkward silence — she suddenly turned to me."
    
    pause(1)
    show ina pink sincere day open with Dissolve(0.5)
    pause(1)
    
    n "Have you noticed?"
    
    #show ina shirt saddened day closed with Dissolve(0.2)
    #show ina shirt saddened day open with Dissolve(0.2)    
    pause(1)
    
    a "What—"
    
    pause(1)
    
    n "It's silent, isn't it?"
    pause(0.5)
    "I listened, and could confirm the town was entirely devoid of sound." #meh
    
    show ina pink neutral day open with Dissolve(0.5) 
    
    n "There's not even a hint of chirping in the air."
    
    n "Do you know why that is?"
    show ina pink dissapointed day open with Dissolve(0.5)
    n "They're all dead—"
        
    n "I found them, in a pond in the woods."
    
    n "Thousands of corpses, all floating belly upwards."
    
    n "Fully exhausted, deceived by the false advent of spring."
    
    n "It'll take nature years to recover, if it ever will—"
    
    show ina pink sincere day open with Dissolve(0.5)  
    
    n "Thus is our fate in the age of decline."
    
    n "Nothing is born — all crumbles."

    play audio "audio/busarriving.ogg" fadein 4.0    
    pause(1)

    hide ina with Dissolve(0.5)
    pause(1)
    
    "The bus arrived. She chose the seat farthest away from mine."
        
    
    pause(1)
    window hide
    pause(2)
    stop music fadeout 5.0
    scene black with Dissolve(5.0)
    pause(2)
    
    jump end  
    
    ############################################################
    ########## BAD ENDING - RIKA ###############################
    ############################################################
    
label rBad:
    
    pause(3)
    play sound "audio/officesound.ogg" loop fadein 2.0
    scene blueroom_twi with Dissolve(3.0)
    pause(1)
    #play music "audio/churchbells.ogg" loop fadein 2.0
    window show
    pause(1) 

    "I spent days in bed, drifting in and out of existence."
    
    "Lost, both mentally and physically — as though I wouldn't even be able to point out my current location on a map."

    "And I feared it would come to the point that even I myself would begin to disappear."
    
    "Simply forgotten — skimmed over, like a footnote without reference."

    pause(1)

    "{i}Guard your heart—{/i}"
    
    "{i}Guard your heart above all else—{/i}"
    
    pause(1)
    scene nightsky with Dissolve(0.5)
    pause(1)
    
    "It was during winter break, that I invited myself to stay with my aunt Maren for two weeks."
    "And after that I simply refused to return to Abbotsford."
    "Especially now that finals were near, it wasn't hard to get transferred back to my old school."
    "I was still in all their systems."
        
    pause(1)
    
    "I've already started hunting for a place of my own."
    
    "Preferably close to the beach—"
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)
    pause(1)
    scene sittingroom_eve with Dissolve(0.5)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    window show
    pause(1)
    
    "It wasn't until April that I set foot in Abbotsford again."
    
    "I needed my father's signature, in order to apply for my High School degree."
    
    "My father acted distant, signing the papers wordlessly."
    
    "And after he was done, my presence felt like a burden."
    
    "During the preceding months, my ties to this place had slowly faded away. I saw no other option than to leave."
    
    pause(1)
    stop sound fadeout 1.0
    scene ichthys_nig with Dissolve(0.5)
    play sound "audio/summernight.ogg" loop fadein 1.0
    pause(1)
    
    "But it was on my way to the station, that I detected a vaguely familiar figure trawling along the pavement."
    
    "Although a lot more trepid than I recalled her — it was unmistakably Rika, the girl that I used to know."
    
    "She flinched when I approached her."
        
    pause(1)
    play music "audio/0goldberg22s.ogg" fadein 5.0 loop
    show rika uni sad day open with Dissolve(0.5)
    pause(1)
    
    r "I thought you had left."
    
    a "Rika—"
    
    "I paused, not really knowing what to say." 
    
    "Rika was staring at me with a detached look in her eyes, indicating that I was the last person she had hoped to meet that day."
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    a "I {i}have{/i} left—"
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "Then please be on your way."
    
    r "You should know we don't take kindly to strangers down here."
    
    "For a second, her demeanor softened."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "I gave you a chance — you know?"
    
    r "I let you into my heart, and for a brief time you truly appeared intent to make it your home."
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "But as an insolent wedding guest, you have taken advantage of my hospitality."
    
    "She stared at me like an angered swan."
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "Please be gone, into the outer darkness—"
    
    r "—where there is weeping and gnashing of teeth."
    pause(2)
    r "For many are called, but few are chosen—"
        
    #r "I'm sorry Abe, I need to go now. And not because I have anything worth doing."
    
    #r "It's just that I need to {i}go{/i}."
    
    #"And with these words she left, in the opposite direction as from which she had come."
    
    pause(1)
    stop music fadeout 5.0
    hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(3.0)
    pause(1)
    
    jump end
    
    ############################################################
    ########## BAD ENDING - MEI ################################
    ############################################################   
    
label mBad:

    scene white with Dissolve(1.0)
    pause(1)
    scene part6_epilogue with Dissolve(1.0)
    pause(3)
    scene white with Dissolve(1.0)
    pause(2)
    play sound "audio/officesound.ogg" loop fadein 1.0
    scene blueroom_twi with Dissolve(0.5)
    pause(1)
    play music "audio/1pianoending.ogg" loop fadein 2.0
    window show
    pause(1) 

    "After Mei's departure, I returned home quietly."
    
    
    "Three days later, Rika came by to thank me."
    "She reassured me that Mei was fitting in brilliantly with her new surroundings, and that my presence that night had made the transition all the more manageable for Mei."
    
    pause(1)
    
    "But even though I tried to find comfort — assuring myself that I'd made the right decision — a lingering doubt gnawed at my conscience. "
    "I questioned my decision to confide in Rika, to deliver Mei into the clutches of the church."
    
    "And no matter what I told myself, that doubt remained, growing into a large, dark hole, into which I gladly stepped. "
    
    # which devoured me with unabating greed. Chastise myself."
    pause(1)
    
    "With Mei gone, I lost interest in everything."
    
    "My grades suffered, and it wasn't long before I sank to the bottom of the class. "
    
    "And when spring came, the inevitable happened — I flunked my finals, condemning me to another year of school in this dead-end town."
    
    pause(1)
    
    "By that time, Ina had already stopped talking to me. And my friendship with Rika was reduced to an incidental formality. "
    "At times I felt that — with the Sunday Abbot gone and Mei conveniently locked away abroad — my utility to both girls had evaporated."
    
    "I had been no more than a useful idiot to them."
    
    "What a cruel fate, to be cast aside this way. "
    
    pause(1)
    
    "It wasn't until autumn next year that Rika contacted me, suggesting I come with her to see Mei."
    
    "It would be my first time since her departure."
    
    "Though I'd initially planned to visit Mei regularly. Her caretakers had explained that my presence would jeopardize her successful integration into the new environment."
    
    "And I hadn't contested their decision, as I admit I was reluctant to face her after my betrayal."
    
    "But now that Mei had settled in, there was no reason to further postpone the visit."
    "With a heavy feeling in my stomach, I boarded the Kuyper family car."
    
    pause(1)
    scene wardroad with Dissolve(1.0) #outside
    pause(1)
    
    "It was a one hour drive."
    "As we approached the German border, the perpetual stretches of endless lowlands made way for an undulating landscape of wooded vales."
    
    pause(1)
    scene ward with Dissolve(1.0) #exterior
    pause(1)    
    
    "Heilanstalt Uelsenkirchen was beautifully situated on one of the northern flood plains of the Rhine."
    
    "Clearly familiar with her surroundings, Rika led the way up to the ward where Mei's room was located."
    
    "She punched in the security code that opened the door."
    
    pause(1)
    scene wardroom with Dissolve(1.0) #room
    pause(1)    
    show rika uni mischievous day open at left with Dissolve(0.5)
    pause(1)
    r "Mei! We're here!"
    "Carefully, a pale figure scuttled towards us."
    pause(1)
    show mei blue sad day open at right with Dissolve(0.5)
    pause(1)
    m "Rika. I'm glad you came—"
    r "And look, I've brought a visitor."
    "Mei stared at me for what felt like a full minute before Rika broke the silence."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)    
    r "You haven't seen Abe for almost a year now."
    show mei blue happy day open with Dissolve(0.5)
    "Mei's lips curled into a watery smile."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)
    m "Rika. Rika."
    m "I am starting on linen duty next week."
    m "I am really looking forward to it."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)    
    r "Linen duty—?"
    r "Oh Mei, that's such a responsible task."
    r "You're settling in so well—"
    show mei blue sad day open with Dissolve(0.5)
    "But Mei appeared distracted."
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)
    m "It's one o clock already. How long are you staying?"
    m "I have a session at a quarter past two."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)    
    r "Don't worry Mei, we can entertain ourselves for a while."
    
    "Rika cast me a sideways glance."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    r "Say Mei, I need to speak with the staff for a moment."
    
    r "How about you talk to Abe."
    r "The two of you used to get on so well—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)    
    m "Okay, Rika."
    m "But don't stay away for long. "
    m "I have a session at a quarter past two."
    hide rika with Dissolve(1.0)
    a "I'm sure she'll be back by then."
       
    "A tense silence filled the room."
    "Mei sat eyeing me suspiciously."
    
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)      
    m "A—Abe?"
    
    a "How have you been getting on—?"
    show mei blue happy day open with Dissolve(0.5)
    "She smiled."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)      
    m "Very good. I will start on linen duty next week."
    m "I really like it here. Everyone's so kind to me."
    
    "I looked into her eyes."
    pause(1)
    a "Are you sure? Are you really happy you came here?"
    show mei blue sad day open with Dissolve(0.5)      
    "From the way she drew backwards, I could tell I had unintentionally raised my voice."
    pause(1)
    a "I'm sorry. I mean, that night, when they first took you here."
    a "Don't you think we should have escaped?"
    a "If you remember that night—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2)  
    m "I—"
    m "I— don't remember everything."
    m "But I know I was unhappy back in Abbotsford."
    m "They say I saw things, that weren't there."
    m "That I was a danger, to myself and others around me."
    show mei blue happy day open with Dissolve(0.5)
    m "But now that I live here — I haven't seen anything strange in a long time."
    m "The bad thoughts are slowly disappearing from my mind."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "So please don't be sad. "
    m "I am very happy here. "
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "People like me shouldn't live alone. You know?"
    m "But here I can do so many things."
    m "In a few years, I may even be able to move—"
    m "—into an assisted living home."
    m "Where I can have my own things. Even a cute pet."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "It's already a quarter past one. "
    m "I have a session in an hour—"
    m "I will start on linen duty next week."
    
    "And as Mei sat there, droning up her day to day activities—"
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)    
    m "I wouldn't want to flee from here. Fleeing is dangerous."
    
    "—it dawned on me that there is never truly such a thing as a wrong decision."
    
    m "We had a girl here, called Gerlinde, and she ran away a week ago. Or maybe it was a month—"
    
    "No matter what choices we make, in the end life always finds a way."
    show mei blue happy day closed with Dissolve(0.2)    
    show mei blue happy day open with Dissolve(0.2)  
    m "And do you know what had happened when they found her?"
    show mei blue sad day open with Dissolve(0.5)    
    m "She had been ran over by a train."
    
    m "A train. Do you see how dangerous that is? One moment you're not looking and you get run over by a train."
    
    m "I would never—"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2) 
    m "What's the matter—?"
    m "Are you okay—?"
    show mei blue sad day closed with Dissolve(0.2)    
    show mei blue sad day open with Dissolve(0.2) 
    m "Why are you crying—?"

    stop music fadeout 5.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)
    
    jump end

###################################################################################################################

label end:

    scene black with fade
    pause(1)

    scene logo with Dissolve(2.0)
    #pause(1)
    play music "audio/1pianotitles.ogg" fadein 8.0
    pause(2)
    show logo_tbc with Dissolve(2.0)
    pause(2)

    pause(2)
    hide logo_tbc with Dissolve(2.0)
    #pause(2)
    #scene black with Dissolve(2.0)
    #pause(1)
       
    pause(3)
    
    show endingcredits1:
        subpixel True
        yalign 0.0
        linear 70.0 yalign 1.0 #linear, easin, easeout
    
    pause(70)
    
    show endingcredits2:
        subpixel True
        yalign 0.0
        linear 80.0 yalign 1.0 #linear, easin, easeout
    
    pause(80)
    
    show endingcredits3:
        subpixel True
        yalign 0.0
        linear 60.0 yalign 1.0 #linear, easin, easeout
    
    pause(70)
    
    "{i}press any key to continue{/i}"
    
    stop sound fadeout 4.0
    stop music fadeout 1.0
    scene black
    pause(2)        
    
    #####################
    if rika_score > 3 and ina_score > 3 and mei_score > 3:
        "You have currently unlocked the ending routes for RIKA, MEI and INA."
    elif rika_score > 3 and ina_score > 3:
        "You have currently unlocked the ending routes for RIKA and INA."
    elif mei_score > 3 and ina_score > 3:
        "You have currently unlocked the ending routes for MEI and INA."
    elif mei_score > 3 and rika_score > 3:
        "You have currently unlocked the ending routes for RIKA and MEI."
    elif rika_score > 3:
        "You have currently unlocked the ending route for RIKA."
    elif ina_score > 3:
        "You have currently unlocked the ending route for INA."
    elif mei_score > 3:
        "You have currently unlocked the ending route for MEI."
    else:
        "You have currently not unlocked any ending routes."
    
    menu:
        with Dissolve(1.0)
        "You can play remaining ending routes by loading a save file, or by returning to PART 4."
    
        "Return to PART 4.":
            stop music fadeout 5.0
            window hide
            jump p4c1
        "Exit game.":
            return
    ######################


#################################################################################################################################
    ########################################### DEBUG ###############################################################################
    #################################################################################################################################
    
label debugmenu:
    
    menu:
        "{i}enter debug menu?{/i}"
       
        "{i}no (start game){/i}":            
            jump prologue
            
        "{i}yes{/i}":            
            ". . ."     
    
    menu:
        "{i}where to?{/i}"
        ####################
        "Part 1_1":            
            jump p1c1            
        "1_2":            
            jump p1c2
        "1_3":            
            jump p1c3
        "1_4":            
            jump p1c4
        ####################    
        "1_5":            
            jump p1c5
        "1_6":            
            jump p1c6
        #"1_7":            
        #    jump p1c7
        #"1_8":            
        #    jump p1c8
        "more":
            ". . ."
            
    menu:
        "{i}where to?{/i}"
        ####################
        "Part 2_1":            
            jump p2c1
        "2_2":            
            jump p2c2
        "2_3":            
            jump p2c3
        "2_4":            
            jump p2c4
        "2_5":            
            jump p2c5
        "2_6":            
            jump p2c6
        "2_7":            
            jump p2c7
        "2_8":            
            jump p2c8
        "more":
            ". . ."  

    menu:
        "{i}where to?{/i}"
        ####################
        "Part 3_1":            
            jump p3c1
        "Part 3_3":            
            jump p3c3
        "Part 3_5":            
            jump p3c5
        "Part 3_7":            
            jump p3c7
        "Part 3_9":            
            jump p3c9            
        "Part 4_1":            
            jump p4c1
        "part 4_1 perfect scores":
            $ ina_score = ina_score + 6
            $ rika_score = rika_score + 6
            $ mei_score = mei_score + 6            
            jump p4c1
        "more":
            ". . ."   
            
    menu:
        "Part 5_Ina 1":            
            jump p5Ic1
        "5_Ina 3":            
            jump p5Ic3
        "5_Ina 5":            
            jump p5Ic5
        "5_Ina 7":            
            jump p5Ic7
        "5_Ina 10":
            jump p5Ic10
        "Part 5_Rika 1":            
            jump p5Rc1
        "5_Rika 3":            
            jump p5Rc3
        "5_Rika 5":            
            jump p5Rc5
        "5_Rika 7":            
            jump p5Rc7
        "5_Rika 10":            
            jump p5Rc10
        "more":
            ". . ."
    
    menu:
        "Part 4_4":            
            jump p4c4
        "part 4_4 perfect scores":
            $ ina_score = ina_score + 6
            $ rika_score = rika_score + 6
            $ mei_score = mei_score + 6            
            jump p4c4
        "Part 5_Mei 1":            
            jump p5M1
        "5_Mei 3":            
            jump p5M3
        "5_Mei 5":            
            jump p5M5
        "5_Mei 7":            
            jump p5M7
        "5_Mei 9":
            jump p5M9   
        "5_Mei 11":
            jump p5M11 
        "5_Mei 14":
            jump p5M14             
        
        #"2_6":            
        #    jump p2c6
        #"2_7":            
        #    jump p2c7
        #"2_8":            
        #    jump p2c8
   
               
