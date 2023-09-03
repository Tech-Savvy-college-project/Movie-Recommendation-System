import { Link } from "react-router-dom";

export default function Movie({ movie, onSelectMovie }) {
  return (
    <div
      className="movies-container"
      onClick={() => onSelectMovie(movie.imdbID)}
    >
      <Link to="/MovieDetails" className="mini-title">
        {movie.Title}
      </Link>
      <img
        className="mini-poster"
        src={movie.Poster}
        alt={`${movie.Title} poster`}
      />
      <div className="movie-lil-detail">
        <span className="mini-year">
          Year : <span>{movie.Year}</span>
        </span>
        <span className="mini-type">
          Type : <span>{movie.Type}</span>
        </span>
      </div>
    </div>
  );
}
