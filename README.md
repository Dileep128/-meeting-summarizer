# Meeting Transcriber + Summarizer

An AI-powered tool for nonprofits to process meeting transcripts into structured action items using Claude API.

## What It Does

Paste any meeting transcript → Claude analyzes it and extracts:
- **Summary**: 2-3 sentence recap
- **Key Decisions**: What was decided
- **Action Items**: Task + owner + deadline
- **Topics**: What was discussed

## Quick Start (5 minutes)

### 1. Get Your API Key
- Go to https://console.anthropic.com
- Create/copy your API key

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=sk-ant-...
```

### 4. Run Locally
```bash
python app.py
```

You'll see:
```
* Running on http://127.0.0.1:5000
```

### 5. Open in Browser
Visit: **http://localhost:5000**

Or open `index.html` directly in your browser.

## How to Use

1. **Paste a transcript** into the left panel
2. **Click "Analyze Meeting"**
3. **Results appear** on the right (summary, decisions, action items, topics)

### Test with Sample
Click **"Load Sample"** to see it working with the food bank expansion example.

## API Response Format

The backend returns clean JSON:
```json
{
  "summary": "...",
  "key_decisions": ["decision1", "decision2"],
  "action_items": [
    {"task": "...", "owner": "...", "deadline": "..."}
  ],
  "topics_discussed": ["topic1", "topic2"]
}
```

## Architecture

```
Frontend (index.html)
    ↓
Flask API (app.py)
    ↓
Claude API
    ↓
Structured JSON response
    ↓
Display in browser
```

## Files

- `app.py` - Flask backend with Claude API integration
- `index.html` - Simple, self-contained frontend
- `requirements.txt` - Python dependencies
- `.env` - Your API key (create this)

## What's Next

### Phase 2: Iterate on Prompt
- Tweak the analysis prompt in `app.py` to extract more/different fields
- Add custom instructions for nonprofit terminology

### Phase 3: Add Features
- File upload support (drag-and-drop transcript files)
- Export to CSV/PDF
- Meeting history/storage
- Real-time transcription (Deepgram API)

### Phase 4: Deploy
- Heroku, Render, or Railway for free hosting
- Add database (SQLite → PostgreSQL)
- Authentication for team access

## Troubleshooting

### "Connection refused"
- Make sure Flask is running: `python app.py`
- Check http://localhost:5000 is accessible

### "API key invalid"
- Verify `.env` file exists with your real API key
- Check key is not expired in console.anthropic.com

### "CORS error"
- Flask-CORS is already enabled in app.py
- If issues persist, check browser console for exact error

## For Claude Corps Fellowship

This is a real-world MVP that:
- ✅ Uses Claude API with structured outputs
- ✅ Solves a nonprofit problem (meeting notes)
- ✅ Runs locally (no deployment needed for MVP)
- ✅ Uses best practices (error handling, clean UI)
- ✅ Ready to iterate on with user feedback

Next step: Test with real nonprofit meetings and refine the extraction logic based on their feedback!

## Questions?

- API docs: https://docs.claude.com/en/api/overview
- Anthropic support: https://support.anthropic.com
