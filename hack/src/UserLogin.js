import React, { useState } from 'react';

const UserLogin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // כאן ניתן להוסיף את הלוגיקה שלך לטיפול בהתחברות המשתמש
  };

  return (
    <div>
      <h2>User Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>שם משתמש:</label>
          <input type="text" value={username} onChange={handleUsernameChange} />
        </div>
        <div>
          <label>סיסמא:</label>
          <input type="password" value={password} onChange={handlePasswordChange} />
        </div>
        <button type="submit">התחבר</button>
      </form>
    </div>
  );
};

export default UserLogin;