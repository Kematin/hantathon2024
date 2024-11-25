// Use for import, change host and port if u need it

const API_HOST = "http://localhost";
const API_PORT = 8000;

import(`${API_HOST}:${API_PORT}/api/js`)
  .then((module) => {
    module.createListener();
  })
  .catch((error) => console.error("Error loading module:", error));
