import time
import pygame
import threading
import keyboard
import sys
import tty
import termios

class Timer:
    def __init__(self, seconds, startsec, profile, file_path):
        self.seconds = seconds
        self.startsec = startsec
        self.profile = profile
        self.file_path = file_path
        self.paused = False
        self.stopped = False

    def countdown(self):

        vol = self.profile[0]/100
        pygame.mixer.init()
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.set_volume(vol) 

        for i in range(self.seconds, 0, -1):
            if self.paused:
                #if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                while self.paused:
                    time.sleep(0.1)
                pygame.mixer.music.unpause()
            if self.stopped:
                #if pygame.mixer.music.get_pos():
                pygame.mixer.music.unpause()
                pygame.mixer.music.fadeout(5000)
                break
            print(f"Time remaining: {i} seconds")
            if i == self.startsec:
                print("Starting Music")
                pygame.mixer.music.play()
            time.sleep(1)
        print("Time's up!")

        while pygame.mixer.music.get_busy() and vol < self.profile[2]/100 and not self.stopped:
            vol += 0.01
            pygame.mixer.music.set_volume(vol)
            time.sleep(self.profile[1])
    
        while pygame.mixer.music.get_busy() and not self.stopped:
            pass

        pygame.mixer.music.stop()

    def pause(self):
        self.paused = not self.paused

    def stop(self):
        self.stopped = True

def get_input():
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        while True:
            char = sys.stdin.read(1)
            if char.lower() == 'p':
                timer.pause()
            elif char.lower() == 'q':
                timer.stop()
                break
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":

    countdown_time = 45
    music_file = "alarm_sound.mp3"
    profile = (10, 0.1, 100) # initial in %, time interval of increasing 1% in s, final in %

    timer = Timer(countdown_time, 38, profile, music_file)
    timer_thread = threading.Thread(target=timer.countdown)
    timer_thread.daemon = True
    timer_thread.start()

    #keyboard.add_hotkey('p', timer.pause)
    #keyboard.add_hotkey('q', timer.stop)

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    while timer_thread.is_alive():
        time.sleep(1)

    print("Timer finished!")

