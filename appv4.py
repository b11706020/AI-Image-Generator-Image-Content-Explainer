import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64
from explainimagecontent import explain_image_content
from editimage import edit_image
from getexplanation import get_input_explanation
from getimageurl import call_image_generation_api
# Function to get image from URL and convert to a displayable format
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Function to create a download link for the image
def get_image_download_link(img, filename, text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download="{filename}">{text}</a>'
    return href

def main():
    st.title('Image Generator/Editor and Analyzer')
    # Text input from user
    user_input = st.text_input("Enter text to generate images:")

    if st.button('Generate Images'):
        # Call the API to get images
        image_urls = call_image_generation_api(user_input)

        # Display each image with a download link
        for idx, url in enumerate(image_urls):
            img = load_image(url)
            st.image(img, caption=f'Image {idx + 1}')
            st.markdown(get_image_download_link(img, f"image_{idx + 1}.jpg", f"Download Image {idx + 1}"),
                        unsafe_allow_html=True)

        # Display explanation of the user's input
        explanation = get_input_explanation(user_input)
        st.subheader("Explanation:")
        st.write(explanation)



    st.subheader("Upload and Analyze/Edit Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        description = st.text_input("Enter description or edit instructions:")

        if st.button('Explain Content'):
            explanation = explain_image_content(image, description)
            st.write(explanation)

        if st.button('Edit Image'):
            edited_image_urls = edit_image(image, description)
            # Display each image with a download link
            for idx, url in enumerate(edited_image_urls):
                img = load_image(url)
                st.image(img, caption=f'Image {idx + 1}')
                st.markdown(get_image_download_link(img, f"image_{idx + 1}.jpg", f"Download Image {idx + 1}"),
                            unsafe_allow_html=True)

            # Display explanation of the user's input
            explanation = get_input_explanation(description)
            st.subheader("Edited Image Explanation:")
            st.write(explanation)
    if st.button('Start New'):
        st.experimental_rerun()


if __name__ == "__main__":
    main()
