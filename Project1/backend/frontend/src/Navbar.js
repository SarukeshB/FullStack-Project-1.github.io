import React from 'react'
import "./Navbar.css";

const Navbar = () => {
    return (
        <nav id="navbar" class="nav">
        <ul>
            <li>
                <a href="aboutme.html">About Me</a>
            </li>
            <li>
                <a href="cv.pdf" target="_blank">resume</a>
            </li>
            <li>
                <a href="contact.html">Contact</a>
            </li>
        </ul>
    </nav>
    )

}


export default Navbar