import { Button, Box } from "@mui/material";
import styled from "styled-components";
import React, { useState } from "react";
import { getOptimizatiom } from "./apiClient";
import { useNavigate } from "react-router-dom";


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
  height: 22vh;
`;

const App = () => {
  return (
    <MainScreen>
      <ImageContainer>
        <Image src="./savas.jpg" alt="Workspace Image" />
      </ImageContainer>
    </MainScreen>
  );
};

function MainPage() {
  const [employees, setEmployees] = useState([]);



  // function handleClickEvents() {
  //   // fetch("http://localhost:8000/employee/all")
  //   //   .then((rep) => rep.json())
  //   //   .then((jsons) => setEmployees(jsons));
  // }

  function schedulehandleClickEvents() {
    getOptimizatiom();
  }

  const navigate = useNavigate();

  return (
    <div>
      <img
        style={{ width: "100%", height: "22vh" }}
        src="./savas.jpg"
        alt="Workspace Image"
      />
      <h1 style={{ fontSize: "70px", color: "#00008B" }}>OptiSpace</h1>
      <div>
        <Box>
          <Button style={{ fontSize: "15px", gap: "4px", color: "#8B4513" }} onClick={()=>navigate(`/about`)}>
            About
          </Button>
          <Button style={{ fontSize: "15px", gap: "4px", color: "#8B4513" }} onClick={()=>navigate(`/bookResourcePage`)}>
            Book a Resource
          </Button>
          <Button
            style={{ fontSize: "15px", gap: "4px", color: "#8B4513" }}onClick={()=>navigate(`/schedule`)}>
            {/* // onClick={()=>handleClickEvents} */}
          
            Schedule
          </Button>
          <Button style={{ fontSize: "15px", gap: "4px", color: "#8B4513" }} onClick={()=>navigate(`/about`)}>
            New Employee
          </Button>
          <Button
            style={{ fontSize: "15px", gap: "4px", color: "#8B4513" }}
            onClick={schedulehandleClickEvents}
          >
            Create Board
          </Button>
        </Box>
        <div>{employees.map((employee, i) => <div key={i}>employ {i}-{employee.email}</div>)}</div>
      </div>
    </div>
  );
}

export default MainPage;
