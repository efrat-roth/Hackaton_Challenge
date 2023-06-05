const express = require("express");
const {searchResults} = require("../BL/searchBL")
const router = express.Router();

/*
CRUD - create, read, update, delete
REST API - אני בונה נתיב עבור כל פונקציה שאני מעוניין לקבל או למסור דרכה מידע 
*/

router.get('/:query', async (req, res) => {
    try {
        const results = await searchResults(req.params.query); // 1-5 - UNDEFINED 6 - VALUES
        res.json(results);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
})

module.exports = router;