import { useState } from "react";
import API from "../api/client";

export function useRAG() {
  const [sessionId, setSessionId] = useState(null);
  const [filename, setFilename] = useState(null);
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState(null);
  const [sources, setSources] = useState([]);

  const uploadFile = async (file) => {
    setLoading(true);
    const form = new FormData();
    form.append("file", file);
    const { data } = await API.post("/upload", form);
    setSessionId(data.session_id);
    setFilename(data.filename);
    setLoading(false);
    return data;
  };

  const askQuestion = async (question) => {
    if (!sessionId) return;
    setLoading(true);
    const { data } = await API.post("/query", { session_id: sessionId, question });
    setAnswer(data.answer);
    setSources(data.sources);
    setLoading(false);
  };

  return { uploadFile, askQuestion, sessionId, filename, answer, sources, loading };
}