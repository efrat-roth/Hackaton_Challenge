import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Schedule = () => {
  const [selectedValues, setSelectedValues] = useState({
    Sunday: 'x',
    Monday: 'x',
    Tuesday: 'x',
    Wednesday: 'x',
    Thursday: 'x',
    Friday: 'x'
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/employee/214430035').json();
      const data = response.data;
      const floors=data.floors

      const updatedSelectedValues = {
        Sunday: floors[0] === 1 ? 'v' : 'x',
        Monday: floors[1] === 1 ? 'v' : 'x',
        Tuesday: floors[2] === 1 ? 'v' : 'x',
        Wednesday: floors[3] === 1 ? 'v' : 'x',
        Thursday: floors[4] === 1 ? 'v' : 'x',
      };

      setSelectedValues(updatedSelectedValues);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleSelectChange = (day, value) => {
    setSelectedValues(prevState => ({
      ...prevState,
      [day]: value
    }));
  };

  return (
    <div className="schedule">
      <h1>Your weekly schedule:</h1>
      <div className="days">
        <div className="day">
          <span>Sunday</span>
          <select value={selectedValues.Sunday} onChange={(e) => handleSelectChange('Sunday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Monday</span>
          <select value={selectedValues.Monday} onChange={(e) => handleSelectChange('Monday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Tuesday</span>
          <select value={selectedValues.Tuesday} onChange={(e) => handleSelectChange('Tuesday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Wednesday</span>
          <select value={selectedValues.Wednesday} onChange={(e) => handleSelectChange('Wednesday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Thursday</span>
          <select value={selectedValues.Thursday} onChange={(e) => handleSelectChange('Thursday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Friday</span>
          <select value={selectedValues.Friday} onChange={(e) => handleSelectChange('Friday', e.target.value)}>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
      </div>
    </div>
  );
};

export default Schedule;
