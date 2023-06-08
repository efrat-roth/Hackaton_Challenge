import React, { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import BookResourcePage from "./BookResourcePage";
import MainPage from "./MainPage";
import TaskForm from "./tfyy";
import { getTasks } from "./apiClient";

export const DataContext = React.createContext({});

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then((tasksFromServer) => {
      console.log(tasksFromServer);
      setTasks(tasksFromServer);
    });
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
          <Route path="/bookResourcePage" element={<BookResourcePage />} />
          <Route path="/TaskForm" element={<TaskForm />} />

          
        </Routes>
      </BrowserRouter>
    </DataContext.Provider>
  );
}

export default App;