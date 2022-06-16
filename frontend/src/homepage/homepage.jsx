import React from "react";
import Header from "./header"
import './homepage.css';

class Homepage extends React.Component {
    render() {
        return (
            <div className="homepage">
                <Header />
            </div>
        );
    }
}

export default Homepage;