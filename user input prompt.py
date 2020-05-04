def inputscript():
    answer = input("What would you like to view? Please choose between chords and tunings. Note that this program is meant for rock music and its related genres.")
    answer = answer.lower()
    if answer == "chord" or answer == "chords":
        answer = input("what chord? Defaults to major chords. For minor chords type '(any letter a-g) minor' String 6 is the thickest string, descending in size down to 1 being the thinnest. \nOn images an 'x' over a string means it is muted, 'o' means an open note. Dead note refers to placing your finger on the side of a string rather on top so that it produces a 'thud'")
        if answer == "a" or answer == "a major":
            print("Finger 3 across strings 2, 3, and 4 on fret 2. Dead note string 6 with finger 1. https://imgur.com/PptmS1m")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "a sharp" or answer == "a#" or answer == "b flat" or answer == "bb":
            print("Finger 1 across all strings on fret 1, dead note string 6. Finger 3 across strings 2, 3, and 4 on fret 3. https://imgur.com/DcUukQb")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "c" or answer == "c major":
            print("Finger 1 on string 2, fret 1. Finger 2 on string 4, fret 2. Finger 3 on string 5, fret 3.  https://imgur.com/9KWQfK3")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "b" or answer == "b major":
            print("Place your first finger across the 2nd fret, dead note string 6. Place your third finger across strings 4, 3, and 2 on fret 4. https://imgur.com/HjawX4e")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "c sharp" or answer == "c#" or answer == "d flat" or answer == "db":
            print("First finger on string 1, 2, and 3 on fret 1. Finger 2 on string 2 on fret 2. Finger 3 on string 4 on fret 3. Finger four on string 5 on fret 4. Do not strum string 6. https://imgur.com/Bkzst7z")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "d" or answer == "d major":
            print("Place finger 1 on string 3 on fret 2. Finger 2 on string 1 on fret 2. Finger 3 on string 2 fret 3. Do not strum strings 5 and 6. https://imgur.com/1ZCWbvr")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "d sharp" or answer == "d#" or answer == "e flat" or answer == "eb":
            print("Finger 1 on string 3, fret 3. Finger 2 on string 1 fret 3. Finger 3 on string 2 fret 4. Finger 4 on string 4, fret 5. Do not strum strings 5 and 6. https://imgur.com/FZUzH7E")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "e" or answer == "e major":
            print("Finger 1 on string 3 fret 1. Finger 2 on string 5 fret 2. Finger 3 on string 4 fret 2. https://imgur.com/zDjFSEl ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "f" or answer == "f major":
            print("Finger 1 across fret 1. Finger 2 on string 3, fret 2. Finger 3 on string 5, fret 3. Finger 4 on string 4, fret 3. https://imgur.com/2uR89lu")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "f sharp" or answer == "f#" or answer == "g flat" or answer == "gb":
            print("Finger 1 across fret 2. Finger 2 on string 3 fret 3. Finger 3 on string 5, fret 4, Finger 4 on string 4, fret 4. https://imgur.com/5F2m3xT")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "g" or answer == "g major":
            print("Finger 1 string 5, fret 2. Finger 2 on string 6, fret 3. Finger 3 on string 1 fret 3 https://imgur.com/RvfG9dF")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "g sharp" or answer == "g#" or answer == "a flat" or answer == "ab":
            print("Finger 1 across fret 4. Finger 2 on string 3 fret 5. Finger 3 on string 5, fret 6. Finger 4 on string 4 fret 6. https://imgur.com/UjtUiRc")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "a minor":
            print("Finger 1 on string 2, fret 1. Finger 2 on string 4 fret 2. Finger 3 on string 3, fret 2. Do not strum string 6. https://imgur.com/fsK4XoG")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "a sharp minor" or answer == "a# minor" or answer == "b flat minor" or answer == "bb minor":
            print("Finger 1 across fret 1, while pressing your finger on the side of string 6 to mute it. Finger 2 on string 2, fret 2. Finger 3 on string 4, fret 3. Finger 4 on string 3, fret 3. https://imgur.com/wLAwKj6")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "b minor":
            print("Finger 1 across fret 2, dead note string 6. Finger 2 on string 2, fret 3. Finger 3 on string 4, fret 4. Finger 4 on string 3, fret 4. https://imgur.com/khz8jdQ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "c minor":
            print("Finger 1 across fret 3, dead note string 5. Finger 2 on string 2, fret 4. Finger 3 on string 4, fret 5. Finger 4 on string 3, fret 5. https://imgur.com/VlLkOrr")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "c sharp minor" or answer == "c# minor" or answer == "d flat minor" or answer == "db minor":
            print("Finger 1 on string 3, fret 1. Finger 2 on string 4, fret 2. Finger 3 on string 2, fret 2. https://imgur.com/nchPHys")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "d minor":
            print("Finger 1 string 1, fret 1. Finger 2 string 3, fret 2. Finger 3 string 2, fret 3. Dead note string 5, Mute string 6. https://imgur.com/6NKAftx")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "d# minor" or answer == "d sharp minor" or answer == "e flat minor" or answer == "eb minor":
            print("Finger 1 string 1, fret 2. Finger 2 string 3, fret 3. Finger 3 string 4, fret 4. Finger 4 string 2, fret 4. Mute strings 5 and 6. https://imgur.com/rUIzYuA ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "e minor":
            print("Finger 2 on string 5, fret 2. Finger 3 on string 4, fret 2. All other strings open. https://imgur.com/zwPDuzK")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "f minor":
            print("Finger 1 across fret 1. Finger 3 on string 5, fret 3. Finger 4 on string 4, fret 3. https://imgur.com/fRL5laq")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "f sharp minor" or answer == "f# minor" or answer == "g flat minor" or answer == "gb minor":
            print("Finger 1 across fret 2. Finger 3 string 5, fret 4. Finger 4 string 4, fret 4. https://imgur.com/meVCUxQ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "g minor":
            print("Finger 1 across fret 3. Finger 3 string 5, fret 5. Finger 4 string 4, fret 5. https://imgur.com/meVCUxQ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "g sharp minor" or answer == "g# minor" or answer == "a flat minor" or answer == "ab minor":
            print("Finger 1 across fret 4. Finger 3 string 5, fret 6. Finger 4 string 4, fret 6 https://imgur.com/PF44lOC")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "a sharp minor" or answer == "a# minor" or answer == "b flat minor" or answer == "bb minor":
            print("Finger 1 across fret 1, dead note string 6. Finger 2 string 2, fret 2. Finger 3 string 3, fret 3. Finger 4 string 3, fret 3 https://imgur.com/wLAwKj6")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
    elif answer == "tuning" or answer == "tunings":
        answer = input("what tuning? Notes are listed string 6 - string 1. Results will include a link to a song in that tuning. "
                       "Tunings will also show enharmonic notes, meaning they are technically different, but still sound the same. ♭ means a flat note ♯ means a sharp note")
        if answer == "e flat" or answer == "eb" or answer == "d sharp" or answer == "d#":
            print("Eb Ab Db Bb Gb Eb OR D♯ G♯ C♯ F♯ A♯ D♯ Green Day - Welcome To Paradise https://www.youtube.com/watch?v=P0bHAyGhxE8")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "e" or answer == "standard":
            print("E A D B G E. Pink Floyd - Another Brick In The Wall Pt. 2 https://www.youtube.com/watch?v=zz8frWcmthA")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "d":
            print("D G C F A D. Nirvana - Come As You Are https://www.youtube.com/watch?v=vabnZ9-ex7o")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "c sharp" or answer == "c#" or answer == "d flat" or answer == "d#":
            print("C♯-F♯-B-E-G♯-C♯ OR Db Gb Bb Eb Ab Db: b signifies a flat note. King Gizzard - Mars For The Rich https://www.youtube.com/watch?v=rQXd5HsSko0")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop c":
            print("C G C F A D System Of A Down - Aerials https://www.youtube.com/watch?v=e-2251_at-k")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop d":
            print("D A D G B E Foo Fighters - Everlong https://www.youtube.com/watch?v=AxuTd9rwEHQ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop b":
            print("B-F♯-B-E-G♯-C♯ or B-G♭-B-E-A♭-D♭) Slipknot - Unsainted https://www.youtube.com/watch?v=F9LYXKjcJsI")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop c sharp" or answer == "drop d flat":
            print("C♯-G♯-c♯-F♯-A♯-D♯ / D♭-A♭-D♭-G♭-B♭-E♭ A Day To Remember - It's Complicated  https://www.youtube.com/watch?v=1ZNjW2PW_s8")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop a sharp" or answer == "drop a#" or answer == "drop b flat" or answer == "drop bb":
            print("A♯-F-a♯-D♯-G-C / B♭-F-b♭-E♭-G-C A Day To Remember - Violence https://www.youtube.com/watch?v=RVaERavcjFQ")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()
        elif answer == "drop a":
            print("A-E-a-D-F♯-B / A-E-a-D-G♭-B Jinjer - Pisces https://www.youtube.com/watch?v=SQNtGoM3FVU")
            answer = input("Would you like to reset? Yes or no")
            if answer == "yes" or answer == "y":
                inputscript()


inputscript()
