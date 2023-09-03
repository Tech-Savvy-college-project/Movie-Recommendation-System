import Search from './Search'
import Movie from './Movie'

export default function MovieList({ movies, onSelectMovie, query, setQuery }) {
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


