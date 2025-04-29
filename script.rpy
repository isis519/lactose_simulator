
define m = Character('Me', color="#ffffff")
define k = Character('Kaiden', color="#fabf51")
define a = Character('Alice', color="#df4c64")
define o = Character('Oliver', color="#4cde2f")
define p = Character('Professor Rosen', color="#3e54f5")
define r = Character('Robinson', color="#c58cf5")

default summary_points = []

label start:

    scene bg SERC

    #put in scene of SERC building
    "Wow, that lunch was so good! My friends were right, the pizza at the dining hall is fire."
    "*stomach rumbles*"

    "Oh my god, I FORGOT I'M LACTOSE INTOLERANT! I need to make it back to my dorm before I have an accident NOW."
   
    #puts choice of which dorm for difficulty

    #starts moving fast with pov moving side to side
    
    "I end up running into my good friend Kaiden, who is someone I'm pretty close to."
    #faze kaiden in 
    show kaiden happy 
    
    "I need to find a way to end the conversation with him without negatively affecting our friend meter. Whatever I say has consequences."
    
    k "Hey bro, I just got out of my calc class, do you wanna grab some halal food?"

menu close_friend:

    "Politely say no and tell him why.":
        $ nice_k = True
        if nice_k:
            $ summary_points.append("Kaiden continues to be friends with you, and brings up this horrible event to laugh about for a long time.")
        m "I'm sorry I can't, I have to run to my dorm or else I'm going to shit myself right now."
        k "Damn that's so real, get going then, I hope you make it! I'll text you later."


    "Tell him to fuck off.":
        $ rude_k = True
        if rude_k:
            $ summary_points.append("Kaiden stopped being your friend, so you lost your only true friend at college.")
        k "Damn, fuck you too! You are such an asshole."
        "Kaiden walks away pissed off, and he immediately blocks you on instagram."


label friend_continued:

    "I run off, making it to in front of the Temple Tech Center when I see Alice."
    #alice fazes in
    a "Hey! I like your outfit, where did you get it from?"
    "Alice is the girl I've been wanting to be closer friends with from my programming class."
    "She's smart, stylish, and she can actually have a conversation, unlike other computer science kids."

menu cool_girl: 
    
    "Give her my contact information to send it later.":
        $ nice_a = True 
        if nice_a:
            $ summary_points.append("You and Alice met up that weekend and hit it off as friends."
        "You tell her what realy happened after a year of the friendship.")
        m "I have to run to my next class, but let me give you my instagram, I'll definitely send it to you later!"
        a "That's so nice, thank you! Here's my phone."
        "I type it in and wave away smiling, while also speed-walking away."
        jump alice_continue

    "Shrug and be vague.":
        $ rude_a = True
        if rude_a:
            $ summary_points.append("Since that day, Alice has never spoken to you again, and you can only see her briefly hanging out with other cool people.")
        m "I don't know, probably a store, anyway I have to go."
        #faze in her annoyed look
        a "Oh, ok. Bye then..."
        jump alice_continue 
   
    "Try to tell her the truth to be closer.":
        $ truth_a = True 
        if truth_a:
            $ summary_points.append("You and Alice talked about what happened at the next class and laughed so hard about it. She became a new close friend of yours.")
       
        m "I actually can't tell you right now because I'm about to shit myself."
        a "Dude what? Then you better run and make it, tell me if you make it when I see you in class tomorrow!"
        jump alice_continue
    
    "Punch her.":
        #faze in her angry look
        $ violent_a = True
        if violent_a:
            $ summary_points.append("Alice filed a restraining order against you, and since everybody likes her, you made no friends at all in that class.")
        a "What the fuck is wrong with you?!"
        jump crime_ending

label crime_ending:
    "The police witnessed your crime and she presses charges against you, so now you ahve a criminal record."

label alice_continue:
    "As I speed walk away, I make it to the end of a street where I have to try to make it across the street in time."
    #put a winding meter where we have to click correctly to move forward 
    "Thank god I made it! Okay, now I just need to-"
    "Is that Professor Rosen?"
    #faze in professor rosen
    p "Good afternoon! I haven't see you in class recently and we just went over Regex, is everything okay?"
    "Professor Rosen teaches my computer science class, and he was the class I just skipped for that stupid pizza slice."
    "I really don't want him to think I hate the class, I just wanted to treat myself because I'm stressed out, I need to find the right way out of this."
