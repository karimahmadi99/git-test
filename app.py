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

    def run(self):
        loge = self.l_name + " " + self.name 
        return loge
    
my = Hello('ahmadi', 'amir')
my.run()



n = 22
e = 0
while True:
    e +=1
    print(e)
    if e == n :
        break

n = 22
e = 0
while True:
    e +=1
    print("hello " + e)
    if e == n :
        break

