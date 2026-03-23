import { useState } from "react";
import Loader from "./Loader";

export default function ChatInterface({ onAsk, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim() || loading) return;
    onAsk(question.trim());
    setQuestion("");
  };

  const handleKey = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const suggestions = [
    "What is the main objective of this document?",
    "Summarize the key points.",
    "What are the eligibility criteria mentioned?",
    "List all important dates or deadlines.",
  ];

  return (
    <div className="chat-section">
      <p className="chat-label">Ask anything about your document</p>

      <div className="suggestions">
        {suggestions.map((s, i) => (
          <button key={i} className="suggestion-chip" onClick={() => onAsk(s)}>
            {s}
          </button>
        ))}
      </div>

      <div className="chat-input-row">
        <textarea
          className="chat-input"
          rows={2}
          placeholder="e.g. What are the tax slabs mentioned in this document?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKey}
          disabled={loading}
        />
        <button
          className="ask-btn"
          onClick={handleSubmit}
          disabled={loading || !question.trim()}
        >
          {loading ? "..." : "Ask"}
        </button>
      </div>

      {loading && <Loader text="Searching document & generating answer..." />}
    </div>
  );
}