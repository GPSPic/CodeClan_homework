const UpperCaser = function (words) {
    this.words = words
}

UpperCaser.prototype.toUpperCase = function () {
    return this.words.map((word) => (word.toUpperCase()));
    // return this.words.map((word) => {
    //     return word.toUpperCase()
    // });
};

module.exports = UpperCaser;
