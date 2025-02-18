import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css'
import App from './App.tsx'
import Script from './Script.tsx'
import Video from './Video.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/Script" element={<Script />} />
        <Route path="/Video" element={<Video />} />
      </Routes>
    </Router>
  </React.StrictMode>
);