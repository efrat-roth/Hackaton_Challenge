// here we set the model of the data from the DB

const mongoose = require("mongoose");

const employeeSchema = new mongoose.Schema({
    id:int,
    first_name : String,
    last_name: String,
    role: Role,
    department: String,
    email: String,
    phone_number:String,
    start_date:Date,
    tags:String,
    frontally: Boolean,
    preferences:preferencesModel

})
const Role=[
    "Manager", 
    "Employee",
    "TeamManager",
    "Receptionist",
    "SuperVisor",
    "Temporary"
];


module.exports = mongoose.model('entries', employeeSchema);