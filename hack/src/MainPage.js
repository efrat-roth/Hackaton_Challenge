import { Button } from '@mui/material';
import React from 'react';

function MainPage() {
  return (
    <div>
      <img src="C:\Users\שמתשמ\Desktop\abcd.jpg" alt="Workspace Image" />
      <h1>The Spacetimize</h1>
      <div>
      {/* <Button variant="text">Text</Button>
<Button variant="contained">Contained</Button>
<Button variant="outlined">Outlined</Button> */}
        <button>About</button>
        <button>Book a Resource</button>
        <button>Check In/Check Out</button>
        <button>Events</button>
      </div>
    </div>
  );
}

export default MainPage;