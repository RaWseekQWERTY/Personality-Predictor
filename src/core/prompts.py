def get_prompt(user_answer: list) -> str:
    gemini_prompt = f'''
        Given someone who approaches problems by {user_answer[0]},
        prefers to spend their free time {user_answer[1]},
        handles unexpected changes by {user_answer[2]},
        makes decisions based on {user_answer[3]},
        and communicates with others {user_answer[4]},
        what is their likely MBTI type? Additionally,
        describe their personality and how they might handle various situations.
    '''

    return gemini_prompt

def questions() -> list:
    """Returns list of questions"""
    questions_options = [
    {
            "id": 1,
            "question": "When faced with a problem, how do you usually approach it?",
            "options": [
                "Analyze the situation and create a logical plan",
                "Consider how others feel about the situation and look for a harmonious solution",
                "Think creatively and brainstorm multiple solutions",
                "Trust your instincts and act quickly"                
            ]
        },
        {
            "id": 2,
            "question": "How do you prefer to spend your free time?",
            "options": [
                "Reading a book or engaging in a solitary hobby",
                "Spending time with friends or family",
                " Exploring new activities or places",
                "Relaxing at home and watching your favorite shows",
                
            ]
        },
        {
            "id": 3,
            "question": "How do you handle unexpected changes in your schedule?",
            "options": [
                "Adapt quickly and find a new plan",
                "Feel stressed but try to accommodate everyone involved",
                "Embrace the change and see it as an adventure",
                "Stick to your original plan as closely as possible"
            ]
        },
        {
            "id": 4,
            "question": "When making a decision, what do you prioritize?",
            "options": [
               "Logical reasoning and factual information",
               "The impact on relationships and people's feelings",
               "Innovative and unique solutions",
               "Practicality and immediate results"
            ]
        },
        {
            "id": 5,
            "question": "How do you usually communicate with others?",
            "options": [
                "Directly and to the point",
                "Considerately, taking others' feelings into account",
                "Enthusiastically and with a lot of energy",
                " Calmly and thoughtfully"
            ]
        }
    ]


    return questions_options