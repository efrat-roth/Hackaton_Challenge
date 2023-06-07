const express = require('express');
const router = express.Router();

// Sample data
let spaces = [];

// Create an schedule
router.post('/', (req, res) => {
    const space = req.body;
    spaces.push(space);
    res.status(201).json(space);
});

// Read all schedules
router.get('/', (req, res) => {
    res.json(spaces);
});

// Read a single schedule
router.get('/:id', (req, res) => {
    const id = req.params.id;
    const space = spaces.find((sce) => sce.id === id);
    if (space) {
        res.json(space);
    } else {
        res.status(404).json({ message: 'space not found' });
    }
});

// Update an schedule
router.put('/:id', (req, res) => {
    const id = req.params.id;
    const updatedSpace = req.body;
    const index = spaces.findIndex((sce) => sce.id === id);
    if (index !== -1) {
        spaces[index] = updatedSpace;
        res.json(updatedSpace);
    } else {
        res.status(404).json({ message: 'space not found' });
    }
});

// Delete an schedule
router.delete('/:id', (req, res) => {
    const id = req.params.id;
    const index = spaces.findIndex((sce) => sce.id === id);
    if (index !== -1) {
        const deletedSpace = spaces.splice(index, 1);
        res.json(deletedSpace[0]);
    } else {
        res.status(404).json({ message: 'space not found' });
    }
});

module.exports = router;
