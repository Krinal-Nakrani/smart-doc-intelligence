export default function SourceCard({ source, score, text }) {
  return (
    <div className="source-card">
      <div className="source-header">
        <span className="source-name">📄 {source}</span>
        <span className="source-score">Match: {(score * 100).toFixed(1)}%</span>
      </div>
      <p className="source-text">{text}</p>
    </div>
  );
}