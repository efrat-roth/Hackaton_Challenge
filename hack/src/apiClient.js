const SERVER_URL = "http://localhost:8000";

export const getOptimizatiom = () => {
  return fetch(`${SERVER_URL}/backend/BL/schedules/update_lists`).then((res) => res.json());
};

export const updateEmployee = (formsValue) => {
  console.log("updating");
  return fetch(`${SERVER_URL}/sced_arr/employee/214430035`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      floors: "[1,0,1,0,1]", //formsValue
    }),
  });
};

