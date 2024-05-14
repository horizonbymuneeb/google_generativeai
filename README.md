
# Google Generative AI

Google Generative AI is a Python package that provides tools for working with Google's generative AI models.

## Installation

You can install the package using pip:

```bash
pip install google_ai
```

## Usage

```python
from google_ai import GenerativeModel

model = GenerativeModel(model_name="gemini-1.5-flash-latest", api_key="YOUR_API_KEY_HERE")
response = model.start_chat("Hello, how are you?")

print("Response:")
print(response.text)
print("Chat History:")
print(response.history)
```

## Configuration

You need to set your API key before using the package. You can set it using the `configure` method:

```python
import os
from google_ai import configure

configure(api_key=os.getenv("GEMINI_API_KEY"))
```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

Replace `"YOUR_API_KEY_HERE"` with your actual API key. Feel free to customize the content and formatting to better suit your package.