const mongoose = require("mongoose");

const officeModelSchema = new mongoose.Schema({
    officeId:int,
    officeName: String,
    location: String,
    floor:int,
    capacity:int,
    
})


module.exports = mongoose.model('entries', officeModelSchema);