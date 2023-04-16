import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import UploadImages from "./components/file-upload";

function App() {
  return (
    <div className="container">
      <h3>Food Classifier App</h3>
      <h4>Image Upload, Preview and Predict</h4>

      <div className="content">
        <UploadImages />
      </div>
    </div>
  );
}

export default App;