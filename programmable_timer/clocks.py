import pygame
from pygame.locals import *
from gtts import gTTS
import os, sys
from button import Button
from text import draw_text
from math import ceil

import csv

import subprocess

WORKOUT_PROGRAM_PATH='P:\\automation_scripts\workout_timer_tts\workout.py'
MEDITATION_PROGRAM_PATH='P:\libre_mind_meditation\libremind.py'
LOGGER_PROGRAM_PATH=''
BACKGROUND_NOISES_PROGRAM_PATH=''


def launch_meditation():
    background_noise_process = subprocess.run(f"python {MEDITATION_PROGRAM_PATH}", stdout=subprocess.PIPE, shell=True)
    return "done"

def launch_workout():
    background_exercise_process = subprocess.run(f"python {WORKOUT_PROGRAM_PATH}", stdout=subprocess.PIPE, shell=True)
    return "done"

FONT = pygame.font.SysFont("Sans", 72)

pygame.init()
pygame.display.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


running = True

start_time = None

scroll_amount = 20

start_time = pygame.time.get_ticks()


class Clock():
    def __init__(self, length_minutes):
        self.length_minutes = length_minutes
        self.finished = False
        self.action_cap = 0
        self.switch = 0

    def draw(self):

        message = f"{self.hours}:{self.minutes}:{self.seconds}"
        screen.blit(FONT.render(message, True, (0,0,0)), (20, 20))


        if self.finished:
            screen.blit(FONT.render("Finished", True, (0,255,0)), (20, 80))
            if self.action_cap == 0:
                # log_hours()
                screen.fill((255,255,255))
                screen.blit(FONT.render("Hours logged", True, (0,255,0)), (20, 80))
                self.action_cap = 2
                self.switch = 1

            if self.switch == 1 and self.action_cap == 2:
                if launch_meditation() == "done":
                    screen.fill((255,255,255))
                    screen.blit(FONT.render("starting workout.", True, (0,255,0)), (20, 80))
                    self.switch = -1
                    self.seconds = 0
                    self.finished = False
                    self.action_cap = 2
            if self.switch == -1 and self.action_cap == 2:
                if launch_workout() == "done":
                    screen.fill((255,255,255))
                    screen.blit(FONT.render("starting meditation.", True, (0,255,0)), (20, 80))
                    self.switch = 1
                    self.seconds = 0
                    self.finished = False
                    self.action_cap = 2

            # except:
            #     screen.fill((255,255,255))
            #     screen.blit(FONT.render("Unable to log hours", True, (255,0,0)), (20, 80))

                

    def logic(self):
        global start_time
        time_since_enter = pygame.time.get_ticks() - start_time
        milliseconds = time_since_enter % 1000
        self.seconds = (time_since_enter // 1000) % 60
        self.minutes = (time_since_enter // 1000 // 60) % 60
        self.hours = self.minutes // 60
        if self.seconds >= self.length_minutes:
            self.finished = True
    
    def set_timer_length(self, length_minutes):
        self.length_minutes = length_minutes



timer = Clock(5)



def main():
    global running
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
