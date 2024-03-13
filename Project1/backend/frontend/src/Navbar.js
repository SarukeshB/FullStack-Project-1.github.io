import React from 'react'
import "./Navbar.css";
import axios from 'axios';

const Navbar = () => {
    const handleGetData = async () => {
        try {
            const response = await axios.get('http://localhost:8000/get-data/');
            const data = response.data;
            // Open a new window with the data
            const newWindow = window.open('', '_blank');
            newWindow.document.write(data);
        } catch (error) {
            console.error('Error fetching data:', error);
            alert('Failed to fetch data. Please try again.');
        }
    };
    const handleDownloadDocumentation = async () => {
        try {
            window.location.href = 'http://localhost:8000/documentation/downloads';
        } catch (error) {
            console.error('Error downloading documentation:', error);
            alert('Failed to download documentation. Please try again.');
        }
    };
    

    return (
        <nav id="navbar" class="nav">
        <ul>
            <li>
                <a href="https://www.sarukesh.com/aboutme.html">About Me</a>
            </li>
            <li>
                <button onClick={handleGetData}>Data</button>
            </li>
            <li>
            <button onClick={handleDownloadDocumentation}>Documentation</button>
            </li>
        </ul>
    </nav>
    );
};

export default Navbar;









