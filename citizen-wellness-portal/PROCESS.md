# Learning Process Documentation

## Prompts Used and What I Learned

### Understanding Streamlit's Model
**Prompt:** I'm a Flask developer learning Streamlit. Explain the key differences in how these frameworks work. Specifically: 1. How does Streamlit handle user interactions vs Flask's routes? 2. What happens when a user clicks a button in Streamlit? 3. Why do I need st.session_state when I didn't need anything special for variables in Flask?
**Key Insight:** Streamlit works as a reactive app where it reruns and updates as you interact with it, where flask uses requests and responses.
**Iteration:** None

### Building the Login Form
**Prompt:** I'm building a Streamlit app with login/registration. I want to store users in st.session_state as a dictionary. Show me how to: 1. Initialize the users dict if it doesn't exist 2. Add a new user during registration 3. Check credentials during login 4. Handle errors (user already exists, wrong password, etc.)
**Challenge:** My app was mostly functional however it would run into a few minor errors.
**Solution:** I would identify the problem and ask chatgpt to help me correct the mistake.

## Flask vs Streamlit: My Observations

The overall file creation was easier in streamlit compared to flask as I had to create many files that worked with eachother in the previous flask assignment.
