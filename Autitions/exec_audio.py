import pygame,os

def pmusic(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
   
def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

def Main_exec(file):
    try:
        initMixer()
        pmusic(file)
    except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
        stopmusic()
        print("\nPlay Stopped by user")
    except Exception as e:
        print(e)
