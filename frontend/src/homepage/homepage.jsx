import React, { useEffect } from "react";
import Header from "./header";
import './homepage.css';
import { Widget, addResponseMessage } from 'react-chat-widget';

const Homepage = () => {

    useEffect(() => {
        addResponseMessage('Welcome to this **awesome** chat!');
    }, []);

    const handleNewUserMessage = (newMessage) => {
        console.log(`New message incoming! ${newMessage}`);
        // Now send the message throught the backend API
    };

    return (
        <div className="homepage">
            <Header />
            <Widget
                handleNewUserMessage={handleNewUserMessage}
                profileAvatar={'https://i.imgur.com/7jH4Kve.png'}
                title="Hello User"
                subtitle="Welcome to Virtual Travel Agent chat bot"
            />
        </div>
    );
}

export default Homepage;