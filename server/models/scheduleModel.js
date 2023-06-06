const mongoose = require("mongoose");
//const scheduleModel = require("./scheduleModel");

const scheduleSchema = new mongoose.Schema({
   id:int,
   officeId:int,
   date:Date,
   starttime:Date,
   endTime:Date
})
module.exports = mongoose.model('entries', scheduleSchema);