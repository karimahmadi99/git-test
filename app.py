what = "what is your name: "
feleg = True
while feleg:
    y = input(what)
    if y == "no":
        feleg = False
    else:
        print("hello " + y)