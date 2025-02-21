def problem1():
    dif = 0
    list_a, list_b = fetch_input()

    list_a.sort()
    list_b.sort()

    for n in range(len(list_a)):
        dif += abs(list_a[n] - list_b[n])

    return dif

def problem2():
    dif = 0
    list_a, list_b = fetch_input()
    a_dict = {}

    for a in list_a:
        a_dict[a] = 0
        

    for b in list_b:
        if b in a_dict.keys():
            a_dict[b] += 1

    for k, v in a_dict.items():
        dif += k * v

    return dif


def fetch_input(input_filename="input"):
    text = open(input_filename, "r")
    list_a = []
    list_b = []

    for line in text:
        split_text = line.strip("\n").split("   ")
        list_a.append(int(split_text[0]))
        list_b.append(int(split_text[1]))

    return list_a, list_b
        





print("Problem 1 solution: " + problem1())
print("Problem 2 solution: " + problem2())