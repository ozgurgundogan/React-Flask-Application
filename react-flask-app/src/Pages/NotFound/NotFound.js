import React from "react";
import "./NotFound.css";

/**
 *  Not Found Page. It renders deafult not found page when route does not exists.
 * */
class NotFound extends React.Component {
    componentDidMount() {
        const script = document.createElement("script");
        script.src = "https://kit.fontawesome.com/4b9ba14b0f.js";
        script.async = true;
        script.onload = () => {
        };
        document.body.appendChild(script);
    }

    render() {
        return (
            <body>
            <div className="mainbox">
                <div className="err">4</div>
                <i className="far fa-question-circle fa-spin"></i>
                <div className="err2">4</div>
                <div className="msg">Probably You Lost ! <p>Let's go <a href="./">home</a> and try from there.</p></div>
            </div>
            </body>
        );
    }

}

export default NotFound;