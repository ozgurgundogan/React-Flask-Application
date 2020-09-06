import logo from "../../logo.png";
import React from "react";

/**
*  Navigation Component. It holds details of navigators menu that exists in every page.
* */

class NavigatorMenu extends React.Component{

    render() {
        console.log(this.props);
        return(<nav className="navbar navbar-expand-lg navbar-light bg-light">
        <img src={logo} className="logo" alt="logo"/>
        <a className="navbar-brand" href="#"></a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                {!this.props.adminloggedin &&
                <li className={this.props.home ? "nav-item active" : "nav-item"}>
                    <a className="nav-link" href="/">Home</a>
                </li>
                }
                {!this.props.adminloggedin &&
                <li className={this.props.brokers ? "nav-item active" : "nav-item"}>
                    <a className="nav-link" href="/broker/add">Brokers</a>
                </li>
                }

                {!this.props.adminloggedin &&
                    <li className={this.props.admin ?  "nav-item active" : "nav-item"}>
                        <a className="nav-link" href="/admin/login">Admin</a>
                    </li>
                }

                {
                    this.props.adminloggedin &&
                    <li className={this.props.brokerlist ? "nav-item active" : "nav-item"}>
                        <a className="nav-link" href="/admin/broker/list">Broker List</a>
                    </li>
                }




                {
                    this.props.adminloggedin &&
                    <li className={this.props.agencylist ? "nav-item active" : "nav-item"}>
                        <a className="nav-link" href="/admin/agency/list">Agency List</a>
                    </li>
                }
                {
                    this.props.adminloggedin &&
                        <li className={this.props.agencywhitelist ?  "nav-item active" : "nav-item"}>
                            <a className="nav-link" href="/admin/agency/whitelist">Agency White List</a>
                        </li>

                }

                {
                    this.props.adminloggedin &&
                    <li className={this.props.blackbrokerlist ? "nav-item active" : "nav-item"}>
                        <a className="nav-link" href="/admin/broker/blacklisted">Broker Black List</a>
                    </li>
                }

                {
                    this.props.adminloggedin &&
                        <li className="nav-item">
                            <a className="nav-link" href="/">Logout</a>
                        </li>

                }
            </ul>
        </div>
    </nav>
    );
    }
}



export default NavigatorMenu;