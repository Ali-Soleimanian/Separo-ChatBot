# Separo ChatBot (sematic parrot)

Separo is a multi-language chatbot powered by [LangChain](https://github.com/langchain-ai/langchain), [Streamlit](https://streamlit.io/), and Groq API. It offers user authentication, customizable assistant personalities, and supports over 30 languages.

## Features

- User registration and login
- Secure API key management per user
- Multi-language support
- Multiple assistant personalities (friendly, professional, casual, etc.)
- Chat history with memory
- Account management (logout, delete account)
- Dockerized for easy deployment

## Installation

### Prerequisites

- Python 3.13+
- [Groq API Key](https://console.groq.com)
- Docker (optional)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/separo.git
    cd separo
    ```

2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run run.py
    ```

### Docker

To build and run with Docker Compose:
```bash
docker compose up --build
```

## Usage

- Register a new account or login.
- Enter your Groq API key in the Options sidebar.
- Select your preferred language, model, and assistant personality.
- Start chatting!

## Project Structure

- `core/` – Authentication, database, chat logic
- `config/` – Settings and options
- `ui/` – Streamlit UI components
- `run.py` – Main entry point

## License

MIT

## Author

Ali Soleimanian – [alisoleimanian.it@gmail.com](mailto:alisoleimanian.it@gmail.com)