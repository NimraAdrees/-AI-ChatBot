import time
import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

# ChatBot Q&A dictionary
now = time.ctime()
qna = {
    "hi": "Hey there!",
    "how are you": "I am fine, thank you! How about you?",
    "what is your name": "My name is Dell Laptop, your friendly assistant.",
    "what is your age": "Age doesn't apply to me, I am as young as AI!",
    "what is the time now": now,
    "good": "Thanks for the appreciation!",
    "nice": "Thanks for the kind words!",
    "who made you": "I was created by a talented developer like you!",
    "what is your purpose": "I am here to assist you and make your tasks easier.",
    "where do you live": "I live in the digital world, powered by electricity and code!",
    "what do you like": "I like learning new things and helping people like you.",
    "can you help me": "Of course! I am always ready to assist you.",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "tell me a fact": "Did you know? The first computer virus was created in 1983.",
    "quit": "Goodbye! It was nice chatting with you.",
    "bye": "Goodbye! Have a great day!",
    "ok": "Goodbye! Take care!"
}

# Function to get the chatbot response
def get_response():
    user_input = user_entry.get().lower()  # Get input and convert to lowercase
    if user_input in qna:
        response = qna[user_input]
    else:
        response = "Sorry, I didn't understand that. Could you try asking something else?"
    
    chat_box.config(state=tk.NORMAL)  # Enable writing in the chat box
    # Insert user input in purple color
    chat_box.insert(tk.END, f"You: {user_input}\n", 'user')
    # Insert bot response in blue color
    chat_box.insert(tk.END, f"Bot: {response}\n\n", 'bot')
    chat_box.config(state=tk.DISABLED)  # Disable writing after inserting the text
    user_entry.delete(0, tk.END)  # Clear input field

    if user_input in ["quit", "bye", "ok"]:
        window.after(2000, window.quit)  # Close after 2 seconds

# Create the main window
window = tk.Tk()
window.title("AI ChatBot")

# Set window background color
window.configure(bg="#000000")

# Load chatbot icon
icon = PhotoImage(file="pic.png")
icon_label = tk.Label(window, image=icon, bg="#000000")
icon_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Create a scrollable chat box
chat_box = scrolledtext.ScrolledText(window, state=tk.DISABLED, wrap=tk.WORD, width=40, height=15, font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
chat_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Add tags for different colors
chat_box.tag_config('user', foreground="#03bffe")  # User text in blue
chat_box.tag_config('bot', foreground="#6a2be9")   # Bot text in purple

# Create a text entry widget for user input
user_entry = tk.Entry(window, width=35, font=("Arial", 12), bg="#333333", fg="#ffffff", insertbackground='white')
user_entry.grid(row=2, column=0, padx=(10, 5), pady=5)  # Reduced space

# Create a send button with color gradient matching the image
send_button = tk.Button(window, text="Send", width=6, bg="#6a2be9", fg="#ffffff", activebackground="#00bfff", command=get_response)
send_button.grid(row=2, column=1, padx=(5, 10), pady=5)  # Reduced space

# Set focus on the entry box initially
user_entry.focus()

# Run the Tkinter event loop
window.mainloop()

