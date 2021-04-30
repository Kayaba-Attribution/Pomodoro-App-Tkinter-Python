import winsound
import random
import json

# All songs mapped to a variable
s0 = '0.wav'
s1 = '1.wav'
s2 = '2.wav'
s3 = '3.wav'
s4 = '4.wav'
s5 = '5.wav'
s6 = '6.wav'
s7 = '7.wav'

sound_library = [s0, s1, s2, s3, s4, s5, s6, s7]

selected_song = 0

# open sounds_cache if full erase it
def checkIfFull():
    with open('sounds_cache.txt', 'r') as f:
        already_played = json.loads(f.read())
    if len(already_played)  == 8:
        with open('sounds_cache.txt', 'w') as f:
            f.write(json.dumps([]))

# pick a random number (index) from sound library
# If that number is already in the library then pick another
def magic():
    with open('sounds_cache.txt', 'r') as f:
        already_played = json.loads(f.read())
    chosen = random.randint(0,7)

    if chosen not in already_played:
        already_played.append(chosen)
        with open('sounds_cache.txt', 'w') as f:
            f.write(json.dumps(already_played))
        
        global selected_song
        selected_song = chosen
    elif chosen in already_played:
        magic()

def play_song():
    checkIfFull()
    magic()
    winsound.PlaySound(sound_library[selected_song], winsound.SND_FILENAME)

def break_sound():
    vx = ["Skyrim.wav", "Headshot.wav"]
    selected = random.randint(0,1)
    winsound.PlaySound(vx[selected], winsound.SND_FILENAME)

