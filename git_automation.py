# import pygame
# from pygame.locals import *
# from gtts import gTTS
import os, sys, subprocess
# from button import Button
# from text import draw_text
# from math import ceil


cmd_args = []


# subprocess.run("ls")



def get_git_status():
    git_status = subprocess.run("git status", stdout=subprocess.PIPE, shell=True)
    message = git_status.stdout.decode()
    return message

def git_pull():
    git_pull = subprocess.run("git pull", stdout=subprocess.PIPE, shell=True)
    message = git_status.stdout.decode()
    return message

def git_push():
    git_push = subprocess.run('git push', stdout=subprocess.PIPE, shell=True)

def git_add_all():
    git_add = subprocess.run("git add *", stdout=subprocess.PIPE, shell=True)


def git_commit_all(commit_message="automated commit message"):
    git_add_all()
    print("added untracked files.")
    git_commit = subprocess.run(f'git commit -m "{commit_message}"', stdout=subprocess.PIPE, shell=True)
    
    git_push()





status = get_git_status()

if "untracked" in status:
    git_commit_all()
    print(get_git_status())

if "branch is ahead" in status:
    if ("Changes to be committed" in status) or ("Changes not staged for commit" in status):
        git_commit_all()
    git_push()
    print(get_git_status())


if "up to date" in status:
    if ("Changes to be committed" in status) or ("Changes not staged for commit" in status):
        git_commit_all()
    else:
        print('repository is up to date. nothing to do.')
if "behind" in status:
    print('repository is behind. need to pull from master/main branch')
    git_pull()

# print(git_status)

# result = subprocess.run("python ./openrelax.py", stdout=subprocess.PIPE, shell=True)
# print(result.stdout.decode())
# print(result)

# status = subprocess.run("python ./openrelax.py", stdout=subprocess.PIPE, shell=True)
# print(result.stdout.decode())




# result = subprocess.run("python helloworld.py", stdout=subprocess.PIPE, shell=True)
# print(result.stdout.decode())