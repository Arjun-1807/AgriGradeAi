"use client";

import { useState } from "react";
import Navbar from "@/components/Navbar";
import ImageUpload from "@/components/ImageUpload";
import ResultCard from "@/components/ResultCard";
import Loader from "@/components/Loader";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface GradeResult {
  produce: string;
  confidence: number;
  defect_percentage: number;
  grade: string;
  label: string;
}

export default function Home() {
  const [preview, setPreview] = useState<string | null>(null);
  const [result, setResult] = useState<GradeResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileSelect = async (file: File) => {
    setResult(null);
    setError(null);
    setPreview(URL.createObjectURL(file));
    setLoading(true);

    try {
      const form = new FormData();
      form.append("file", file);

      const res = await fetch(`${API_URL}/grade`, {
        method: "POST",
        body: form,
      });

      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail || `Server error (${res.status})`);
      }

      const data: GradeResult = await res.json();
      setResult(data);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setPreview(null);
    setResult(null);
    setError(null);
  };

  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />

      <main className="mx-auto flex w-full max-w-xl flex-1 flex-col gap-6 px-4 py-12">
        <div className="text-center">
          <h1 className="text-3xl font-bold tracking-tight text-gray-900">
            Produce Quality Grader
          </h1>
          <p className="mt-2 text-gray-500">
            Upload a photo of your produce to get an instant quality grade.
          </p>
        </div>

        <ImageUpload onFileSelect={handleFileSelect} preview={preview} />

        {loading && <Loader />}

        {error && (
          <div className="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        )}

        {result && <ResultCard result={result} />}

        {(preview || result) && !loading && (
          <button
            onClick={reset}
            className="mx-auto rounded-lg bg-gray-900 px-6 py-2.5 text-sm font-medium text-white transition-colors hover:bg-gray-700"
          >
            Grade Another
          </button>
        )}
      </main>

      <footer className="border-t border-gray-200 py-4 text-center text-xs text-gray-400">
        AgriGrade AI &mdash; Intelligent Produce Grading
      </footer>
    </div>
  );
}
