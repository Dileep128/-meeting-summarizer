# Quick Start Reference

## File Structure
```
project/
├── app.py              ← Flask backend
├── index.html          ← Web interface
├── test.py             ← API test (optional)
├── requirements.txt    ← Dependencies
├── .env                ← Your API key (you create this)
└── README.md          ← Full documentation
```

## Step 1: Get API Key
→ https://console.anthropic.com/account/keys

## Step 2: Create `.env` File
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

## Step 3: Install & Run
```bash
pip install -r requirements.txt
python app.py
```

## Step 4: Open Browser
- **Option A:** http://localhost:5000
- **Option B:** Open `index.html` directly

## Step 5: Test with Sample
Click "Load Sample" → "Analyze Meeting"

---

## Backend Endpoints

### POST /analyze
Analyzes a meeting transcript.

**Request:**
```json
{
  "transcript": "Sarah: Good morning... [full transcript]"
}
```

**Response:**
```json
{
  "success": true,
  "analysis": {
    "summary": "...",
    "key_decisions": ["..."],
    "action_items": [
      {"task": "...", "owner": "...", "deadline": "..."}
    ],
    "topics_discussed": ["..."]
  }
}
```

### GET /health
Quick health check.

---

## What's Using Claude API?

In `app.py`, the `/analyze` endpoint:
1. Takes transcript from frontend
2. Sends to Claude via Anthropic SDK
3. Claude uses extended thinking (optional, enabled for complex reasoning)
4. Returns structured JSON
5. Sends back to frontend for display

The model is **claude-opus-4-6** (latest available).

---

## Optional: Test Backend Only

Before running the Flask server, test the API directly:
```bash
python test.py
```

This verifies your API key works without needing the web server.

---

## Next Steps to Improve

### Better Prompting
In `app.py`, line ~50, customize the prompt for nonprofit meetings:
- Add terminology specific to your nonprofit
- Change what fields to extract
- Add validation rules

### Add File Upload
In `index.html`, add a file input:
```html
<input type="file" id="fileInput" accept=".txt,.pdf">
```

Then in JavaScript, read the file and send to `/analyze`.

### Store Results
Add SQLite to save analyses:
```python
import sqlite3
# In /analyze endpoint, save to database after analysis
```

### Real Transcription
Integrate Deepgram (real-time transcription):
```bash
pip install deepgram-sdk
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Port 5000 in use | `python app.py --port 5001` |
| API key error | Check `.env` file exists with real key |
| CORS errors | Already handled, check browser console |
| Blank response | Make sure transcript has 50+ words |

---

## For the Fellowship Application

Highlight that this MVP:
- ✅ Solves a real nonprofit problem
- ✅ Uses Claude API best practices
- ✅ Has clean, production-ready code
- ✅ Runs locally (easy to test)
- ✅ Ready to scale with feedback from nonprofits

You can show it working with any meeting transcript in your interview!
