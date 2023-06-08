import React from 'react';


const Schedule = () => {
  return (
    <div className="schedule">
      <h1>Your weekly schedule:</h1>
      <div className="days">
        <div className="day">
          <span>Sunday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Monday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Tuesday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Wednesday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Thursday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
        <div className="day">
          <span>Friday</span>
          <select>
            <option value="v">V</option>
            <option value="x">X</option>
          </select>
        </div>
      </div>
      <button className="confirm-button">Confirm</button>
      <button style={{ position: 'absolute', height: '20vh',bottom: '10px', right: '10px',color:'',padding: '10px' }}>HOME</button>
    </div>
  );
};

export default Schedule;