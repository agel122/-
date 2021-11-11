class IntGuesser {
    constructor(startint, endint) {
        this.startint = startint;
        this.endint = endint;
        this.counter = [];
    }

    getRandomIntInclusive() {
        let min = Math.ceil(this.startint);
        let max = Math.floor(this.endint);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    guessInt_demo() {
        let intToGuess = this.getRandomIntInclusive();
        let max_limit = this.endint;
        let min_limit = this.startint;
        let user_guess = Math.floor((max_limit - min_limit) / 2);
        let counter = 1;
        console.log(`required number is ${intToGuess}. you try ${counter} time`);
        while (true) {
            if (user_guess === intToGuess) {
                console.log(`your guess is correct! required number was ${intToGuess}. you have got it in ${counter} times!`);
                this.counter.push(counter);
                break;
            } else if (intToGuess > user_guess) {
                console.log(`required number ${intToGuess} is bigger than ${user_guess}, next try!`);
                min_limit = user_guess;
            } else if (intToGuess < user_guess) {
                console.log(`required number ${intToGuess} is smaller than ${user_guess}, next try!`);
                max_limit = user_guess;
            }
            counter++;
            console.log(`${max_limit}, ${min_limit}, ${counter}`);
            user_guess = min_limit + Math.ceil((max_limit - min_limit) / 2);
        }
    }

    repeat_guess(repetitions) {
        for (let count = 1; count <= repetitions; count++) {
            this.guessInt_demo()
        }
        return Math.max(...this.counter);
    }
}


const demo1 = new IntGuesser(0, 10);
//demo1.guessInt_demo();
console.log(`${demo1.repeat_guess(10)} times as maximum you needed to find number`);



