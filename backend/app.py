from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'pdf' in request.files:
            pdf_file = request.files['pdf']
            if pdf_file.filename:
                pdf_file.save(os.path.join(UPLOAD_FOLDER, "resume.pdf"))

        if 'video' in request.files:
            video_file = request.files['video']
            if video_file.filename:
                video_file.save(os.path.join(UPLOAD_FOLDER, "video.mp4"))

        return jsonify({'message': 'success'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)