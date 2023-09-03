import { useState, useEffect } from "react";

import * as React from "react";

import { BrowserRouter, Route, Routes } from "react-router-dom";
import { MovieDetails } from "./pages/MovieDetails";
import { Login } from "./pages/Login";
import { Registration } from "./pages/registration";
import NavBar from "./pages/NavBar";
import useMovies from "./pages/userMovie";
import MovieList from "./pages/MovieList";
export const KEY = "893b5d8f";

export default function App() {
  const [query, setQuery] = useState("");
  const { movies, isLoading, error } = useMovies(query);
  const [selectedId, setSelectedId] = useState(null);
  const [name, setName] = useState("");

  useEffect(() => {
    (async () => {
      const response = await fetch("http://localhost:8000/api/user", {
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      const content = await response.json();
      setName(content.name);
    })();
  }, []);

  function handleSelectMovie(id) {
    setSelectedId((selectedId) => (id === selectedId ? null : id));
  }

  return (
    <div className="App">
      <BrowserRouter>
        <NavBar name={name} setName={setName} />

        <Routes>
          <Route
            path="/"
            exact
            element=<MovieList
              movies={movies}
              onSelectMovie={handleSelectMovie}
              query={query}
              setQuery={setQuery}
            />
          />
        </Routes>

        <Routes>
          <Route path="/Moviedetails" element={<MovieDetails selectedId={selectedId}/>} />
        </Routes>
        <Routes>
          <Route path="/LogIn" element={<Login setName={setName} />} />
        </Routes>
        <Routes>
          <Route path="/SignUp" element=<Registration /> />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
