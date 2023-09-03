import { Link, Navigate } from "react-router-dom";
import "./registration.css";
import { useState } from "react";

export function Registration() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [redirect, setRedirect] = useState(false);

  const submit = async (e) => {
    e.preventDefault();

    await fetch("http://localhost:8000/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        email,
        password,
      }),
    });
    setRedirect(true);
    // const content = await response.json();
    // console.log(content);
  };

  if (redirect) {
    return <Navigate to="/LogIn" />;
  }

  return (
    <div className="Registration">
      <div className="registration-container">
        <div className="registration-img-box">
          <h1 className="savy">ScreenSavvy</h1>
          <img className="back-img" src="./login-image.jpg" alt="neon red" />
        </div>
        <div className="registration-form-box">
          <div className="unForm">
            <img className="the-logo" src="./the-logo.png" alt="logo" />
            <span className="login-text">REGISTRATION</span>
          </div>

          <form onSubmit={submit} action="POST">
            <div className="input-name">
              <input
                type="text"
                placeholder="Full Name"
                required
                onChange={(e) => setName(e.target.value)}
              />
            </div>
            <div className="input-email">
              <input
                type="email"
                placeholder="Email"
                required
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="input-password">
              <input
                type="password"
                placeholder="Password"
                required
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <button className="btn">Create Account</button>
            <div className="account-already">
              <span className="yes-account" href="#">
                Already have an account?
              </span>
              <Link className="signin" to="/LogIn">
                Sign In
              </Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
