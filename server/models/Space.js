const mongoose = require("mongoose");

const spaceSchema = new mongoose.Schema({
   id:int,
   offices:[int],
   location:String,
   floors:int,
   description:String,
})
module.exports = mongoose.model('entries', spacesSchema);