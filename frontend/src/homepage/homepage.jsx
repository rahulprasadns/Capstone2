import React, { useEffect, useState } from "react";
import Header from "./header";
import './homepage.css';
// eslint-disable-next-line no-unused-vars
import { Widget, addResponseMessage } from 'react-chat-widget';
import './chatbot.css';

const Homepage = () => {


    const [isOpen, setIsOpen] = useState(false)
    useEffect(() => {
        addResponseMessage('Welcome to travel booking chatbot!');
    }, []);

    const handleNewUserMessage = (newMessage) => {
        console.log(`New message incoming! ${newMessage}`);
        // Now send the message throught the backend API
    };

    return (
        <div className="homepage">
            <Header chatopen={isOpen} />
            <iframe
                title = 'chatbot'
                className = 'chatbot'
                allow="microphone;"
                width="350"
                height="430"
                src="https://console.dialogflow.com/api-client/demo/embedded/c542017f-1d3e-432d-af21-ec82ab6f6816">
            </iframe>

        </div>
    );
}

export default Homepage;