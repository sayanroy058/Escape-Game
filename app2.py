import streamlit as st
import random
from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    text: str
    choices: List[str]
    correct_answer: str

@dataclass
class Room:
    name: str
    questions: List[Question]
    feedback: str
    background_image: str

# Initialize session state
if 'current_room' not in st.session_state:
    st.session_state.current_room = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_complete' not in st.session_state:
    st.session_state.game_complete = False

# Background images
backgrounds = [
    "https://img.freepik.com/free-photo/abstract-colorful-splash-3d-background-generative-ai-background_60438-2509.jpg",
    "https://img.freepik.com/free-photo/abstract-wavy-background_23-2150534036.jpg",
    "https://img.freepik.com/free-photo/vibrant-colors-flow-abstract-wave-pattern-generated-by-ai_188544-9781.jpg",
    "https://img.freepik.com/free-photo/abstract-flames-exploding-multi-colored-ink-paint-generated-by-ai_188544-15568.jpg",
    "https://img.freepik.com/free-photo/vibrant-yellow-blue-waves-showcase-modern-creativity-generated-by-ai_188544-9593.jpg"
]

# Room data
rooms = [
    Room(
        "Introduction Room",
        [
            Question("What is 7 + 2?", ["8", "9", "10", "11"], "9"),
            Question("What is 10 - 3?", ["5", "6", "7", "8"], "7"),
            Question("If you have 6 pencils and get 4 more, how many pencils do you have in total?", ["9", "10", "11", "12"], "10"),
            Question("What is 4 + 5?", ["8", "9", "10", "11"], "9"),
            Question("What is 12 - 8?", ["2", "3", "4", "5"], "4")
        ],
        "Great start! You've cracked the first code and can move to the next room.",
        backgrounds[0]
    ),
    Room(
        "The Library of Numbers",
        [
            Question("If you have 8 books and give 3 to a friend, how many books do you have now?", ["4", "5", "6", "7"], "5"),
            Question("What is 3 + 3 + 2?", ["6", "7", "8", "9"], "8"),
            Question("Solve the code: If there are 2 books on each shelf and there are 4 shelves, how many books are there?", ["6", "8", "10", "12"], "8"),
            Question("If you start with 9 stones and give away 2, how many are left?", ["6", "7", "8", "9"], "7"),
            Question("Find the sum: 4 + 5 + 1.", ["8", "9", "10", "11"], "10")
        ],
        "Great job! You’ve cracked the library’s code and the hidden door opens!",
        backgrounds[1]
    ),
    Room(
        "The Hall of Shapes",
        [
            Question("Which shape has no sides?", ["Triangle", "Square", "Circle", "Rectangle"], "Circle"),
            Question("How many sides does a square have?", ["3", "4", "5", "6"], "4"),
            Question("Which shape has 3 sides?", ["Circle", "Square", "Triangle", "Rectangle"], "Triangle"),
            Question("How many corners does a rectangle have?", ["3", "4", "5", "6"], "4"),
            Question("Which shape is round and has no corners?", ["Triangle", "Rectangle", "Circle", "Square"], "Circle")
        ],
        "You mastered the shapes! The next room unlocks!",
        backgrounds[2]
    ),
    Room(
        "The Dungeon of Word Problems",
        [
            Question("There are 8 birds on a tree. 3 fly away. How many are left?", ["5", "6", "7", "8"], "5"),
            Question("If you have 5 red marbles and 4 blue marbles, how many marbles do you have in total?", ["8", "9", "10", "11"], "9"),
            Question("Sarah has 7 cookies. She eats 2. How many cookies are left?", ["4", "5", "6", "7"], "5"),
            Question("There are 10 apples in a basket. 4 fall out. How many apples remain?", ["5", "6", "7", "8"], "6"),
            Question("Jack has 4 pets. His friend gives him 3 more. How many pets does Jack have now?", ["6", "7", "8", "9"], "7")
        ],
        "Well done! You’ve solved the dungeon’s riddles.",
        backgrounds[3]
    ),
    Room(
        "The Treasure Room",
        [
            Question("If you have 15 coins and give 5 to the Math Wizard, how many do you have left?", ["8", "9", "10", "11"], "10"),
            Question("The wizard has 20 potions and drinks 6. How many are left?", ["12", "13", "14", "15"], "14"),
            Question("If there are 7 keys and you find 3 more, how many keys do you have?", ["9", "10", "11", "12"], "10"),
            Question("The treasure chest has 8 jewels, and you add 2 more. How many jewels are in the chest?", ["9", "10", "11", "12"], "10"),
            Question("The wizard has 18 magic dust pouches and gives away 9. How many does he have now?", ["8", "9", "10", "11"], "9")
        ],
        "Congratulations! You have successfully reclaimed the Golden Calculator!",
        backgrounds[4]
    )
]

