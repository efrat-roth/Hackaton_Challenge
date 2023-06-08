import React from 'react';
// import './About.css';

const About = () => {
  return (
    <div className="about-container">
      <h1>About OptySpace</h1>
      <div className="image-container">
     
        <img style={{ width: '25%', height: '30vh' }} src="./cap.png" alt="About OptySpace" />
        
      </div>
      <button style={{ position: 'absolute', height: '20vh',bottom: '10px', right: '10px',color:'',padding: '10px' }}>HOME</button>
      
      <p className="description"  style={{ fontSize:"1.2rem" }}>
        <span>  חברתנו מתמחה בפיתוח וישום כלי תכנון וניהול למקומות עבודה היברידיים. </span>
      <span>  הכלי שלנו מאפשר למעסיקים לנהל ולתכנן בצורה מיטבית את לוחות הזמנים וההגעות למשרדים, בהתאם למידע שהם מזינים על שטחי המשרדים, העובדים והעדפותיהם.</span>
      </p>
    </div>
  );
};

export default About;