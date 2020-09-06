import React from "react";
import "./HomePage.css";
import NavigatorMenu from "../NavigatorMenu/NavigatorMenu";

/**
 *  Index page. It renders index page with a couple of statistics.
 * */
class HomePage extends React.Component {

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
                <h1 className="jumbotron-heading">Welcome to Coalition Inc! </h1>
                <p className="lead text-muted">Coalition Inc. currently serves you
                    with {this.state.data.agencies} agencies and {this.state.data.brokers} brokers.</p>

                <a href="/broker/add" className="btn btn-primary my-2">Sign Up</a>

            </div>
            </body>
        );
    }
}


export default HomePage;