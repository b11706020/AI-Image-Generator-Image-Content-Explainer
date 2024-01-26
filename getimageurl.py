from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
# Placeholder for your image generation API call
def call_image_generation_api(user_input):
    # Replace this with your actual API call to generate images
    # This function should return a list of image URLs or binary image data
    # For demonstration, it returns empty list
    try:
        print("input",user_input)
        response = client.images.generate(
        model="dall-e-3",
        prompt=user_input,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        print("Response:",response)
        images_arr=[]

        for images in response.data:
            images_arr.append(images.url)

        print("image url",images_arr)
        return images_arr
    except:
        return []