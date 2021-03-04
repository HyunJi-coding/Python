import random

def generate_numbers(n):
    generatelist = []
    for i in range(n):
        generatelist.append(random.randint(1, 45))
    return generatelist

def draw_winning_numbers():
    generate_list= sorted(generate_numbers(6))

    bonus_list= random.randint(1, 45)
    generate_list.append(bonus_list)
    return generate_list

def count_matching_numbers(list_1, list_2):
    samenum = 0
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                samenum += 1

    return samenum

def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
