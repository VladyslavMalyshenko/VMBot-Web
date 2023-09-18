import React from "react"
import "./Main.css"

import LogInButton from "../../Components/LogIn/LogIn.jsx"

//Source
import Introduce from "../../sources/photo1.png"

const Main = () => {

    return (
        <div className="main-page">
            <div className="Top">
                <div className="block-main">
                    <div className="info-main left white">
                        <h1 className="header">NEW COOL BOT!</h1>
                        <p className="descr">TRY OUR FEATURES FOR FREE! MANY FREE FUNCTIONALITY THAT’RE PAID IN OTHER BOTS!</p>
                        <LogInButton text="ADD TO SERVER"/>
                    </div>
                    <img src={Introduce}/>
                </div>
            </div>
            <div className="invited-servers-info white">
                <h1 className="header--mid">OUR BOT WAS INVITED FOR SERVER_COUNT SERVERS!</h1>
                <img className="server-logo-isi" src={Introduce} />
                <img className="server-logo-isi" src={Introduce} />
                <img className="server-logo-isi" src={Introduce} />
                <img className="server-logo-isi" src={Introduce} />
                <img className="server-logo-isi" src={Introduce} />
            </div>
            <div className="Mid">
                <div className="block-main">
                    <div className="info-main left white">
                        <h1 className="header--mid">Customizable Welcome Messages 👋</h1>
                        <p className="descr">Make your own custom invitations to make your server better!</p>
                        <LogInButton text="ADD TO SERVER"/>
                    </div>
                    <img src={Introduce}/>
                </div>
                <div className="block-main">
                    <div className="info-main left white">
                        <h1 className="header--mid">Customizable Welcome Messages 👋</h1>
                        <p className="descr">Make your own custom invitations to make your server better!</p>
                        <LogInButton text="ADD TO SERVER"/>
                    </div>
                    <img src={Introduce}/>
                </div>
            </div>
        </div>
    )
}

export default Main;