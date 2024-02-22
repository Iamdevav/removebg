from flask import Blueprint, jsonify, request
from flask_cors import CORS
from rembg import remove
from io import BytesIO
from PIL import Image
import base64
import concurrent.futures
 
bp = Blueprint('routes', __name__)
CORS(bp)
 
def process_image(image_data):
    try:
        image = Image.open(BytesIO(image_data))
        output_image = remove(image)
        output_data = BytesIO()
        output_image.save(output_data, format='PNG')
        encoded_image = base64.b64encode(output_data.getvalue()).decode('utf-8')
        return encoded_image
    except Exception as e:
        return str(e)
 
@bp.route('/remove_background', methods=['POST'])
def remove_background():
    try:
        image_files = request.files.getlist('images[]')
        
        result_images = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_image, image_file.read()) for image_file in image_files]
            for future in concurrent.futures.as_completed(futures):
                result_images.append(future.result())
 
        return jsonify({
            'success': True,
            'message': 'Background removed successfully',
            'result_images': result_images
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})