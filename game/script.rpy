# right_or_wrong_game.rpy
# Ren'Py single-file "Right or Wrong" demo
# Place your video files in the game/ directory (or game/videos/) and adjust paths below.
# Supported video formats depend on platform. mp4 (h.264) usually works on most platforms.

# Initialize persistent variables
default score = 0

define e = Character("Professor Billie ")

label start:
    # Reset score at the start of run
    $ score = 0

    scene bg washington
    show billie vhappy

   
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
        e"Is this fake or is it a fact?"
        "Fact":
            $ score += 1
            e"Correct. This recording comes directly from Beyoncé’s global virtual graduation speech on June 7th 2020 at around the 46-second mark."
            e"You verified a legitimate message of hope broadcast during the pandemic years, a rare intact primary source."

        "Fake":
            e"Actually, that was authentic footage from June 7 2020, the YouTube Global Graduation ceremony."
            e"Your skepticism is good; just remember, sincerity and compositional consistency often reveal truth more clearly than pixel analysis alone."


    return

label Trump:
    # Scene 2: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to Sep 28, 2024. Attend Donald Trump’s Campaign Rally in Prairie du Chien, Wisconsin. Watch Donald Trump deliver his speech."

    $ renpy.movie_cutscene("videos/fake/Trump_Wall.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Incorrect. That was synthetic. The visuals were from a 2024 rally, but the speech came from impersonator John Di Domenico, digitally reshaped to sound authentic."
            e"Note how crowd reaction timing lags behind phrasing which is another telltale sign of dubbed content."

        "Fake":
            $ score += 1
            e"You spotted it. This rally footage from Wisconsin 2024 used genuine visuals but an impersonator’s audio from comedian John Di Domenico’s line about the 'really tall ladder.'"
            e"AI tuning then morphed the voice to fit the former president’s tone. A textbook case of comedic material repurposed for disinformation."


    return

label Elon:
    # Scene 3: a RIGHT video
    with fade

    e"Time travel to June 12, 2024. Connect to the Internet and watch Elon Musk’s interview on Farzad’s YouTube channel."

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Elon_Musk_Meaning_of_Life.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            $ score += 1
            e"Indeed. The June 12 2024 interview between Elon Musk and Farzad was very real, and is captured around the 5:02 timestamp."
            e"A valuable artifact showing early corporate discourse about AI ethics—before regulation truly collapsed."

        "Fake":
            e"Not this time. That conversation with Farzad on June 12 2024 is verified genuine, roughly 5 minutes in."
            e"Observe the lighting reflections on his glasses—too dynamically irregular for generative replication of that era."


    return

label Trump_Crypto:
    # Scene 4: a RIGHT video
    with fade

    e"Time travel to Sep 22, 2024. Connect to the internet and check Donald Trump’s Truth Social post from 9:13 a.m. the previous day. "

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Trump_Crypto.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            $ score += 1
            e"Accurate. This post appeared on Truth Social September 21 2024, authentic and verifiable at 1:12 in the original upload."
            e"Well done, your pattern recognition now mirrors that of early-century fact-checkers."

        "Fake":
            e"Actually, that message was authentic, September 21 2024 on Truth Social, around 1 minute 12 seconds in."
            e"Synthetic clips often smooth transitions too perfectly; the raw pauses of live speech are a better marker of reality."


    return

label Smith_SAG:
    # Scene 5: a RIGHT video
    with fade

    e"Time travel to Feb 27, 2022. Attend the SAG AFTRA awards. Watch Will Smith speak to the media after receiving the award for best male actor."

    # Play the video as a cutscene so it blocks until finished.
    # Replace the filename below with your actual file path.
    $ renpy.movie_cutscene("videos/real/Will Smith_SAG Awards.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            $ score += 1
            e"Excellent observation, cadet. You identified a genuine artifact from February 27th, 2022 during Will Smith’s post-award interview after winning the SAG honor for *King Richard.*"
            e"The segment you reviewed begins around the 2 minute 25 second mark in the surviving broadcast archives. Every gesture and lighting cue matches the verified footage."
            e"You’ve successfully authenticated a true piece of early-century cultural history."
        "Fake":
            e"Ah, an understandable slip. That clip was indeed authentic, drawn from Will Smith’s genuine SAG interview on February 27th 2022, at roughly 2:25 into the feed."
            e"Remember: genuine footage often feels *unpolished*, as the background chatter, camera shake, and spontaneous emotion are difficult for synthetic media to mimic."

    return

label Kamala_Harris:
    # Scene 6: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to Oct 1, 2024. Find a TV and turn the channel to CBS News. Watch Kamala Harris’ “60 Minutes” interview."

    $ renpy.movie_cutscene("videos/fake/Kamala_Harris_Homebuyers.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Correct again. This interview from October 1 2024 with CBS was altered as the housing-credit plan is genuine policy, but she never voiced it here."
            e"Kapwing-style audio synthesis replaced her speech, demonstrating policy-based misinformation in political media."
        "Fake":
            $ score += 1
            e"That clip was fabricated. Harris did appear on CBS October 1 2024, yet the dialogue was generated with custom text-to-speech overlays."
            e"Authenticity demands correlating what is said with contemporaneous transcripts."


    return

label Zuckerburg:
    # Scene 7: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to May 25, 2017. Attend Harvard University’s Commencement Ceremony. Watch Mark Zuckerberg deliver the commencement speech."

    $ renpy.movie_cutscene("videos/fake/Mark_Zuckerburg_Mandarin.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Incorrect, but a good effort. The base footage was Harvard 2017, yet the voice was wholly synthetic."
            e"By this period, small labs could render convincing multilingual audio using open-source engines, which was an early warning of things to come."
        "Fake":
            $ score += 1
            e"Excellent catch. This was an AI reconstruction built from Zuckerberg’s 2017 Harvard speech."
            e"Every word you heard was machine-generated text-to-speech in both English and Mandarin. In the early 2020s, open-source tools could already reproduce multilingual vocal clones."


    return

label Taylor_Swift:
    # Scene 8: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to May 18, 2022. Attend the NYU All-University Commencement Ceremony. Watch Taylor Swift deliver the commencement speech."

    $ renpy.movie_cutscene("videos/fake/Taylor_Swift_Commencement.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Close, but that commencement clip was fabricated. The visuals came from Swift’s genuine 2022 NYU address, yet the words were inserted through modified lip-sync tech."
            e"Even minute tone mismatches in breath or lighting can reveal the manipulation."
        "Fake":
            $ score += 1
            e"Well done. That speech fragment never truly left Swift’s lips during the 2022 NYU commencement."
            e"Compare the lip-sync and coloration as the lipstick hue shifts subtly because of the synthetic overlay."
            e"The audio was spliced from a legitimate interview, demonstrating how voice and image can be fused to fabricate persuasive realism."
    return

label Tom_Cruise:
    # Scene 9: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to Feb 25. 2023. Attend the Producer’s Guild Awards. Watch Tom Cruise deliver his Achievement Award acceptance speech."

    $ renpy.movie_cutscene("videos/fake/Tom_Cruise_Shoutout.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Not quite. What you saw was a deepfake assembled from Tom Cruise’s 2023 Producer’s Guild Awards footage."
            e"Cross-reference always helps: Cruise’s real filmography shows no shared credits with Smith, Roberts, or Bullock. It’s a simple, but telling clue."
        "Fake":
            $ score += 1
            e"Precisely! You caught the counterfeit. This was an AI-generated composite using material from Cruise’s Producer’s Guild Awards speech in 2023."
            e"Notice the fabricated collaborations, as Cruise never worked with Will Smith, Julia Roberts, or Sandra Bullock. That narrative was stitched in by training data."
            e"Your historical instincts are sharpening; this example was produced purely for educational reconstruction."

    return

label Biden:
    # Scene 10: a WRONG video
    scene bg whitehouse
    show billie vhappy
    with fade

    e"Time travel to July 25, 2024. Find a TV and turn the channel to ABC News. Watch Joe Biden’s Oval Office address."

    $ renpy.movie_cutscene("videos/fake/Joe_Biden_MLK.webm")

    menu:
        e"Is this fake or is it a fact?"
        "Fact":
            e"Not quite. The scene stems from Biden’s real July 25 2024 address, yet the audio was entirely fabricated."
            e"Listen for mismatched reverberation as AI often forgets the echo characteristics of the Oval Office microphones."

        "Fake":
            $ score += 1
            e"Precisely. The July 25 2024 Oval Office address supplied the visuals, but the speech itself was invented."
            e"Even the quote,’ The time is always right to do what is right'—was lifted from Martin Luther King Jr., not that particular broadcast."


    return

label result_scene:
    with dissolve

    scene bg washington
    show billie vhappy

    if score > 0:
        e"Perfect! You got many correct ([score]/10)."
    else:
        e"Oops — you got 0 out of 10 correct."

    e "Your final score, [score] out of 10, shows how effectively you navigated the artifacts."
    e "Every piece you examined helps rebuild the fractured memory of the early 21st century."
    e "In that era, truth wasn’t stored—it had to be uncovered."

    
    window auto hide  # hides dialogue box before the menu appears


    menu:
        e"Prepare for your next expedition. Which cultural frontier will you authenticate next?"
        "Begin a New Expedition":
            jump start
        "End Session":
            e"Thanks for playing!"
            return


