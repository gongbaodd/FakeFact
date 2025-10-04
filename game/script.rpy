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

    e "Welcome to Right or Wrong! You'll watch 2 short videos and decide whether each is Right or Wrong."

    call scene_one
    call scene_two
    call scene_three
    call scene_four
    call scene_five
    call scene_six
    call scene_seven
    call scene_eight
    call scene_nine
    call scene_ten
    call result_scene

    return

image movie = Movie(play="videos/real/Beyonce_Commencement.mp4")

label scene_one:
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

label scene_two:
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
label scene_three:
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
label scene_four:
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
label scene_five:
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

label scene_six:
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


label scene_seven:
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

label scene_eight:
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

label scene_nine:
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

label scene_ten:
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

