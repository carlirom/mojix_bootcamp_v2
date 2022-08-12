import streamlit as st
from PIL import Image

image = Image.open('image.jpeg')

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')

st.text('Simple but effective tips for every python lovers')
st.image(image, caption='Photo by Miesha Maiden from Pexels')
st.text('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.')
st.text('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

st.header('1. Walrus operator')
st.text('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')
st.subheader('Example')
code = '''
Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')
st.subheader('Output')
code = '''3'''
st.code(code, language='python')


st.header('2. Splitting a string')
st.text('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')
st.subheader('Example')
code = '''
string = “hello world”
string.split()'''
st.code(code, language='python')
st.subheader('Output')
code = '''[‘hello’, ‘world’]'''
st.code(code, language='python')


st.header('3. Reversing a string')
st.text('If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')
st.subheader('Example')
code = '''
str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')
st.subheader('Output')
code = '''!dlrow olleh'''
st.code(code, language='python')


st.header('4. Merging two dictionaries')
st.text('This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:')
st.subheader('Example')
code = '''
d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
st.code(code, language='python')
st.subheader('Output')
code = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
st.code(code, language='python')


st.header('5. The zip() function')
st.text('The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.')
st.subheader('Example')
code = '''
colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
st.code(code, language='python')
st.subheader('Output')
code = '''
red apple
yellow banana
green mango'''
st.code(code, language='python')
st.text('The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.')
st.subheader('Example')
code = '''
students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
st.code(code, language='python')
st.subheader('Output')
code = '''{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}'''
st.code(code, language='python')


st.header('6. Assigning multiple list values to a variable')
st.text('If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:')
st.subheader('Example')
code = '''
mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
st.code(code, language='python')
st.subheader('Output')
code = '''
a = 1
b = [2, 3, 4, 5]'''
st.code(code, language='python')
st.text('This process is also called list unpacking and you can apply this method for more than 2 variables also!')


st.header('7. Remove duplicate list items')
st.text('Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.')
st.subheader('Example')
code = '''
mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)'''
st.code(code, language='python')
st.subheader('Output')
code = '''
{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
st.code(code, language='python')


st.header('8. Lambda function')
st.text('If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.')
st.subheader('Example')
st.text('Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :')
code = '''
mul = lambda a,b: a*b
mul(5,6)'''
st.code(code, language='python')
st.subheader('Output')
code = '''30'''
st.code(code, language='python')


st.header('9. Swapping variable value')
st.text('One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:')
st.subheader('Example')
code = '''
a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)'''
st.code(code, language='python')
st.subheader('Output')
code = '''
a = 200
b = 100'''
st.code(code, language='python')


st.header('10. Use a password in your code')
st.text('This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!')
st.subheader('Example')
code = '''
from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)'''
st.code(code, language='python')
st.subheader('Output')
code = '''
password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password'''
st.code(code, language='python')
st.text('Here is a book on Python programming that I would definitely recommend for all beginners.')

st.subheader('Conclusion')
st.text('These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.')
st.text('Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.')
st.text('However, the recommended resource is experienced by me and helped me in my data science career journey.')

st.subheader('Before you go…')
st.text('If you liked this article and want to stay tuned with more exciting articles on Python & Data Science — do consider becoming a medium member by clicking here https://pranjalai.medium.com/membership. Please do consider signing up using my referral link. In this way, the portion of the membership fee goes to me, which motivates me to write more exciting stuff on Python and Data Science. Also, feel free to subscribe to my free newsletter: Pranjal’s Newsletter.')
