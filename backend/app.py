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

        writing_sample = request.form.get('text', '').strip()
        if writing_sample:
            writing_sample_path = os.path.join(UPLOAD_FOLDER, "writing_sample.txt")
            with open(writing_sample_path, 'w', encoding='utf-8') as writing_sample_file:
                writing_sample_file.write(writing_sample)

        job_description = request.form.get('text', '').strip()
        if job_description:
            job_description_path = os.path.join(UPLOAD_FOLDER, "job_description.txt")
            with open(job_description_path, 'w', encoding='utf-8') as job_description_file:
                job_description_file.write(job_description)

        return jsonify({'message': 'success'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)