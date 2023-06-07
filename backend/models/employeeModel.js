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
    frontally:tuplefrontallySchema,
    hasPreferences:Boolean,

})
const Role=[
    "Manager", 
    "Employee",
    "TeamManager",
    "Receptionist",
    "SuperVisor",
    "Temporary"
];

const tuplefrontallySchema = new mongoose.Schema({
    fron: Boolean,
    id_room: Number,
  });





module.exports = mongoose.model('entries', employeeSchema);