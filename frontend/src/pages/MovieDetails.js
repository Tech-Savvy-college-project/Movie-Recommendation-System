import { useEffect, useState } from "react";
import * as React from "react";
import { KEY } from "../App";

export function MovieDetails({ selectedId }) {
  const [movie, setMovie] = useState({});

  const {
    Title: title,
    Year: year,
    Poster: poster,
    imdbRating,
    Plot: plot,
    Actors: actors,
    Director: director,
    Genre: genre,
    Writer: writer,
  } = movie;

  useEffect(
    function () {
      async function getMovieDetails() {
        const res = await fetch(
          `http://www.omdbapi.com/?apikey=${KEY}&i=${selectedId}`
        );
        const data = await res.json();
        setMovie(data);
      }
      getMovieDetails();
    },
    [selectedId]
  );

  return (
    <div className="details-section">
      <div className="movie-details">
        <div>
          <h1 className="movie-title">{title}</h1>
        </div>
        <div className="movie-desc">
          <p>{plot}</p>
        </div>
        <div className="genre">
          <span>{genre}</span>
        </div>
        <div className="other-details">
          <span>Director : {director}</span>
          <span>Writer : {writer}</span>
          <span>Starring : {actors}</span>
        </div>
      </div>
      <div className="movie-poster">
        <img src={poster} alt="movie-img" />
      </div>
    </div>
  );
}
