import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

     # Define colors
        self.bg_color = "#f0f8ff"  # Light blue background
        self.question_color = "#4682b4"  # Steel blue for question text
        self.button_color = "#87ceeb"  # Sky blue for buttons
        self.selected_color = "#ff4500"  # Orange-red for selected options
        self.default_color = "#ffffff"  # Default white for options

        # Questions and options
        self.questions = [
            {"question": "What is the capital of Italy?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": "Rome"},
            {"question": "Which continent is Spain located on?", "options": ["Africa", "Europe", "Australia", "Asia"], "answer": "Europe"},
            {"question": "What is the chemical symbol of water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": "H2O"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Jupiter"},
            {"question": "Who was the first man to walk on the moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Yuri Gagarin"], "answer": "Neil Armstrong"}
        ]
        
        self.current_question_index = 0
        self.score = 0

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        # Create and display the question label
        self.question_label = tk.Label(self.root, text="", font=("Times", "24", "bold italic"))
        self.question_label.pack(pady=15)

        # Create buttons for options
        self.selected_option = tk.StringVar(value="")

        self.option_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="")
            rb.pack(anchor='w')
            self.option_buttons.append(rb)

        # Create submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

 # Set background color for the main window
        self.root.configure(bg=self.bg_color)


    def display_question(self):
        if self.current_question_index >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.current_question_index]
        self.question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def check_answer(self):
        selected = self.selected_option.get()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your score is {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()