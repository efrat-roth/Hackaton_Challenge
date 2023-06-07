import React, { useState } from 'react';

function BookResourcePage() {
  const [selectedDay, setSelectedDay] = useState(null);
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');
  const [isFrontalEmployee, setIsFrontalEmployee] = useState(false);
  const [selectedOption, setSelectedOption] = useState('');

  const handleDayClick = (day) => {
    setSelectedDay(day);
  };

  const handleStartTimeChange = (event) => {
    setStartTime(event.target.value);
  };

  const handleEndTimeChange = (event) => {
    setEndTime(event.target.value);
  };

  const handleFrontalEmployeeChange = () => {
    setIsFrontalEmployee(!isFrontalEmployee);
  };

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <h1>Book Resource Page</h1>
      <div>
        Weekly Calendar:
        {/* Render the weekly calendar here */}
      </div>
      {selectedDay && (
        <div>
          <h2>{selectedDay}</h2>
          <div>
            <label>Start Time:</label>
            <input type="text" value={startTime} onChange={handleStartTimeChange} />
          </div>
          <div>
            <label>End Time:</label>
            <input type="text" value={endTime} onChange={handleEndTimeChange} />
          </div>
          <div>
            <label>
              <input type="checkbox" checked={isFrontalEmployee} onChange={handleFrontalEmployeeChange} />
              Frontal Employee
            </label>
          </div>
          <div>
            <label>Select an option:</label>
            <select value={selectedOption} onChange={handleOptionChange}>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
              <option value="D">D</option>
            </select>
          </div>
        </div>
      )}
    </div>
  );
}

export default BookResourcePage;