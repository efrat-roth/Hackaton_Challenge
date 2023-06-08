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
  height: 100%;
  object-fit: cover;
`;

const App = () => {
  return (
    <MainScreen>
      <ImageContainer>
        <Image src="D:\שנה ב\סמסטר ב\האקתון\Hackaton_Challenge\hack\public\oppo_headquarters_bjarke_ingels_1.jpg" alt="Your Image" />
      </ImageContainer>
    </MainScreen>
  );
};


function MainPage() {
  return (
    <div>
      <img src="D:\שנה ב\סמסטר ב\האקתון\Hackaton_Challenge\hack\public\oppo_headquarters_bjarke_ingels_1.jpg" alt="Workspace Image" />
      <h1 style={{ fontSize: '70px', color: '#8B008B' }}>The Spacetimize</h1>
      <div>
        <Box>
          <Button>About</Button>
          <Button>Book a Resource</Button>
          <Button>Check In/Check Out</Button>
          <Button>Events</Button>
          
        </Box>
      </div>
    </div>
  );
}


export default MainPage;
