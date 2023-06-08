import React, { useState } from 'react';

function Employeepage() {
  const [id, setId] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [role, setRole] = useState('');
  const [department, setDepartment] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [startDate, setStartDate] = useState('');
  const [skills, setSkills] = useState('');
  const [isFrontend, setIsFrontend] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
  };

  return (
    <div>
      <h1>Employee Page</h1>
      <form onSubmit={handleSubmit}>
        <label>
          תעודת זהות:
          <input type="text" value={id} onChange={(e) => setId(e.target.value)} />
        </label>
        <br />
        <label>
          שם פרטי:
          <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
        </label>
        <br />
        <label>
          שם משפחה:
          <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
        </label>
        <br />
        <label>
          תפקיד:
          <select value={role} onChange={(e) => setRole(e.target.value)}>
            <option value="">בחר תפקיד</option>
            <option value="Manager">מנהל</option>
            <option value="Employee">עובד</option>
            <option value="TeamManager">מנהל צוות</option>
            <option value="Receptionist">מקבל</option>
            <option value="Supervisor">מפקח</option>
            <option value="Temporary">זמני</option>
          </select>
        </label>
        <br />
        <label>
          מחלקה:
          <input type="text" value={department} onChange={(e) => setDepartment(e.target.value)} />
        </label>
        <br />
        <label>
          מייל:
          <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          מספר טלפון:
          <input type="text" value={phone} onChange={(e) => setPhone(e.target.value)} />
        </label>
        <br />
        <label>
          תאריך תחילת העבודה:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <br />
        <label>
          מיומנויות:
          <input type="text" value={skills} onChange={(e) => setSkills(e.target.value)} />
        </label>
        <br />
        <label>
          פרונטלי:
          <input type="checkbox" checked={isFrontend} onChange={(e) => setIsFrontend(e.target.checked)} />
        </label>
        <br />
        <button type="submit">שלח</button>
      </form>
    </div>
  );
}

export default Employeepage;