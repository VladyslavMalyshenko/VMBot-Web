import React from "react"
import "./Navbar.css"
import { Link } from "react-router-dom"

//Components
import LogInButton from "../LogIn/LogIn.jsx"

//Sources
import Logo from "../../sources/favicon.png"

const Navbar = () => {

    return (
        <div className="Navbar">
            <div className="nav-links">
                <div className="nav-logo">
                    <img alt="VMBot" src={Logo} />
                </div>
                <Link to={'/'}>Documentation</Link>
                <Link to={'/'}>Plugins</Link>
            </div>
            <LogInButton text="LOG IN VIA DISCORD"/>
        </div>
    )
}

export default Navbar;