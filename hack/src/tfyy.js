  import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import { DataContext } from "./App";
import { updateEmployee } from "./apiClient";

function TaskForm() {
  let { id } = useParams();
  const [formValues, setFormValues] = React.useState({});
  const { tasks } = React.useContext(DataContext);
  const isEdit = !!id;

  useEffect(() => {
    if (!!id) {
      console.log("Edit task", id);
      const task = tasks.find((task) => task._id === id);
      if (task) {
        setFormValues(task);
      }
    }
  }, [id, tasks]);

  const handleEditTask = () => {
    console.log("Update employee", formValues);
    updateEmployee(formValues)
      .then((task) => {
        console.log(task);
      })
      .then(() => {
      });
  };


  return (
    <div>
      <div className="d-flex justify-content-start mt-5 ms-5">
        <h1>{isEdit ? "Edit Task" : "Create Task"}</h1>
      </div>
      <div className="p-5 ">
        <div className="my-3 row">
          <label className="col-1" htmlFor="title">
            Title
          </label>
          <input
            className="col-4"
            type="text"
            id="title"
            name="title"
            value={formValues?.fullName || ""}
            onChange={(e) =>
              setFormValues({ ...formValues, fullName: e.target.value })
            }
          />
        </div>
        <div className="my-3 row">
          <label className="col-1" htmlFor="description">
            Description
          </label>
          <input
            className="col-4"
            type="text"
            id="description"
            name="description"
            value={formValues?.id || ""}
            onChange={(e) =>
              setFormValues({ ...formValues, id: e.target.value })
            }
          />
        </div>
        <div className="col-4 d-flex justify-content-center">
          <button
            className=""
            onClick={ handleEditTask }
          >
             "Update Tas"
          </button>
        </div>
      </div>
    </div>
  );
}

export default TaskForm;