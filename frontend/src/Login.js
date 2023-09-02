import "./login.css";

export function Login() {
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
          <form action="#">
            <div className="input-box">
              <input type="text" placeholder="Username" required />
            </div>
            <div className="input-box">
              <input type="password" placeholder="Password" required />
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
              <a className="no-account" href="#">
                Don't have an account?
              </a>
              <a className="signup" href="#">
                Sign Up
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
