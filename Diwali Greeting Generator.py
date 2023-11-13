import sys
import openai
import random

# Set the standard output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_gift_ideas(age):
    prompt = f"Generate Diwali gift ideas for a {age}-year-old person:, use  Unicode equivalents emojis that could sync with gift ideas. Format one idea per line for a readability"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_random_image():
    # Replace the list below with the paths to your available images
    available_images = ["diwali_image1.png", "diwali_image2.png", "diwali_image3.png"]
    return random.choice(available_images)

def generate_html_gift_ideas(age, gift_ideas):
    # Get a random image
    gift_image = get_random_image()

    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diwali Gift Ideas</title>
        <style>
            body {{
                background-color: #f5f5f5;
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }}
            .gift-ideas-card {{
                max-width: 500px;
                padding: 20px;
                background: linear-gradient(45deg, #ffcc00, #ff6699);
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                color: #fff;
            }}
            h1 {{
                font-size: 28px;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 18px;
                line-height: 1.5;
                margin-bottom: 20px;
            }}
            img {{
                width: 100%;
                max-width: 300px;
                border-radius: 10px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="gift-ideas-card">
            <h1>Diwali Gift Ideas</h1>
            <p>Wishing you a joyous Diwali celebration! Here are some classy and elegant gift ideas for a {age}-year-old:</p>
            <p>{gift_ideas}</p>
            <img src="{gift_image}" alt="Gift Image">
        </div>
    </body>
    </html>
    """

    return html_code

if __name__ == "__main__":
    # Get user's age as input
    age = input("Enter the recipient's age: ")

    # Generate Diwali Gift Ideas
    gift_ideas = generate_gift_ideas(age)

    # Generate HTML code
    generated_html = generate_html_gift_ideas(age, gift_ideas)

    # Save the HTML code to a file
    with open("diwali_gift_ideas.html", "w", encoding="utf-8") as file:
        file.write(generated_html)

    print("Diwali Gift Ideas HTML generated successfully.")
