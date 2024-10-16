# # university-advisor/streamlit_app.py
# import streamlit as st
# from api.gpt_api import ask_question
# from utils.prompts import degree_choice_prompt, subfield_prompt, career_goals_prompt
# from utils.roadmap import generate_roadmap,generate_career_roadmap


# # Streamlit app setup
# st.title("AI-Powered University Admission Advisor")
# st.write("Helping you decide Take Admission in university in Computer science!")


# if 'step' not in st.session_state:
#     st.session_state.step = 1


# # Step 1: Asking the student's interests
# if st.session_state.step == 1:
#     st.write("Step 1: Answer a few questions about your preferences.")
    
#     user_response = st.text_input("Tell us about your interests in software or computing:")

#     if st.button("Next"):
#         if 'software' or 'computing' in user_response.lower():  # Check if 'software' is in the input
#             st.session_state.interests = user_response
#             st.session_state.step = 2  # Proceed if input is valid
#         else:
#             st.warning("Please enter a response related to software or computing.")  # Warn user if input is not valid



# # # Step 2: Ask specific degree-related questions
# # if st.session_state.step == 2:
# #     degree_question = degree_choice_prompt()
# #     st.write(degree_question)
    
# #     user_input = st.text_input("Your Answer:")
    
# #     if st.button("Next",'k3'):
# #         st.session_state.degree_input = user_input
# #         st.session_state.step = 3
# if st.session_state.step == 2:
#     degree_question = degree_choice_prompt()
#     st.write(degree_question)

#     user_input = st.text_input("Your Answer:")

#     # Valid responses that match the prompt
#     valid_phrases = [
#         "building large-scale software systems",
#         "solving algorithmic problems",
#         "developing applications",
#         "understanding the theory behind computing"
#     ]

#     # Check if user input contains any of the valid phrases
#     if st.button("Next", key='k3'):
#         if any(phrase in user_input.lower() for phrase in valid_phrases):
#             st.session_state.degree_input = user_input
#             st.session_state.step = 3  # Move to the next step if input is valid
#         else:
#             st.error("Invalid input. Please answer based on the given questions.")

# # Step 3: Narrowing down subfield choices
# if st.session_state.step == 3:
#     subfield_question = subfield_prompt()
#     st.write(subfield_question)
    
#     subfield_choice = st.text_input("Choose a subfield (e.g., Web Development):")
    
#     if st.button("Next",'k4'):
#         st.session_state.subfield_choice = subfield_choice
#         st.session_state.step = 4

# # Main logic to integrate the career goals prompt
# if st.session_state.step == 4: 
#     st.write(career_goals_prompt())  # Show the career goals prompt

#     # Capture the user's career choice
#     career_choice = st.radio(
#         "Choose your long-term career goal:",
#         ("1. Working in industry", "2. Research in academia", "3. Entrepreneurship")
#     )

#     # Generate the roadmap based on the career choice
#     roadmap = generate_career_roadmap(career_choice)

#     # Check if the roadmap is valid or contains an error message
#     if 'message' in roadmap:
#         st.write(roadmap['message'])
#     else:
#         st.write(f"Here is your customized learning path for {career_choice}:")
#         for level, courses in roadmap.items():
#             st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")

#     if st.button("Next",'k5'):
#         st.session_state.subfield_prompt = subfield_prompt
#         st.session_state.step = 5


# # # Step 4: Generate a learning roadmap based on the subfield choice
# # if st.session_state.step == 4:
# #     roadmap = generate_roadmap(st.session_state.subfield_choice)
# #     st.write(f"Here is your customized learning path for {st.session_state.subfield_choice}:")
    
# #     for level, courses in roadmap.items():
# #         st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")
    
# #     if st.button("Finish"):
# #         st.write("Good luck with your learning journey!")
# # university-advisor/streamlit_app.py

# # Step 4: Generate a learning roadmap based on the subfield choice
# if st.session_state.step == 5:
#     roadmap = generate_roadmap(st.session_state.subfield_choice)

#     # Check if the roadmap is valid or contains an error message
#     if 'message' in roadmap:
#         st.write(roadmap['message'])
#     else:
#         st.write(f"Here is your customized learning path for {st.session_state.subfield_choice}:")
#         for level, courses in roadmap.items():
#             st.write(f"**{level.capitalize()} \n Level**: {', '.join(courses)}")
    
