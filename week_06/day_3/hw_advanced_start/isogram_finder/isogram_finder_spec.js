const assert = require('assert');
const IsogramFinder = require('./isogram_finder.js');

describe('IsogramFinder', function () {
  it('should be able to detect an isogram', function () {
    const isogramFinder = new IsogramFinder('subdermatoglyphic');
    assert.strictEqual(isogramFinder.isIsogram(), true);
  });

  it('should be able to detect a non-isogram', function () {
    const isogramFinder = new IsogramFinder('repeated');
    assert.strictEqual(isogramFinder.isIsogram(), false);
  });

  it('should be able to detect an isogram case insensitively', function () {
    const isogramFinder = new IsogramFinder('Uncopyrightable');
    assert.strictEqual(isogramFinder.isIsogram(), true);
  });

  it('should be able to detect a non-isogram case insensitively', function () {
    const isogramFinder = new IsogramFinder('NOtAnIsogram');
    assert.strictEqual(isogramFinder.isIsogram(), false);
  });
});

  // it('should be able to detect if 2 consecutives letters in an array are the same', function () {
  //   const consecutivesFinder = new IsogramFinder('blabla')
  //   assert.strictEqual(consecutivesFinder.sameLetterInArray(), true)
  // });