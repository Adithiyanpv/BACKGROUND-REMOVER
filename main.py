import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np

def removebg(img):
    input_image = Image.open(img)
    input_array = np.array(input_image)
    result_array = remove(input_array)
    result_image = Image.fromarray(result_array)
    return result_image

def main():
    st.title("BACKGROUND REMOVER")
    uploaded_file = st.file_uploader("Choose an Image: ", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image")

        result = removebg(uploaded_file)
        st.image(result, caption="Output Image")

if __name__ == '__main__':
    main()
