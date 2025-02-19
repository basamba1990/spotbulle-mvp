import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("http://localhost:5000/upload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    setResult(response.data);
  };

  return (
    <div className="App">
      <h1>Spot Bulle</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept="video/*" />
        <button type="submit">Uploader</button>
      </form>
      {result && (
        <div>
          <h2>Résultats</h2>
          <p><strong>Transcription :</strong> {result.transcription}</p>
          <p><strong>Analyse :</strong> {result.analysis.tone}</p>
          <p><strong>Suggestions :</strong> {result.analysis.vocab_suggestions}</p>
        </div>
      )}
    </div>
  );
}

export default App;
