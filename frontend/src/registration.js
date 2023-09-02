import "./registration.css";

export function Registration() {
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
          <form action="#">
            <div className="input-name">
              <input type="text" placeholder="First Name" />
              <input type="text" placeholder="Last Name" />
            </div>
            <div className="input-email">
              <input type="email" placeholder="Email" />
            </div>
            <div className="input-password">
              <input type="password" placeholder="Password" />
            </div>
            <button className="btn">Create Account</button>
            <div className="account-already">
              <a className="yes-account" href="#">
                Already have an account?
              </a>
              <a className="signin" href="#">
                Sign In
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
