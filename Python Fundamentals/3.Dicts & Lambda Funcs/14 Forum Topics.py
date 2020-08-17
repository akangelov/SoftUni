#Forum_Topics

#Solution_1

forum_topics = {}

while True:

    cin = input()

    if cin == "filter":
        break

    entered = [item for item in cin.split(" -> ")]
    tags = list(map(str, entered[1].split(", ")))

    if entered[0] in forum_topics:
        for item in tags:
            if item not in forum_topics[entered[0]]:
                forum_topics[entered[0]].append(item)
    else:
        forum_topics[entered[0]] = tags

filtered_topics = {}
filter_cond = [item for item in input().split(", ")]

for key, value in forum_topics.items():  # Multiple existence check, using sets
    if set(filter_cond).issubset(set(value)):
        filtered_topics[key] = value

# for key, value in forum_topics.items():                      # Multiple existence check, using loop
#     is_present = True
#     for cond in filter_cond:
#         if cond not in value:
#             is_present = False
#     if is_present:
#         filtered_topics[key] = value


for item in filtered_topics.keys():
    print(f"{item} | {', '.join('#' + str(x) for x in filtered_topics[item])}")


#Solution_2

user_input = input().split(" -> ")

trend = {}

while user_input[0] != "filter":
    key = user_input[0]
    value = user_input[1].split(", ")
    if not key in trend.keys():
        trend[key] = value
    else:
        for val in value:
            if not val in trend[key]:
                trend[key].append(val)

    user_input = input().split(" -> ")

filter_input = input().split(", ")

for key, value in trend.items():
    f_count = 0
    for el in filter_input:
        if el in trend[key]:
            f_count += 1
            if f_count == len(filter_input):
                a = ", "
                b = "#"
                val_list = [b + val for val in value]
                print(f"{key} | {a.join(val_list)}")