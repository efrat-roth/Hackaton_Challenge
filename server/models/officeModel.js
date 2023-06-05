const mongoose = require("mongoose");

const officeModelSchema = new mongoose.Schema({
    officeName: int,
    location: String,
    capacity:int,
    facilities:Facilities
})
const Facilities=[
    "headphones", 
    "Camera",
    "printer",
    "AnotherScreen",
    "WirelessMouse",
    "coffeeMachine",
    "selfChoose"
];

module.exports = mongoose.model('entries', officeModelSchema);