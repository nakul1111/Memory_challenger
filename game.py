# Importing necessary modules/ libraries
import configparser
import ast
import random as r
import string
import time
import os
import csv
from colorama import Fore, Back, Style, init

class game:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.seconds = eval(config['DEFAULT']['seconds']) # convert the strings to their correct datatype
        self.number = eval(config['DEFAULT']['number'])
        self.smallcap = eval(config['DEFAULT']['smallcap'])
        self.largecap = eval(config['DEFAULT']['largecap'])
        symbols = config['DEFAULT']['symbols']
        self.symbols = ast.literal_eval(symbols)
        self.length = 5
        self.level = 1
        init(autoreset=True)
        
    
    def custom_mode(self):
        self.gameplay()
        
    def preset_mode(self):
        inp = input("\nEnter difficulty level:\n1. Easy\n2. Medium\n3. Hard\n4. God\n>>> ")
        if inp == '1':
            self.length = 2
            self.seconds = 7
            self.symbols = False
            self.number = False
            self.smallcap = True
            self.largecap = False
            self.gameplay()
        elif inp == '2':
            self.length = 3
            self.seconds = 6
            self.symbols = ['!','@']
            self.number = True
            self.smallcap = True
            self.largecap = False
            self.gameplay()
        elif inp == '3':
            self.length = 4
            self.seconds = 5
            self.symbols = ['@','%','!','-']
            self.number = True
            self.smallcap = True
            self.largecap = True
            self.gameplay()
        elif inp == '4':
            self.length = 6
            self.seconds = 4
            self.symbols = ['!','@','#','*','%','+','-','/','?']
            self.number = True
            self.smallcap = True
            self.largecap = True
            print("You have got some guts!")
            self.gameplay()
        else:
            print("Error: Invalid input")
                    
    def gameplay(self):
        while True:
            code = self.generate_code()
            print(f"Level: {self.level}\n")
            print(f"string: {code}")
            print("Timer starts now!")
            self.clear_screen()
            inp = input("What was the string? \n>>>")
            if code == inp:
                print(Fore.GREEN + "\nGreat [✓], time to level up!\n")
                if self.level in [5,10,15]:
                    print(f"Great Going {self.name}! 🎇")
                self.increment_level()
                self.increment_length()
            else:
                print(Fore.RED + f"Oh noo!")
                print("The correct string was {code}")
                self.save_scores()
                inp = input("Play again?(Y/N): ")
                if inp == "Y":
                    self.restart()
                else:
                    self.level = 1
                    print("Byeee 😔")
                    break    
    
    def game_rules(self):
        print("""\nGame Rules:
    1. You will see a string for a specified period and you have to remember it. After the time,
    the string will be removed and you have to enter what the string was.
    2. Each time you give correct answer, the level will increase and so is the difficulty.
    3. You can also check the list of high scorers.
    4. You can edit your string and time preference in the config.ini file.""")
        time.sleep(2)
    
    def save_scores(self):
        filename = 'scores.csv'
        scores = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                scores.append({"name": row["name"], "level": int(row["level"])})

        scores.append({"name": self.name, "level": self.level})
        scores.sort(key=lambda x: x["level"], reverse=True)

        with open(filename, "w", newline='') as csvfile:
            fieldnames = ["name", "level"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in scores:
                writer.writerow(entry)
    
    def display_scores(self):
        filename = 'scores.csv'
        print(Fore.YELLOW + "\n🏆 Leaderboard:")
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader, 1):
                if i > 5:
                    break
                print(f"{i}. {row['name']} - Level {row['level']}")
                                    
    def restart(self):
        print("\nWelcome back!\n")
        self.level = 1
        self.length = 5
        
    def clear_screen(self):
        i = self.seconds
        time.sleep(1)
        while i != 0:
            print(i)
            time.sleep(1)
            i -= 1
        os.system('cls')
    
    def generate_code(self):
        characters = ''
        if self.number :
            characters = characters + ''.join(string.digits)
        if self.symbols :
            characters = ''.join(self.symbols)
        if self.smallcap :
            characters = characters + ''.join(string.ascii_lowercase)
        if self.largecap :
            characters = characters + ''.join(string.ascii_uppercase)
        code = ''.join(r.choice(characters) for i in range(self.length))
        return code
    
    def increment_level(self):
        self.level += 1
        
    def increment_length(self):
        self.length += 1
        
    def main(self):
        game1 = game()
        
        print(Fore.YELLOW + f"\n\t\t-|{'-' * 37}|-")
        print(Fore.YELLOW + f"\t\t |{' ' * 37}|")   
        print(Fore.YELLOW + "\t\t |WELCOME TO THE MEMORY CHALLENGE GAME |")
        print(Fore.YELLOW + "\t\t |  BE READY TO GET YOUR MIND BLOWN!   |")
        print(Fore.YELLOW + f"\t\t |{' ' * 17}🎮{' ' * 18}|")   
        print(Fore.YELLOW + f"\t\t-|{'-' * 37}|-\n")
        
        time.sleep(1)
        self.name = input("\nEnter your name: ")
        print(Back.BLACK + Fore.WHITE + f"Welcome to the game {self.name}💫")
        while True:
            time.sleep(1)
            print("\n\nGame Menu:")
            print('-' * 27)
            print("1. Play game in custom mode\n2. Play game in preset mode\n3. Check High scores\n4. Rules of the game\n5. Exit")
            user_input = input(">>> ")
        
            if user_input == '1':
                self.custom_mode()
            elif user_input == '2':
                self.preset_mode()
            elif user_input == '3':
                self.display_scores()
            elif user_input == '4':
                self.game_rules()
            elif user_input == '5':
                print(f"\nSee ya {self.name}! Bye!")
                break
            else:
                print("Error: Invalid input\nTry again")