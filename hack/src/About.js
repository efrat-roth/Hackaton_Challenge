import React from 'react';
// import './About.css';

const About = () => {
  return (
    <div className="about-container">
      <h1 style={{ fontSize: '45px', color: '#FF69B4' }}>About OptiSpace</h1>
      <div className="image-container">
     
        <img style={{ width: '25%', height: '30vh' }} src="./cap.png" alt="About OptySpace" />
        
      </div>
      <button style={{ position: 'absolute', height: '20vh',bottom: '10px', right: '10px',color:'',padding: '10px' }}>HOME</button>
      
      <p className="description"  style={{ fontSize:"1.2rem" ,fontSize: '19px', color: '#00008B'}}>
      <span> Our company specializes in the development and implementation of planning and management tools for hybrid workplaces. </span>
       <span> Our tool allows employers to manage and optimally plan the schedules and arrivals to the offices, according to the information they enter about the office spaces, the employees and their preferences.</span>
      </p>
    </div>
  );
};

export default About;