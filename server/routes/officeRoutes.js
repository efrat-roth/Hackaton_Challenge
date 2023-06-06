const express = require('express');
const router = express.Router();

// Sample data
let offices = [];

// Create an office
router.post('/', (req, res) => {
    const office = req.body;
    offices.push(office);
    res.status(201).json(office);
});

// Read all offices
router.get('/', (req, res) => {
    res.json(employees);
});

// Read a single office
router.get('/:id', (req, res) => {
    const id = req.params.id;
    const office = offices.find((of) => of.id === id);
    if (office) {
        res.json(office);
    } else {
        res.status(404).json({ message: 'Employee not found' });
    }
});

// Update an office
router.put('/:id', (req, res) => {
    const id = req.params.id;
    const updatedOffice = req.body;
    const index = offices.findIndex((of) => of.id === id);
    if (index !== -1) {
        offices[index] = updatedOffice;
        res.json(updatedOffice);
    } else {
        res.status(404).json({ message: 'office not found' });
    }
});

// Delete an office
router.delete('/:id', (req, res) => {
    const id = req.params.id;
    const index = offices.findIndex((of) => of.id === id);
    if (index !== -1) {
        const deletedOffice = offices.splice(index, 1);
        res.json(deletedOffice[0]);
    } else {
        res.status(404).json({ message: 'office not found' });
    }
});

module.exports = router;
