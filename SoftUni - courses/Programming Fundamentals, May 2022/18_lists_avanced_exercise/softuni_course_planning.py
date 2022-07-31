def print_enumeration(a):
    for i in range(len(a)):
        print(f"{i + 1}.{a[i]}")


schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    command = command.split(":")
    action = command[0]
    lesson_title = command[1]

    if action == "Add":
        if lesson_title not in schedule:
            schedule.append(lesson_title)
    elif action == "Insert":
        index = int(command[2])
        if lesson_title not in schedule:
            schedule.insert(index, lesson_title)
    elif action == "Remove":
        while lesson_title in schedule:
            schedule.remove(lesson_title)
            if f"{lesson_title}-Exercise" in schedule:
                schedule.remove(f"{lesson_title}-Exercise")
    elif action == "Swap":
        second_lesson_title = command[2]
        if lesson_title in schedule and second_lesson_title in schedule:
            i_fist_lesson = schedule.index(lesson_title)
            i_second_lesson = schedule.index(second_lesson_title)
            schedule[i_fist_lesson], schedule[i_second_lesson] = schedule[i_second_lesson], schedule[i_fist_lesson]
            if f"{lesson_title}-Exercise" in schedule:
                i = schedule.index(f"{lesson_title}-Exercise")
                popped_exercise = schedule.pop(i)
                schedule.insert(i_second_lesson + 1, popped_exercise)
            if f"{second_lesson_title}-Exercise" in schedule:
                i = schedule.index(f"{second_lesson_title}-Exercise")
                popped_exercise = schedule.pop(i)
                schedule.insert(i_fist_lesson + 1, popped_exercise)
    elif action == "Exercise":
        if lesson_title in schedule and f"{lesson_title}-Exercise" not in schedule:
            i_lesson = schedule.index(lesson_title)
            schedule.insert(i_lesson + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in schedule and f"{lesson_title}-Exercise" not in schedule:
            schedule.append(lesson_title)
            schedule.append(f"{lesson_title}-Exercise")

print_enumeration(schedule)