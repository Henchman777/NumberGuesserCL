from random import randint


class NumberGuesser:
    def __init__(self):
        self.number = 0
        self.min = -1000000
        self.max = 1000000
        self.maxGame = 0
        self.minGame = 0
        self.attempts = 0
        self.highScore = 1000000000

    def startup(self):
        print('Welcome to random number guesser.')
        print('In this game, you will try to guess a random number between two numbers given clues.')
        print('The numbers you can choose as your max and min can be between -100,000 and 100,000.')
        print('If you want to quit, type in "exit" at any time.')

        while True:
            self.check_min_max()

            print('Please confirm if these are the numbers you want to choose. Y or N.')
            print('Min: {}, Max: {}.'.format(self.min, self.max), end=' ')
            cont = get_input()
            if cont == 'Y' or cont == 'y':
                break
        self.number = randint(self.min, self.max)
        self.minGame = self.min
        self.maxGame = self.max
        self.game_start()

    def get_min_max(self):
        while True:
            print('Please choose the minimum number:', end=' ')
            try:
                self.min = int(get_input())
                if self.check_valid_number(self.min):
                    break
            except ValueError:
                print('This is not a valid number')

        while True:
            print('Now choose the maximum number:', end=' ')
            try:
                self.max = int(get_input())
                if self.check_valid_number(self.max):
                    break
            except ValueError:
                print('This is not a valid number')

    def check_min_max(self):
        self.get_min_max()
        while True:
            if self.min >= self.max or self.max <= self.min:
                print('Minimum number is greater than maximum number. Please choose values again.')
                self.get_min_max()
            else:
                break

    def check_valid_number(self, num):
        if num < self.min or num > self.max:
            print('Number is outside of the range.')
            return False
        return True

    def change_min_max(self, number):
        if number > self.number:
            self.max = number - 1
        else:
            self.min = number + 1

    def game_start(self):
        userInput = 0
        print('Guess a number between {} and {}, inclusive.'.format(self.min, self.max), end=' ')
        while True:
            self.attempts += 1
            while True:
                try:
                    userInput = int(get_input())
                    if self.check_valid_number(userInput):
                        break
                    print('Guess a number between {} and {}, inclusive.'.format(self.min, self.max), end=' ')
                except ValueError:
                    print('This is not a valid number')
            if userInput == self.number:
                self.win()
                break
            else:
                self.change_min_max(userInput)
                print('Close!, The number is between {} and {}, inclusive.'.format(self.min, self.max), end=' ')

    def win(self):
        print('Congratulations, you guessed the number.')
        print('It took you {} attempts.'.format(self.attempts))
        if self.highScore > self.attempts:
            self.highScore = self.attempts
        print('Your high score is currently {}.'.format(self.highScore))
        print('Play again?. Y or N', end=' ')
        userInput = get_input()
        if userInput == 'Y' or userInput == 'y':
            self.max = self.maxGame
            self.min = self.minGame
            self.attempts = 0
            self.game_start()
        else:
            return


def get_input():
    userInput = input()
    if userInput == 'exit':
        exit(0)
    else:
        return userInput


if __name__ == '__main__':
    numGuesser = NumberGuesser()
    numGuesser.startup()
