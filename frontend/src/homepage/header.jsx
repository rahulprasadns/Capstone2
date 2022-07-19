import React from "react";
import './header.css';

const Header = ({chatopen, chatopenreturn}) => {

    return (
        <>
            <div className="header">
                <div className="toggle-button">
                    <p> Hello User   |</p>
                    <p> Normal User </p>
                    <input type="checkbox" id="switch" /><label for="switch">Toggle</label>
                    <p> Premium User </p>
                </div>
                <div className="inner-header">
                    <svg
                        className="logo"
                        baseProfile="tiny"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 500 500"
                        xmlSpace="preserve"
                    >
                        <path
                            fill="#fff"
                            d="M250.4.8C112.7.8 1 112.4 1 250.2c0 137.7 111.7 249.4 249.4 249.4s249.4-111.7 249.4-249.4C499.8 112.4 388.1.8 250.4.8zm133.4 325.5c-62 0-101.4-14.1-117.6-46.3-17.1-34.1-2.3-75.4 13.2-104.1-22.4 3-38.4 9.2-47.8 18.3-11.2 10.9-13.6 26.7-16.3 45-3.1 20.8-6.6 44.4-25.3 62.4-19.8 19.1-51.6 26.9-100.2 24.6l1.8-39.7c35.9 1.6 59.7-2.9 70.8-13.6 8.9-8.6 11.1-22.9 13.5-39.6 6.3-42 14.8-99.4 141.4-99.4h41L333 166c-12.6 16-45.4 68.2-31.2 96.2 9.2 18.3 41.5 25.6 91.2 24.2l1.1 39.8c-3.6 0-7 .1-10.3.1z"
                        />
                    </svg>
                    <h1>Virtual Travel Agent</h1>
                </div>

                <div>
                    <svg
                        className="waves"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlnsXlink="http://www.w3.org/1999/xlink"
                        viewBox="0 24 150 28"
                        preserveAspectRatio="none"
                        shape-rendering="auto"  >
                        <defs>
                            <path
                                id="a"
                                d="M-160 44c30 0 58-18 88-18s58 18 88 18 58-18 88-18 58 18 88 18v44h-352z"
                            />
                        </defs>
                        <g className="parallax">
                            <use xlinkHref="#a" x={48} fill="rgba(255,255,255,0.7" />
                            <use xlinkHref="#a" x={48} y={3} fill="rgba(255,255,255,0.5)" />
                            <use xlinkHref="#a" x={48} y={5} fill="rgba(255,255,255,0.3)" />
                            <use xlinkHref="#a" x={48} y={7} fill="#fff" />
                        </g>
                    </svg>
                </div>
            </div>
            <>
                <main class="page-content">
                    <div class="card">
                        <div class="content">
                            <h2 class="title">India</h2>
                            <p class="copy">Check out all of these gorgeous mountain trips with beautiful views of, you guessed it, the mountains</p>
                            <button onClick = {() => {chatopenreturn(true);}} class="btn">Book Now</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="content">
                            <h2 class="title">Brazil</h2>
                            <p class="copy">Plan your next beach trip with these fabulous destinations</p>
                            <button onClick = {() => {chatopenreturn(true);}} class="btn">Book Now</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="content">
                            <h2 class="title">Albania</h2>
                            <p class="copy">It's the desert you've always dreamed of</p>
                            <button onClick = {() => {chatopenreturn(true);}} class="btn">Book Now</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="content">
                            <h2 class="title">Explore The Galaxy</h2>
                            <p class="copy">Seriously, straight up, just blast off into outer space today</p>
                            <button onClick = {() => {chatopenreturn(true);}} class="btn">Book Now</button>
                        </div>
                    </div>
                </main>
            </>
            <div className="content1 flex">
                <h3>An app that changes travel and chat experience</h3>
            </div>
            <div className= {`content1 flex ${chatopen ? 'show-chat': 'hide-chat'}`}>
                <h4>{chatopen ? 'Chat is live' : ''}</h4>
            </div>
            <div className="App">
            </div>
        </>
    );
}

export default Header;