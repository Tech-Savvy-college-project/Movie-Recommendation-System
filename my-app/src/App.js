import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="images/logo.png" alt="Logo" id = 'logo-header' />
        <nav>
          <ul className="nav-bar">
            <li><a href="#">Feature1</a></li>
            <li><a href="#">Feature2</a></li>
            <li><a href="#">Feature3</a></li>
            <li><a href="#">Feature4</a></li>
            <li><a href="#"><img src="images/Sample_User_Icon.png" alt="user" id = 'user-header'/></a></li>
          </ul>
        </nav>
      </header>
      <main>
      <div className="main-body">
        <div className="column">
          <div className="row-scrollbar">
              <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
            </div>
            <div className="row-scrollbar">
              <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
            </div>          
            <div className="row-scrollbar">
              <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
              <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
            </div> 
        </div>
        <div className="column">
          <h2>Movie Recommendation</h2>
          <input type="text" placeholder="Search" />
          <ul>
            <li>Image 1</li>
            <li>Image 2</li>
            <li>Image 3</li>
            {/* Add more image list items as needed */}
          </ul>
        </div>
        <div className="column">
        <div className="row-scrollbar">
            <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
          </div>
          <div className="row-scrollbar">
            <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
          </div>          
          <div className="row-scrollbar">
            <div className="value"><img src = "/images/1.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/2.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/3.png" className='scrollimg'/></div>
            <div className="value"><img src = "/images/4.png" className='scrollimg'/></div>
          </div>        
        </div>
      </div>
      </main>
      <footer>
        <p>&copy; {new Date().getFullYear()} Movie Recommendation. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
