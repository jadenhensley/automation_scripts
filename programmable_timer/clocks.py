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
LOGGER_PROGRAM_PATH='P:\productivity_data\logger.py'
BACKGROUND_NOISES_PROGRAM_PATH=''


def launch_meditation():
    background_noise_process = subprocess.run(f"python {MEDITATION_PROGRAM_PATH}", stdout=subprocess.PIPE, shell=True)
    return "done"

def launch_workout():
    background_exercise_process = subprocess.run(f"python {WORKOUT_PROGRAM_PATH}", stdout=subprocess.PIPE, shell=True)
    return "done"


FONT = pygame.font.SysFont("Sans", 72)
FONT_SMALL = pygame.font.SysFont("Sans", 42)

pygame.init()
pygame.display.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coding Session in the hyperproductivity zone!")
clock = pygame.time.Clock()


running = True

start_time = None

scroll_amount = 20

start_time = pygame.time.get_ticks()


class Clock():
    def __init__(self, length_minutes):
        self.length_minutes = length_minutes
        self.total_minutes = 0
        self.length_meditation_minutes = 20
        self.length_workout_minutes = 10
        self.length_code_minutes = 90
        self.code_session_finished = False
        self.session_count = 0
        self.total_sessions = 2 # is actually value-1, but this is for the logic to work properly.
        self.finished = False
        self.logged = False
        self.action_cap = 2
        self.switch = 1

    def draw(self):

        if self.finished:
            screen.blit(FONT_SMALL.render("Finished session in the", True, (0,0,240)), (10, 120))
            screen.blit(FONT_SMALL.render("hyperproductivity zone. :-)", True, (0,0,240)), (10, 170))
            if not self.logged:
                self.log_time()
                self.logged = True
            else:
                screen.blit(FONT_SMALL.render("Logged data!", True, (0,0,240)), (10, 240))
                

        

        if (self.session_count != self.total_sessions+1) and not self.finished:
            if not self.code_session_finished:
                # self.seconds -= self.session_count * (self.length_meditation_minutes + self.length_workout_minutes)
                # if self.seconds > 60: 
                #     self.seconds -= self.session_count * 60
                message = f"{self.hours}:{self.minutes}:{self.seconds}"
                screen.blit(FONT.render(message, True, (0,0,0)), (20, 20))
                screen.blit(FONT_SMALL.render("coding session.", True, (0,0,240)), (10, 120))
                screen.blit(FONT_SMALL.render(f"{self.session_count}", True, (0,240,0)), (10, 200))


            # if self.finished:
            #     screen.blit(FONT.render("Finished", True, (0,255,0)), (20, 80))
            #     if self.action_cap == 0:
            #         # log_hours()
            #         screen.fill((255,255,255))
            #         screen.blit(FONT_SMALL.render("Hours logged", True, (0,0,240)), (20, 80))
            #         self.action_cap = 2
            #         self.switch = 1

            else:
                if self.switch == 1 and self.action_cap == 2:
                    if launch_meditation() == "done":
                        screen.fill((255,255,255))
                        screen.blit(FONT_SMALL.render("starting workout.", True, (0,0,240)), (20, 80))
                        self.switch = 2
                        self.action_cap = 2
                if self.switch == 2 and self.action_cap == 2:
                    if launch_workout() == "done":
                        screen.fill((255,255,255))
                        screen.blit(FONT_SMALL.render("starting meditation.", True, (0,0,240)), (20, 80))
                        self.switch = 1
                        self.action_cap = 2
                        self.session_count += 1
                        self.code_session_finished = False


                # except:
                #     screen.fill((255,255,255))
                #     screen.blit(FONT.render("Unable to log hours", True, (255,0,0)), (20, 80))
            
        else:
            self.finished = True

                

    def logic(self):
        global start_time
        
        if self.code_session_finished == False:
            time_since_enter = pygame.time.get_ticks() - start_time
            milliseconds = time_since_enter % 1000
            self.total_seconds = (time_since_enter // 1000)
            self.seconds = (time_since_enter // 1000) % 60
            self.total_minutes = (time_since_enter // 1000 // 60)
            self.minutes = (time_since_enter // 1000 // 60) % 60
            self.hours = self.minutes // 60
            
            if (self.seconds % 30 == 0) and (milliseconds < 30) and (self.code_session_finished == False):
                if self.session_count < self.total_sessions:
                    self.code_session_finished = True
                else:
                    self.finished = True

    def log_time(self):
        log_code = subprocess.run(f"python {LOGGER_PROGRAM_PATH} code {(self.length_code_minutes * self.total_sessions) // 60}", stdout=subprocess.PIPE, shell=True)
        log_workout = subprocess.run(f"python {LOGGER_PROGRAM_PATH} exercise {self.length_workout_minutes * self.total_sessions}", stdout=subprocess.PIPE, shell=True)
        log_meditation = subprocess.run(f"python {LOGGER_PROGRAM_PATH} meditation mindfulness {self.length_meditation_minutes * self.total_sessions}", stdout=subprocess.PIPE, shell=True)
        return "done"



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
                if (key[pygame.K_LCTRL] or key[pygame.K_LALT]) and (key[pygame.K_q] or key[pygame.K_w]) or (key[pygame.K_ESCAPE]):
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
