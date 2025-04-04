import requests
from utils.ocr_extended import OCR_extract_txt

def is_valid_image_url(url):
    try:
        response = requests.get(url, stream=True)
        content_type = response.headers.get("Content-Type", "")

        if response.status_code == 200 and "image" in content_type:
            return True
        else:
            return False
    except requests.RequestException:
        return False
    
def extract_text(image_url):
    result_text = OCR_extract_txt(image_url, show_im=False)

    return result_text