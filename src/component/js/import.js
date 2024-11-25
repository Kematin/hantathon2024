// Use for import, change host and port if u need it

import("http://localhost:8000/api/js")
  .then((module) => {
    module.createListener();
  })
  .catch((error) => console.error("Error loading module:", error));
