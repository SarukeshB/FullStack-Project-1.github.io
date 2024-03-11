import React from 'react'
import './Footer.css'

const Footer = () => {
const year = new Date();
  return (
  
  <footer>
    <p> Copyright &copy; {year.getFullYear()}, All Rights Reserved <span>Sarukesh</span> </p> 
  </footer>
  
  
  )
}

export default Footer