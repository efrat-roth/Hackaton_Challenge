const mongoose = require("mongoose");
//const scheduleModel = require("./scheduleModel");

const scheduleSchema = new mongoose.Schema({
   id:int,
   office:officeModel,
   date:Date,
   starttime:Date,
   endTime:Date
})
module.exports = mongoose.model('entries', scheduleSchema);