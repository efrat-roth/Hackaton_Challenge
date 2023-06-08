const mongoose = require("mongoose");

mongoose.set('strictQuery', false);

// contact the DB
const dbConfig = (uri) => {
    mongoose.connect(uri)
    .then(() => console.log('Database Engaged'))
    .catch((error) => console.log(error))
}

const connection = mongoose.connection;

connection.once("open", ()=> console.log("Database Available"));

module.exports = dbConfig;
