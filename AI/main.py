"""main"""
import ollama

# Model to use
MODEL_NAME = "deepseek-r1:1.5b"

# Store conversation history
messages = []

def chat():
    print("🤖 DeepSeek R1 Chat (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # Append user message to history
        messages.append({"role": "user", "content": user_input})

        # Get model response with streaming
        print("DeepSeek:", end=" ", flush=True)
        response_text = ""
        for chunk in ollama.chat(model=MODEL_NAME, messages=messages, stream=True):
            text = chunk["message"]["content"]
            response_text += text
            print(text, end="", flush=True)

        print("\n")  # Newline for formatting

        # Append model response to history
        messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    chat()
