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

    "Scene 1: Watch the video. (Correct answer: Right)"

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

    e"Scene 2: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Trump_Wall.webm")

    menu:
        "What's your answer for scene 2?"
        "Right":
            "You chose: Right."
        "Wrong":
            $ score += 1
            "You chose: Wrong."

    return

label Elon:
    # Scene 3: a RIGHT video
    with fade

    "Scene 3: Watch the video. (Correct answer: Right)"

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Elon_Musk_Meaning_of_Life.webm")

    menu:
        "What's your answer for scene 3?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Trump_Crypto:
    # Scene 4: a RIGHT video
    with fade

    "Scene 4: Watch the video. (Correct answer: Right)"

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Trump_Crypto.webm")

    menu:
        "What's your answer for scene 4?"
        "Right":
            $ score += 1
            "You chose: Right."
        "Wrong":
            "You chose: Wrong."

    return

label Smith_SAG:
    # Scene 5: a RIGHT video
    with fade

    "Scene 5: Watch the video. (Correct answer: Right)"

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Will Smith_SAG Awards.webm")

    menu:
        "What's your answer for scene 5?"
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

    e"Scene 6: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Kamala_Harris_Homebuyers.webm")

    menu:
        "What's your answer for scene 6?"
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

    e"Scene 7: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Mark_Zuckerburg_Mandarin.webm")

    menu:
        "What's your answer for scene 7?"
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

    e"Scene 8: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Taylor_Swift_Commencement.webm")

    menu:
        "What's your answer for scene 8?"
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

    e"Scene 9: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Tom_Cruise_Shoutout.webm")

    menu:
        "What's your answer for scene 9?"
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

    e"Scene 10: Watch the video. (Correct answer: Wrong)"

    $ renpy.movie_cutscene("videos/fake/Joe_Biden_MLK.webm")

    menu:
        "What's your answer for scene 10?"
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

