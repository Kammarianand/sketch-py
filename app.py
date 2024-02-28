import streamlit as st
import numpy as np
import cv2
import time
from io import BytesIO

st.set_page_config(page_title="sketchi-py",page_icon="🎨")

st.markdown(
    f'<h1 style="color:#22ebff;">StreamlitSketchr: Magical Sketches</h1>',
    unsafe_allow_html=True
)

with  st.expander("about this project 🎦"):
    st.markdown("""
    The application is created for fun, utilizing the Python programming language along with modules such as OpenCV, NumPy, and Streamlit. 
    I'm fine-tuning my skills as part of my data analysis journey, and the project is still in its initial phase. 
    While it may not consistently produce accurate sketch images, I'm striving to optimize the output quality. 
    
    Have a great day! 🌥️
    
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Kammari%20Anand-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/kammari-anand-504512230/)
    
""")



def sketchify_img(img):
    nparr = np.frombuffer(img.read(), np.uint8)
    original_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    inverted_gray_img = cv2.bitwise_not(gray_img)
    blurred_image = cv2.GaussianBlur(inverted_gray_img, (111, 111), 0)
    inverted_blurred_img = cv2.bitwise_not(blurred_image)
    pencil_sketch = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
    pencil_sketch_rgb = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2RGB)


    return pencil_sketch_rgb



def download_sketch(sketch_img):
    # Convert the NumPy array to bytes
    img_bytes = cv2.imencode('.png', sketch_img)[1].tobytes()
    # Create a BytesIO object to hold the bytes data
    img_io = BytesIO(img_bytes)
    # Return a download link for the BytesIO object
    return img_io




def spinner():
    with st.spinner("Please wait for sometime"):
        time.sleep(2.5)

def balloons():
    for i in range(3):
        st.balloons()

img_file = st.file_uploader("Upload your image",type=['png','jpeg','jpg'])

if st.button("sketch-me"):
    if img_file is not None:
        sk_img = sketchify_img(img_file)
        spinner()
        st.image(sk_img,caption="SketchImage",use_column_width=True)
        balloons()
        download_link = download_sketch(sk_img)
        st.download_button(label="Download Sketch", data=download_link, file_name='sketch.png', mime='image/png')
    else:
        st.error("atleast upload an img")
        st.snow()









