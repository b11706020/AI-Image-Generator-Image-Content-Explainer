from openai import OpenAI
import os
import io
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
# Placeholder for your image generation API call
def edit_image(image, instructions):

    try:
        print(instructions)
        # Convert the image to 'RGBA' format
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)  # Go to the start of the BytesIO object
        response = client.images.edit(
            model="dall-e-2",
        image=img_byte_arr,
            mask=img_byte_arr,
            prompt=instructions,
            n=1,
            size="1024x1024"
        )
        print(response)
        image_url = response.data[0].url
        return [image_url]
    except Exception as e:
        print("exception ",e)
        return []
