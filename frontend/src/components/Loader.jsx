export default function Loader({ text = "Processing..." }) {
  return (
    <div className="loader-wrapper">
      <div className="spinner" />
      <p className="loader-text">{text}</p>
    </div>
  );
}