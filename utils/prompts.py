# university-advisor/utils/prompts.py

def degree_choice_prompt():
    return """
    To help us recommend the best degree, please answer the following:
    1. Do you prefer building large-scale software systems or solving algorithmic problems?
    2. Are you more interested in developing applications or understanding the theory behind computing?
    """

def subfield_prompt():
    return """
    Based on your degree interest, which of the following subfields appeals to you more?
    1. Web Development
    2. Mobile App Development
    3. Data Science
    4. Machine Learning
    """

def career_goals_prompt():
    return """
    What are your long-term career goals? 
    1. Working in industry (e.g., software development, data science)
    2. Research in academia (e.g., AI, algorithms)
    3. Entrepreneurship (e.g., building your own tech product)
    """
