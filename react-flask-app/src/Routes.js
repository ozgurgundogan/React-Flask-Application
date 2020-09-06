import React from "react";import {
  Route,
  BrowserRouter as Router,
  Switch,
  Redirect,
} from "react-router-dom";

// import files
import BrokerListing from "./Pages/BrokerListing/BrokerListing";
import NotFound from "./Pages/NotFound/NotFound";
import Main from "./Pages/Main/Main"
import AddBroker from "./Pages/AddBroker/AddBroker";
import WhiteList from "./Pages/WhiteListListing/WhiteListListing";
import AgencyListing from "./Pages/AgencyListing/AgencyListing";
import AdminLogin from "./Pages/AdminLogin/AdminLogin";
import BlacklistBrokerListing from "./Pages/BlacklistBrokerListing/BlacklistBrokerListing";
// define routes

/**
*  It defines all possible routes.
* */

const Routes = (props) => (
  <Router {...props}>
    <Switch>
      <Route path="/broker/add">
        <AddBroker />
      </Route>
      <Route path="/admin/login">
        <AdminLogin />
      </Route>
      <Route path="/admin/agency/whitelist">
        <WhiteList />
      </Route>
      <Route path="/admin/agency/list">
        <AgencyListing />
      </Route>
      <Route path="/admin/broker/list">
          <BrokerListing />
      </Route>

      <Route path="/admin/broker/blacklisted">
          <BlacklistBrokerListing />
      </Route>

      <Route exact path="/">
        <Main />
      </Route>
      <Route path="*">
        <NotFound />
      </Route>
    </Switch>
  </Router>
);

export default Routes;