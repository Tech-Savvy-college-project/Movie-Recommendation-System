export default function Search({ query, setQuery }) {
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
