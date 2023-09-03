import { Link } from "react-router-dom";

export default function NavBar({ name, setName }) {
  let menu;

  const handleLogOut = () => {
    fetch("http://localhost:8000/api/logout", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
    });
    setName("");
  };

  if (name === "" || name === undefined || name === null) {
    menu = (
      <ul className="nav-links">
        <li>
          <Link to="/SignUp">Sign Up</Link>
        </li>
        <li>
          <Link to="/LogIn">Log In</Link>
        </li>
      </ul>
    );
  } else {
    menu = (
      <ul className="nav-links">
        <li>
          <span>{name}</span>
        </li>
        <li>
          <Link to="/LogIn" onClick={handleLogOut}>
            LogOut
          </Link>
        </li>
      </ul>
    );
  }

  return (
    <header className="hero-header">
      <Link to="/">
        <img className="the-logo-img" src="./the-logo.png" alt="logo" />
      </Link>
      <div>{menu}</div>
    </header>
  );
}
