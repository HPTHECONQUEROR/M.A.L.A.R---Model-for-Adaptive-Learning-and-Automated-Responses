import requests

class RunMalar:
    def RunBot(self, command):
        try:
            api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(api_url, headers=headers, json=payload)
                return response.json()

            with open("text files/userdata.txt", "r") as file:
                lines = file.readlines()

            if len(lines) < 2 or lines[0].strip() == "<User Data> ---- THIS IS AN HIGHLY ENCRYPTED":
                ind = 4
            else:
                ind = len(lines) + 1

            new_content = f"<user>: {command} <u/> <malar>: {self.get_bot_response(command)} <m/>\n"
            lines.insert(ind - 1, new_content)

            with open("text files/userdata.txt", "w") as file:
                file.writelines(lines)

            return self.get_bot_response(command).title()

        except Exception as e:
            print(e)
            self.RunBot(command)

    def get_bot_response(self, command):
        content1 = self.read_file_content("text files/userdata.txt")
        content2 = self.read_file_content("text files/malarPrompt.txt")
        content = content1 + content2
        output = self.query_model(content, command)
        outn = output.find("<|malar|>")
        out = output[outn + 10:]
        end = out.find("<m/>")
        out = out[:end]
        result = out.split('\n', 1)[0].capitalize()
        return result

    def query_model(self, content, command):
        api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        headers = {"Authorization": "Bearer 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"}
        payload = {"inputs": f'''{content} <story starts>  <|user|> {command} <u/> Malar Reacts to user's reply <|malar|> '''}
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()[0]["generated_text"]

    def read_file_content(self, filename):
        with open(filename, "r") as file:
            content = file.read().replace('\n', '')
        return content


if __name__ == "__main__":
    Alli = RunMalar()
    out = Alli.RunBot("?")
    print(out)
