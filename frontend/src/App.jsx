import { useState } from "react";
import { useRAG } from "./hooks/useRAG";
import UploadZone from "./components/UploadZone";
import ChatInterface from "./components/ChatInterface";
import SourceCard from "./components/SourceCard";

export default function App() {
  const { uploadFile, askQuestion, filename, answer, sources, loading } = useRAG();

  return (
    <div className="app">
      <header>
        <h1>📚 Smart Doc Intelligence</h1>
        <p>Built for CA Exam Papers & Indian Government Policy Documents</p>
      </header>

      <UploadZone onUpload={uploadFile} currentFile={filename} loading={loading} />

      {filename && (
        <ChatInterface onAsk={askQuestion} loading={loading} />
      )}

      {answer && (
        <div className="answer-section">
          <h3>Answer</h3>
          <p>{answer}</p>
          <h4>Sources</h4>
          {sources.map((s, i) => <SourceCard key={i} {...s} />)}
        </div>
      )}
    </div>
  );
}