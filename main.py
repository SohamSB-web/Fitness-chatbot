import os
from openai import OpenAI

# --- Configuration ---
# IMPORTANT: For this script to work, you need to set up your Groq API key.
# 1. Get your API key from https://console.groq.com/keys
# 2. Set it as an environment variable named 'GROQ_API_KEY'.
#    - On Windows: set GROQ_API_KEY=your_api_key_here
#    - On macOS/Linux: export GROQ_API_KEY=your_api_key_here
#
# You will also need to install the library:
# pip install openai

try:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not found.")
    
    # Point the OpenAI client to the Groq API
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

except Exception as e:
    print(f"Error during API client setup: {e}")
    print("Please make sure your GROQ_API_KEY is set correctly.")
    # Exit if the API key is not configured, as the bot cannot function.
    exit()

# --- AI Model Interaction ---
def generate_workout_from_groq(user_input):
    """
    Uses the Groq-powered model to generate a workout plan from the user's input.

    Args:
        user_input (str): The natural language input from the user.

    Returns:
        str: A formatted workout plan or a refusal message.
    """
    # The prompt remains the same, guiding the LLM on its role and response format.
    prompt = f"""
    You are an expert fitness coach chatbot. Your ONLY function is to create a personalized workout plan based on the user's request.

    The user's request is: "{user_input}"

    **Your Task:**
    1.  Analyze the user's request to determine if it is about fitness.
    2.  If the request is about fitness, generate a clear, concise, and safe workout plan. The plan MUST include:
        - A suitable title.
        - A brief, encouraging description.
        - A list of 4-6 exercises with sets and reps/duration.
        - A reminder to warm up and cool down.
    3.  If the user's request is NOT about fitness (e.g., asking for a joke, a story, a recipe, math help, etc.), you MUST strictly respond with the following sentence and nothing else: "I am programmed only to help with workout plans."
    """

    try:
        # Create the chat completion request to the Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192", # Using a powerful model available on Groq
        )
        # Extract the response content
        return chat_completion.choices[0].message.content
            
    except Exception as e:
        print(f"An error occurred while calling the Groq API: {e}")
        return "Sorry, I'm having trouble creating a workout right now. Please try again later."

# --- Chatbot Functions ---
def welcome_message():
    """Prints the welcome message for the user."""
    print("\n-----------------------------------------")
    print("💪 Welcome to your AI Fitness Coach! 💪")
    print("        (Powered by Groq)          ")
    print("-----------------------------------------")
    print("I can create a personalized workout plan for you.")
    print("Be specific! Try 'a 30-minute workout for my legs at home' or 'a quick cardio routine for the gym'.")
    print("Type 'help' for more examples or 'exit' to quit.")
    print()

def show_help():
    """Prints the help message."""
    print("\nHow I can help:")
    print("  - Just tell me your goal in plain English and I'll generate a plan!")
    print("\nExample requests:")
    print("  'Create a beginner workout for building muscle at the gym.'")
    print("  'I need a 15-minute ab workout with no equipment.'")
    print("  'A workout to improve my stamina for running.'")
    print("\nOther commands:")
    print("  'help' - Show this message.")
    print("  'exit' - Quit the chatbot.")
    print()

def main():
    """Main function to run the chatbot loop."""
    welcome_message()
    
    while True:
        user_input = input("What kind of workout do you want today? > ").strip()
        
        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("\nGreat work today! Keep it up. Goodbye! 👋")
            break
        elif user_input.lower() == "help":
            show_help()
        else:
            # Use Groq to generate a workout plan from scratch
            print("\nOkay, creating a custom workout plan for you (at Groq speed!)...")
            workout_plan = generate_workout_from_groq(user_input)
            print("-----------------------------------------")
            print(workout_plan)
            print("-----------------------------------------")


if __name__ == "__main__":
    main()