import re
import random
import logging

# ---------------------------------------------------------------
# Setup logging for unknown queries
# ---------------------------------------------------------------
logging.basicConfig(
    filename='chatbot_unknowns.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# ---------------------------------------------------------------
# Step 1: Define Intents with Patterns and Responses
# ---------------------------------------------------------------
INTENTS = {
    'greeting': {
        'patterns': [r'\bhi\b', r'\bhello\b', r'\bhey\b'],
        'responses': ["Hi there!", "Hello!", "Hey! How can I help you today?"]
    },
    'faq_hours': {
        'patterns': [r'working hours', r'hours of (operation|service)'],
        'responses': ["Our working hours are 9 AM to 5 PM, Monday through Friday."]
    },
    'faq_location': {
        'patterns': [r'where.*(office|located)', r'\blocation\b', r'where do you operate'],
        'responses': ["We are located in New Delhi, India, and serve customers worldwide."]
    },
    'faq_order_status': {
        'patterns': [r'order status', r'shipping', r'delivery', r'track my order'],
        'responses': ["You can track your order using the link provided in your email."]
    },
    'faq_pricing': {
        'patterns': [r'\bprice\b', r'\bcost\b', r'\baffordable\b'],
        'responses': ["Our products are priced competitively. You can check our website for detailed pricing."]
    },
    'thanks': {
        'patterns': [r'\bthanks\b', r'\bthank you\b'],
        'responses': ["You're welcome!", "Anytime!", "Glad to help!"]
    },
    'farewell': {
        'patterns': [r'\bbye\b', r'\bgoodbye\b', r'\bsee you\b'],
        'responses': ["Goodbye! Have a great day!", "See you next time!", "Farewell!"]
    },
    'small_talk': {
        'patterns': [r'how are you\b', r"what's up", r'how is it going'],
        'responses': ["I'm just a bot, but I'm here to help!", "I'm doing well, thank you!", "I'm here to assist you!"]
    },
    'help': {
        'patterns': [r'\bhelp\b', r'\bsupport\b', r'\bassist\b'],
        'responses': ["How can I assist you?", "What do you need help with?", "I'm here to support you."]
    },
    'faq_contact': {
        'patterns': [r'contact number', r'phone number', r'how to contact'],
        'responses': ["You can contact us at +91-XXXXXXXXXX or via email at support@example.com."]
    },
    'faq_refund': {
        'patterns': [r'refund process', r'money back', r'how to get refund', r'cancel order', r'refund'],
        'responses': ["Refunds are processed within 5-7 business days. You can request a refund via your account dashboard."]
    },
    'faq_payment_methods': {
        'patterns': [r'payment options', r'how can I pay', r'accepted payment methods'],
        'responses': ["We accept credit cards, debit cards, PayPal, and online bank transfers."]
    },
    'faq_technical_issue': {
        'patterns': [r'not working', r'issue with website', r'error message'],
        'responses': ["Try clearing your cache or using a different browser. If the issue persists, contact our support team."]
    },
    'faq_discounts': {
        'patterns': [r'discounts', r'coupon code', r'promo offers'],
        'responses': ["We have seasonal discounts. Check our website for the latest promo codes."]
    }
}

# ---------------------------------------------------------------
# Step 2: Precompile Regular Expressions
# ---------------------------------------------------------------
compiled_intents = {
    intent: {
        'regexes': [re.compile(pattern, re.IGNORECASE) for pattern in data['patterns']],
        'responses': data['responses']
    }
    for intent, data in INTENTS.items()
}

# ---------------------------------------------------------------
# Step 3: Preprocess User Input
# ---------------------------------------------------------------
def preprocess_message(message):
    """
    Normalize the user message by converting to lowercase and stripping extra spaces.
    """
    return message.lower().strip()

# ---------------------------------------------------------------
# Step 4: Match User Message to an Intent
# ---------------------------------------------------------------
def match_intent(message):
    """
    Scans the user message against precompiled regex patterns.
    Returns the matching intent if found, or "unknown" if no match.
    """
    message = preprocess_message(message)
    for intent, data in compiled_intents.items():
        for regex in data['regexes']:
            if regex.search(message):
                return intent
    return "unknown"

# ---------------------------------------------------------------
# Step 5: Get a Response Based on the Matched Intent
# ---------------------------------------------------------------
def get_response(intent, user_message):
    """
    Returns an appropriate response for the detected intent.
    Logs any unrecognized queries for further analysis.
    """
    if intent in INTENTS:
        return random.choice(INTENTS[intent]['responses'])
    else:
        logging.info(f"Unknown query: {user_message}")
        return "I'm sorry, I didn't understand that. Let me connect you to our support team."

# ---------------------------------------------------------------
# Step 6: Main Chat Loop
# ---------------------------------------------------------------
def run_chatbot():
    """
    Runs the interactive terminal-based chatbot loop.
    Accepts user input until the user types 'bye' or 'exit.'
    """
    print("Welcome to Customer Support Chatbot! (Type 'bye' or 'exit' to quit.)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit']:
            print("Chatbot: Thank you! Goodbye!")
            break

        intent = match_intent(user_input)
        response = get_response(intent, user_input)
        print(f"Chatbot: {response}")

# ---------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------
if __name__ == "__main__":
    run_chatbot()


