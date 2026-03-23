import { useRef, useState } from "react";
import Loader from "./Loader";

export default function UploadZone({ onUpload, currentFile, loading }) {
  const inputRef = useRef(null);
  const [dragging, setDragging] = useState(false);
  const [status, setStatus] = useState(null);

  const handleFile = async (file) => {
    if (!file) return;
    const allowed = [".pdf", ".docx", ".txt"];
    const ext = "." + file.name.split(".").pop().toLowerCase();
    if (!allowed.includes(ext)) {
      setStatus({ type: "error", msg: "Only PDF, DOCX, and TXT files are supported." });
      return;
    }
    setStatus({ type: "info", msg: "Uploading & indexing..." });
    try {
      const data = await onUpload(file);
      setStatus({ type: "success", msg: `✅ Indexed ${data.chunks_indexed} chunks from "${data.filename}"` });
    } catch (e) {
      setStatus({ type: "error", msg: "Upload failed. Check your backend." });
    }
  };

  const onDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    handleFile(e.dataTransfer.files[0]);
  };

  return (
    <div className="upload-section">
      <div
        className={`upload-zone ${dragging ? "dragging" : ""} ${currentFile ? "has-file" : ""}`}
        onClick={() => inputRef.current.click()}
        onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
        onDragLeave={() => setDragging(false)}
        onDrop={onDrop}
      >
        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.docx,.txt"
          style={{ display: "none" }}
          onChange={(e) => handleFile(e.target.files[0])}
        />
        {loading ? (
          <Loader text="Indexing document..." />
        ) : currentFile ? (
          <>
            <span className="upload-icon">📄</span>
            <p className="upload-filename">{currentFile}</p>
            <p className="upload-hint">Click to upload a different file</p>
          </>
        ) : (
          <>
            <span className="upload-icon">☁️</span>
            <p className="upload-title">Drop your document here</p>
            <p className="upload-hint">PDF, DOCX, or TXT — CA papers, policy docs, reports</p>
            <button className="upload-btn">Browse File</button>
          </>
        )}
      </div>
      {status && (
        <p className={`upload-status status-${status.type}`}>{status.msg}</p>
      )}
    </div>
  );
}