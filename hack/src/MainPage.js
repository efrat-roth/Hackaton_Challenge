import {Button,Box} from "@mui/material";
import styled from 'styled-components';
import React from "react";


const MainScreen = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const ImageContainer = styled.div`
  width: 25%;
  height: 25vh;
`;

const Image = styled.img`
  width: 100%;
  height: 22vh
`;

const App = () => {
  return (
    <MainScreen>
      <ImageContainer>
        <Image src= "./savas.jpg" alt="Workspace Image"  />
        
      </ImageContainer>
    </MainScreen>
  );
};


function MainPage() {
  return (
    <div>
      <img style={{ width: '100%', height: '22vh' }} src="./savas.jpg" alt="Workspace Image"/>
      <h1 style={{ fontSize: '70px', color: '#00008B' }}>OptySpace</h1>
      <div>
        <Box>
          <Button style={{ fontSize: '15px', gap: '4px' , color: '#8B4513' }}>About</Button>
          <Button style={{ fontSize: '15px', gap: '4px' , color: '#8B4513' }}>Book a Resource</Button>
          <Button style={{ fontSize: '15px' ,gap: '4px', color: '#8B4513' }}>Contact Us</Button>
          <Button style={{ fontSize: '15px' ,gap: '4px', color: '#8B4513' }}>Events</Button>
          
        </Box>
      </div>
    </div>
  );
}


export default MainPage;