#     if st.button("Finish"):
#         st.write("Good luck with your learning journey!")

# university-advisor/streamlit_app.py
import streamlit as st
from api.gpt_api import ask_question
from utils.prompts import degree_choice_prompt, subfield_prompt, career_goals_prompt
from utils.roadmap import generate_roadmap,generate_career_roadmap

# Streamlit app setup
st.title("AI-Powered University Admission Advisor")
st.write("Helping you decide Take Admission in university in Computer science!")

if 'step' not in st.session_state:
    st.session_state.step = 1


# Step 1: Asking the student's interests
# if st.session_state.step == 1:
#     st.write("Step 1: Answer a few questions about your preferences.")
    
#     user_response = st.text_input("Tell us about your interests in software or computing:")

#     if st.button("Next"):
#         if 'software' or 'computing' in user_response.lower():  # Check if 'software' is in the input
#             st.session_state.interests = user_response
#             st.session_state.step = 2  # Proceed if input is valid
#         else:
#             st.warning("Please enter a response related to software or computing.")  # Warn user if input is not valid
# Step 1: Asking the student's interests
if st.session_state.step == 1:
    st.write("Step 1: Answer a few questions about your preferences.")
    
    user_response = st.text_input("Tell us about your interests in software or computing:")

    if st.button("Next"):
        if "software" in user_response.lower():  # Check if 'software' is in the input
            st.session_state.interests = user_response
            st.session_state.step = 2  # Proceed if input is valid
        else:
            st.warning("Please enter a response related to software or computing.")  # Warn user if input is not valid



# # Step 2: Ask specific degree-related questions
# if st.session_state.step == 2:
#     degree_question = degree_choice_prompt()
#     st.write(degree_question)
    
#     user_input = st.text_input("Your Answer:")
    
#     if st.button("Next",'k3'):
#         st.session_state.degree_input = user_input
#         st.session_state.step = 3
if st.session_state.step == 2:
    degree_question = degree_choice_prompt()
    st.write(degree_question)

    user_input = st.text_input("Your Answer:")

    # Valid responses that match the prompt
    valid_phrases = [
        "building large-scale software systems",
        "solving algorithmic problems",
        "developing applications",
        "understanding the theory behind computing"
    ]

    # Check if user input contains any of the valid phrases
    if st.button("Next", key='k3'):
        if any(phrase in user_input.lower() for phrase in valid_phrases):
            st.session_state.degree_input = user_input
            st.session_state.step = 3  # Move to the next step if input is valid
        else:
            st.error("Invalid input. Please answer based on the given questions.")

# Step 3: Narrowing down subfield choices
if st.session_state.step == 3:
    subfield_question = subfield_prompt()
    st.write(subfield_question)
    
    subfield_choice = st.text_input("Choose a subfield (e.g., Web Development):")
    
    if st.button("Next",'k4'):
        st.session_state.subfield_choice = subfield_choice
        st.session_state.step = 4

# Main logic to integrate the career goals prompt
if st.session_state.step == 4: 
    st.write(career_goals_prompt())  # Show the career goals prompt

    # Capture the user's career choice
    career_choice = st.radio(
        "Choose your long-term career goal:",
        ("1. Working in industry", "2. Research in academia", "3. Entrepreneurship")
    )

    # Generate the roadmap based on the career choice
    roadmap = generate_career_roadmap(career_choice)

    # Check if the roadmap is valid or contains an error message
    if 'message' in roadmap:
        st.write(roadmap['message'])
    else:
        st.write(f"Here is your customized learning path for {career_choice}:")
        for level, courses in roadmap.items():
            st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")

    if st.button("Next",'k5'):
        st.session_state.subfield_prompt = subfield_prompt
        st.session_state.step = 5


# # Step 4: Generate a learning roadmap based on the subfield choice
# if st.session_state.step == 4:
#     roadmap = generate_roadmap(st.session_state.subfield_choice)
#     st.write(f"Here is your customized learning path for {st.session_state.subfield_choice}:")
    
#     for level, courses in roadmap.items():
#         st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")
    
#     if st.button("Finish"):
#         st.write("Good luck with your learning journey!")
# university-advisor/streamlit_app.py

