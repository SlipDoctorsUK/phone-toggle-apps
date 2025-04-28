from flask import Flask, render_template_string, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # << ADD THIS LINE

# Simple in-memory status (Available or Unavailable)
status = {"available": True}

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global status
    if request.method == 'POST':
        availability = request.form.get('availability')
        status['available'] = (availability == 'on')
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toggle Availability</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
        }
        .switch {
          position: relative;
          display: inline-block;
          width: 80px;
          height: 44px;
        }
        .switch input {
          opacity: 0;
          width: 0;
          height: 0;
        }
        .slider {
          position: absolute;
          cursor: pointer;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: #ccc;
          transition: .4s;
          border-radius: 34px;
        }
        .slider:before {
          position: absolute;
          content: "";
          height: 34px;
          width: 34px;
          left: 5px;
          bottom: 5px;
          background-color: white;
          transition: .4s;
          border-radius: 50%;
        }
        input:checked + .slider {
          background-color: #2196F3;
        }
        input:checked + .slider:before {
          transform: translateX(36px);
        }
        .save-btn {
          display: block;
          margin: 20px auto;
          padding: 10px 20px;
          background-color: #032f57;
          color: white;
          border: none;
          border-radius: 8px;
          font-size: 18px;
          cursor: pointer;
        }
    </style>
</head>
<body>

    <h1>Toggle Availability</h1>

    <form method="post">
        <label class="switch">
          <input type="checkbox" name="availability" {% if available %}checked{% endif %}>
          <span class="slider"></span>
        </label>
        <br><br>
        <input type="submit" value="Save" class="save-btn">
    </form>

</body>
</html>
''', available=status['available'])
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
