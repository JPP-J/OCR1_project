import cv2
import numpy as np
import requests
import pytesseract
from io import BytesIO
# from IPython.display import display, Image as IPImage  # For displaying images in the notebook
import matplotlib
matplotlib.use("TkAgg")  # Use an interactive backend
import matplotlib.pyplot as plt  # For displaying images using matplotlib
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # use your path here

def image_show(link):

  link = link

  # try:
  #     response = requests.get(link, stream=True)
  #     response.raise_for_status()  # Raise an error for bad status codes

  #     # Check if the response content is not empty
  #     if response.content:
  #         image = Image.open(BytesIO(response.content)).convert("RGB")
  #         # image.show()  # Show the image
  #         return image
  #     else:
  #         print("The response content is empty.")
  # except requests.exceptions.RequestException as e:
  #     print(f"An error occurred while fetching the image: {e}")
  # except Image.UnidentifiedImageError:
  #     print("The file could not be identified as an image.")
  # except Exception as e:
  #     print(f"An unexpected error occurred: {e}")

  # Fetch image
  response = requests.get(link)
  image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
  img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

  return img  


def OCR_extract_txt(link, show_im=False):
  # URL of the image
  image_url = link  # Replace with your image link

  # Step 1: Download the image from the URL
  response = requests.get(image_url)
  if response.status_code == 200:  # Check if the request was successful
      image_bytes = BytesIO(response.content)  # Convert response to bytes

      # Step 2: Convert image bytes to a NumPy array
      image_array = np.frombuffer(image_bytes.getvalue(), np.uint8) # unsigned 8-bit integer standard format for image data

      # Step 3: Decode image using OpenCV
      image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

      # Step 4: Convert to grayscale for OCR
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Step 5: Extract text using Tesseract OCR
      text = pytesseract.image_to_string(gray)

      if show_im == True:
        # Step 6: Display the image in the notebook
        # Option 1: Using matplotlib
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
        plt.axis('off')  # Hide axes
        plt.title("Downloaded Image")
        plt.show()

      # # Option 2: Using IPython.display
      # # Convert the OpenCV image to bytes and display
      # _, encoded_image = cv2.imencode(".jpg", image)
      # display(IPImage(data=encoded_image.tobytes()))

  else:
      print("Error: Failed to download the image. Check the URL.")
  return text

def image_show2(link):


  url = link
  response = requests.get(url)
  image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
  img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

  # Convert BGR to RGB for Matplotlib
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  plt.imshow(img)
  plt.axis("off")
  plt.show()

if __name__=="__main__":
  link = "https://www.investopedia.com/thmb/w959_gtyU1UGzJDZYJSX1GgWzCI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bookvalue-3e517fff0e004e5e9279c0061cae4aa0.png"
  image = image_show(link) 

  # cv2.imshow("Image", image)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  # # Show the image
  # plt.imshow(image)
  # plt.axis("off")  # Hide axes
  # plt.show()

  # image_show2(link)
    
    
  text = OCR_extract_txt(link, show_im=True)  # Replace with your image link    
  print(text)

