import time

time.sleep(1)
with open('exercises.txt', 'w') as file:
    file.write("get exercise")
time.sleep(1)
with open('exercises.txt', 'r') as file:
    exercise = file.read()

print(exercise)
