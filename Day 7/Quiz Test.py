logo='''
                        88            
                        ""            
                                      
 ,adPPYb,d8 88       88 88 888888888  
a8"    `Y88 88       88 88      a8P"  
8b       88 88       88 88   ,d8P'    
"8a    ,d88 "8a,   ,a88 88 ,d8"       
 `"YbbdP'88  `"YbbdP'Y8 88 888888888  
         88                           
         88  
'''
print(logo)
import random
print("Welcome to my Rapid Quiz Test program. Let's get started.\n")
everything_list = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "Harper Lee"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Fe"], "Au"),
    ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "Leonardo da Vinci"),
    ("What is the smallest prime number?", ["1", "2", "3", "5"], "2"),
    ("What year did the Titanic sink?", ["1912", "1905", "1898", "1923"], "1912"),
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], "Diamond"),
    ("Who is known as the father of modern physics?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "Albert Einstein"),
    ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
    ("What planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], "Mars"),
    ("How many continents are there on Earth?", ["5", "6", "7", "8"], "7"),
    ("What is the main ingredient in guacamole?", ["Tomato", "Onion", "Avocado", "Pepper"], "Avocado"),
    ("Who was the first President of the United States?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "George Washington"),
    ("What is the capital of Japan?", ["Beijing", "Seoul", "Tokyo", "Hong Kong"], "Tokyo"),
    ("In which year did World War I begin?", ["1914", "1912", "1920", "1939"], "1914"),
    ("What is the chemical symbol for silver?", ["Ag", "Au", "Pb", "Fe"], "Ag"),
    ("Who wrote the play 'Romeo and Juliet'?", ["William Shakespeare", "George Bernard Shaw", "Tennessee Williams", "Arthur Miller"], "William Shakespeare"),
    ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"], "Blue Whale"),
    ("What is the capital city of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "Canberra"),
    ("How many rings are on the Olympic flag?", ["3", "4", "5", "6"], "5"),
    ("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
    ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Michael Faraday"], "Alexander Graham Bell"),
    ("Which planet is known as the Morning Star?", ["Venus", "Mars", "Mercury", "Saturn"], "Venus"),
    ("What is the currency of Japan?", ["Yuan", "Won", "Yen", "Ringgit"], "Yen"),
    ("Who is known as the 'King of Pop'?", ["Elvis Presley", "Michael Jackson", "Prince", "David Bowie"], "Michael Jackson"),
    ("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Silver", "Iron"], "Oxygen"),
    ("Who was the 16th President of the United States?", ["Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "James Buchanan"], "Abraham Lincoln"),
    ("What is the largest island in the world?", ["New Guinea", "Greenland", "Borneo", "Madagascar"], "Greenland"),
    ("What is the capital of Canada?", ["Toronto", "Montreal", "Vancouver", "Ottawa"], "Ottawa"),
    ("In which country would you find the city of Cairo?", ["Egypt", "Greece", "Turkey", "Iran"], "Egypt"),
    ("What is the chemical symbol for lead?", ["Pb", "Fe", "Hg", "Zn"], "Pb"),
    ("What type of animal is the Komodo dragon?", ["Lizard", "Snake", "Crocodile", "Bird"], "Lizard"),
    ("Who discovered penicillin?", ["Louis Pasteur", "Alexander Fleming", "Joseph Lister", "Robert Koch"], "Alexander Fleming"),
    ("What is the largest country in the world by land area?", ["Russia", "Canada", "United States", "China"], "Russia"),
    ("What is the capital of Spain?", ["Barcelona", "Madrid", "Seville", "Valencia"], "Madrid"),
    ("What is the currency of the United Kingdom?", ["Euro", "Pound Sterling", "Dollar", "Franc"], "Pound Sterling"),
    ("What element does 'Na' represent on the periodic table?", ["Sodium", "Neon", "Nickel", "Nitrogen"], "Sodium"),
    ("Who painted the ceiling of the Sistine Chapel?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Titian"], "Michelangelo"),
    ("What is the smallest country in the world?", ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "Vatican City"),
    ("Which planet is known for its rings?", ["Saturn", "Uranus", "Neptune", "Jupiter"], "Saturn"),
    ("What is the boiling point of water in Celsius?", ["90", "100", "110", "120"], "100"),
    ("What is the largest desert in the world?", ["Sahara", "Gobi", "Antarctic", "Arabian"], "Antarctic"),
    ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Charlotte Brontë", "Emily Dickinson", "Mary Shelley"], "Jane Austen"),
    ("What is the capital of Italy?", ["Florence", "Venice", "Rome", "Milan"], "Rome"),
    ("What is the most abundant gas in Earth's atmosphere?", ["Oxygen", "Hydrogen", "Nitrogen", "Carbon Dioxide"], "Nitrogen"),
    ("What is the name of the longest river in South America?", ["Amazon", "Orinoco", "Paraná", "São Francisco"], "Amazon"),
    ("Who invented the light bulb?", ["Thomas Edison", "Nikola Tesla", "Michael Faraday", "James Watt"], "Thomas Edison"),
    ("What is the smallest planet in our solar system?", ["Mars", "Mercury", "Venus", "Pluto"], "Mercury"),
    ("What is the capital of Brazil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "Brasília")
]
total_questions = len(everything_list)
random.shuffle(everything_list)
score=0
n=1
for n in range(total_questions):
    questions = everything_list[n][0]
    options = everything_list[n][1]
    correct_answer = everything_list[n][2] 
    n+=1  
    print(f"Question {n}: {questions}")
    print(f"A. {options[0]}")
    print(f"B. {options[1]}")
    print(f"C. {options[2]}")
    print(f"D. {options[3]}")
    user_answer = input("Your answer (A-D): ").upper()
    if user_answer == "A" and options[0] == correct_answer:
        print("Correct Answer!!!!\n")
        score += 1
    elif user_answer == "B" and options[1] == correct_answer:
        print("Correct Answer!!!!\n")
        score += 1
    elif user_answer == "C" and options[2] == correct_answer:
        print("Correct Answer!!!!\n")
        score += 1
    elif user_answer == "D" and options[3] == correct_answer:
        print("Correct Answer!!!!\n")
        score += 1
    else:
        print(f"Wrong Answer!!!!!\nThe correct answer was {correct_answer}.\n")
print(f"\nYou scored {score} out of {total_questions}.")
percentage = (score / total_questions) * 100
print(f"You got {percentage:.2f}% right answers in this quiz.")
print("Thanks for using my Quiz program.")