# Step 4: Generate a learning roadmap based on the subfield choice
if st.session_state.step == 5:
    roadmap = generate_roadmap(st.session_state.subfield_choice)

    # Check if the roadmap is valid or contains an error message
    if 'message' in roadmap:
        st.write(roadmap['message'])
    else:
        st.write(f"Here is your customized learning path for {st.session_state.subfield_choice}:")
        for level, courses in roadmap.items():
            st.write(f"**{level.capitalize()} \n Level**: {', '.join(courses)}")
    
    if st.button("Finish"):
        st.write("Good luck with your learning journey!")


########################################################

# # university-advisor/streamlit_app.py
# import streamlit as st
# from api.gpt_api import ask_question
# from utils.prompts import degree_choice_prompt, subfield_prompt, career_goals_prompt
# from utils.roadmap import generate_roadmap, generate_career_roadmap

# # Streamlit app setup
# st.title("AI-Powered University Admission Advisor")
# st.write("Helping you decide which Computer Science field to pursue!")

# if 'step' not in st.session_state:
#     st.session_state.step = 1

# # Step 1: Asking the student's interests (use GPT to personalize questions)
# if st.session_state.step == 1:
#     st.write("Step 1: Answer a few questions about your preferences.")
    
#     # Use GPT to ask personalized questions about software and computing
#     user_response = st.text_input("Tell us about your interests in software or computing:")
    
#     if st.button("Next"):
#         if 'software' in user_response.lower() or 'computing' in user_response.lower():
#             st.session_state.interests = user_response
#             # Generate follow-up questions based on interests
#             follow_up_question = ask_question("Based on your interest, what kind of software do you like to work with?")
#             st.session_state.follow_up_question = follow_up_question
#             st.session_state.step = 2
#         else:
#             st.warning("Please enter a response related to software or computing.")

# # Step 2: Follow-up question on degree choice
# if st.session_state.step == 2:
#     st.write("Step 2: Let's dive deeper into your degree preferences.")
    
#     degree_question = st.session_state.follow_up_question  # Personalized question
#     st.write(degree_question)
    
#     user_input = st.text_input("Your Answer:")
    
#     if st.button("Next", key='degree'):
#         # Process valid responses that match the prompt
#         valid_phrases = [
#             "building large-scale software systems",
#             "solving algorithmic problems",
#             "developing applications",
#             "understanding the theory behind computing"
#         ]
#         if any(phrase in user_input.lower() for phrase in valid_phrases):
#             st.session_state.degree_input = user_input
#             st.session_state.step = 3
#         else:
#             st.error("Invalid input. Please answer based on the provided questions.")

# # Step 3: Subfield choices
# if st.session_state.step == 3:
#     subfield_question = subfield_prompt()
#     st.write(subfield_question)

#     subfield_choice = st.text_input("Choose a subfield (e.g., Web Development):")
    
#     if st.button("Next", key='subfield'):
#         st.session_state.subfield_choice = subfield_choice
#         st.session_state.step = 4

# # Step 4: Ask about career goals (use GPT)
# if st.session_state.step == 4:
#     st.write(career_goals_prompt())  # Show the career goals prompt

#     # Capture the user's career choice
#     career_choice = st.radio(
#         "Choose your long-term career goal:",
#         ("1. Working in industry", "2. Research in academia", "3. Entrepreneurship")
#     )

#     # Generate a roadmap based on the career choice
#     roadmap = generate_career_roadmap(career_choice)
    
#     if 'message' in roadmap:
#         st.write(roadmap['message'])
#     else:
#         st.write(f"Here is your customized learning path for {career_choice}:")
#         for level, courses in roadmap.items():
#             st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")
    
#     if st.button("Next", key='career'):
#         st.session_state.step = 5

# # Step 5: Generate a learning roadmap based on the subfield choice
# if st.session_state.step == 5:
#     roadmap = generate_roadmap(st.session_state.subfield_choice)
    
#     if 'message' in roadmap:
#         st.write(roadmap['message'])
#     else:
#         st.write(f"Here is your customized learning path for {st.session_state.subfield_choice}:")
#         for level, courses in roadmap.items():
#             st.write(f"**{level.capitalize()} Level**: {', '.join(courses)}")
    
#     if st.button("Finish"):
#         st.write("Good luck with your learning journey!")
