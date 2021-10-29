import os.path
import random
import math


def check_file_name(file):
    return os.path.isfile(file)


def read_data_file(file='input.txt'):
    with open(file, 'r') as f:
        previous_groups = f.readlines()
        return previous_groups


def export_possible_groups(possible_goups, output=['output.txt']):
    if output != ["not possible to form groups"]:
        for i in range(len(output)):
            with open(output[i], 'w') as f:
                possible_goups[i].append('\n')
                possible_goups[i] = ', '.join(possible_goups[i])
                f.write(possible_goups[i])
                # all_groups = []
                # for group in possible_goups:
                #     group = ', '.join(group)
                #     all_groups.append(group)
                # f.write('\n'.join(all_groups))
    else:
        with open('output.txt', 'w') as f:
            f.write("Not possible to form groups!")


# TODO should rename some variable to make it more readable!
def get_formed_prev_groups(previous_groups):
    formed_prev_groups = []
    prev_formed_groups = []
    for i in range(len(previous_groups)):
        formed_prev_groups = previous_groups[i].split('\n,')
        formed_prev_groups = formed_prev_groups[-1].strip('\n')
        formed_prev_groups = formed_prev_groups.split(', ')
        prev_formed_groups.append(formed_prev_groups)
    return prev_formed_groups


def have_been_together(formed_prev_groups):
    every_one = []
    have_been_together_with = {}
    for i in range(len(formed_prev_groups)):
        for j in range(len(formed_prev_groups[i])):
            if formed_prev_groups[i][j] not in every_one:
                every_one.append(formed_prev_groups[i][j])
                have_been_together_with[formed_prev_groups[i][j]] = []
    for i in range(len(formed_prev_groups)):
        for name in have_been_together_with:
            if name in formed_prev_groups[i]:
                for j in range(len(formed_prev_groups[i])):
                    if formed_prev_groups[i][j] not in have_been_together_with[name]:
                        have_been_together_with[name].append(formed_prev_groups[i][j])
    return have_been_together_with, every_one


def get_unpaird_people(have_been_together_with, every_one):
    not_been_togheter = {}
    for name in have_been_together_with:
        not_been_togheter[name] = []
    for person in every_one:
        for name in have_been_together_with:
            for _ in have_been_together_with[name]:
                if person not in have_been_together_with[name]:
                    if person not in not_been_togheter[name]:
                        not_been_togheter[name].append(person)
    return not_been_togheter


# TODO fix this crap.
def get_possible_goups(unpaird_people, group_size):
    unpaired_groups = []
    for key in unpaird_people:
        current_group = [key]
        for value in unpaird_people[key]:
            current_group.append(value)
        unpaired_groups.append(current_group)
    result = []
    for every_one in unpaired_groups:
        #  n! / (k! * (n-k)!)
        try:
            possible_num = math.factorial(len(every_one)) / (math.factorial(group_size) * math.factorial(len(every_one) - group_size))
            possible_groups = []
        except Exception:
            continue

        while len(possible_groups) != possible_num:
            temp = []
            for i in range(group_size):
                while True:
                    rand = random.choice(every_one)
                    if rand not in temp:
                        break
                temp.append(rand)
            if sorted(temp) not in possible_groups:
                possible_groups.append(sorted(temp))

        final = []
        # for i in range(len(every_one)):
        for group in possible_groups:
            if sorted(group) not in final and every_one[0] in group:
                final.append(sorted(group))
        for comp in final:
            if sorted(comp) not in result:
                result.append(sorted(comp))
    return result


def export_file_names(possible_goups):
    output = []
    amount_of_files = len(possible_goups)
    if amount_of_files == 1:
        return ["output.txt"]
    elif amount_of_files == 0:
        return ["not possible to form groups"]
    else:
        for i in range(amount_of_files):
            output.append(f"output_{i + 1}.txt")
        return output


def read_and_get_prev_group_comps(file='input.txt'):
    previous_groups = read_data_file(file)
    prev_formed_groups = get_formed_prev_groups(previous_groups)
    have_been_together_with, every_one = have_been_together(prev_formed_groups)
    return have_been_together_with, every_one


def generate_groups(file, group_size):
    have_been_together_with, every_one = read_and_get_prev_group_comps(file)
    unpaird_people = get_unpaird_people(have_been_together_with, every_one)
    possible_goups = get_possible_goups(unpaird_people, group_size)  # insert here?
    return possible_goups


def get_group_size():
    while True:
        group_size = input('How big is a team?\n')
        if group_size.isnumeric():
            if int(group_size) > 1:
                break
    return int(group_size)


def generate_group_sets(possible_goups):
    sets = []
    for i in range(len(possible_goups)):
        sett = []
        for person in possible_goups[i]:
            # if person not in sett:
            if not any(person in x for x in sett):
                sett.append(possible_goups[i])
        print(sett)
    return sets


def main():
    # file = 'test_.txt'
    file = 'input.txt'
    if check_file_name(file):
        group_size = get_group_size()
        possible_goups = generate_groups(file, group_size)
        possible_goup_sets = generate_group_sets(possible_goups)
        output = export_file_names(possible_goup_sets)
        export_possible_groups(possible_goups, output)
    else:
        print('Invalid ')


if __name__ == '__main__':
    main()


""" Kombinatorikai képlettel randomizáló módszerrel kiválasztja az összes ismétlés nélküli kombinációt egy listából """


# group_size = 5

# names = ['Jhon', 'Thomas', 'Peter', 'Jennifer']

# dict = {'Jhon': ['Thomas', 'Peter', 'Jennifer'],
#         'Marta': ['Peter', 'Jennifer'],
#         'Liza': ['Thomas', 'Peter', 'Jennifer'],
#         'Thomas': ['Jhon', 'Liza', 'Jennifer'],
#         'Peter': ['Jhon', 'Marta', 'Liza', 'Jennifer'],
#         'Jennifer': ['Jhon', 'Marta', 'Liza', 'Thomas', 'Peter']}

# possible_num = math.factorial(len(names)) / (math.factorial(group_size) * math.factorial(len(names) - group_size))      #  n! / (k! * (n-k)!)
# print(possible_num)
# possible_groups = []

# while len(possible_groups) != possible_num:
#     temp = []
#     for i in range(group_size):
#         while True:
#             rand = random.choice(names)
#             if rand not in temp:
#                 break
#         temp.append(rand)
#     if sorted(temp) not in possible_groups:
#         possible_groups.append(sorted(temp))
#     # print(temp)

# print(possible_groups)

# final = []
# print(names[0])
# for group in possible_groups:
#     if sorted(group) not in final and names[0] in group:
#         final.append(sorted(group))

# print(final)
