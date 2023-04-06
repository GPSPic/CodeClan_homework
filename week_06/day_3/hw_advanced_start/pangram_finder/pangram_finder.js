const PangramFinder = function (phrase) {
  this.alphabet = 'qwertyuiopasdfghjklzxcvbnm'.split('');
  this.phrase = phrase
}

// FOR every letter in the alphabet
// IF every letter is in this.phrase
// RETURN true

PangramFinder.prototype.isPangram = function () {
  const phraseArray = this.phrase.split('')
  return this.alphabet.every((alphabetLetter) => {
    return phraseArray.find((phraseLetter) => {
      return phraseLetter.toLowerCase() === alphabetLetter
    });
  });
};




module.exports = PangramFinder;
