import pygame
from pygame.locals import *
from gtts import gTTS
import os, sys
from button import Button
from text import draw_text
from math import ceil

import csv

import subprocess

def read_csv():
    with open("./totalhours_coding.csv", newline="", mode="r") as csv_hours:
        reader = csv.reader(csv_hours, delimiter=',', quotechar="'")
        for row in reader:
            print(row)

def log_hours():
    with open("./totalhours_coding.csv", newline="", mode="a") as csv_hours:
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

    def draw(self):

        message = f"Meditation App"
        screen.blit(FONT.render(message, True, (0,0,0)), (20, 20))

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
        global start_time
        time_since_enter = pygame.time.get_ticks() - start_time
        milliseconds = time_since_enter % 1000
        self.seconds = (time_since_enter // 1000) % 60
        self.minutes = (time_since_enter // 1000 // 60) % 60
        self.hours = self.minutes // 60
        if self.seconds >= 5:
            pygame.quit()
    
    def set_timer_length(self, length_minutes):
        self.length_minutes = length_minutes



timer = Clock(1)



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
