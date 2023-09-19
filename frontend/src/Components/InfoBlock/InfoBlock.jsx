import React from "react"

import "./InfoBlock.css"

//Components and Utils
import LogInButton from "../LogIn/LogIn.jsx"
import { formatDescription } from "../../utils/description_formator"

//Template of the blocks on main page
const InfoBlock = ({
    image,
    imageName,
    imageSideRight = true,
    header,
    headerEmoji,
    headerClass = 'header--mid',
    description
    }) => {

    let descriptionDevided = []
    descriptionDevided = formatDescription(description)

    return (
        <div className="block-main up--anim">
            { !imageSideRight &&  <img alt={imageName} src={image}/> }
            <div className={`info-main ${imageSideRight ? 'left' : 'right'} white`}>
                <h1 className={headerClass}>{!imageSideRight && headerEmoji}{header}{imageSideRight && headerEmoji}</h1>
                <div>
                    {
                    descriptionDevided.map((element, index) => (
                        <p key={index} className="descr">{element}</p>
                    ))
                    }
                </div>
                <LogInButton text="ADD TO SERVER"/>
            </div>
            { imageSideRight &&  <img alt={imageName} src={image}/> }
        </div>
    )
}

export default InfoBlock;