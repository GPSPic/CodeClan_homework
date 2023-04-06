const IsogramFinder = function (word) {
    this.word = word
}

//SPLIT this.word into an array
//FOR every letter in this.word(array)
//IF any letter is counted more than once
//RETURN false

// IsogramFinder.prototype.sameLetterInArray = function () {
//     const wordArray = this.word.split('').sort();
//     return wordArray.
// }

// IsogramFinder.prototype.isIsogram = function () {
//     const wordArray = this.word.split('');
//     const sortedWordArray = wordArray.sort();
//     return sortedWordArray.every((letter) => {
//         const index = wordArray.indexOf(letter);
//         if (index > 0) {
//         return wordArray[index].toLowerCase() !== wordArray[index - 1].toLowerCase();
//         };
//     });
// };

IsogramFinder.prototype.isIsogram = function () {
    const wordArray = this.word.split('');
    return wordArray.every((letter) => {
        return wordArray.find((repeatLetter) => {
            const foundletter = wordArray.pop(letter)
            const repeatedLetter = wordArray.pop(repeatLetter)
            return foundletter === repeatedLetter
        })
    })
};

module.exports = IsogramFinder;
