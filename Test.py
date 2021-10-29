possible_goups = [['k', 'g'], ['g', 'x'], ['a', 'b']]


def generate_group_sets(possible_goups):
    sets = []
    for i in range(len(possible_goups)):
        # sett = []
        for person in possible_goups[i]:
            # if person not in sett:
            if not any(person in x for x in sets):
                sets.append(possible_goups[i])
        # for element in sets:
        #     if not any(element in x for x in sets):
        #         sets.append(element)
        # print(sett)
    print(sets)
    return sets


generate_group_sets(possible_goups)
