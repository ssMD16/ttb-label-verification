import { useState } from "react";
import { API_BASE_URL } from "./config";

function App() {
  const [singleResult, setSingleResult] = useState(null);
  const [batchJobId, setBatchJobId] = useState(null);
  const [batchResults, setBatchResults] = useState({});

  const uploadSingle = async (e) => {
    e.preventDefault();
    const file = e.target.single.files[0];
    const form = new FormData();
    form.append("image", file);

    const res = await fetch(`${API_BASE_URL}/image/process`, {
      method: "POST",
      body: form,
    });

    setSingleResult(await res.json());
  };

  const uploadBatch = async (e) => {
    e.preventDefault();
    const file = e.target.batch.files[0];
    const form = new FormData();
    form.append("zip_file", file);

    const res = await fetch(`${API_BASE_URL}/batch/process`, {
      method: "POST",
      body: form,
    });

    const data = await res.json();
    setBatchJobId(data.job_id);
    pollStatus(data.job_id);
  };

  const pollStatus = (jobId) => {
    const interval = setInterval(async () => {
      const res = await fetch(`${API_BASE_URL}/batch/status/${jobId}`);
      const data = await res.json();
      setBatchResults(data.results);

      if (data.status === "done") clearInterval(interval);
    }, 2000);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>TTB Label Verification</h1>

      <h2>Single Image</h2>
      <form onSubmit={uploadSingle}>
        <input type="file" name="single" />
        <button>Upload</button>
      </form>
      {singleResult && <pre>{JSON.stringify(singleResult, null, 2)}</pre>}

      <h2>Batch ZIP</h2>
      <form onSubmit={uploadBatch}>
        <input type="file" name="batch" />
        <button>Upload ZIP</button>
      </form>

      {batchJobId && <p>Job ID: {batchJobId}</p>}

      {Object.keys(batchResults).length > 0 && (
        <pre>{JSON.stringify(batchResults, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;