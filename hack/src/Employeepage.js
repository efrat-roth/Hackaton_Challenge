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
        ID:
          <input type="text" value={id} onChange={(e) => setId(e.target.value)} />
        </label>
        <br />
        <label>
        First name:
          <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
        </label>
        <br />
        <label>
        Last Name:
          <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
        </label>
        <br />
        <label>
        role:
          <select value={role} onChange={(e) => setRole(e.target.value)}>
            <option value="">Choose a role </option>
            <option value="Manager">Manager</option>
            <option value="Employee">Employee</option>
            <option value="TeamManager">TeamManager</option>
            <option value="Receptionist">Receptionist</option>
            <option value="Supervisor">Supervisor</option>
            <option value="Temporary">Temporary</option>
          </select>
        </label>
        <br />
        <label>
        department:
          <input type="text" value={department} onChange={(e) => setDepartment(e.target.value)} />
        </label>
        <br />
        <label>
        mail:
          <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
        Phone Number:
          <input type="text" value={phone} onChange={(e) => setPhone(e.target.value)} />
        </label>
        <br />
        <label>
        Start date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <br />
        <label>
        Skills:
          <input type="text" value={skills} onChange={(e) => setSkills(e.target.value)} />
        </label>
        <br />
        <label>
        frontal:
          <input type="checkbox" checked={isFrontend} onChange={(e) => setIsFrontend(e.target.checked)} />
        </label>
        <br />

        <button type="submit">Save</button>
        <button type="submit">Delete</button>
        <button type="submit">Update</button>
        <button style={{ position: 'absolute', height: '20vh',bottom: '10px', right: '10px',color:'',padding: '10px' }}>HOME</button>
      </form>
    </div>
  );
}

export default Employeepage;