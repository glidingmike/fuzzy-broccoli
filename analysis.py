def personality_test():
    print("Welcome to the Personality Test! Answer the following questions to learn about yourself.")

    # Question 1: Favorite color
    color = input("What is your favorite color and why? ")
    print("Interesting choice!")

    # Question 2: Favorite animal
    animal = input("What is your favorite animal and why? ")
    print("Great choice!")

    # Question 3: Waterfall, lake, or sea
    nature = input("Do you prefer a waterfall, a lake, or the sea, and why? ")
    print("Got it!")

    print("\nAnalyzing your responses...\n")

    # Analysis
    # Color analysis
    if "blue" in color.lower():
        print("You value peace and stability. Blue reflects a calm and thoughtful personality.")
    elif "red" in color.lower():
        print("You are bold, passionate, and unafraid to take risks. Red symbolizes energy and determination.")
    elif "green" in color.lower():
        print("You appreciate balance and growth. Green reflects a connection to nature and harmony.")
    elif "yellow" in color.lower():
        print("You are cheerful, optimistic, and creative. Yellow represents a bright and enthusiastic outlook.")
    else:
        print("Your favorite color reveals your individuality and unique way of seeing the world!")

    # Animal analysis
    if "dog" in animal.lower():
        print("You are loyal and value strong relationships. Dogs often reflect warmth and trustworthiness.")
    elif "cat" in animal.lower():
        print("You are independent, curious, and enjoy exploring new perspectives. Cats represent self-reliance.")
    elif "bird" in animal.lower():
        print("You crave freedom and new experiences. Birds symbolize vision and an expansive mindset.")
    elif "horse" in animal.lower():
        print("You value strength, freedom, and a deep connection to nature. Horses reflect a spirited personality.")
    else:
        print("Your favorite animal reveals a unique part of your character and how you relate to the world.")

    # Nature setting analysis
    if "waterfall" in nature.lower():
        print("You are drawn to energy, power, and transformation. Waterfalls represent dynamic change and inspiration.")
    elif "lake" in nature.lower():
        print("You value peace, reflection, and emotional depth. Lakes symbolize tranquility and inner clarity.")
    elif "sea" in nature.lower():
        print("You are adventurous, open-minded, and connected to the vast possibilities of life. The sea represents boundlessness.")
    else:
        print("Your choice of natural setting reflects your personal view of beauty and where you find solace.")

    print("\nThank you for taking the Personality Test! Remember, this is just for fun and not a scientific assessment.")

# run
personality_test()