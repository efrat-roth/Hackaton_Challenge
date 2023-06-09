import React from 'react';
import { useNavigate } from "react-router-dom";


function BookResourcePage() {

  const navigate = useNavigate();



  return (
    <div
    className="my-container"
    style={{
      backgroundImage: 'url(./vie.png)',
      // backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      height: '10vh'

    }}
  >
<div className="book-resource-page">
      <h1 style={{ fontSize: '23px', gap: '4px' , color: '#8B4513',fontFamily:'Amasis MT Pro' }}>Mark the days you work from the office,</h1>
      <h1 style={{ fontSize: '23px', gap: '4px' , color: '#8B4513',fontFamily:'Amasis MT Pro' }}>we will try to fulfill your request:</h1>        
      <div className="checkbox-container">
        <div className="day-box">
          <input type="checkbox" id="sunday" />
          <label htmlFor="sunday">Sunday</label>
        </div>
        <div className="day-box">
          <input type="checkbox" id="monday" />
          <label htmlFor="monday">Monday</label>
        </div>
        <div className="day-box">
          <input type="checkbox" id="tuesday" />
          <label htmlFor="tuesday">Tuesday</label>
        </div>
        <div className="day-box">
          <input type="checkbox" id="wednesday" />
          <label htmlFor="wednesday">Wednesday</label>
        </div>
        <div className="day-box">
          <input type="checkbox" id="thursday" />
          <label htmlFor="thursday">Thursday</label>
        </div>
        <div className="day-box">
          <input type="checkbox" id="friday" />
          <label htmlFor="friday">Friday</label>
        </div>
      </div>
      <button style={{ fontSize: '15px' ,gap: '4px', color: '#8B4513' }}className="confirm-button">Confirm</button>
      <button style={{ position: 'absolute', height: '20vh',bottom: '10px', right: '10px',color:'',padding: '10px' } }onclick={()=>navigate('/')}>HOME</button>
    </div>


  </div>



    
  );
}

export default BookResourcePage;