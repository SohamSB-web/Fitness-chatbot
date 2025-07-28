AI Fitness Coach Chatbot

This is a Python-based command-line chatbot that acts as a personal AI fitness coach. Powered by the high-speed Groq API, it generates custom workout plans instantly based on your specific goals.

Features

  * Dynamic Workout Generation: Get unique workout plans tailored to your requests. No pre-canned responses\!
  * Natural Language Understanding: Simply ask for what you want, like "a 20-minute ab workout" or "a routine to build upper body strength."
  * Blazing Fast: Leverages the Groq API for near-instantaneous responses from the Llama 3 language model.
  * Focused and Safe: The chatbot is designed to only respond to fitness-related queries, ensuring it stays on topic.

How It Works

The application prompts the user for their fitness goal. This input is then sent to the Groq API with a carefully crafted prompt that instructs the AI to act as an expert fitness coach. The model generates a complete workout plan, which is then printed directly to the console.

Technology Stack

  * Language: Python
  * AI/LLM Provider: Groq
  * Model: `llama3-70b-8192`
  * API Wrapper: `openai` Python library

## Setup and Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  Install dependencies:

    ```bash
    pip install openai
    ```

3.  Set up your API Key:
    Get your free API key from [Groq](https://console.groq.com/keys). Then, set it as an environment variable.

      * On macOS/Linux:
        ```bash
        export GROQ_API_KEY='your_api_key_here'
        ```
      * On Windows:
        ```bash
        set GROQ_API_KEY=your_api_key_here
        ```

4.  Run the chatbot:

    ```bash
    python your_script_name.py
    ```
