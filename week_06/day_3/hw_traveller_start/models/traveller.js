const Traveller = function(journeys) {
  this.journeys = journeys;
};

Traveller.prototype.getJourneyStartLocations = function() {

};

Traveller.prototype.getJourneyEndLocations = function () {

};

Traveller.prototype.getJourneysByTransport = function (transport) {

};

Traveller.prototype.getJourneysByMinDistance = function (minDistance) {

};

Traveller.prototype.calculateTotalDistanceTravelled = function () {

};

Traveller.prototype.getUniqueModesOfTransport = function () {
  // we'll use the fact that an object's keys are unique to solve this
  // if we add a value under an existing key, it's a replacement not an addition...
  const modesOfTransport = {}
  this.journeys.forEach(journey => {
    // value ("found") here doesn't matter that much - we care about keys
    modesOfTransport[journey.transport] = "found";
  })
  return Object.keys(modesOfTransport);
};

module.exports = Traveller;
