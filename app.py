from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

# Simple in-memory status (Available or Unavailable)
status = {"available": True}

@app.route('/')
def get_status():
    return jsonify(status)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global status
    if request.method == 'POST':
        availability = request.form.get('availability')
        status['available'] = (availability == 'on')
    return render_template_string('''
        <h1>Toggle Availability</h1>
        <form method="post">
            <input type="checkbox" name="availability" {% if status['available'] %}checked{% endif %}>
            Available<br><br>
            <input type="submit" value="Save">
        </form>
    ''', status=status)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
