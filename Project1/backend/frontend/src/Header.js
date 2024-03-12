import React from 'react'
import './Header.css';
import image from './logo.jpg';
import image_png from './logo1.jpg';

const Header = () => {
  return(
    <header>
    <div id='logo_pic'>
      <img class="profile-in-about" src={image_png}
        alt="image"></img><br></br>
    
        <h1>SARUKESH BOOMINATHAN</h1>
    
    </div>
    </header>
  ) 
  
}

export default Header