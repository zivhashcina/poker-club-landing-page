import requests
import json

# הכנס כאן את ה-API Key שלך
API_KEY = "YOUR_API_KEY"  # החלף במפתח שלך

# כתובת ה-API של D-ID
url = "https://api.d-id.com/talks"

# הגדרת הנתונים ליצירת הסרטון
payload = {
    "script": {
        "type": "text",
        "input": """שלום חברים.
        הגעתם למועדון מספר אחד בישראל.
        אצלנו תקבלו שירות אדיב ומקצועי.
        בונוסים שווים במיוחד.
        יש לנו את כל סוגי המשחקים במועדון.
        אומהה. הולדם. טורנירים. ועוד הפתעות והשקעות מיוחדות לחברי המועדון בלבד.
        הצטרפו אלינו עוד היום, ונשמח לדאוג לכם לסוכן מקצועי.
        הסוכנים אצלנו במועדון זמינים עשרים וארבע שבע.
        אשמח לראות את כולכם.""",
        "provider": {"type": "elevenlabs", "voice_id": "hebrew_female_professional"} # קול עברי מקצועי
    },
    "source_url": "https://your-image-url.com",  # הכנס כאן תמונה של הדמות
    "voice": {"language": "he"}
}

# שליחת הבקשה
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

# הדפסת תגובת השרת (קישור להורדת הסרטון)
print(response.json())
