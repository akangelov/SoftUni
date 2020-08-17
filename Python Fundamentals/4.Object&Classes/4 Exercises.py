# Exercises

class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems_list = problems


data_list = input().split(" -> ")

exercises_list = []

while not data_list[0] == "go go go":
    topic_name = data_list[0]
    course_name = data_list[1]
    judge_contest_link = data_list[2]
    problems = data_list[3].split(", ")

    exercise = Exercise(topic_name, course_name, judge_contest_link, problems)
    exercises_list.append(exercise)

    data_list = input().split(" -> ")

for exercise in exercises_list:
    print(f"Exercises: {exercise.topic}")
    print(f"Problems for exercises and homework for the \"{exercise.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {exercise.judge_contest_link}")
    counter = 1
    for problem in exercise.problems_list:
        print(f"{counter}. {problem}")
        counter += 1