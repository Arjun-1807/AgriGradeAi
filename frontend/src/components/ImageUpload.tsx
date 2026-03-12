"use client";

import { useCallback } from "react";

interface Props {
  onFileSelect: (file: File) => void;
  preview: string | null;
}

export default function ImageUpload({ onFileSelect, preview }: Props) {
  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      const file = e.dataTransfer.files[0];
      if (file) onFileSelect(file);
    },
    [onFileSelect],
  );

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) onFileSelect(file);
  };

  return (
    <div
      onDrop={handleDrop}
      onDragOver={(e) => e.preventDefault()}
      className="relative flex min-h-[280px] cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-300 bg-gray-50 transition-colors hover:border-green-500 hover:bg-green-50/30"
    >
      <input
        type="file"
        accept="image/jpeg,image/png,image/webp"
        onChange={handleChange}
        className="absolute inset-0 z-10 cursor-pointer opacity-0"
      />
      {preview ? (
        <img
          src={preview}
          alt="Selected produce"
          className="max-h-60 rounded-lg object-contain"
        />
      ) : (
        <div className="flex flex-col items-center gap-2 p-6 text-center">
          <svg
            className="h-10 w-10 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M12 16v-8m0 0l-3 3m3-3l3 3M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1"
            />
          </svg>
          <p className="text-sm font-medium text-gray-600">
            Drag & drop an image or click to browse
          </p>
          <p className="text-xs text-gray-400">
            JPEG, PNG, or WebP up to 10 MB
          </p>
        </div>
      )}
    </div>
  );
}
