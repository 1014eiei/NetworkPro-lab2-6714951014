from flask import Flask, request, render_template_string
from datetime import datetime
import os

app = Flask(__name__)

# หน้าเว็บฟอร์มและส่วนแสดงผลข้อความล่าสุด
form_html = """
<!doctype html>
<html>
<head>
    <title>Submit Message</title>
</head>
<body>
    <h1>Submit your message</h1>
    <form method="post">
        <textarea name="message" rows="4" cols="40" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>

    {% if submitted_message %}
        <hr>
        <h3>ข้อความล่าสุดที่ได้รับ:</h3>
        <p>{{ submitted_message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    submitted_message = None
    if request.method == "POST":
        submitted_message = request.form.get("message", "")
        if submitted_message:
            # บันทึกข้อความลงไฟล์ log.txt พร้อมเวลาใน Container
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {submitted_message}\n")
                
    return render_template_string(form_html, submitted_message=submitted_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)