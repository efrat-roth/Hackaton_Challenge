const express = require('express');
const router = express.Router();

// Sample data
let employees = [];

// Create an employee
router.post('/', (req, res) => {
    const employee = req.body;
    employees.push(employee);
    res.status(201).json(employee);
});

// Read all employees
router.get('/', (req, res) => {
    res.json(employees);
});

// Read a single employee
router.get('/:id', (req, res) => {
    const id = req.params.id;
    const employee = employees.find((emp) => emp.id === id);
    if (employee) {
        res.json(employee);
    } else {
        res.status(404).json({ message: 'Employee not found' });
    }
});

// Update an employee
router.put('/:id', (req, res) => {
    const id = req.params.id;
    const updatedEmployee = req.body;
    const index = employees.findIndex((emp) => emp.id === id);
    if (index !== -1) {
        employees[index] = updatedEmployee;
        res.json(updatedEmployee);
    } else {
        res.status(404).json({ message: 'Employee not found' });
    }
});

// Delete an employee
router.delete('/:id', (req, res) => {
    const id = req.params.id;
    const index = employees.findIndex((emp) => emp.id === id);
    if (index !== -1) {
        const deletedEmployee = employees.splice(index, 1);
        res.json(deletedEmployee[0]);
    } else {
        res.status(404).json({ message: 'Employee not found' });
    }
});

module.exports = router;
