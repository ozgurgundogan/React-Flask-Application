import React from "react";
import "./Main.css";
import NavigatorMenu from "../NavigatorMenu/NavigatorMenu";

/**
 *  Index page. It renders index page with a couple of statistics.
 * */
class Main extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            data: {},
        };
    }

    componentDidMount() {
        fetch('/get-counts')
            .then(response => response.json())
            .then(counts => {
                this.setState({data: counts});
                console.log(this.data);
            });

    }

    render() {
        return (
            <body>
            <NavigatorMenu home="1"/>

            <div className="container">
                <h1 className="jumbotron-heading">Are you still confident for your system security ? </h1>
                <p className="lead text-muted">Coalition Inc. currently serves you
                    with {this.state.data.agencies} agencies and {this.state.data.brokers} brokers.</p>

                <a href="/broker/add" className="btn btn-primary my-2">Are you a broker ?</a>
                <a href="#" className="btn btn-secondary my-2 custom-button">Are you a client ?</a>

            </div>
            </body>
        );
    }
}


export default Main;