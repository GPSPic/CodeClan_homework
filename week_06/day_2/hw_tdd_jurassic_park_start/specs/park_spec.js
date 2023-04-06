const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {
  let dinosaur1;
  let dinosaur2;
  let dinosaur3;
  let dinosaur4;
  let dinosaur5;
  let park;
  
  beforeEach(function () {
    dinosaur1 = new Dinosaur('t-rex', 'carnivore', 50);
    dinosaur2 = new Dinosaur('triceratops', 'herbivore', 40);
    dinosaur3 = new Dinosaur('ankylosaurus', 'herbivore', 30);
    dinosaur4 = new Dinosaur('t-rex', 'carnivore', 50);
    dinosaur5 = new Dinosaur('t-rex', 'carnivore', 50);
    park = new Park("Jurrasic Park", 20, [dinosaur1, dinosaur2]);
  })

  it('should have a name', function () {
    const actual = park.name
    assert.strictEqual(actual, "Jurrasic Park")
  });
  
  it('should have a ticket price', function () {
    const actual = park.ticketPrice
    assert.strictEqual(actual, 20)
  });
  
  it('should have a collection of dinosaurs', function () {
    const actual = park.dinosaurCollection
    assert.deepStrictEqual(actual, [dinosaur1, dinosaur2])
  });

  it('should be able to add a dinosaur to its collection', function () {
    park.addDinosaur(dinosaur3)
    const actual = park.dinosaurCollection.length
    assert.strictEqual(actual, 3)
  });

  it('should be able to remove a dinosaur from its collection', function () {
    park.removeDinosaur(dinosaur1)
    const actual = park.dinosaurCollection.length
    assert.strictEqual(actual, 1)
  });


  it('should be able to find the dinosaur that attracts the most visitors', function () {
    const actual = park.mostPopularAttraction()
    assert.deepStrictEqual(actual, dinosaur1)
  });

  it('should be able to find all dinosaurs of a particular species', function () {
    const actual = park.findDinosaursBySpecies('t-rex')
    assert.deepStrictEqual(actual, [dinosaur1])
  });

  it('should be able to calculate the total number of visitors per day', function () {
    const actual = park.totalVisitorsPerDay()
    assert.strictEqual(actual, 90)
  });

  it('should be able to calculate the total number of visitors per year', function () {
    const actual = park.totalVisitorsPerYear()
    assert.strictEqual(actual, 32850)
  });

  it('should be able to calculate total revenue for one year', function () {
    const actual = park.yearlyRevenue()
    assert.strictEqual(actual, 657000)
  });

  it('should be able to remove all dinosaurs of a particular species', function () {
    park.addDinosaur(dinosaur4)
    park.addDinosaur(dinosaur5)
    const actual = park.dinosaurCollection.length
    assert.strictEqual(actual, 4)
    park.removeAllDinoBySpecies('t-rex')
    const newActual = park.dinosaurCollection.length
    assert.strictEqual(newActual, 1)
  });
});
