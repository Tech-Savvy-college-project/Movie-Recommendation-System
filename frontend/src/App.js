import { useEffect, useRef, useState } from "react";

import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { createBrowserRouter, Link, RouterProvider } from "react-router-dom";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Login } from "./Login";
import { Registration } from "./registration";
import { MovieDetails } from "./MovieDetails";

export default function App() {
  const [query, setQuery] = useState("");
  const { movies, isLoading, error } = useMovies(query);
  const [selectedId, setSelectedId] = useState(null);

  function handleSelectMovie(id) {
    setSelectedId((selectedId) => (id === selectedId ? null : id));
  }
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />

        <Routes>
          <Route
            path="/"
            element={
              <MovieList
                movies={movies}
                onSelectMovie={handleSelectMovie}
                query={query}
                setQuery={setQuery}
              />
            }
          />

          <Route
            path="/MovieDetails"
            element={<MovieDetails selectedId={selectedId} />}
          />

          <Route path="/LogIn" element={<Login />} />

          <Route path="/SignUp" element={<Registration />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

function NavBar() {
  return (
    <header className="hero-header">
      <Link to="/">
        <img className="the-logo-img" src="./the-logo.png" alt="logo" />
      </Link>
      <ul className="nav-links">
        <li>
          <Link to="/SignUp">Sign Up</Link>
        </li>
        <li>
          <Link to="/LogIn">Log In</Link>
        </li>
      </ul>
    </header>
  );
}

//dsdsds

//ccccc

//csdsds

export const KEY = "893b5d8f";
function useMovies(query) {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(
    function () {
      // callback?.();

      async function fetchMovies() {
        try {
          setIsLoading(true);
          setError("");

          const res = await fetch(
            `http://www.omdbapi.com/?apikey=${KEY}&s=${query}`
          );

          if (!res.ok)
            throw new Error("Something went wrong with fetching movies");

          const data = await res.json();
          if (data.Response === "False") throw new Error("Movie not found");

          setMovies(data.Search);
          setError("");
        } catch (err) {
          if (err.name !== "AbortError") {
            console.log(err.message);
            setError(err.message);
          }
        } finally {
          setIsLoading(false);
        }
      }

      if (query.length < 3) {
        setMovies([]);
        setError("");
        return;
      }

      fetchMovies();
    },
    [query]
  );

  return { movies, isLoading, error };
}

//ddwsfds

function MovieList({ movies, onSelectMovie, query, setQuery }) {
  return (
    <>
      <Search query={query} setQuery={setQuery} />
      <div className="movies-wrapper">
        {movies?.map((movie) => (
          <Movie
            movie={movie}
            key={movie.imdbID}
            onSelectMovie={onSelectMovie}
          />
        ))}
      </div>
    </>
  );
}

function Search({ query, setQuery }) {
  return (
    <div className="search-box">
      <input
        className="search"
        type="text"
        placeholder="Search movies..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
    </div>
  );
}

function Movie({ movie, onSelectMovie }) {
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
