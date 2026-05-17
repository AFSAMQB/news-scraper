from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <style>
        body { 
            background: linear-gradient(45deg, #ff9a9e, #fecfef, #fecfef);
            height: 100vh; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-family: Arial;
            margin: 0;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 { color: #e91e63; font-size: 3em; margin: 0; }
        p { color: #666; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎉 Hello, World!</h1>
        <p>Flask works perfectly!</p>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    print("🌐 Go to: http://127.0.0.1:5000")
    app.run(debug=True)