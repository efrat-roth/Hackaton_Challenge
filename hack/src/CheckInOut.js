import React, { useState } from 'react';
import './CheckInOut.css';

function CheckInOut() {
  const [isCheckedIn, setIsCheckedIn] = useState(false);

  const handleCheckIn = () => {
    setIsCheckedIn(true);
  };

  const handleCheckOut = () => {
    setIsCheckedIn(false);
  };

  return (
    <div className="check-in-out-container">
      <button className={`check-in-button ${isCheckedIn ? 'disabled' : ''}`} onClick={handleCheckIn}>
        Check In
      </button>
      <button className={`check-out-button ${!isCheckedIn ? 'disabled' : ''}`} onClick={handleCheckOut}>
        Check Out
      </button>
    </div>
  );
}

export default CheckInOut;