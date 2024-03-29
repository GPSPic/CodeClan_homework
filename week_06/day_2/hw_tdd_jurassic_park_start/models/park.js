const Park = function (name, ticketPrice, dinosaurCollection) {
    this.name = name
    this.ticketPrice = ticketPrice
    this.dinosaurCollection = dinosaurCollection
}

Park.prototype.addDinosaur = function (dinosaur) {
    this.dinosaurCollection.push(dinosaur);
};

Park.prototype.removeDinosaur = function (dinosaur) {
    const indexOfDinosaur = this.dinosaurCollection.indexOf(dinosaur);
    if (indexOfDinosaur > -1) { 
    this.dinosaurCollection.splice(indexOfDinosaur, 1);
    };
};

Park.prototype.mostPopularAttraction = function () {
    let mostPopular = [];
    for (const dinosaur of this.dinosaurCollection) {
        mostPopular.push(dinosaur.guestsAttractedPerDay);
    };
    const index = mostPopular.indexOf(Math.max(...mostPopular));
    const mostPopularDinosaur = this.dinosaurCollection[index];
    return mostPopularDinosaur;
};

Park.prototype.findDinosaursBySpecies = function (species) {
    const dinoMatchingSpecies = [];
    for (const dinosaur of this.dinosaurCollection) {
        if (species === dinosaur.species) {
            dinoMatchingSpecies.push(dinosaur);
        };
    };
    return dinoMatchingSpecies;
};

Park.prototype.totalVisitorsPerDay = function () {
    let total = 0;
    for (const dinosaur of this.dinosaurCollection) {
        total += dinosaur.guestsAttractedPerDay;
    };
    return total;
};

Park.prototype.totalVisitorsPerYear = function () {
    let yearlyTotal = 0;
    const dailyTotal = this.totalVisitorsPerDay()
    yearlyTotal = dailyTotal * 365;
    return yearlyTotal;
};

Park.prototype.yearlyRevenue = function () {
    let yearlyIncome = 0
    const yearlyVisits = this.totalVisitorsPerYear()
    yearlyIncome = yearlyVisits * this.ticketPrice
    return yearlyIncome
};

Park.prototype.removeAllDinoBySpecies = function (species) {
    const newDinoArray = [];
    for (const dinosaur of this.dinosaurCollection) {
        if (dinosaur.species !== species) {
            newDinoArray.push(dinosaur)
        };
    };
    this.dinosaurCollection = newDinoArray;
    // return this.dinosaurCollection
};

Park.prototype.numberOfDinosaursByDiet = function () {
    const dinosaursByDiet = {};
  
    for (const dinosaur of this.dinosaurs) {
      if (dinosaursByDiet[dinosaur.diet]) {
        dinosaursByDiet[dinosaur.diet] += 1;
      }
      else {
        dinosaursByDiet[dinosaur.diet] = 1;
      };
    };
  
    return dinosaursByDiet;
  };
  
module.exports = Park