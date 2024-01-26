import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Placeholder function for explaining content of the image
def explain_image_content(image, description):
    # Integrate with an image analysis API or implement logic
    # Return the explanation as a string
    model = genai.GenerativeModel('gemini-pro-vision')
    description="Explain the contents in the IMage" + description
    response = model.generate_content([description,image], stream=True)
    response.resolve()

    return response.text