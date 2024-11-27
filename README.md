# CodeAlpha

# How It Works: Hangman Game in Python

The program randomly selects a word from the word_list.
The player guesses one letter at a time. If the letter is in the word, it is revealed in the correct positions.
The player has a limited number of incorrect guesses (attempts_left), set to 6 in this example.
The game ends either when the player correctly guesses the entire word or runs out of attempts.

# Stock Portfolio Tracker
Features:
Add Stock: Users can add a stock ticker and specify the number of shares.
Remove Stock: Users can remove a stock by its ticker symbol.
Display Portfolio: Displays the portfolio with real-time stock prices and calculates the total portfolio value.
Real-Time Data: Utilizes the yfinance library to fetch live stock prices.
Example Run:
Menu:
markdown
Copy code
--- Stock Portfolio Tracker ---
1. Add Stock
2. Remove Stock
3. Display Portfolio
4. Exit
Enter your choice:
Output for Portfolio Display:
perl
Copy code
Fetching real-time stock data...

+----------+---------+---------+---------+
| Ticker   | Shares  | Price   | Value   |
+----------+---------+---------+---------+
| AAPL     | 10      | $174.50 | $1745.00|
| TSLA     | 5       | $242.30 | $1211.50|
+----------+---------+---------+---------+

Total Portfolio Value: $2956.50
Notes:
Replace the yfinance library with a different API if needed, such as Alpha Vantage, by modifying the fetch_stock_data method.
This program uses real-time data but requires an internet connection.
The tabulate library formats data into a neat table. You can customize the display as needed.

# Basic Chatbot
Explanation:
First Version (Basic):

Matches input using simple keyword-based logic.
Responses are pre-defined and selected randomly for variety.
Second Version (Advanced):

Uses NLTK's Chat class for pattern matching.
Utilizes regular expressions to make the chatbot more dynamic.
Reflections are used to adapt user input for more natural responses (e.g., "I am" → "You are").
Example Run:
Input:
vbnet
Copy code
You: Hello
Chatbot: Hi there!
You: What is your name?
Chatbot: I am a chatbot. You can call me Chatbot!
You: Bye
Chatbot: Goodbye! Take care!
Output:
A friendly chatbot that responds to user inputs using pre-defined patterns or responses.

Enhancements:
Use spaCy for better NLP capabilities (e.g., named entity recognition, dependency parsing).
Integrate APIs (like OpenAI's GPT models) for advanced conversational abilities.
Add custom features like learning new responses during the chat.
