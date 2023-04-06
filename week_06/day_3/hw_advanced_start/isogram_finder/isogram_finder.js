const IsogramFinder = function (word) {
    this.word = word.toLowerCase()
}

//SPLIT this.word into an array
//FOR every letter in this.word(array)
//IF any letter is counted more than once
//RETURN false

// IsogramFinder.prototype.sameLetterInArray = function () {
//     const wordArray = this.word.split('').sort();
//     return wordArray.
// }

IsogramFinder.prototype.isIsogram = function () {
    const sortedWordArray = this.word.split('').sort();
    return sortedWordArray.every((letter) => {
        const index = sortedWordArray.indexOf(letter);
        return sortedWordArray[index] !== sortedWordArray[index + 1];
    });
};

// IsogramFinder.prototype.isIsogram = function () {
//     const wordArray = this.word.split('');
//     return wordArray.every((letter) => {
//         return wordArray.find((repeatLetter) => {
//             const foundletter = wordArray.pop(letter)
//             const repeatedLetter = wordArray.pop(repeatLetter)
//             return foundletter === repeatedLetter
//         })
//     })
// };

module.exports = IsogramFinder;
