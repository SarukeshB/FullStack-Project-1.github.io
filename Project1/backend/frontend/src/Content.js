import React from 'react'
import './Content.css'

const Content = () => {

    function handleNameChange(){
        const name = ["Front-End", "Back-End", "FullStack"]
        const int = Math.floor(Math.random()*3);
        return name[int]
      }

  return(
    <div>
   <p> A {handleNameChange()} Developer </p>
   
   </div>

  ) 
  
}

export default Content