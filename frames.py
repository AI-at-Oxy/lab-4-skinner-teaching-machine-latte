"""
Skinner Teaching Machine - Frame Definitions
COMP 395: AI and Learning Technologies

This file contains the instructional frames for your teaching machine.

=============================================================================
YOUR TASK:
=============================================================================
1. Choose a topic you want to teach (5-10 frames minimum)
2. Design your frame structure (see options below)
3. Write frames that follow Skinner's principles:
   - Small steps: Each frame teaches ONE small concept
   - Build sequentially: Later frames build on earlier ones
   - High success rate: Design for ~95% correct answers
   - Clear prompts: Unambiguous fill-in-the-blank or short answer

=============================================================================
FRAME STRUCTURE OPTIONS:
=============================================================================

OPTION A - Minimal:
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris"
}

OPTION B - With feedback (RECOMMENDED):
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris",
    "feedback_correct": "Correct! Paris is the capital of France.",
    "feedback_incorrect": "Not quite. The answer is Paris."
}

OPTION C - Rich (with hints and multiple answers):
frame = {
    "prompt": "What keyword defines a function in Python?",
    "answer": "def",
    "answers": ["def"],  # List for multiple acceptable answers
    "hint": "It's a 3-letter word.",
    "feedback_correct": "Yes! 'def' is used to define functions.",
    "feedback_incorrect": "Not quite. We use 'def' to define functions.",
    "topic": "python-functions"
}

Choose a structure and be CONSISTENT across all your frames!
=============================================================================
"""

# =============================================================================
# EXAMPLE FRAMES: Introduction to Python Variables
# Replace these with your own topic!
# =============================================================================

FRAMES = [
    # Frame 1: Period
    {
        "prompt": "At the end of a declarative sentence, we use a _____. ",
        “answer”: “.”,
        "answer": "period",
        "feedback_correct": "Correct! Periods are used to mark the end of a declarative sentence.",
        "feedback_incorrect": "Not quite. We use the period to end a sentence."
    },
    
    # Frame 2: Question Mark
    {
        "prompt": "At the end of an interrogative sentence we use a ______. ",
        "answer": "?",
        “answer”: “question mark”,
        "feedback_correct": "Yes! The question mark indicates a question has been asked.",
        "feedback_incorrect": "Not quite. We use the question mark (?) sign."
    },
    
    # Frame 3: Exclamation Point
    {
        "prompt": "At the end of an exclamatory sentence we use a ______.",
        "answer": "exclamation point",
        “answer”: “!”,
        "feedback_correct": "Correct! The exclamation point indicates an exclamatory sentence has been made .",
        "feedback_incorrect": "Remember, we use the exclamation point (!) to indicate a sentence with strong emotions has been made.”
    },
    
    # Frame 4: Complete the sentence
    {
        "prompt": "Light takes about 8 minutes to travel from the Sun to Earth, but up to 40,000 years to travel from the Sun's core to its surface _",
        "answer": ".",
        "feedback_correct": "Yes! This sentence has a period (.) at the end of it.",
        "feedback_incorrect": "Not quite. This sentence has a period (.) at the end of it."
    },
    
    # Frame 5: Complete the sentence
    {
        "prompt": "What time is it _",
        "answer": "?",
        "feedback_correct": "Correct! This sentence indicates a question is being asked, therefore the correct punctuation mark is (?).",
        "feedback_incorrect": "Not quite. The punctuation at the end of this sentence should be (?). ""
    },
    
    # Frame 6: Complete the sentence
    {
        "prompt": "Happy Birthday_",
        "answer": "!",
        "feedback_correct": "Right! This sentence would end with an exclamation point (!).",
        "feedback_incorrect": "This sentence would end with an exclamation point (1)."
    },



# =============================================================================
# TIPS FOR WRITING GOOD FRAMES:
# =============================================================================
# 
# 1. START EASY: First frames should be very simple
# 
# 2. ONE CONCEPT PER FRAME: Don't combine multiple ideas
# 
# 3. USE BLANKS STRATEGICALLY: 
#    "In Python, we use _____ to define a function."
#    Not: "What do we use to define a function in Python?"
# 
# 4. BUILD ON PREVIOUS FRAMES: Frame 5 can reference concepts from Frame 3
# 
# 5. ANTICIPATE ERRORS: Your feedback_incorrect should address common mistakes
# 
# 6. NORMALIZE ANSWERS: The app converts to lowercase and strips whitespace,
#    but consider if "=" and "equals" should both be accepted
#
# =============================================================================
