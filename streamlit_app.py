import streamlit as st
from openai import OpenAI

# Global items
number1 = 0
number2 = 100
FIXED_RATE = 0.03

# Access the OpenAI API key from the secrets
api_key = st.secrets["openai"]["api_key"]

# Set up the OpenAI API client
client = OpenAI(api_key=api_key)

def generate_completion(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content


# Function used to add two numbers together
def addTwoNumbers(a, b):
    sum = a + b
    return sum

def main():
  # Streamlit UI
  st.title("OpenAI GPT-3.5 Turbo Demo")
  prompt = st.text_input("Enter a prompt:")

  if st.button("Generate"):
    if prompt:
        completion = generate_completion(prompt)
        st.markdown(completion)
    else:
        st.write("Please enter a prompt.")

  st.button("Enter Numbers Please")
  # Ask for two numbers and get from user
  number1 = st.text_input("Please enter first number: ")
  number2 = st.text_input("Please enter first number: ")
  
  # Send the two numbers to function and get the result to store in 'total'
  total = addTwoNumbers(number1, number2)
  
  # Calculate 3% using the constant of the total and save it in 'amount'
  amount = round(total * FIXED_RATE, 2)
  
  # Print the total and its amount in a one complete sentence
  st.write("the total is:", total, "and the amount is:", amount)

