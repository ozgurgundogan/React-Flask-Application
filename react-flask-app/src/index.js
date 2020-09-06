import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
// import routes
import Routes from "./Routes";
//import bootstrap
import "bootstrap/dist/css/bootstrap.css";

ReactDOM.render(<Routes />, document.getElementById("root"));

serviceWorker.unregister();
