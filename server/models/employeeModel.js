// here we set the model of the data from the DB

const mongoose = require("mongoose");

const employeeSchema = new mongoose.Schema({
    first_name : String,
    last_name: String
    // have to continue the fields

})

module.exports = mongoose.model('entries', employeeSchema);