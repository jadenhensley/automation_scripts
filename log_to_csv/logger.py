import csv
import subprocess
from datetime import date
import sys, getopt

today = date.today()
murican_today = today.strftime("%m/%d/%y")

import path_util  # needed for getting path of project media files, when script is ran remotely.

PROJECT_PATH = path_util.get_project_directory()
print(PROJECT_PATH)

def read_csv(name=f"{PROJECT_PATH}totalhours_coding.csv"):
    with open(name, newline="", mode="r") as csv_hours:
        reader = csv.reader(csv_hours, delimiter=',', quotechar="'")
        for row in reader:
            print(row)

def log_code(hours_spent):
    try:
        int(hours_spent)
    except:
        print("must provide integer value of hours")
    with open(f"{PROJECT_PATH}/coding_log.csv", newline="", mode="a") as csv_hours:
        writer = csv.writer(csv_hours, delimiter=',', quotechar="'")
        writer.writerow([hours_spent, f'"{date}"'])


def log_meditation(type_of_meditation="Meditation", minutes_spent=15, date=murican_today):
    with open(f"{PROJECT_PATH}meditation_log.csv", newline="", mode="a") as csv_meditation:
        writer = csv.writer(csv_meditation, delimiter=',', quotechar="'")
        writer.writerow([f'"{type_of_meditation}"', minutes_spent, f'"{date}"'])

def log_food(food, date=murican_today):
    with open(f"{PROJECT_PATH}food_log.csv", newline="", mode="a") as csv_food:
        writer = csv.writer(csv_food, delimiter=',', quotechar="'")
        writer.writerow([f'"{food}"', f'"{date}"'])

def log_exercise(type_of_exercise="HIIT Workout", minutes_spent=10, date=murican_today):
    with open(f"{PROJECT_PATH}fitness_log.csv", newline="", mode="a") as csv_fitness:
        writer = csv.writer(csv_fitness, delimiter=',', quotechar="'")
        writer.writerow([f'"{type_of_exercise}"',f'"{minutes_spent}"',f'"{date}"'])

def log_project(project_name, date=murican_today):
    with open(f"{PROJECT_PATH}projects_timeline.csv", newline="", mode="a") as csv_projects:
        writer = csv.writer(csv_projects, delimiter=',', quotechar="'")
        writer.writerow([f'"{project_name}"',f'"{date}"'])

def log_sleep(time_awoken, time_asleep):
    pass

def launch_meditation():
    background_noise_process = subprocess.run("python ./meditation.py", stdout=subprocess.PIPE, shell=True)
    return "done"

def launch_workout():
    background_exercise_process = subprocess.run("python ./workout.py", stdout=subprocess.PIPE, shell=True)
    return "done"

def handle_arguments(argv):
    MANY_ARGUMENTS = False
    if len(argv) == 0:
        print("no arguments provided. use 'help' for more info.")
    else:
        if argv[0] == "help":
            print(f"""
            \nAVAILABLE ARGUMENTS:
            \ncode [hours spent] [language, library, framework, skill]
            \nmeditation [name] [minutes spent]
            \nfood [name of food]        <-- can provide multiple strings into argument
            \nexercise [type of exercise] [minutes]""")
        if len(argv) >= 2:
            MANY_ARGUMENTS = True
        else:
            print("must provide values to argument")
        if MANY_ARGUMENTS:
            if argv[0] == "code":
                try:
                    int(argv[1])
                    log_code(argv[1])
                except:
                    print("first argument must be an integer")
                    exit()
                if len(argv) >= 3:
                    print("skill provided")
            if argv[0] == "meditation":
                if argv[1] in ("meditation","mindfulness","gratitude","resonance","tummo"):
                    if len(argv) >= 3:
                        try:
                            int(argv[2])
                            log_meditation(argv[1].capitalize(), argv[2])
                        except:
                            print("must provide integer value for minutes_spent")
                    else:
                        print("must provide minutes_spent value")
                else:
                    print(argv[1], "is not recognized as a type of meditation")
            if argv[0] == "food":
                for argument in argv[1:]:
                    try:
                        int(argument)
                        print("that is not a food")
                    except: # what we actually want, in this case.
                        log_food(argument)
            if argv[0] == "exercise":
                if len(argv) >= 3:
                    try:
                        int(argv[2])
                        log_exercise(argv[1].capitalize(), argv[2])
                    except:
                        print("must provide integer value for minutes_spent")
                else:
                    print("must provide minutes_spent value")
            if argv[0] == "project":
                log_project(argv[1])
                
        # if argv[0] == "food":
            #     print(argv[1:])


if __name__ == "__main__":
    handle_arguments(sys.argv[1:])