# 🤝 Meeting Summarizer

An AI-powered tool for nonprofits to analyze meeting transcripts and extract action items automatically.

## What It Does

Upload or paste a meeting transcript → Claude AI extracts:
- **Summary** (2-3 sentences)
- **Key Decisions** made during the meeting
- **Action Items** (task + owner + deadline)
- **Topics Discussed**

## Problem It Solves

Nonprofits spend hours managing meeting notes and tracking action items. This tool automates that process in seconds.

## Features

✅ Analyze meeting transcripts in seconds  
✅ Extract action items with deadlines  
✅ Beautiful, easy-to-use interface  
✅ Built with Claude API  
✅ Works locally  

## Quick Start

### Requirements
- Python 3.8+
- Claude API Key (get free credits at https://console.anthropic.com)

### Install
```bash
pip install -r requirements.txt
```

### Setup
1. Create a `.env` file with your API key:
ANTHROPIC_API_KEY=sk-ant-your-key-here

2. Run the app:
```bash
python app.py
```

3. Open in browser:
http://localhost:5000

## Test It

1. Click **"Load Sample"** to see example meeting
2. Click **"Analyze Meeting"**
3. See results in 5 seconds!

## How It Works

1. **Frontend** (index.html) - Paste meeting transcript
2. **Backend** (app.py) - Flask server + Claude API
3. **Claude** - Analyzes and extracts structured data
4. **Results** - Displayed in clean format

## Files

- `app.py` - Flask backend
- `index.html` - Web interface
- `requirements.txt` - Python dependencies
- `test.py` - API test script

## For Fellowship

This project demonstrates:
- ✅ Real nonprofit problem
- ✅ Working Claude API integration
- ✅ Production-ready code
- ✅ Clean architecture
- ✅ Ready to deploy

## Next Steps

- Add file upload support
- Store meeting history
- Add real-time transcription
- Deploy to production

## Author

Built for Claude Corps Fellowship application

---

Made for nonprofits
