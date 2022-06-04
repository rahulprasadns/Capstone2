import React, { useState, useEffect} from "react";
import io from "socket.io-client";
let endPoint = "http://1ocalhost:5000";
let socket = io.connect(`${endPoint}`);
const App = () => {
  // create state using hooks
  const [messages, setMessages] = useState ( ["Hello And Welcome"])
  const [message, setMessage] = useState("")

  useEffect(() => {
    getMessages()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [messages.length])

  const getMessages = () => {
    socket.on("message", msg => {
      setMessages([...messages, msg])
    })
  }

  const onChange = e => {
    setMessage(e.target.value)
  }

  const onClick = () => {
    if(message !== ""){
      socket.emit("message", message)
      setMessage("")
    } else {
      alert("Please enter a message")
    }
  }

  return (
    <div>
      <h1>Chat App</h1>
    
      {messages.length > 0 && messages.map((msg) => {(
        <div> <p> {msg} </p> </div>
      )}
      )}

      <input type="text" value={message} onChange={e => onChange(e)} />
      <button onClick={() => onClick()}>Send</button>

    </div>
  )
}

export default App;