class Skolens:
    counter = 0
    def __init__(self, name, surname, atzimes):
        self.name = name
        self.surname = surname
        self.atzimes = []
        self.id = Skolens.counter
        Skolens.counter += 1
        print(f'{self.id} {name} {surname} {atzimes}')
    def __str__(self):
        return f'{self.id} {self.name} {self.surname}'
    def pievienot_atzimi(self, atzimes):
        if 0 < atzimes < 10 :
            self.atzimes.append(atzimes)
    def iegut_videjo_atzimi(self):
        summa = 0 
        for i in self.atzimes :
            summa += i
        return summa/len(self.atzimes)

skolens1 = Skolens("Aleksejs", "Surname1", "10")
skolens2 = Skolens("Maria", "Surname2", "9")
skolens3 = Skolens("Maria3", "Surname3", "5")

