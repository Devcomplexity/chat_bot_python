# chat_bot_python
A standard rule based chatbot, trying to test what i learned 
# Customer Support Chatbot

## Overview

This is a rule-based chatbot built using Python that handles basic customer service interactions via the terminal. It leverages regular expressions to match user intents (like greetings or frequently asked questions) and responds accordingly. The project is designed with performance improvements and logging for unknown queries, which helps in future refinement and expansion.

## Features

- **Intent Recognition:**  
  Uses regex to identify and match various user inputs such as greetings and FAQs.

- **Precompiled Regex Patterns:**  
  Improves efficiency by precompiling patterns with case-insensitive matching.

- **Dynamic Responses:**  
  Chooses random responses from a predefined set, making conversation feel more natural.

- **Logging Unknown Queries:**  
  Unknown or unmapped queries are logged (in `chatbot_unknowns.log`) for analysis and future improvements.

- **Terminal Interface:**  
  Operates directly from the command line, facilitating easy testing and use.

## Requirements

- Python 3.6 or higher

## How to Run

1. **Clone or download the repository.**

2. **Navigate to the project directory** in your terminal.

3. **Run the chatbot:**
   ```bash
   python chatbot.py
