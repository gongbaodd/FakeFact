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

label result_scene:
    with dissolve

    scene bg washington
    show eileen vhappy

    "Results"

    if score == 2:
        "Perfect! You got both correct (2/2)."
    elif score == 1:
        "Not bad — you got 1 out of 2 correct."
    else:
        "Oops — you got 0 out of 2 correct."

    "Final score: [score] / 2"

    menu:
        "Play again?"
        "Yes":
            jump start
        "No":
            "Thanks for playing!"
            return

