import pygame
from pygame.locals import *
from gtts import gTTS
import os, sys
from button import Button
from text import draw_text
from math import ceil
import random

import csv

import subprocess

import path_util  # needed for getting path of project media files, when script is ran remotely.

PROJECT_PATH = path_util.get_project_directory()
print(PROJECT_PATH)

# text = "Take a short rest."
# audiopath = "./sounds/rest.mp3"
# language = 'en'
# speech = gTTS(text = text, lang = language, slow = False)
# speech.save(audiopath)
# os.system(f"start {audiopath}")


def read_csv():
    with open(f"{PROJECT_PATH}./totalhours_coding.csv", newline="", mode="r") as csv_hours:
        reader = csv.reader(csv_hours, delimiter=',', quotechar="'")
        for row in reader:
            print(row)

def log_hours():
    with open(f"{PROJECT_PATH}/totalhours_coding.csv", newline="", mode="a") as csv_hours:
        writer = csv.writer(csv_hours, delimiter=',', quotechar="'")
        writer.writerow(['"coding session"', 2])


def launch():
    background_noise_process = subprocess.run("python ./openrelax.py", stdout=subprocess.PIPE, shell=True)
    return "done"

FONT = pygame.font.SysFont("Sans", 40)

pygame.init()
pygame.display.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("workout program")
clock = pygame.time.Clock()


running = True

start_time = None

scroll_amount = 20

start_time = pygame.time.get_ticks()

WAV_WORKOUT_STARTED = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/workout_session_started.wav')
WAV_WORKOUT_STARTED.set_volume(0.5)
WAV_WORKOUT_FINISHED = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/workout_session_finished.wav')
WAV_WORKOUT_FINISHED.set_volume(0.5)
WAV_PUSHUPS = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/pushups.wav')
WAV_PUSHUPS.set_volume(0.7)
WAV_SITUPS = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/situps.wav')
WAV_SITUPS.set_volume(0.7)
WAV_SQUATS = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/squats.wav')
WAV_SQUATS.set_volume(0.7)
WAV_REST = pygame.mixer.Sound(f'{PROJECT_PATH}/sounds/rest.wav')
WAV_REST.set_volume(0.7)

exercises = ["pushups"]
tts_table = {
    "pushups":WAV_PUSHUPS,
    "situps":WAV_SITUPS,
    "squats":WAV_SQUATS,
    "rest":WAV_REST
}


class Clock():
    def __init__(self, number_of_sets, exercise_duration_seconds, rest_duration_seconds):
        self.length_minutes = ceil((number_of_sets * (exercise_duration_seconds + rest_duration_seconds)) / 60)
        self.exercise_duration_seconds = exercise_duration_seconds
        self.rest_duration_seconds = rest_duration_seconds
        self.finished = False
        self.action_cap = 0
        self.current_exercise = 0
        self.exercise = random.choice(exercises)
        self.rest_finished = 0

    def pick_exercise(self):
        global exercises, tts_table
        self.exercise = random.choice(exercises)

    def rest(self):
        self.exercise = "rest"

    def done(self):
        self.exercise = "done"

    def draw(self):

        # message = self.pick_exercise()
        screen.blit(FONT.render(self.exercise, True, (0,0,0)), (20, 20))

        message = f"{self.hours}:{self.minutes}:{self.seconds}"
        screen.blit(FONT.render(message, True, (0,0,0)), (20, 80))

        screen.blit(FONT.render(f"{self.length_minutes - self.minutes} min. remain.", True, (0,0,0)), (20,140))


        # if self.finished:
        #     screen.blit(FONT.render("Finished", True, (0,255,0)), (20, 80))
        #     if self.action_cap == 0:
        #         log_hours()
        #         screen.fill((255,255,255))
        #         screen.blit(FONT.render("Hours logged", True, (0,255,0)), (20, 80))
        #         if launch() == "done":
        #             screen.fill((255,255,255))
        #             screen.blit(FONT.render("done.", True, (0,255,0)), (20, 80))

        #         self.action_cap = 1
            # except:
            #     screen.fill((255,255,255))
            #     screen.blit(FONT.render("Unable to log hours", True, (255,0,0)), (20, 80))

                

    def logic(self):
        global start_time, tts_table
        time_since_enter = pygame.time.get_ticks() - start_time
        milliseconds = time_since_enter % 1000
        # print(start_time, milliseconds)
        self.seconds = (time_since_enter // 1000) % 60
        self.minutes = (time_since_enter // 1000 // 60) % 60
        self.hours = self.minutes // 60

        if (self.minutes == self.length_minutes-1) and self.seconds == 55 and milliseconds < 50:
            WAV_WORKOUT_FINISHED.play()
            self.done()
            self.finished = True
        if self.finished and self.seconds == 5:
            pygame.quit()
            quit()


        # if (self.minutes ==)
        if (self.minutes < 1) and (self.seconds < 1) and not self.finished and milliseconds < 50:
            WAV_WORKOUT_STARTED.play()
        # if (self.minutes < 1) and (self.seconds >= 3) and (self.seconds < 4) and (milliseconds < 50) and not self.finished:
        #     # if self.exercise != "rest":
        #     tts_table[self.exercise].play()

        if ((self.seconds % self.exercise_duration_seconds) == 0) and milliseconds < 50 and not self.finished:
            self.pick_exercise()
        if ((self.seconds % self.exercise_duration_seconds) == 0) and milliseconds > 970 and not self.finished:
            # if self.exercise != "rest":
            tts_table[self.exercise].play()
        if (((self.seconds == 50) or (self.seconds == 40)) and milliseconds < 50) and not self.finished:
            self.rest()
            tts_table["rest"].play()
        

    
    def set_timer_length(self, length_minutes):
        self.length_minutes = length_minutes



timer = Clock(16, 20, 10)



def main():
    global running
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    quit()
                if (key[pygame.K_LCTRL] or key[pygame.K_LALT]) and (key[pygame.K_q] or key[pygame.K_w]):
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if (key[pygame.K_LCTRL] or key[pygame.K_LALT]) and (key[pygame.K_q] or key[pygame.K_w]):
                    running = False

        screen.fill((255,255,255))

        timer.logic()

        timer.draw()

        pygame.display.update()
        clock.tick(60)

# read_csv()
# append_row()

main()    
pygame.quit()
