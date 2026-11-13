"""
DecodeLabs - Project 1: Rule-Based AI Chatbot
Architecture: Input -> Process -> Output (IPO model)
Run: python chatbot.py
"""

# KNOWLEDGE BASE: dictionary of intents (key -> response), O(1) lookup
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's up?",
    "salam": "Walaikum Assalam! Kaise help karoon?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "what is your name": "I'm DecoBot, a rule-based AI chatbot.",
    "who made you": "I was built by Minahil as part of the DecodeLabs AI internship.",
    "what is ai": "AI is the ability of machines to perform tasks that normally need human intelligence.",
    "what is python": "Python is a high-level programming language popular in AI and data science.",
    "help": "Try: hello, how are you, what is your name, what is ai, what is python, bye.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}
FALLBACK = "I do not understand. Type 'help' to see what I can answer."


def sanitize(raw_text):
    """Phase 1: normalize case, whitespace and trailing punctuation."""
    return raw_text.lower().strip().rstrip("?!.,")


def main():
    print("DecoBot: Hello! I'm DecoBot. Type 'bye' to exit.")
    while True:                                   # continuous loop
        raw_input_text = input("You: ")           # INPUT
        clean_input = sanitize(raw_input_text)    # SANITIZATION

        if clean_input in EXIT_COMMANDS:          # EXIT STRATEGY
            print("DecoBot: Goodbye! Have a great day.")
            break

        if not clean_input:                       # empty input guard
            continue

        reply = responses.get(clean_input, FALLBACK)  # PROCESS: lookup + fallback
        print(f"DecoBot: {reply}")                # OUTPUT


if __name__ == "__main__":
    main()
