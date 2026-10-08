# Project Structure

```text
AI-Project-Report-Generator/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── index.html
├── docs/
│   └── PROJECT_STRUCTURE.md
├── screenshots/
├── .gitignore
├── LICENSE
├── README.md
└── render.yaml
```

## Main modules

### Frontend
The frontend contains the complete responsive ReportAI interface:
- Home dashboard
- Report generator
- Project information form
- Academic report sections
- AI Workspace
- Report history
- Templates
- Print / Save as PDF

### Backend
The Flask backend exposes:
- `GET /` — health check
- `POST /api/generate` — report generation endpoint

The current endpoint contains a safe demo generator. Connect it to Gemini or another AI provider using an environment variable rather than committing an API key.

### Docs
Project documentation and architecture notes.

### Screenshots
Store screenshots of the deployed application here.
