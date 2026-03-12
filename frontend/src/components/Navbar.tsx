"use client";

export default function Navbar() {
  return (
    <nav className="w-full border-b border-gray-200 bg-white">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🌿</span>
          <span className="text-xl font-semibold tracking-tight text-gray-900">
            AgriGrade AI
          </span>
        </div>
        <span className="text-sm text-gray-500">Produce Quality Grading</span>
      </div>
    </nav>
  );
}
