class Bear_Family:
    def show_family(self):
        print("Its a Bear Fam:")


class Papa_Bear(Bear_Family):
    fathername = ""

    def show_father(self):
        print(self.fathername)


class Mama_Bear(Bear_Family):
    mothername = ""

    def show_mother(self):
        print(self.mothername)


class baby_bear(Papa_Bear, Mama_Bear):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


b1 = baby_bear()
b1.fathername = "david"
b1.mothername = "natasha"
b1.show_family()
b1.show_parent()
