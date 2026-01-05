from flask import Flask, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>UW-Stout Blue Devils--CNIT 300</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #0033A0 0%, #FFD100 100%);
      color: white;
      text-align: center;
      padding: 50px;
      min-height: 100vh;
      margin: 0;
    }
    .container {
      background: rgba(0, 51, 160, 0.9);
      border-radius: 20px;
      padding: 40px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
      max-width: 800px;
      margin: 0 auto;
    }
    h1 { color: #FFD100; font-size: 3em; margin: 0; }
    .mascot { font-size: 4em; margin: 20px 0; }
    .info {
      background: rgba(255,255,255,0.1);
      padding: 20px;
      border-radius: 10px;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class='container'>
    <h1>GO BLUE DEVILS!</h1>
    <div class='mascot'>🔵⚪🏈</div>
    <h2>University of Wisconsin-Stout</h2>
    <p style='font-size:1.5em;'>CI/CD Pipeline - LIVE!</p>
    <div class='info'>
      <p><strong>Revision:</strong> {{ revision }}</p>
      <p><strong>Deployed:</strong> {{ timestamp }}</p>
      <p><strong>Built with:</strong> CI/CD + DevSecOps</p>
    </div>
  </div>
</body>
</html>
'''

@app.route('/')
def home():
    revision = os.environ.get('K_REVISION', 'dev')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template_string(HTML, revision=revision,
                                  timestamp=timestamp)

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
