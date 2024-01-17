import requests
import os
import time
import webbrowser

class ImageGenerator:
    def __init__(self):
        self.headers = {"Authorization": "Bearer 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"}

    def sanitize_filename(self, filename):
        invalid_chars = r'<>:"/\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename

    def query_api(self, api_url, payload):
        response = requests.post(api_url, headers=self.headers, json=payload)
        return response.content

    def generate_variations(self, input_text):
        com = input_text.split()
        temp = ''
        for i in com[1:]:
            temp += i + ' '

        api1_url = "https://api-inference.huggingface.co/models/goofyai/3d_render_style_xl"
        api2_url = "https://api-inference.huggingface.co/models/goofyai/Leonardo_Ai_Style_Illustration"
        api3_url = "https://api-inference.huggingface.co/models/goofyai/cyborg_style_xl"
        var1 = "8k 3d render"
        var2 = "oil painting"
        var3 = "Cyborg style neon background"

        input_time = time.strftime("%Y%m%d%H%M%S")
        output_directory = r"C:\Users\harit\PycharmProjects\ALLI - Artificial Language Learning Interface\GenImages"
        os.makedirs(output_directory, exist_ok=True)

        # API 1 - GoofyGen
        input_var1 = f"{input_text} {var1}"
        image_bytes_var1 = self.query_api(api1_url, {"inputs": input_var1})

        # API 2  - Leonardo AI Style
        input_var2 = f"{input_text} {var2}"
        image_bytes_var2 = self.query_api(api2_url, {"inputs": input_var2})

        # API 2 - Cyborg style
        input_var3 = f"{input_text} {var3}"
        image_bytes_var3 = self.query_api(api3_url, {"inputs": input_var3})

        # API 4 - Anime style

        variations = [
            (image_bytes_var1, var1, api1_url),
            (image_bytes_var2, var2, api2_url),
            (image_bytes_var3, var3, api3_url),
        ]

        for i, (image_bytes, variation, model_name) in enumerate(variations):
            filename = f"{input_text[(len(input_text)//2):-1]}_{input_time}_{variation}_{model_name.split('/')[-1]}_{i + 1}.png"
            filename = self.sanitize_filename(filename)
            file_path = os.path.join(output_directory, filename)

            with open(file_path, "wb") as file:
                file.write(image_bytes)
            webbrowser.open(file_path)

        return f"generating {temp}"

if __name__ == "__main__":
    image_gen = ImageGenerator()
    user_input = input("Enter a text prompt: ")
    print(image_gen.generate_variations(user_input))
