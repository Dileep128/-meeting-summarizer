import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Serve the HTML file
@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

client = Anthropic()

# The structured schema we want Claude to follow
MEETING_ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "2-3 sentence summary of the meeting"
        },
        "key_decisions": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of key decisions made during the meeting"
        },
        "action_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "task": {"type": "string"},
                    "owner": {"type": "string"},
                    "deadline": {"type": "string"}
                },
                "required": ["task", "owner", "deadline"]
            },
            "description": "List of action items with task, owner, and deadline"
        },
        "topics_discussed": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Topics that were discussed in the meeting"
        }
    },
    "required": ["summary", "key_decisions", "action_items", "topics_discussed"]
}

@app.route('/analyze', methods=['POST'])
def analyze_transcript():
    """Analyze a meeting transcript and extract structured data"""
    try:
        data = request.json
        transcript = data.get('transcript', '').strip()
        
        if not transcript:
            return jsonify({'error': 'No transcript provided'}), 400
        
        # Call Claude with structured output
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=2000,
            thinking={
                "type": "enabled",
                "budget_tokens": 1024
            },
            messages=[
                {
                    "role": "user",
                    "content": f"""Analyze this meeting transcript and extract:
1. A 2-3 sentence summary
2. Key decisions made
3. Action items (with task, owner, and deadline)
4. Topics discussed

Meeting Transcript:
---
{transcript}
---

Return the analysis as JSON matching this structure:
{{
    "summary": "...",
    "key_decisions": ["decision1", "decision2"],
    "action_items": [
        {{"task": "...", "owner": "...", "deadline": "..."}},
    ],
    "topics_discussed": ["topic1", "topic2"]
}}"""
                }
            ]
        )
        
        # Extract the text response
        analysis_text = response.content[0].text
        
        # Parse JSON from response (Claude will return pure JSON)
        # Remove markdown code blocks if present
        if "```json" in analysis_text:
            analysis_text = analysis_text.split("```json")[1].split("```")[0]
        elif "```" in analysis_text:
            analysis_text = analysis_text.split("```")[1].split("```")[0]
        
        analysis = json.loads(analysis_text.strip())
        
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    
    except json.JSONDecodeError as e:
        return jsonify({'error': f'Failed to parse response: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
