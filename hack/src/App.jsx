import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import BookResourcePage from "./BookResourcePage";
import MainPage from "./MainPage";
import TaskForm from "./tfyy";
import { getTasks } from "./apiClient";
import About from "./About";

export const DataContext = React.createContext({});

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // getTasks().then((tasksFromServer) => {
      console.log('tasksFromServer');
      // setTasks(tasksFromServer);
    // },[]);
  }, []);

  return (
    <DataContext.Provider
      value={{
        tasks: tasks,
      }}
    >
      <BrowserRouter>
        <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path='/about' element={<About />} />
        <Route path="/bookResourcePage" element={<bookResourcePage />} />
        <Route path="/about" element={<About />} />
{/*           
          <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/about" element={<About />} />
        <Route path="/bookResourcePage" element={<bookResourcePage />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router> */}


        </Routes>
      </BrowserRouter>
    </DataContext.Provider>
  );
}

export default App;