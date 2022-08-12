import streamlit as st

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.text('Simple but effective tips for every python lovers')
st.text('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.')
st.text('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')