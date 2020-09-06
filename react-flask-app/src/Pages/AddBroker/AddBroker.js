import React, { useState } from "react";
import "./AddBroker.css";
// import links for routing
import { Link } from "react-router-dom";
// form validation
import { useForm } from "react-hook-form";
// switching between routes
import { useHistory } from "react-router-dom";
import NavigatorMenu from "../NavigatorMenu/NavigatorMenu";

/**
*  Broker Adding page. It renders broker registration form and submit the data to backend when submit button is clicked.
* */
const AddBroker = () => {
    const { register, handleSubmit, errors } = useForm();
    const [message, setMessage] = useState();

    const onSubmit = (data, e) => {
        setMessage({
          data: "Registration is in progress...",
          type: "alert-warning",
        });
        fetch('/add-broker', {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            const hasError = "error" in data && data.error !== false;
            setMessage({
              data: data.message,
              type: hasError ? "alert-danger" : "alert-success",
            });

            !hasError && e.target.reset();
          });
      };

    return(
        <body>
        <NavigatorMenu brokers="1"/>
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
              Registration Form
            </legend>
            <form onSubmit={handleSubmit(onSubmit)} noValidate autoComplete="off">
              <div className="form-group">
                <label htmlFor="inputForFirstName">Your First Name</label>
                <span className="mandatory">*</span>
                <input
                  id="inputForFirstName"
                  name="firstname"
                  type="text"
                  className="form-control"
                  aria-describedby="Enter your first name"
                  placeholder="Enter your first name"
                  ref={register({
                  required: {
                    value: true,
                    message: "Please enter your first name",
                  },
                  minLength: {
                    value: 1,
                    message: "Minimum 1 characters are allowed",
                  },
                  maxLength: {
                    value: 255,
                    message: "Maximum 255 characters are allowed",
                  },
                    })}
                  />
                  {errors.firstname && (
                    <span className="errorMessage mandatory">
                      {errors.firstname.message}
                    </span>
                  )}

              </div>
              <div className="form-group">
                <label htmlFor="inputForLastName">Your Last Name</label>
                <span className="mandatory">*</span>
                <input
                  id="inputForLastName"
                  name="lastname"
                  type="text"
                  className="form-control"
                  aria-describedby="Enter your last name"
                  placeholder="Enter your last name"
                  ref={register({
                  required: {
                    value: true,
                    message: "Please enter your last name",
                  },
                  minLength: {
                    value: 1,
                    message: "Minimum 1 characters are allowed",
                  },
                  maxLength: {
                    value: 255,
                    message: "Maximum 255 characters are allowed",
                  },
                    })}
                  />
                  {errors.lastname && (
                    <span className="errorMessage mandatory">
                      {errors.lastname.message}
                    </span>
                  )}

              </div>
              <div className="form-group">
                <label htmlFor="inputForAddress">Your Address</label>
                <span className="mandatory">*</span>
                <input
                  id="inputForAddress"
                  name="address"
                  type="text"
                  className="form-control"
                  aria-describedby="Enter your address"
                  placeholder="Enter your last address"
                  ref={register({
                  required: {
                    value: true,
                    message: "Please enter your address",
                  },
                  minLength: {
                    value: 6,
                    message: "Minimum 6 characters are allowed",
                  },
                  maxLength: {
                    value: 255,
                    message: "Maximum 255 characters are allowed",
                  },
                    })}
                  />
                  {errors.address && (
                    <span className="errorMessage mandatory">
                      {errors.address.message}
                    </span>
                  )}

              </div>

                <div className="form-group">
                <label htmlFor="inputForEmail">Email address</label>
                <span className="mandatory">*</span>
                <input
                  id="inputForEmail"
                  name="email"
                  type="email"
                  className="form-control"
                  aria-describedby="Enter email address"
                  placeholder="Enter email address"
                  ref={register({
                    required: {
                      value: true,
                      message: "Please enter your email address",
                    },
                    pattern: {
                      value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                      message: "Enter a valid email address",
                    },
                    minLength: {
                      value: 6,
                      message: "Minimum 6 characters are allowed",
                    },
                    maxLength: {
                      value: 255,
                      message: "Maximum 255 characters are allowed",
                    },
                    })}
                />
                {errors.email && (
                  <span className="errorMessage mandatory">
                    {errors.email.message}
                  </span>
                )}
              </div>

              <div className="form-group">
                <label htmlFor="inputForPassword">Password</label>
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
                    value: 6,
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
export default AddBroker;