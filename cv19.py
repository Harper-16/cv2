import html
import random
import requests

def fetch_questions():
    """Fetches 5 multiple-choice questions from the Open Trivia Database API."""
    url = "https://opentdb.com"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['results']
        else:
            print("Error: Could not retrieve data from the quiz server.")
            return []
    except requests.exceptions.RequestException:
        print("Network error: Please check your internet connection.")
        return []

def run_quiz():
    """Runs the interactive command-line trivia quiz game."""
    questions = fetch_questions()
    
    # Exit early if the API call failed or returned empty
    if not questions:
        print("Unable to start quiz without questions.")
        return
        
    score = 0
    
    for i, q in enumerate(questions, 1):
        
        # Decode HTML entities and prepare options
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]
        
        # Create and shuffle options
        options = incorrects + [correct]
        random.shuffle(options)
        
        # Display question
        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
            
        # Get and validate user input
        while True:
            try:
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <= 4:
                    break
            except ValueError:
                pass
            print("Invalid input! Please enter 1-4")
            
        # Check answer
        if options[choice-1] == correct:
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"X Wrong! Correct answer: {correct}\n")
            
    # Display final results
    print(f"Final Score: {score}/{len(questions)}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")

if __name__ == "__main__":
    run_quiz()
