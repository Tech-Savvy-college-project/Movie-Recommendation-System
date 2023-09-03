import { Link, Navigate } from "react-router-dom";
import "./login.css";
import { useState } from "react";

export function Login(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [redirect, setRedirect] = useState(false);

  const submit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:8000/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        email,
        password,
      }),
    });

    const content = await response.json();
    console.log(content);

    content.jwt ? setRedirect(true) : setRedirect(false);
    props.setName(content.name);
  };

  if (redirect) {
    return <Navigate to="/" />;
  }

  return (
    <div className="Login">
      <div className="login-container">
        <div className="login-img-box">
          <h1 className="savy">ScreenSavvy</h1>
          <img className="back-img" src="./login-image.jpg" alt="neon red" />
        </div>
        <div className="login-form-box">
          <div className="unForm">
            <img className="the-logo" src="./the-logo.png" alt="logo" />
            <span className="login-text">LOGIN</span>
          </div>

          <form action="POST" onSubmit={submit}>
            <div className="input-box">
              <input type="email" placeholder="Email" required onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="input-box">
              <input type="password" placeholder="Password" required onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <div className="forgor">
              <a className="forgotPassword" href="#">
                Forgot Password?
              </a>
            </div>
            <button type="submit" className="btn">
              LOGIN
            </button>
            <div className="account-xaina">
              <span className="no-account" href="#">
                Don't have an account?
              </span>
              <Link className="signup" to="/SignUp">
                Sign Up
              </Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
