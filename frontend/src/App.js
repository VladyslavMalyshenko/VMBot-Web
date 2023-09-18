import React from "react";
import {BrowserRouter, Routes, Route} from 'react-router-dom'

//Components Import
import Navbar from "./Components/Navbar/Navbar";

//Pages Import
import Main from "./Pages/Main/Main.jsx";

const App = () => {
  return (
    <div className="App">
      <Navbar />
        <Routes>
          <Route path="/" element={<Main />}></Route>
        </Routes>
    </div>
  );
}

export default App;
