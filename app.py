from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/shrink', methods=['POST'])
def shrink_image():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    
    img = Image.open(file.stream)
    img.thumbnail((300, 300))
    
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)