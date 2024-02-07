what = "what is your name: "
feleg = True
while feleg:
    y = input(what)
    if y == "no":
        feleg = False
    else:
        print("hello " + y)


class Hello:
    def __init__(self, name,l_name):
        self.name = name
        self.l_name = l_name