def main():
    st.set_page_config(page_title="Math Escape Room", layout="wide")
    
    # Apply background image using custom CSS
    background_style = f"""
    <style>
    .stApp {{
        background-image: url({rooms[st.session_state.current_room].background_image});
        background-size: cover;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    
    # Rest of the custom CSS
    st.markdown("""
        <style>
        .main-title {
            color: #FFD700;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
            padding: 20px;
            background: linear-gradient(45deg, rgba(0,0,0,0.7), rgba(0,0,0,0.3));
            border-radius: 15px;
            margin-bottom: 30px;
            font-family: 'Arial Black', sans-serif;
        }
        .question-text {
            color: white;
            font-size: 28px;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000000;
            padding: 30px;
            background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6));
            border-radius: 15px;
            margin-bottom: 30px;
            border: 2px solid rgba(255,255,255,0.1);
        }
        .choice-button {
            background-color: rgba(255, 255, 255, 0.9);
            color: black;
            padding: 15px;
            border-radius: 10px;
            margin: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 20px;
            font-weight: bold;
            width: 100%;
        }
        .choice-button:hover {
            transform: scale(1.05);
            background-color: rgba(255, 215, 0, 0.9);
        }
        .feedback {
            color: white;
            font-size: 24px;
            text-align: center;
            padding: 20px;
            background: linear-gradient(45deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6));
            border-radius: 15px;
            margin: 20px 0;
            border: 2px solid rgba(255,215,0,0.3);
        }
        .try-again {
            color: #FF0000;
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            margin: 20px 0;
            border: 3px solid #FF0000;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .sidebar-content {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 15px;
            color: white;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton button {
            width: 100%;
            font-size: 20px;
            font-weight: bold;
            background: linear-gradient(45deg, rgba(255,255,255,0.9), rgba(255,255,255,0.8));
            color: black;
            border: 2px solid rgba(0,0,0,0.1);
            border-radius: 10px;
            padding: 15px;
            margin: 5px 0;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: scale(1.02);
            background: linear-gradient(45deg, rgba(255,215,0,0.9), rgba(255,215,0,0.8));
        }
        </style>
        """, unsafe_allow_html=True)

    # Header
    st.markdown(f'<div class="main-title">Math Escape Room - {rooms[st.session_state.current_room].name}</div>', 
               unsafe_allow_html=True)
    
    current_room = rooms[st.session_state.current_room]
    current_question = current_room.questions[st.session_state.current_question]

    # Display question
    st.markdown(f'<div class="question-text">{current_question.text}</div>', unsafe_allow_html=True)

    # Create columns for answer choices
    col1, col2 = st.columns(2)

    # Display choices in columns
    with col1:
        for i in range(0, len(current_question.choices), 2):
            if st.button(current_question.choices[i], 
                        key=f"choice_{i}_{st.session_state.current_question}",
                        use_container_width=True):
                check_answer(current_question.choices[i], current_question.correct_answer)

    with col2:
        for i in range(1, len(current_question.choices), 2):
            if st.button(current_question.choices[i], 
                        key=f"choice_{i}_{st.session_state.current_question}",
                        use_container_width=True):
                check_answer(current_question.choices[i], current_question.correct_answer)

    # Display score and progress in sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown(f"### Score: {st.session_state.score}")
        st.progress((st.session_state.current_room * 5 + st.session_state.current_question) / 
                   (len(rooms) * 5))
        st.markdown('</div>', unsafe_allow_html=True)

def check_answer(selected_answer: str, correct_answer: str):
    if selected_answer == correct_answer:
        st.session_state.score += 1
        st.session_state.current_question += 1
        
        # Check if room is complete
        if st.session_state.current_question >= len(rooms[st.session_state.current_room].questions):
            st.markdown(f'<div class="feedback">{rooms[st.session_state.current_room].feedback}</div>', 
                       unsafe_allow_html=True)
            st.session_state.current_room += 1
            st.session_state.current_question = 0
            
            # Check if game is complete
            if st.session_state.current_room >= len(rooms):
                st.session_state.game_complete = True
                st.balloons()
                st.markdown('<div class="feedback">🏆 Congratulations! You have successfully reclaimed '
                          'the Golden Calculator! 🏆</div>', unsafe_allow_html=True)
            st.rerun()  # Changed from st.experimental_rerun()
    else:
        st.markdown('<div class="try-again">❌ Try Again! ❌</div>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()