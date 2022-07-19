import React, { useEffect, useState } from "react";
import Header from "./header";
import './homepage.css';
// eslint-disable-next-line no-unused-vars
import { Widget, addResponseMessage } from 'react-chat-widget';
import './chatbot.css';
import { AiFillRobot, AiFillCloseCircle } from 'react-icons/ai';

const Homepage = () => {


    const [isOpen, setIsOpen] = useState(false);
    const [hideChat, setHideChat] = useState('hide-chat');
    useEffect(() => {
        console.log(isOpen);
        if (isOpen) {
            setHideChat('show-chat');
        }
        else {
            setHideChat('hide-chat');
        }
    }, [isOpen]);

    return (
        <div className="homepage">
            <Header chatopen={isOpen} chatopenreturn = {(val) => setIsOpen(val)}/>
            <div
                className='chatbot'
            >
                <iframe
                    title='chatbot'
                    className= {`chatbot-iframe ${hideChat}`}
                    allow="microphone;"
                    width="350"
                    height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/c542017f-1d3e-432d-af21-ec82ab6f6816">
                </iframe>
                <button 
                    className="chat-button" 
                    onClick={() => 
                        {
                            console.log(isOpen);
                            setIsOpen(!isOpen);
                        }}
                    >
                    {!isOpen ? <AiFillRobot size='3em'/> : <AiFillCloseCircle size='3em'/> }
                </button>
            </div>

        </div>
    );
}

export default Homepage;