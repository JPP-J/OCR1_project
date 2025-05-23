
import os
from utils.ocr_extended import OCR_extract_txt, image_show, image_show2



def test_():
  
  print('FLASK_APP:', os.getenv('FLASK_APP'))
  print('FLASK_DEBUG:', os.getenv('FLASK_DEBUG'))
  print('FLASK_ENV:', os.getenv('FLASK_ENV'))

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

  # test_()



