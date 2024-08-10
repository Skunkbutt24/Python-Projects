import random

# Word list
word_list = [
    # A words
    "apple", "ant", "axe", "apricot", "arm", "atom", "asthma", "angel", "aim", "art",
    "alley", "address", "affect", "attempt", "arrival", "ability", "appetite", "acquire", "actor", "abandon",
    "adventure", "adopt", "analyze", "articulate", "aspire", "article", "approve", "ancestor", "attempt", "anatomy",
    "aluminum", "activate", "action", "assume", "admission", "appreciate", "alarm", "aroma", "angle", "archive",
    "agreement", "ambition", "adapt", "amount",
    
    # B words
    "banana", "ball", "bat", "bag", "box", "bus", "bottle", "bike", "bake", "boat",
    "bread", "broom", "building", "button", "brave", "bird", "book", "brother", "bacon", "base",
    "blouse", "bicycle", "balance", "blanket", "baker", "bark", "bricks", "bachelor", "bore", "beach",
    "barrier", "breeze", "business", "bridge", "biography", "bronze", "buzz", "bungee", "billion", "bravery",
    "bargain", "brilliance", "bubble", "ballet", "bonfire",
    
    # C words
    "cat", "car", "cup", "cake", "coat", "cane", "city", "cold", "corn", "chair",
    "cage", "clock", "cloud", "candy", "camel", "crab", "crow", "celebrate", "council", "canvas",
    "cycle", "cucumber", "capital", "current", "course", "calendar", "concept", "create", "community", "collaborate",
    "capture", "control", "culture", "camera", "charity", "charge", "cluster", "complete", "chemistry", "courage",
    "compete", "climate", "costume", "clothing", "committee", "chronic",
    
    # D words
    "dog", "duck", "door", "doll", "desk", "dice", "day", "dust", "dome", "dream",
    "diner", "date", "donkey", "dragon", "dance", "duty", "dish", "dolphin", "deer", "doctor",
    "distance", "deliver", "dinner", "diamond", "danger", "divide", "doubt", "delight", "distant", "demand",
    "detect", "discuss", "delicate", "design", "develop", "depend", "display", "decrease", "destroy", "defend",
    "definite", "desire", "decent", "discover", "department",
    
    # E words
    "elephant", "egg", "ear", "engine", "eye", "earth", "eat", "eggplant", "excited", "envelope",
    "exit", "electric", "expert", "event", "eagle", "erase", "entertain", "energy", "engineer", "educate",
    "example", "execute", "enjoy", "expand", "effort", "exercise", "elegant", "enhance", "examine", "enrich",
    "emergency", "essential", "emerge", "express", "engage", "education", "excuse", "embody", "encounter", "element",
    "evidence", "efficient", "expect", "evident",
    
    # F words
    "fish", "frog", "flower", "fence", "fan", "fork", "fast", "fall", "fruit", "fire",
    "furniture", "focus", "find", "future", "funny", "fact", "flag", "finish", "freedom", "family",
    "friend", "failure", "famous", "fitness", "fraction", "furnace", "fashion", "forever", "finance", "fantasy",
    "fairy", "fold", "fantastic", "feather", "foster", "fruitful", "forest", "frost", "frequent", "feature",
    "feedback", "fascinate", "factory",
    
    # G words
    "goat", "gift", "game", "glove", "green", "grape", "gold", "goal", "garage", "grill",
    "great", "grow", "glue", "globe", "guitar", "grand", "giraffe", "golf", "gap", "grocery",
    "group", "gather", "garden", "groom", "gallery", "grace", "glow", "govern", "gadget", "gravity",
    "gesture", "generate", "garnish", "growth", "guardian", "gameplay", "graceful", "glimpse", "generate",
    "genuine", "gathering", "galaxy", "gradient", "glitter", "gaze",
    
    # H words
    "hat", "house", "hand", "honey", "hill", "horse", "hope", "hard", "hike", "hot",
    "hello", "height", "hair", "hammer", "heat", "health", "hatch", "hobby", "huge", "hug",
    "history", "hotel", "harmony", "human", "hunt", "horizon", "hero", "habitat", "humor", "highlight",
    "habit", "helicopter", "honest", "heroic", "hardware", "headline", "harness", "hurdle", "hasty", "hustle",
    "hollow",
    
    # I words
    "ice", "igloo", "iron", "idea", "ink", "inch", "island", "item", "income", "image",
    "internet", "insect", "invisible", "involve", "invade", "interest", "important", "illness", "instrument", "isolate",
    "invention", "input", "imagine", "inform", "institute", "include", "inject", "indicate", "intelligent",
    "inspire", "influence", "innovation", "incorporate", "immigrant", "intricate", "infect", "impact",
    "inquiry", "intense", "increase", "interview", "indoor",
    
    # J words
    "jack", "jacket", "jam", "jelly", "joke", "jug", "juice", "jungle", "jump", "jellybean",
    "jewel", "jockey", "jog", "joy", "junior", "jar", "judge", "jazz", "jumper", "jury",
    "journal", "jester", "jovial", "juggle", "jeep", "jumpy"
]

# Hangman art
logo = r"""
╔═╗┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬╔═╗
╠╣__        __   _                            _          _   _                 
╠╣\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___          
╠╣ \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \         
╠╣  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/         
╠╣ _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/__ \__|_| |_| \___|         
╠╣| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __    / ___| __ _ _ __ ___   ___   
╠╣| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |  _ / _` | '_ ` _ \ / _ \  
╠╣|  _  | (_| | | | | (_| | | | | | | (_| | | | | | |_| | (_| | | | | | |  __/_ 
╠╣|_| |_|\__,_|_|_|_|\__, |_|_|_| |_| \__,_|_|_|_|  \____|\__,_|_| |_| |_|\___(_) 
╠╣| |    ___| |_( )__|___/ ___| ___| |_  / ___|| |_ __ _ _ __| |_ ___  __| |  _ 
╠╣| |   / _ \ __|// __| | |  _ / _ \ __| \___ \| __/ _` | '__| __/ _ \/ _` | (_) 
╠╣| |__|  __/ |_  \__ \ | |_| |  __/ |_   ___) | || (_| | |  | ||  __/ (_| |  _ 
╠╣|_____\___|\__| |___/  \____|\___|\__| |____/ \__\__,_|_|   \__\___|\__,_| (_) 
╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
"""



stages = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

# Main game logic

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Create a display list with underscores for each letter in the chosen word
display = ["_" for _ in range(word_length)]

# Display the number of letters in the word
print(f"The word has {word_length} letters: {' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True

    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True

    # Display the current hangman stage
    print(stages[6 - lives])

# Reveal the chosen word at the end with the win/lose message
if lives > 0:
    print(f"You win! The word was: {chosen_word}")
else:
    print(f"You lose! The word was: {chosen_word}")
    
