# right_or_wrong_game.rpy
# Ren'Py single-file "Right or Wrong" demo
# Place your video files in the game/ directory (or game/videos/) and adjust paths below.
# Supported video formats depend on platform. mp4 (h.264) usually works on most platforms.

# Initialize persistent variables
default score = 0

define e = Character("Eileen")

label start:
    # Reset score at the start of run
    $ score = 0

    scene bg washington
    show eileen vhappy

   
    with dissolve

    e "You are a time-travelling history professor from the future and have been sent back in time to witness a series of events in 2020s America. Your mission is to monitor the start of AI deepfakes and go back to your class and teach them the real history of the period that led to their dystopian AI-dominated present.  "
    e "Once your mission is complete, you must go back to the future and teach your students how to differentiate between fake videos and facts."
    e "On your time-travels, you navigated a series of events in 2020s American culture:"

    call Smith_SAG
    call Tom_Cruise
    call Taylor_Swift
    call Beyonce
    call Elon
    call Zuckerburg
    call Kamala_Harris
    call Biden
    call Trump
    call Trump_Crypto
    call result_scene

    return

image movie = Movie(play="videos/real/Beyonce_Commencement.mp4")

label Beyonce:
    # Scene 1: a RIGHT video
    with fade

    e"Time travel to June 7, 2020. Connect to the Internet and watch live as Beyonce delivers the commencement speech at YouTube's Global Virtual Graduation Ceremony."

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Beyonce_Commencement.webm")

    menu:
        "What's your answer for scene 1?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Trump:
    # Scene 2: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to Sep 28, 2024. Attend Donald Trump’s Campaign Rally in Prairie du Chien, Wisconsin. Watch Donald Trump deliver his speech."

    $ renpy.movie_cutscene("videos/fake/Trump_Wall.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Elon:
    # Scene 3: a RIGHT video
    with fade

    "Time travel to June 12, 2024. Connect to the Internet and watch Elon Musk’s interview on Farzad’s YouTube channel."

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Elon_Musk_Meaning_of_Life.webm")

    menu:
        "What's your answer?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Trump_Crypto:
    # Scene 4: a RIGHT video
    with fade

    e"Time travel to Sep 22, 2024. Connect to the internet and check Donald Trump’s Truth Social post from 9:13 a.m. the previous day. "

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Trump_Crypto.webm")

    menu:
        "What's your answer?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Smith_SAG:
    # Scene 5: a RIGHT video
    with fade

    "Time travel to Feb 27, 2022. Attend the SAG AFTRA awards. Watch Will Smith speak to the media after receiving the award for best male actor."

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Will Smith_SAG Awards.webm")

    menu:
        "What's your answer?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Kamala_Harris:
    # Scene 6: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to Oct 1, 2024. Find a TV and turn the channel to CBS News. Watch Kamala Harris’ “60 Minutes” interview."

    $ renpy.movie_cutscene("videos/fake/Kamala_Harris_Homebuyers.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Zuckerburg:
    # Scene 7: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to May 25, 2017. Attend Harvard University’s Commencement Ceremony. Watch Mark Zuckerberg deliver the commencement speech."

    $ renpy.movie_cutscene("videos/fake/Mark_Zuckerburg_Mandarin.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Taylor_Swift:
    # Scene 8: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to May 18, 2022. Attend the NYU All-University Commencement Ceremony. Watch Taylor Swift deliver the commencement speech."

    $ renpy.movie_cutscene("videos/fake/Taylor_Swift_Commencement.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Tom_Cruise:
    # Scene 9: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to Feb 25. 2023. Attend the Producer’s Guild Awards. Watch Tom Cruise deliver his Achievement Award acceptance speech."

    $ renpy.movie_cutscene("videos/fake/Tom_Cruise_Shoutout.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Biden:
    # Scene 10: a WRONG video
    scene bg whitehouse
    show eileen vhappy
    with fade

    e"Time travel to July 25, 2024. Find a TV and turn the channel to ABC News. Watch Joe Biden’s Oval Office address."

    $ renpy.movie_cutscene("videos/fake/Joe_Biden_MLK.webm")

    menu:
        "What's your answer?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label result_scene:
    with dissolve

    scene bg washington
    show eileen vhappy

    "Results"

    if score > 0:
        "Perfect! You got many correct ([score]/10)."
    else:
        "Oops — you got 0 out of 10 correct."

    "Final score: [score] / 10"

    menu:
        "Play again?"
        "Yes":
            jump start
        "No":
            "Thanks for playing!"
            return

