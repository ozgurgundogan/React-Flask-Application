import React from "react";
import {
    Route,
    BrowserRouter as Router,
    Switch,
    Redirect,
} from "react-router-dom";

// import files
import BrokerList from "./Pages/BrokerList/BrokerList";
import NotFound from "./Pages/NotFound/NotFound";
import HomePage from "./Pages/HomePage/HomePage"
import AddBroker from "./Pages/BrokerAdd/BrokerAdd";
import WhiteList from "./Pages/AgencyWhiteList/AgencyWhiteList";
import AgencyList from "./Pages/AgencyList/AgencyList";
import AdminLogin from "./Pages/AdminLogin/AdminLogin";
import BrokerBlackList from "./Pages/BrokerBlackList/BrokerBlackList";
import BrokerAdd from "./Pages/BrokerAdd/BrokerAdd";
import AgencyWhiteList from "./Pages/AgencyWhiteList/AgencyWhiteList";
// define routes

/**
 *  It defines all possible routes.
 * */

const Routes = (props) => (
    <Router {...props}>
        <Switch>
            <Route path="/broker/add">
                <BrokerAdd/>
            </Route>
            <Route path="/admin/login">
                <AdminLogin/>
            </Route>
            <Route path="/admin/agency/whitelist">
                <AgencyWhiteList/>
            </Route>
            <Route path="/admin/agency/list">
                <AgencyList/>
            </Route>
            <Route path="/admin/broker/list">
                <BrokerList/>
            </Route>
            <Route path="/admin/broker/blacklist">
                <BrokerBlackList/>
            </Route>

            <Route exact path="/">
                <HomePage/>
            </Route>
            <Route path="*">
                <NotFound/>
            </Route>
        </Switch>
    </Router>
);

export default Routes;