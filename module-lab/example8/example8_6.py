# Python3 program for a word frequency
# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from collections import Counter

def start(url):
    # Fetch the webpage using the URL
    source_code = requests.get(url).text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(source_code, 'html.parser')

    # Initialize an empty list to store the words
    wordlist = []

    # Find all 'div' elements with the 'entry-content' class and extract text
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # Convert text to lowercase and split into words
        words = content.lower().split()

        # Add words to the wordlist
        for each_word in words:
            wordlist.append(each_word)

    # Clean the word list and create the frequency dictionary
    clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    # Initialize an empty list to store clean words
    clean_list = []

    # Define symbols to be removed from words
    symbols = "!@#$%^&*()_-+={[}]|\\;:\"<>?/.,"

    # Clean the words in the wordlist
    for word in wordlist:
        for symbol in symbols:
            word = word.replace(symbol, '')

        # Only add non-empty words to the clean list
        if len(word) > 0:
            clean_list.append(word)

    # Create a dictionary and count word frequencies
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    # Create a Counter object to count word frequencies
    word_count = Counter(clean_list)

    # Get the 10 most common words
    top = word_count.most_common(10)

    # Print the top 10 most common words
    print("Top 10 most frequent words:")
    for word, count in top:
        print(f'{word}: {count}')

if __name__ == "__main__":
    # Replace the URL with the webpage you want to scrape
    url = 'https://techcrunch.com/2023/08/22/microsoft-is-bringing-python-to-excel/'

    # Call the start function with the URL
    start(url)
