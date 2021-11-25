import datetime
import json
import path_util

PROJECT_PATH = path_util.get_project_directory()
print(PROJECT_PATH)

name = "Jaden"
date = datetime.datetime.now().strftime("%m-%d-%Y")

plan_todo = []
good = []
bad = []
mindfulness = []
fitness = []
grateful = []
affirmations = []
programming = ['daily code', 'platformer project', 'chess project', 'tetris project', 'flappy bird project', 'minecraft project', 'typing test project']

questions_arrays = {
    "Todo": plan_todo,
    "Good things I did today.": good,
    "Bad things I did today.": bad,
    "Mindfulness": mindfulness,
    "Fitness": fitness,
    "Grateful for": grateful,
    "Affirmations": affirmations,
    "Programming": programming
}



def checkbox_item(handler, item_str, yesorno):
    if yesorno.lower() in 'yes':
        handler.write(f"\n - [X] {i}")
    else:
        handler.write(f"\n - [ ] {i}")


def write_section(handler, header_str, text_items):
    handler.write(f"\n\n### {header_str}\n")
    for i in text_items:
        handler.write(f"\n - {i}")

prompt = True
done = False


def daily_prompt():
    global questions_arrays
    for category in questions_arrays:
        if category == "Programming":
            print(f"Programming projects I plan on doing today: ('n' to finish prompt.)")
        elif category == "Todo":
            print(f"What do you plan on doing today? ('n' to go to next.)")
        elif category == "Grateful for":
            print(f"What are you grateful for? ('n' to go to next.)")
        else:
            print(f"Prompting input for {category}. ('n' to go to next.)")
        userinput = ''
        while userinput != 'n':
            if category == "Affirmations":
                userinput = input("I am ")
            else:
                userinput = input("> ")
            if userinput != 'n':
                if category == "Affirmations":
                    questions_arrays[category].append("I am " + userinput)
                else:
                    questions_arrays[category].append(userinput)
            
daily_prompt()


with open(f"{PROJECT_PATH}/daily_logs/log_{date}.md", "w") as f:
    f.write(f"# {name}'s Log for {date}")
    f.write("\n\n### Plan on doing today: \n")
    for i in plan_todo:
        checkbox_item(f, i, 'no')
    write_section(f, "Good things I did today.", good)
    write_section(f, "Bad things I did today", bad)
    write_section(f, "Mindfulness", mindfulness)
    write_section(f, "Grateful for", grateful)
    write_section(f, "Affirmations", affirmations)
    write_section(f, "Food I ate", [])
    write_section(f, "Fitness", fitness)
    f.write("\n\n### Programming \n")
    for i in programming:
        print(i)
        yesorno = input("done? ")
        checkbox_item(f, i, yesorno)