'''Реализация метода половинного деления для угадывания чисел в указанном диапазоне
Позволяет задать диапазон, увидеть переборы при включенном логировании,
посмотреть максимальное количество случившихся переборов в заданном диапазоне'''


import random, logging, math

logging.basicConfig(level=logging.DEBUG)


class IntGuesser:
    def __init__(self, startint, endint):
        self.startint = startint
        self.endint = endint
        self.counter = []

    def guessInt_demo(self):
        intToGuess = random.randint(self.startint, self.endint)
        #intToGuess = 10 #here you can specify exact value if needed
        max_limit = self.endint
        min_limit = self.startint
        user_guess = (max_limit-min_limit)//2
        counter = 1
        logging.debug("required number is {}. you try {} time".format(intToGuess, counter))
        while True:
            if user_guess == intToGuess:
                logging.debug("your guess is correct! required number was {}. you have got it in {} times!".format(intToGuess, counter))
                self.counter.append(counter)
                break
            else:
                if intToGuess > user_guess:
                    logging.debug("required number {} is bigger than {}, next try!".format(intToGuess, user_guess))
                    min_limit = user_guess
                if intToGuess < user_guess:
                    logging.debug("required number {} is smaller than {}, next try!".format(intToGuess, user_guess))
                    max_limit = user_guess
                counter+=1
                logging.debug("{},{},{}".format(max_limit, min_limit, counter))
                user_guess = min_limit + math.ceil((max_limit - min_limit)/2)

    def repeat_guess(self, repetitions):
        for i in range(repetitions):
            self.guessInt_demo()
        return max(self.counter)
    
    
if __name__=='__main__':
    demo1 = IntGuesser(0, 10)
    logging.debug("{} times as maximum you needed to find number".format(demo1.repeat_guess(10)))
    
   
    






    
    
    