menu teacher:

    "Make up an excuse.":
        $ lie_p = True 
        if lie_p:
            $ summary_points.append("Professor Rosen never called on you, or gave you an extension on an assignment, ever again in that class. It remained extremely tense between the both of you.")
        m "I'm sorry, I just haven't been feeling well, I need to rush back."
        p "That's bullshit, you are literally out right now, you know I hate lying."
        "He angrily walks off."
        #have that make the meter go down
    "Give him the truth.":
        $ truth_p = True
        if truth_p:
            $ summary_points.append("You and Professor Rosen mainatined a good friendship, and he later recommended you for a research lab position.")
        m "I honestly just really needed a break for a second, I've been really stressed out, I swear I will watch the recording to stay caught up."
        p "That's completely fair, and yes please do. It's a really important thing to learn, I'll see you on Thursday!"
   
    "Be rude.":
        $ mean_p = True
        if mean_p:
            $ summary_points.append("You failed that class, he reported you to the dean and you had to retake it in the summer.")
        m "Honestly that's not your business, just leave me the fuck alone."
        p "Woah there, chill out dude."
        "He walks away, in shock and horror."

label p_continue:
    "I return to speedwalking, upping up my speed as I face the hill up."
    "This is when I see the worst person I could run into."
    #faze in Oliver
    o "Hey! Were you in calculus yesterday? I didn't see you. It was packed, but I was looking. Wow it was a lot to learn. If you didn't it was about-"
    "Oliver is this annoying classmate I have in my calculus class, who talks SO MUCH."
    "But he sends me the answers to the homework, so I can't be as rude as I would like to."

menu annoying: 

    "Tell him off.":
        $ angry_o = True
        if angry_o:
            $ summary_points.append("Oliver went home and cried himself to sleep, and then he killed himself, and wrote your name in the suicide note. His parents are currently pressing charges.")
        m "Oh my god just shut the fuck up, I have an emergency dickhead."
        #faze in sad oliver
        #make meter go down
        o "Wow, okay, I'll just see you in class then."

    "Be polite.":
        $ nice_o = True
        if nice_o:
            $ summary_points.append("Oliver continued to give you the answers, and you guys ended up becoming closer over a video game.")
        m "I can't really talk right now but let me call you later!"
        o "Okay! It was nice seeing you!"

    "Just run past him.":
        $ run_o = True 
        if run_o:
            $ summary_points.append("Oliver stopped giving you the answers, and he got super hot to spite you.")
        "I shove past him and keep running."
        #faze in confused oliver
        o "Uh-okay, bye?"
        #make meter go down


label crush:
    "I make it up to the light, I'm so close! I'm holding in every fart because I do not trust them to not just release everything."
    "Wait is this-what the actual fuck."
    #faze robby in 
    r "Hi, you're in my Gen-Ed arts class, right?"
    "This is Robinson, my class crush I've been wanting to talk to all semester."
    "He's finally talking to me, and it's when I'm two minutes away from shitting myself. I can't mess this up."

menu crush_encounter:

    "Try to flirt.":
        $ flirt_r = True
        if flirt_r:
            $ summary_points.append("Robinson avoided you heavily after that, and what happened spread and you were seen as creepy by many.")
        m "I am! But I'm pretty sure the class just got a lot more interesting now that you're talking to me."
        "I smirk flirtatiously."
        "Robinson's face morphs into being completely uncomfortable."
        r "Ohhh, okay, thanks. I'm going to leave now, I REALLY need to get to my next class."
        "He speedwalks away."

    "Play it off.":
        $ calm_r = True
        if calm_r:
            $ summary_points.append("You did meet up with Robinson that night, and since then you guys have been dating for 3 years.")
        m "Yeah, what's your name again?"
        r "I'm Robinson, I just saw you and I've been wanting to get to know you since you have fire outfits everytime."
        m "Thank you, you don't dress so bad yourself. I really need to go to my dorm because my roommate needs me to let her in, she lost her keycard."
        m "Can I get your instagram?"
        r "Yeah sure, here let me type it in."
        "My stomach is fluttering and I can tell it's not from the dairy."
        m "Thanks, I'll text you later, we can talk more about fashion at the skatepark tonight."
        r "I am so down for that, see you later!"

    "Panic.":
        $ loser_r = True
        if loser_r:
            $ summary_points.append("Robinson never spoke to you again, and ended up dating someone new and hot.")
        m "Uhhh...no."
        "I run away from him and look behind me to see him look so bewildered, scratching his head in confusion."

label game_continue:

    "We made it! Here is the summary of what our actions led to."

    python:
        summary_text = ""
        for point in summary_points:
            summary_text += "• " + point + "\n"
    
    "[summary_text]"
    #fix the summary to be displayed on the middle of the screen instead of in the text-box