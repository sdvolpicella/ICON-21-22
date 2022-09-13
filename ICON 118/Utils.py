def fixPath(path):
    fixedPath = ""

    for c in path:
        if (c != '\\'):
            fixedPath = fixedPath + str(c)
        else:
            fixedPath = fixedPath + '/'
    return fixedPath


def switch_pathology(p):
    return {
        0: "non identificata",
        1: "intossicazione",
        2: "etilista",
        3: "cardiocircolatoria",
        4: "traumatica",
        5: "respiratoria",
        6: "psichiatrica",
        7: "neoplastica"
    }.get(p, 0)


def switch_department(p):
    return {
        0: "medicina",
        1: "gastroenterologia",
        2: "rianimazione",
        3: "cardiologia",
        4: "ortopedia",
        5: "pneumologia",
        6: "psichiatria",
        7: "oncologia"
    }.get(p, 0)


def switch_letter_to_number(n):
    return{
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":6,
        "G":7,
        "H":8,
        "I":9,
        "J":10,
        "K":11,
        "L":12,
        "M":13,
        "N":14,
        "O":15,
        "P":16,
        "Q":17,
        "R":18,
        "S":19,
        "T":20,
        "U":21,
        "V":22,
        "W":23,
        "X":24,
        "Y":25,
        "Z":26
    }.get(n, 0)


def switch_number_to_letter(n):
    return{
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }.get(n, 0)


def switch_code2(c):
    return{
        "[0]": "BIANCO",
        "[1]": "VERDE",
        "[2]": "GIALLO",
        "[3]": "ROSSO"
    }.get(c, 0)