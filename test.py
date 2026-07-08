#!/usr/bin/env python3
"""
Quick test to verify Claude API integration works.
Run this before starting the Flask app.
"""

import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

SAMPLE_TRANSCRIPT = """Sarah: Good morning everyone. Quick sync on the food bank expansion.
John: Hey! So we got the space on 5th Avenue. We can move in next month.
Sarah: Great! John, you're handling the setup, right?
John: Yeah, I'll get it ready by June 15th. Need to buy shelves and organize the system.
Lisa: What about staffing? Do we have volunteers?
Sarah: I'll recruit 10 volunteers by June 1st. Already have 3 commitments.
John: Perfect. Also, we need to update our donor database before the move.
Lisa: I can do that. I'll have it done by May 25th.
Sarah: Great. So to recap - move happens early June, volunteers recruited, database updated. Any blockers?
Everyone: Nope!
Sarah: Alright, let's reconvene next week to check progress."""

def test_api():
    print("🧪 Testing Claude API integration...\n")
    
    # Check API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ERROR: ANTHROPIC_API_KEY not found in .env file")
        return False
    
    print("✅ API key found")
    
    # Initialize client
    client = Anthropic()
    
    try:
        print("📞 Calling Claude API...")
        
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=2000,
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
{SAMPLE_TRANSCRIPT}
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
        
        print("✅ API call successful\n")
        
        # Parse response
        response_text = response.content[0].text
        
        # Clean JSON
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0]
        
        analysis = json.loads(response_text.strip())
        
        print("📊 Analysis Result:\n")
        print(f"Summary: {analysis['summary']}\n")
        print(f"Key Decisions: {analysis['key_decisions']}\n")
        print("Action Items:")
        for item in analysis['action_items']:
            print(f"  - {item['task']} (Owner: {item['owner']}, Due: {item['deadline']})")
        print(f"\nTopics: {analysis['topics_discussed']}\n")
        
        print("✅ Everything works! Start Flask with: python app.py")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON: {e}")
        print(f"Response was: {response_text}")
        return False
    except Exception as e:
        print(f"❌ API Error: {e}")
        return False

if __name__ == '__main__':
    success = test_api()
    exit(0 if success else 1)
