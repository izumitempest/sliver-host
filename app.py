from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/sliver_implant')
def serve_implant():
    return send_from_directory('.', 'sliver_implant', as_attachment=True)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)