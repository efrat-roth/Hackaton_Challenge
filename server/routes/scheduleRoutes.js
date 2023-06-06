const express = require('express');
const router = express.Router();

// Sample data
let schedules = [];

// Create an schedule
router.post('/', (req, res) => {
    const schedule = req.body;
    schedules.push(schedule);
    res.status(201).json(schedule);
});

// Read all schedules
router.get('/', (req, res) => {
    res.json(schedules);
});

// Read a single schedule
router.get('/:id', (req, res) => {
    const id = req.params.id;
    const schedule = schedules.find((sce) => sce.id === id);
    if (schedule) {
        res.json(schedule);
    } else {
        res.status(404).json({ message: 'schedule not found' });
    }
});

// Update an schedule
router.put('/:id', (req, res) => {
    const id = req.params.id;
    const updatedSchedule = req.body;
    const index = schedules.findIndex((sce) => sce.id === id);
    if (index !== -1) {
        schedules[index] = updatedSchedule;
        res.json(updatedSchedule);
    } else {
        res.status(404).json({ message: 'schedule not found' });
    }
});

// Delete an schedule
router.delete('/:id', (req, res) => {
    const id = req.params.id;
    const index = schedules.findIndex((sce) => sce.id === id);
    if (index !== -1) {
        const deletedSchedule = schedules.splice(index, 1);
        res.json(deletedSchedule[0]);
    } else {
        res.status(404).json({ message: 'schedule not found' });
    }
});

module.exports = router;
