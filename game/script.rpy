define fr = Character("{b}Liam{/b}", color="#90ee90")
define mc = Character("{b}[you]{/b}", color="#87ceeb")
define a = Character("{b}Amy{/b}", color="#f08080")
define i = Character("{b}Ivan{/b}", color="#6495ed")
define m = Character("{b}Mother{/b}", color="#536878")
define f = Character("{b}Father{/b}", color="#4682b4")
define am = Character("{b}Amy{/b}", image = "cryamy", color="#f08080")
define an = Character("{b}Amy{/b}", image = "angryamy", color="#f08080")


image cryamy :
    "side cryamy"

image angryamy :
    "side angryamy"

label splashscreen :
    scene welcome with dissolve
    with Pause(3)
    scene blackvscode with fade
    return
label start:
    scene warning with dissolve
    with Pause(3)
    scene headphones with dissolve
    with Pause(2)
    play music "audio/cozy.mp3" loop
    scene blackvscode with dissolve
    $ you = renpy.input("{color=#ffffff}Enter your name{/color}", length = 32)
    scene back1 at Transform(xzoom=-0.78, yzoom=0.8) with dissolve
    show friendvscode with moveinleft:
        xalign 0.5
        zoom 0.5
    fr "{color=#ffffff}{size=45}See ya tomorrow! Bye!{/size}{/color}"
    mc "{color=#ffffff}{size=45}Bye! See ya!{/color}{/size}"
    hide friendvscode 
    show brothervscode with moveinleft:
        xalign 0.5
        zoom 0.5
    i "{color=#ffffff}{size=45}Sorry for keeping you waiting, let's go home!{/color}{/size}"
    mc "{color=#ffffff}{size=45}Let's go!{/color}{/size}"
    scene blackvscode with fade
    scene kitchenvscode at Transform(xzoom=-1.5, yzoom=1.5) with dissolve
    show im3vscode:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    mc "{color=#ffffff}{size=45}Hi sis! How are you?{/color}{/size}"
    a "{color=#ffffff}{size=45}Hi! How was school?{/color}{/size}"
    mc "{color=#ffffff}{size=45}It was AMAZING! We played basketball and I won!{/color}{/size}"
    hide im3vscode
    show im4vscode:
        xalign 0.5
        zoom 0.5
    a "{color=#ffffff}{size=45}Good to hear that.{/size}{/color}" 
    a "{color=#ffffff}{size=45}Now go upstairs and change your clothes, dinner is waiting{/color}{/size}"
    mc "{color=#ffffff}{size=45}Okay sis!{/size}{/color}"
    scene blackvscode with fade
    scene dinner at Transform(xzoom=1.3, yzoom=1.3) with dissolve :
        ypos -90
    show im4vscode1 :
        ypos -232
        xpos 1200
        zoom 0.7
    show brother2:
        ypos -300
        xpos -250
        zoom 0.7
    i "{color=#ffffff}{size=45}I was barely able to finish the exam this time{/color}{/size}"
    hide im4vscode1
    show im42 :
        ypos -230
        xpos 1200
        zoom 0.7
    a "{color=#ffffff}{size=45}It's okay, you will do better next time{/color}{/size}"
    hide im42
    show im4vscode1 :
        ypos -232
        xpos 1200
        zoom 0.7
    a "{color=#ffffff}{size=45}Do you have another upcoming exam?{/color}{/size}"
    i "{color=#ffffff}{size=45}Yes, I've got Math next week{/color}{/size}"
    hide im4vscode1
    hide brother2
    show im4vscode44 :
        ypos -232
        xpos 900
        zoom 0.7
    show brother3 :
        ypos -300
        xpos -250
        zoom 0.7
    mc "{color=#ffffff}{size=45}Can we eat rice tomorrow, Amy?{/color}{/size}"
    hide im4vscode44
    show im42 :
        ypos -230
        xpos 1200
        zoom 0.7
    a "{color=#ffffff}{size=45}Of course, anything for you sweetie~{/color}{/size}"
    stop music
    play sound "audio/knock.mp3"
    hide brother3
    hide im42
    show im43:
        ypos -230
        xpos 1200
        zoom 0.7
    show brother2:
        ypos -300
        xpos -250
        zoom 0.7
    pause
    i "{color=#ffffff}{size=45}Are we expecting anyone today?{/color}{/size}"
    a "{color=#ffffff}{size=45}No I don't think so{/color}{/size}"
    stop sound
    scene door at Transform(xzoom=1.2, yzoom=1.2) with dissolve
    show ima9vscode :
        xalign 0.5
        yalign 0.5
        zoom 0.5
        linear 2.0
    an "{color=#ffffff}{size=45}Why are you here?{/color}{/size}"
    play music "audio/scary.mp3" loop
    m "{color=#ffffff}{size=45}And what other reason could there be besides the fact that i wanted to see you?{/color}{/size}"
    an "{color=#ffffff}{size=45}you never cared enough to do it!!!{/color}{/size}"
    mc "{color=#ffffff}{size=45}Who is it?{/color}{/size}"
    m "{color=#ffffff}{size=45}Hi [you], Look how much you have grown!{/color}{/size}"
    menu :
        m "{color=#ffffff}{size=45}It's been so long since the last time I've seen you! Did you miss your mother?{/color}{/size}"
        "{color=#000000}{size=45}Yes{/color}{/size}" :
            jump mt
        "{color=#000000}{size=45}No{/color}{/size}" :
            jump is
        "{color=#000000}{size=45}Who are you?{/color}{/size}" :
            jump df
    label mt :
        hide imavscode
        show ima9vscode1 :
            xalign 0.5
            yalign 0.5
            zoom 0.5
            linear 2.0
        m "{color=#ffffff}{size=45}I missed you a lot too. Let us have some family time together!{/color}{/size}"
        jump proceed
    label is :
        hide imavscode
        show ima9vscode1 :
            xalign 0.5
            yalign 0.5
            zoom 0.5
            linear 2.0
        m "{color=#ffffff}{size=45}oh, it is sad to hear that from you.{/color}{/size}"
        m "{color=#ffffff}{size=45}Actually i missed you a lot. Let’s have some time together{/color}{/size}"
        jump proceed
    label df :
        hide imavscode
        show ima9vscode1 :
            xalign 0.5
            yalign 0.5
            zoom 0.5
            linear 2.0
        m "{color=#ffffff}{size=45}Did you forget me already? I am your mother!{/color}{/size}"
        m "{color=#ffffff}{size=45}The woman who raised you when you were a baby. Let us have some time together i missed you a lot{/color}{/size}"
        jump proceed
    label proceed :
        scene blackvscode with dissolve
        show 1
        pause
        hide 1
        show ima92 :
            xalign 0.5
            yalign 0.5
            ypos 1200
            zoom 1.5
        show see
        m "{color=#ffffff}{size=45}Good night my baby...{/color}{/size}"
        scene blackvscode with dissolve
        show 2
        pause
        scene back4 :
            zoom 0.8
            ypos -72
        pause
        menu :
            "{color=#000000}{size=45}Call for your sister and brother{/color}{/size}" :
                jump shutit
            "{color=#000000}{size=45}Remain silent{/color}{/size}" :
                jump fll
    label shutit :
        mc "{color=#ffffff}{size=45}Amy! Ivan!{/color}{/size}"
        scene 3 with dissolve
        pause
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        show father :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}There's no one here t help you, so shut it and follow me{/color}{/size}"
        jump continue
    label fll :
        scene 3 with dissolve
        pause
        scene back4 with dissolve:
            zoom 0.8
            ypos -72
        show father :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}Follow me{/color}{/size}"
        mc "{color=#ffffff}{size=45}Who are you and what am I doing here? Where's sis Amy?{/color}{/size}"
        f "{color=#ffffff}{size=45}Stop asking questions{/color}{/size}"
        jump continue
    label continue :
        scene 4 with dissolve
        pause
        scene lab with dissolve
        show fatherlab with moveinleft:
            zoom 0.5
        show motherlab with moveinright:
            zoom 0.5
            xpos 930
        mc "{color=#ffffff}{size=45}Mother? What's happening? Who is this man?!{/color}{/size}"
        m "{color=#ffffff}{size=45}That's your father and you must obey him{/color}{/size}"
        mc "{color=#ffffff}{size=45}I don't understand! What am I doing here?!{/color}{/size}"
        hide motherlab
        show mother1 :
            zoom 0.5
            xpos 930
        m "{color=#ffffff}{size=45}Hear me out, arent we the ones who provided you with everything you need?{/color}{/size}"
        m "{color=#ffffff}{size=45}Think about it as the time to finally pay us for our efforts{/color}{/size}"
        mc "{color=#ffffff}{size=45}But sis Amy is the one who did all of that!{/color}{/size}"
        m "{color=#ffffff}{size=45}She helped, we did the big part. So now stay silent and be OBIDIENT!{/color}{/size}"
        scene blurry with dissolve:
            zoom 1.1
        "{color=#ffffff}{size=45}Before i even realized, my mother injected me with some weird liquid that caused pain throught my whole body{/color}{/size}"
        "{color=#ffffff}{size=45}I screamed, cried and begged for mercy, but she didnt feel any sympathy towards me.{/color}{/size}"
        scene 5 with dissolve
        pause
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        "{color=#ffffff}{size=45}i was back in this tiny scary room. I couldn’t do anything .i just looked at the ceiling with tired eyes then fell asleep{/color}{/size}"
        show see2
        pause 1.0
        show see1
        pause 1.0
        scene blackvscode
        scene 6 with dissolve
        pause
        scene 7 with dissolve
        scene blackvscode with dissolve
        "{color=#ffffff}{size=45}The door opened , i woke up but it wasnt my father this time..{/color}{/size}"
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        show sit12 :
            zoom 0.4
            xalign 0.5
            yalign 0.5
            ypos 700
        "{color=#ffffff}{size=45}It was my sister, crying while hugging me{/color}{/size}"
        "{color=#ffffff}{size=45}she seemed so tired, so angry, so sad but relieved to see me alive.{/color}{/size}"
        a "{color=#ffffff}{size=45} I am sorry for not coming sooner, i am sorry for letting you alone{/color}{/size}"
        mc "{color=#ffffff}{size=45}I missed you!{/color}{/size}"
        a "{color=#ffffff}{size=45}I promise i wont leave you alone anymore... I promise...{/color}{/size}"
        show blackvscode with dissolve
        hide blackvscode
        hide sit12
        show sit1 :
            xalign 0.5
            yalign 0.5
            zoom 0.4
            ypos 700
        mc "{color=#ffffff}{size=45}What did they do to you?{/color}{/size}"
        a "{color=#ffffff}{size=45}Nothing important, I'm fine.{/color}{/size}"
        a "{color=#ffffff}{size=45}What about you? Are you okay?{/color}{/size}"
        mc "{color=#ffffff}{size=45}Sister, it was so painful. i want to leave this place .can’t we go back home?{/color}{/size}"
        a "{color=#ffffff}{size=45}I don't know but I will try my best{/color}{/size}"
        show blackvscode with fade
        hide blackvscode
        hide sit1
        show father with moveinleft :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}Follow me{/color}{/size}"
        am "{color=#ffffff}{size=45}Leave him alone! How can you do that to a child!{/color}{/size}"
        f "{color=#ffffff}{size=45}We accepted to let you stay with him but that doesn’t mean we will give up our work.{/color}{/size}"
        am "{color=#ffffff}{size=45}Just use me instead of him!{/color}{/size}"
        hide father
        show father1 :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}Unfortuantly, he is a better test subject then you are. In fact he is very promising{/color}{/size}"
        am "{color=#ffffff}{size=45}You devils! How can you sleep peacefully after destroying the lives of YOUR kids!!{/color}{/size}"
        f "{color=#ffffff}{size=45}Destroying? I don't actually understand...Why would you describe our actions as something evil?{/color}{/size}"
        f "{color=#ffffff}{size=45}As a matter of fact, I am just doing the right thing here and i believe there is nothing wrong with it.{/color}{/size}"
        f "{color=#ffffff}{size=45}You can tell me i am a devil or whatever, I am not stopping this.{/color}{/size}"
        hide father1
        show crazyfather :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}My path to creating my biggest PRIDE in this world! All scientists would respect me!{/color}{/size}"
        f "{color=#ffffff}{size=45}The world would be at my hands and I would dominate it as I please!{/color}{/size}"
        f "{color=#ffffff}{size=45}Unlike how they looked down at me during my childhood...My mom seemed scared at some point when she found dead animals in my room{/color}{/size}"
        hide crazyfather
        show father1 :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}I mean, I just used them for simple expirements! And they accused me of being a pshycopath!{/color}{/size}"
        hide father1
        show crazyfather :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}LOOK AT ME I'M THE GREATEST SCIENTIST IN THE WORLD!{/color}{/size}"
        hide crazyfather
        show father :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}If you want something, earn it by yourself, I do not care enough about other people'sproblems, that's too much of a hassle{/color}{/size}"
        f "{color=#ffffff}{size=45}Now [you], let’s go already...{/color}{/size}"
        hide father
        show sit12 :
            zoom 0.4
            xalign 0.5
            yalign 0.5
            ypos 700
        mc "{color=#ffffff}{size=45}It's okay sis, I will be okay, I'm used to it{/color}{/size}"
        scene 8 with dissolve
        pause
        scene 9 with dissolve
        pause
        scene 10 with dissolve
        pause
        scene 11 with dissolve
        pause
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        show sit2 :
            zoom 0.45
            xpos 1000
            ypos 160
        show sit3 :
            zoom 0.6
            ypos 150
        a "{color=#ffffff}{size=45}Okay [you], you try to look for the spare key of the room when they are not around{/color}{/size}"
        a "{color=#ffffff}{size=45}then you give it to us and we will look for the exit while they are busy with you.{/color}{/size}"
        mc "{color=#ffffff}{size=45}Okay, I will try{/color}{/size}"
        i "{color=#ffffff}{size=45}But what if they catch us? What are we gonna do?{/color}{/size}"
        a "{color=#ffffff}{size=45}We will do everything to escape. You know we can also fight{/color}{/size}"
        mc "{color=#ffffff}{size=45}Do you think you can win against father? He looks strong...{/color}{/size}"
        i "{color=#ffffff}{size=45} actually i am scared. I feel like they are going to catch us...What do you think [you]?{/color}{/size}"
        mc "{color=#ffffff}{size=45}I actually wanna do this. I don’t care how much it takes to escape this hell!{/color}{/size}"
        i "{color=#ffffff}{size=45}Are you sure? I think we should really wait for everything to be over. It’s not like we are going to die, right?{/color}{/size}"
        a "{color=#ffffff}{size=45}I know you are really scared but we can’t let [you] suffer any longer. Who said these experiments won’t actually kill him?{/color}{/size}"
        i "{color=#ffffff}{size=45}They are our parents i don’t think they will do something this dangerous.{/color}{/size}"
        a "{color=#ffffff}{size=45}You really still trust them much after this shit they’ve done to us{/color}{/size}"
        mc "{color=#ffffff}{size=45}It’s okay brother we will be just fine!{/color}{/size}"
        scene blackvscode with dissolve
        stop music fadeout 1.0
        play music "audio/dramatic.mp3"
        scene room :
            zoom 1.3
        "{color=#ffffff}{size=45}There's only me in this room, and a camera...{/color}{/size}"
        scene camera
        pause 0.5
        scene camera1
        pause 0.5
        scene camera
        pause 0.5
        scene camera1
        pause 0.5
        scene camera
        pause 0.5
        scene camera1
        pause 0.5
        scene blackvscode with dissolve
        scene room :
            zoom 1.3
        menu :
            mc "{color=#ffffff}{size=45}Will you look for the key?{/color}{/size}"
            "{color=#000000}{size=45}YES{/color}{/size}" :
                jump search
            "{color=#000000}{size=45}NO{/color}{/size}" :
                jump Bye
    label Bye :
        stop music
        scene 20 with dissolve
        pause
        scene blurr with dissolve 
        play sound "audio/beat.ogg"
        a "{color=#ffffff}{size=45}Hey [you]? Can you hear me? [you]! Please! Wake up!{/color}{/size}"
        stop sound
        scene 21 with dissolve
        pause
        scene 22 with dissolve
        pause
    return    
    label search :
        menu :
            mc "{color=#ffffff}{size=45}Where to look?{/color}{/size}"
            "{color=#000000}{size=45}In the closet...{/color}{/size}" :
                jump machines
            "{color=#000000}{size=45}Under the bed...{/color}{/size}" :
                jump nothing
            "{color=#000000}{size=45}Under the books...{/color}{/size}" :
                jump Yes
    label machines :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 1.0 yalign 0.0
        mc "{color=#ffffff}{size=45}There's nothing except some strange machines...{/color}{/size}"
        show room :
            linear 1.0 zoom 1.3
        menu :
            "{color=#000000}{size=45}Under the bed...{/color}{/size}" :
                jump nothing2
            "{color=#000000}{size=45}Under the books...{/color}{/size}" :
                jump Yes2
    label nothing2 :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 0.5 yalign 1.0
        mc "{color=#ffffff}{size=45}Nope, it's empty...{/color}{/size}"
        show room :
            linear 1.0 zoom 1.3
        menu :
            "{color=#000000}{size=45}Under the books...{/color}{/size}" :
                jump Yes2
    label Yes2 :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 0.0 yalign 0.0
        mc "{color=#ffffff}{size=45}I found it!!!{/color}{/size}" 
        menu :
            "{color=#000000}{size=45}Keep going...{/color}{/size}" :
                jump keepgoing

    label nothing :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 0.5 yalign 1.0
        mc "{color=#ffffff}{size=45}Nope, it's empty...{/color}{/size}"
        show room :
            linear 1.0 zoom 1.3
        menu :
            "{color=#000000}{size=45}In the closet...{/color}{/size}" :
                jump machines2
            "{color=#000000}{size=45}Under the books...{/color}{/size}" :
                jump Yes2
    label machines2 :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 1.0 yalign 0.0
        mc "{color=#ffffff}{size=45}There's nothing except some strange machines...{/color}{/size}"
        show room :
            linear 1.0 zoom 1.3
        menu :
            "{color=#000000}{size=45}Under the books...{/color}{/size}" :
                jump Yes2
    label Yes :
        show room :
            zoom 1.3
            linear 1.0 zoom 2.0 xalign 0.0 yalign 0.5
        mc "{color=#ffffff}{size=45}I found it!!!{/color}{/size}" 
        menu :
            "{color=#000000}{size=45}Keep going...{/color}{/size}" :
                jump keepgoing
    label keepgoing :
        play sound "audio/walk.ogg"
        show room :
            linear 1.0 zoom 1.3
            pause 2.0
        mc "{color=#ffffff}{size=45}Crap! Somebody's coming{/color}{/size}"
        menu :
            "{color=#000000}{size=45}Hide the key in your mouth{/color}{/size}" :
                jump more
    label more :
        scene blackvscode with dissolve
        stop sound
        scene room with dissolve :
            zoom 1.3
        show father :
            zoom 0.5
            xalign 0.5
            yalign 0.5
        f "{color=#ffffff}{size=45}Let's g back to your room{/color}{/size}"
        scene blackvscode with dissolve
        stop music
        play music "audio/scary.mp3"
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        show sit2 :
            zoom 0.45
            xpos 1000
            ypos 160
        show sit3 :
            zoom 0.6
            ypos 150
        mc "{color=#ffffff}{size=45}I found it sis!{/color}{/size}"
        a "{color=#ffffff}{size=45}Good job sweetie! Now leave the rest to us.{/color}{/size}"
        scene blackvscode with dissolve
        scene 12 with dissolve
        pause
        scene blackvscode with dissolve
        scene back4 with dissolve :
            zoom 0.8
            ypos -72
        show sit2 :
            zoom 0.45
            xpos 1000
            ypos 160
        show sit3 :
            zoom 0.6
            ypos 150
        a "{color=#ffffff}{size=45}We will escape tonigh, go it??{/color}{/size}"
        i "{color=#ffffff}{size=45}Are we sure now of this plan? I suggest we just ask them{/color}{/size}"
        a "{color=#ffffff}{size=45}Yes, we will do it without their mercy.{/color}{/size}"
        scene blackvscode with dissolve
        scene 13 with dissolve
        pause
        scene blurr with dissolve 
        play sound "audio/beat.ogg"
        a "{color=#ffffff}{size=45}[you]? Are you okay?{/color}{/size}"
        "{color=#ffffff}{size=45}I couldn't see her nor answer her...{/color}{/size}"
        scene blackvscode with dissolve
        play sound "audio/run.ogg"
        scene 14 with dissolve
        pause
        scene blackvscode with dissolve
        a "{color=#ffffff}{size=45}H-How did you know?{/color}{/size}"
        scene exit with dissolve
        stop sound
        show father with moveinleft:
            zoom 0.45
        show ima92 with moveinright:
            zoom 0.45
            xpos 930
        m "{color=#ffffff}{size=45}How wouldn't WE know?{/color}{/size}"
        m "{color=#ffffff}{size=45}I can’t believe he looked for the key knowing we were looking at him through the camera!{/color}{/size}"
        am "{color=#ffffff}{size=45}I should have knew since the door was unlocked! You really do enjoy humiliating us. I just want to know...{/color}{/size}"
        am "{color=#ffffff}{size=45}How did you know the exact time of our escape? Did youplant something in the room and was listening to us all the time?{/color}{/size}"
        show blackvscode with dissolve
        pause 1.0
        hide blackvscode
        show brothercry :
            xalign 0.5
            yalign 0.5
            zoom 0.5
            ypos 600
            xpos 900
        i "{color=#ffffff}{size=45}I'm...I'm sorry Amy, I'm really sorry, I didn't mean to...{/color}{/size}"
        "{color=#ffffff}{size=45}{b}...{/b}{/color}{/size}"
        am "{color=#ffffff}{size=45}YOU DEVILS!{/color}{/size}"
        m "{color=#ffffff}{size=45}All it took was a simple phrase. Do you want to live? Tell us everything{/color}{/size}"
        am "{color=#ffffff}{size=45}Damn it Ivan! You should've told me!{/color}{/size}"
        hide father
        show father1 :
            zoom 0.45
        f "{color=#ffffff}{size=45}Your are like everyone, dear Amy. Slaves under the perfectly coded system, while you could've been part of the innovation of humanity, part of the biggest pride...{/color}{/size}"
        am "{color=#ffffff}{size=45}I hate you both! You do not have a drop of humanity in your rotted hearts!{/color}{/size}"
        scene blurr2 with dissolve
        play sound "audio/beat.ogg"
        "{color=#ffffff}{size=45}I was barely able to hear the conversation{/color}{/size}"
        "{color=#ffffff}{size=45}but i was clearly able to hear the way my brother cryied, the way my sister sounded hopeless, and the way my mother laughed.{/color}{/size}"
        "{color=#ffffff}{size=45}I couldn’t hold myself. Suddenly I lost control over my body, and i was able to seeeverything clearly now...{/color}{/size}"
        scene back8 with dissolve
        play sound "audio/kill.ogg" 
        show byebyefather :
            zoom 0.5
            rotate 140
            ypos -700
            xpos -650
        show byebyemother :
            zoom 0.5
            rotate 300
            xpos 1000
        "{color=#ffffff}{size=45}the way my parents were on the floor, looking at the ceiling, full of blood, unable to breath...{/color}{/size}"
        stop sound
        stop music
        play sound "audio/bg.ogg"
        mc "{color=#ffffff}{size=45}You made me experience the ghastliness of your selfishness and sense of superiority.{/color}{/size}"
        mc "{color=#ffffff}{size=45}you made me feel like nothing, like a tool. Now please just leave...forever{/color}{/size}"
        scene blackvscode with dissolve
        scene 15 with dissolve
        pause

    return