import React from "react";
import "./LogIn.css"

//Sources
import DiscordLogo from "../../sources/discord_logo.png"

const LogInButton = ({text}) => {
    return(
        <a href="/" className="Log-In">
            <img alt="VMBot" src={DiscordLogo} />
            <p>{text}</p>
        </a>
    )
}

export default LogInButton;