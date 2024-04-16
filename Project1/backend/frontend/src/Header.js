import React, { useState } from 'react';
import './Header.css';
import axios from 'axios';
import image_png from './logo1.jpg';


const Header = () => {
  const [searchId, setSearchId] = useState('');
  const [taskDetails, setTaskDetails] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await axios.post('/search-task-details/', { id: searchId });
      setTaskDetails(response.data);
      setError(null);
    } catch (error) {
      console.error('Error searching task details:', error);
      setTaskDetails(null);
      setError('Task not found');
    }
  };
  function handleNameChange() {
    const name = ["Front-End", "Back-End", "FullStack"]
    const int = Math.floor(Math.random() * 3);
    return name[int]
  }

  return (
    <header>
      <div id='logo_pic'>
        <img className="profile-in-about" src={image_png} alt="" /><br />
        <h1>SARUKESH BOOMINATHAN</h1>
        <div>
          <p> A {handleNameChange()} Developer </p>

        </div>
      </div>
      <div id="search">
        <input
          className="search-bar"
          type="text"
          placeholder="Enter ID to search task details"
          value={searchId}
          onChange={(e) => setSearchId(e.target.value)}
        /><br></br>
        <button className='button-38' onClick={handleSearch}>Search</button>
      </div>
      {taskDetails && (
        <div className='task_detail' id="task-details">
          <h2>Task Details</h2>
          <p>ID: {taskDetails.id}</p>
          <p>Task: {taskDetails.title}</p> 
          <p>Due Date: {taskDetails.due_date}</p> 
        </div>
      )}
      {error && <p className="error-message">{error}</p>}
    </header>
  );
};

export default Header;
