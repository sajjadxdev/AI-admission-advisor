# university-advisor/utils/roadmap.py

def generate_roadmap(subfield):
    """
    Generate a learning roadmap based on the selected subfield.\n now you take correct data thrgough decide field.
    
    Each roadmap contains different learning levels (beginner, intermediate, advanced)
    with links to Coursera, Udemy, and YouTube for further study.
    """
    roadmaps = {
        'web development': {
            'beginner': [
                'HTML/CSS basics - [Udemy](https://www.udemy.com/course/web-development/)','\n',
                'JavaScript fundamentals - [Coursera](https://www.coursera.org/courses?query=javascript)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6PrE9srvEn8nbhOOyxnWXfp)','\n',
            ],
            'intermediate': [
                'ReactJS - [Udemy](https://www.udemy.com/course/react-the-complete-guide/)','\n',
                'Node.js - [Coursera](https://www.coursera.org/specializations/full-stack-react)','\n',
                'Full-stack web apps - [YouTube](https://www.youtube.com/playlist?list=PLillGF-RfqbbiTGgA77tGO426V3hRF9iE)','\n',
            ],
            'advanced': [
                'Scaling web apps - [Udemy](https://www.udemy.com/course/advanced-web-applications/)','\n',
                'Backend with Express - [Coursera](https://www.coursera.org/courses?query=express.js)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PLk6CEY9XxSIAeK-EAhIRlP1lH9yIIVbFg)','\n',
            ]
        },
        'machine learning': {
            'beginner': [
                'Python Basics - [Coursera](https://www.coursera.org/learn/python)',
                'Intro to Machine Learning - [Udemy](https://www.udemy.com/course/machinelearning/)',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D)',
            ],
            'intermediate': [
                'Linear Regression, SVMs - [Udemy](https://www.udemy.com/course/machine-learning-a-z/)','\n',
                'Deep Learning basics - [Coursera](https://www.coursera.org/specializations/deep-learning)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnNg8cyjDOaQcx9pSP4MvWJ)','\n',
            ],
            'advanced': [
                'Reinforcement Learning - [Coursera](https://www.coursera.org/specializations/reinforcement-learning)','\n',
                'Advanced NLP - [Udemy](https://www.udemy.com/course/nlp-natural-language-processing-with-python/)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)','\n',
            ]
        },
        'mobile app development': {
            'beginner': [
                'Intro to Android Studio - [Udemy](https://www.udemy.com/course/android-development-tutorial-for-beginners/)','\n',
                'Swift and iOS Basics - [Coursera](https://www.coursera.org/courses?query=ios%20development)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PLgCYzUzKIBE8TUoCyjomGFqzTFcJ05OaC)','\n',
            ],
            'intermediate': [
                'Flutter Basics - [Udemy](https://www.udemy.com/course/flutter-bootcamp-with-dart/)','\n',
                'React Native - [Coursera](https://www.coursera.org/learn/react-native)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gXdVXVJBmHpSI7zCEcjLUX)','\n',
            ],
            'advanced': [
                'Building Complex Mobile Apps - [Udemy](https://www.udemy.com/course/complex-android-apps/)','\n',
                'Advanced iOS Development - [Coursera](https://www.coursera.org/specializations/ios-development)','\n',
                'YouTube Playlist - [YouTube](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnNg8cyjDOaQcx9pSP4MvWJ)'
            ]
        }
    }

    # Return the roadmap if it exists, otherwise return a default dictionary
    return roadmaps.get(subfield.lower(), {'message': 'No roadmap available for this field'})

# Define the career goals prompt
def career_goals_prompt():
    return """
    What are your long-term career goals? 
    1. Working in industry (e.g., software development, data science)
    2. Research in academia (e.g., AI, algorithms)
    3. Entrepreneurship (e.g., building your own tech product)
    """

# Mock function to generate a career roadmap based on the selected career goal
def generate_career_roadmap(career_choice):
    # Sample roadmaps based on the career choice
    if career_choice == "1. Working in industry":
        return {
            "beginner": ["Python programming", "Data structures", "Software development methodologies"],
            "intermediate": ["Web development", "Machine learning basics", "Cloud computing"],
            "advanced": ["System design", "Advanced algorithms", "DevOps"]
        }
    elif career_choice == "2. Research in academia":
        return {
            "beginner": ["Introduction to research methods", "Mathematics for AI", "Algorithms basics"],
            "intermediate": ["Advanced AI", "Paper writing", "Experimental design"],
            "advanced": ["Publishing in journals", "Advanced machine learning models", "Grant writing"]
        }
    elif career_choice == "3. Entrepreneurship":
        return {
            "beginner": ["Business fundamentals", "Tech product development", "Market analysis"],
            "intermediate": ["Funding options", "Growth hacking", "Business scaling strategies"],
            "advanced": ["Building a sustainable business", "Investor relations", "Global market expansion"]
        }
    else:
        return {"message": "Invalid career choice. Please select a valid option."}