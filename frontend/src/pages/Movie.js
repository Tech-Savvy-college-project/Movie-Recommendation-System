import { Link } from "react-router-dom";

export default function Movie({ movie, onSelectMovie }) {
  console.log(movie);

  return (
    <div
      className="box"
      onClick={() => onSelectMovie(movie.imdbID)}
    >
      <Link to="/MovieDetails">
        <div class="card">
          <div class="details">
            <div class="left">
              <p class="name">{movie.Title}</p>
              <div class="date_quality">
                <p class="quality">HD</p>
                <p class="date">{movie.Year}</p>
              </div>
              {/* <p class="category">Horror | Mystery | Thriller</p> */}

              <div class="info">
                <div class="rate">
                  <i class="fa-solid fa-star"></i>
                  <p>9.2</p>
                </div>
                <div class="time">
                  <i class="fa-solid fa-clock"></i>
                  <p>120min</p>
                </div>
              </div>
            </div>

            <div class="right">
              <i class="fa-solid fa-play"></i>
            </div>
          </div>
          <img src={movie.Poster} alt={`${movie.Title} poster`} srcset="" />
        </div>
      </Link>
    </div>
  );

  // return ( <div
  //     className="movies-container"
  //     onClick={() => onSelectMovie(movie.imdbID)}
  //   >
  //     <Link to="/MovieDetails" className="mini-title">
  //       {movie.Title}
  //     </Link>
  //     <img
  //       className="mini-poster"
  //       src={movie.Poster}
  //       alt={`${movie.Title} poster`}
  //     />
  //     <div className="movie-lil-detail">
  //       <span className="mini-year">
  //         Year : <span>{movie.Year}</span>
  //       </span>
  //       <span className="mini-type">
  //         Type : <span>{movie.Type}</span>
  //       </span>
  //     </div>
  //   </div>
  // );
}
