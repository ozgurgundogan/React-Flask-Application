import React, { useState } from "react";
import "./AdminLogin.css"

// import links for routing
import { Link } from "react-router-dom";
// form validation
import { useForm } from "react-hook-form";

// switching between routes
import { useHistory } from "react-router-dom";
import NavigatorMenu from "../NavigatorMenu/NavigatorMenu";

/**
*  Admin Login page. It asks password to be able to reach out dashboard view. If the password is correct, it submits the data and let the person see dashboard.
* */
const AdminLogin = () => {
    const { register, handleSubmit, errors } = useForm();
    const [message, setMessage] = useState();
    const history = useHistory();

    const onSubmit = (data, e) => {
        //StatContext.stat.adminLoggedIn=true;
        //this.toggleAdminLoggedIn();
        setMessage({
          data: "Login is in progress...",
          type: "alert-warning",
        });
        fetch('/admin-login', {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })
          .then((res) => res.json())
          .then((data) => {
            const hasError = "error" in data && data.error !== false;
            setMessage({
              data: data.message,
              type: hasError ? "alert-danger" : "alert-success",
            });
            !hasError && e.target.reset();
            !hasError && history.push("/admin/broker/list");
          });

    };

    return(
        <body>
        <NavigatorMenu admin="1"/>
      <div className='container container-fluid d-flex align-items-center justify-content-center'  >
        <div className="registrationFormContainer">
            {message && (
            <div
              className={`alert fade show d-flex ${message.type}`}
              role="alert"
            >
              {message.data}
              <span
                aria-hidden="true"
                className="ml-auto cursor-pointer"
                onClick={() => setMessage(null)}
              >
                &times;
              </span>
            </div>
          )}
          <fieldset className="border p-3 rounded">
            <legend className="registrationFormLegend border rounded p-1 text-center">
              Dashboard Login Form
            </legend>
            <form onSubmit={handleSubmit(onSubmit)} noValidate autoComplete="off">
              <div className="form-group">
                <label htmlFor="inputForPassword">Password for Admin</label>
                <span className="mandatory">*</span>
                <input
                    name="password"
                  type="password"
                  className="form-control"
                  id="inputForPassword"
                  placeholder="Enter password"
                  ref={register({
                  required: {
                    value: true,
                    message: "Please enter password",
                  },
                  minLength: {
                    value: 1,
                    message: "Minimum 6 characters are allowed",
                  },
                  maxLength: {
                    value: 255,
                    message: "Maximum 255 characters are allowed",
                  },
                })}
              />
              {errors.password && (
                <span className="errorMessage mandatory">
                  {errors.password.message}
                </span>
              )}

              </div>
              <div className="d-flex align-items-center justify-content-center">
                <button type="submit" className="btn btn-outline-primary">
                  Submit
                </button>
                <button className="btn btn-link">
                  <Link to="/">Cancel</Link>
                </button>
              </div>
            </form>
          </fieldset>
        </div>
      </div>
        </body>
    );
}
export default AdminLogin;