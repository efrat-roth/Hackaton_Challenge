const express = require("express");
const cors = require('cors');
const dbConfig = require('./config/dbConfig');
const searchRoute = require("./routes/searchRoute")

require("dotenv").config();

const app = express(); // initialize the app
app.use(cors());
app.use(express.json());

const dbURI = process.env.MONGODB_CONNECT_STR;
dbConfig(dbURI);

app.use(express.urlencoded({ extended: true }));
app.use('/search', searchRoute);


app.listen(4000, () => console.log("Listening on port 4000"));