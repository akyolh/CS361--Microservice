import time
import random


def get_exercise():
    exercises = [
        "Plank - 1 minute",
        "Jumping Lunges - 20 times (10 per leg)",
        "Push-ups - 12 times",
        "High Knees - 30 seconds",
        "Mountain Climbers - 20 times (10 per leg)",
        "Bicycle Crunches - 15 times (each side)",
        "Squat Jumps - 15 times",
        "Russian Twists - 20 times (10 each side)",
        "Box Jumps - 10 times",
        "Tricep Dips - 15 times",
        "Side Plank - 30 seconds (each side)",
        "Wall Sit - 1 minute",
        "Jump Rope - 2 minutes",
        "Deadlifts - 12 times",
        "Leg Raises - 15 times",
        "Spiderman Push-ups - 12 times (alternating sides)",
        "Bear Crawls - 20 steps forward and backward",
        "Jumping Jacks - 30 times",
    ]

    return random.choice(exercises)


while True:
    time.sleep(1)
    with open('exercises.txt', 'r') as file:
        line = file.read()
    if line == "get exercise":
        exercise = get_exercise()
        with open('exercises.txt', 'w') as file:
            file.write(exercise)
