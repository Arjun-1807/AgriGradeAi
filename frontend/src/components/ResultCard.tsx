interface Result {
  produce: string;
  confidence: number;
  defect_percentage: number;
  grade: string;
  label: string;
}

const GRADE_COLORS: Record<string, string> = {
  A: "bg-green-100 text-green-800 border-green-300",
  B: "bg-yellow-100 text-yellow-800 border-yellow-300",
  C: "bg-orange-100 text-orange-800 border-orange-300",
  Reject: "bg-red-100 text-red-800 border-red-300",
};

export default function ResultCard({ result }: { result: Result }) {
  const gradeStyle = GRADE_COLORS[result.grade] ?? GRADE_COLORS["Reject"];

  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="mb-5 flex items-center justify-between">
        <h2 className="text-lg font-semibold text-gray-900">Grading Result</h2>
        <span
          className={`rounded-full border px-4 py-1 text-sm font-bold ${gradeStyle}`}
        >
          Grade {result.grade}
        </span>
      </div>

      <div className="grid grid-cols-2 gap-4">
        <Stat label="Produce" value={capitalize(result.produce)} />
        <Stat
          label="Confidence"
          value={`${(result.confidence * 100).toFixed(1)}%`}
        />
        <Stat label="Defect" value={`${result.defect_percentage}%`} />
        <Stat label="Quality" value={result.label} />
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-gray-50 px-4 py-3">
      <p className="text-xs font-medium uppercase tracking-wide text-gray-400">
        {label}
      </p>
      <p className="mt-1 text-base font-semibold text-gray-800">{value}</p>
    </div>
  );
}

function capitalize(s: string) {
  return s.charAt(0).toUpperCase() + s.slice(1);
}
