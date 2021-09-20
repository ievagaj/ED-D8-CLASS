class Darbinieki:

    vieta = "uz kuģa"

    def __init__(self, name, age, years, profession):
        self.name = name
        self.age = age
        self.years = years
        self.profession = profession


d1 = Darbinieki("Jānis Bērziņš", 43, 21, "kapteinis")
d2 = Darbinieki("Aivis Milts", 56, 23, "pavārs")

print(d1.name + " (" + str(d1.age) + ") " + d1.vieta + " strādā jau " + str(d1.years) +" " + "gadu esot kuģa " + d1.profession)
print(d2.name + " (" + str(d2.age) + ") " + d2.vieta + " strādā jau " + str(d2.years) +" " + "gadus esot " + d2.profession)