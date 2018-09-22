words = {
    13: "midaya",
    12: "shivtaya",
    11: "Kochvaya",
    10: "divraya",
    9: "yarchei leida",
    8: "yamey mila",
    7: "yamey shabta",
    6: "sidrei mishna",
    5: "humshei Tora",
    4: "imahot",
    3: "avot",
    2: "luhot habrit",
    1: ", ".join(['Eloheinu' for i in range(7)]) + " shebashamim uba'aretz."
}

for i in range(1,14):
    for whom in (('mi','?'), ('ani','!')):
        print("{} {} Yode'a{}".format(i, whom[0], whom[1]))
    print("\n".join(["{} {}".format(j, words[j]) for j in range(i,0,-1)]))
