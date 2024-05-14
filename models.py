import google.generativeai as genai

class GenerativeModel:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.api_key = api_key
        self.model = None

    def start_chat(self, input_text):
        if not self.model:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                safety_settings=self._get_safety_settings(),
                generation_config=self._get_generation_config()
            )

        chat_session = self.model.start_chat(history=[])
        response = chat_session.send_message(input_text)
        return response


    def _get_safety_settings(self):
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]
        return safety_settings

    def _get_generation_config(self):
        return {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
