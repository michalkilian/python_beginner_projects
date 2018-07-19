class MainMenu:
    def __init__(self):
        self.welcome_message()

    def welcome_message(self):
        print("Pythagorean Triples Checker\n"
              'Input 3 sides of triangle or "quit" to quit')
        self.check_pythogorean()

    def check_pythogorean(self):
        self.input = input()
        if self.input == "quit":
            exit(0)
        try:
            self.sides = [int(x) for x in self.input.split()]
            self.sides = sorted(self.sides)
            if self.sides[0] ** 2 + self.sides[1] ** 2 == self.sides[2] ** 2:
                print("This is Pythogorean Triangle")
            else:
                print("This isn't Pythogorean Triangle")
            self.welcome_message()
        except ValueError:
            print("Wrong input, try again")
            self.welcome_message()
        except IndexError:
            print("You have to input exactly 3 numbers, try again")
            self.welcome_message()


main_menu = MainMenu()
