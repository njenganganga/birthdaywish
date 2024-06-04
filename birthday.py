import random

def generate_birthday_quote():
    quotes = [
        "May your birthday be filled with sunshine and smiles, laughter, love, and cheer.",
        "Wishing you a day filled with happiness and a year filled with joy.",
        "Hope your special day brings you all that your heart desires!",
        "May all your wishes come true today and always.",
        "Here's to a bright, healthy, and exciting future, Happy Birthday!"
        "On your special day, may you be surrounded by those who love and cherish you. Happy Birthday to the one who makes every day brighter!"
        "Another year of your life has passed, but your heart remains as young and vibrant as ever. Wishing you a birthday filled with endless joy and unforgettable moments."
        "Birthdays are the universe's way of celebrating you. May your day be as beautiful and extraordinary as the impact you've made on the lives of those around you."
        "Your birthday is a reminder of all the wonderful moments we’ve shared and the beautiful memories yet to be made. Cheers to a year filled with love, laughter, and boundless happiness."
        "May your birthday be the start of a year filled with good luck, good health, and much happiness. Your presence is a gift to the world, and I’m grateful for every moment with you."
        "As you blow out the candles, may each flame carry a wish for your heart's deepest desires. Happy Birthday to someone who is loved more than words can express."
        "Every year with you is a treasure, and your birthday is a golden milestone on this journey of life. May your path ahead be paved with success and joy."
        "Happy Birthday! May your special day be as enchanting as the smile that lights up your face and as magical as the love that fills your heart."
        "Wishing you a birthday filled with the love of family, the joy of friends, and the warmth of good memories. You deserve all the happiness in the world."
        "On this beautiful day, we celebrate the gift of your life. May your birthday be filled with the same joy and wonder that you bring into the lives of others."
    ]
    return random.choice(quotes)

def create_birthday_message():
    # Ask for the user's name
    name = input("What is your name? ")

    # Generate a sentimental birthday quote
    quote = generate_birthday_quote()

    # Create a personalized birthday message
    birthday_message = f"Celebrating you today and always, {name}! 🎉🎂 {quote} Have a fabulous birthday. "

    # Print the birthday message
    print(birthday_message)

# Run the function to create the birthday message
create_birthday_message()
