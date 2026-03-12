# AgriGrade AI

AI-powered produce quality grading system. Upload an image of produce and receive an instant quality grade based on defect analysis.

## Architecture

```
Image → Produce Classifier → Defect Detector → Defect % Calculation → Grading Engine → Grade A/B/C
```

**Backend** — FastAPI serving two YOLOv8 models (classification + detection)  
**Frontend** — Next.js 14 with TailwindCSS

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## Frontend Setup

```bash
cd frontend
npm install
```

### Start the Next.js dev server

```bash
cd frontend
npm run dev
```

The UI will be available at `http://localhost:3000`.

## API

### `POST /grade`

Upload an image file to receive a grading result.

```bash
curl -X POST http://localhost:8000/grade \
  -F "file=@apple.jpg"
```

**Response:**

```json
{
  "produce": "apple",
  "confidence": 0.94,
  "defect_percentage": 12.3,
  "grade": "B",
  "label": "Standard Quality",
  "defects": [
    {
      "label": "bruise",
      "confidence": 0.87,
      "bbox": [120.5, 80.3, 200.1, 160.7]
    }
  ]
}
```

### `GET /health`

Health check endpoint.

## Grading Scale

| Grade  | Defect % | Label            |
| ------ | -------- | ---------------- |
| A      | < 5%     | Premium Quality  |
| B      | 5–15%    | Standard Quality |
| C      | 15–30%   | Below Standard   |
| Reject | > 30%    | Rejected         |

## Project Structure

```
backend/
  app/
    main.py
    api/routes.py
    services/
      classifier.py
      defect_detector.py
      area_calculator.py
      grading_engine.py
      pipeline.py
    utils/image_processing.py
    models/
      produce_classifier.pt
      defect_detector.pt
frontend/
  src/
    app/
      layout.tsx
      page.tsx
    components/
      Navbar.tsx
      ImageUpload.tsx
      ResultCard.tsx
      Loader.tsx
```
