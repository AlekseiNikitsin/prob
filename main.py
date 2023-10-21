import string


class Alphabet:
    def __init__(self,lang,letters):# инициализатор класса Alphabet
        self.lang = lang #Динамическое свойство язык
        self.letters = list(letters)#Динамическое свойство буквы
    def print(self): print(f"Alphabet({self.lang}):{self.letters}")#метод выводящий вконсоль буквы алфавита
    def letters_num(self): return len(self.letters)# метод возвращающий колличество букв в алфавите
class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase) # приватное статическое свойство - колличество букв в алфавите
    def __init__(self,lang,letters): # инициализатор класса EngAlpabet
        super().__init__(lang,letters) # вызов родительского инициализатора
    @staticmethod
    def example(s):#статический метод возвращающий переданную строку 2 раза
        return s * 2
alphabet1 = Alphabet(lang='Generic',letters="ABC")
alphabet1.print()
print("number of letters:",alphabet1.letters_num())
eng_alpabet1 = EngAlphabet(lang="EN",letters=string.ascii_uppercase)
eng_alpabet1.print()
print("Numbers of letters in English alpabet",eng_alpabet1.letters_num())
print("Example:",EngAlphabet.example("Hello "))










