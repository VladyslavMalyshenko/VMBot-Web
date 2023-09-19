import React, {useEffect} from "react"
import "./Main.css"


//Components and utils
import InfoBlock from "../../Components/InfoBlock/InfoBlock"
import { onLoadUp } from "../../utils/onMainLoad"

//Source
import Introduce from "../../sources/photo1.png"

const Main = () => {
    onLoadUp(useEffect, '.up--anim', 'up_show')
    onLoadUp(useEffect, '.left--anim', 'left_show')
    const blocks = [
        {
            image: Introduce,
            imageName: "Introduce",
            imageSideRight: true,
            header: 'Customizable Welcome Messages',
            headerEmoji: '👋',
            description: 'Make your own custom invitations to make your server better!',
        },
        {
            image: Introduce,
            imageName: "Introduce",
            imageSideRight: false,
            header: 'Socials Notifications',
            headerEmoji: '🔔',
            description: 'Add your or someone’s channel to get notifications about new videos from this channel!',
        },
        {
            image: Introduce,
            imageName: "Introduce",
            imageSideRight: true,
            header: 'Discord Reaction Roles',
            headerEmoji: '🥰',
            description: 'Make roles on reaction click! It’s cool thing, isn’t it?',
        },
        {
            image: Introduce,
            imageName: "Introduce",
            imageSideRight: false,
            header: 'Cool user cards and level system!',
            headerEmoji: '🎴',
            description: 'Have fun with full customizable user cards, there’re many backgrounds and colors you can use for your chioce. Level system will complete it!',
        },
        {
            image: Introduce,
            imageName: "Introduce",
            imageSideRight: true,
            header: 'Polls for your discord server',
            headerEmoji: '🤩',
            description: 'Make polls with style😎\nChoose with reactions!',
        }
    ]
    return (
        <div className="main-page">
            <div className="Top">
                <InfoBlock
                image={Introduce}
                imageName={"Introduce"}
                imageSideRight={true}
                headerClass="header"
                header={'NEW COOL BOT!'}
                description={'TRY OUR FEATURES FOR FREE! MANY FREE FUNCTIONALITY THAT’RE PAID IN OTHER BOTS!'}
                />
            </div>
            <div className="invited-servers-info white">
                <h1 className="header--mid">OUR BOT WAS INVITED FOR SERVER_COUNT SERVERS!</h1>
                <img className="server-logo-isi left--anim" src={Introduce} />
                <img className="server-logo-isi left--anim" src={Introduce} />
                <img className="server-logo-isi left--anim" src={Introduce} />
                <img className="server-logo-isi left--anim" src={Introduce} />
                <img className="server-logo-isi left--anim" src={Introduce} />
            </div>
            <div className="Mid">
                {
                    blocks.map(block => (
                        <InfoBlock
                        image={block.image}
                        imageName={block.imageName}
                        imageSideRight={block.imageSideRight}
                        header={block.header}
                        headerEmoji={block.headerEmoji}
                        description={block.description}
                        />
                    ))
                }
            </div>
        </div>
    )
}

export default Main;