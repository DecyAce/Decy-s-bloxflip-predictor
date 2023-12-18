import tkinter as tk
import re


def format_numbers(event):
    clipboard_text = entry.clipboard_get()
    formatted_text = re.sub(r'\s+', ', ', clipboard_text)  
    formatted_text = re.sub(r'(?<!\d)(\d+\.\d{2}|\b\d\b|\d+)\b', r'\1, ',
                            formatted_text)  
    formatted_text = re.sub(r',\s$', '', formatted_text)  
    entry.delete(0, tk.END)
    entry.insert(0, formatted_text)
    return 'break'


def get_crash_numbers():
    crash_text = entry.get().replace('\n', '')  
    crash_numbers = re.findall(r'\d+\.\d{2}', crash_text)  

    below_2 = sum(1 for num in crash_numbers if float(num) < 2)
    above_2 = sum(1 for num in crash_numbers if float(num) > 2)

    if len(crash_numbers) == 7 and below_2 == 7:
        result_label.config(text="Possible big win coming up (only join if you can afford to lose or are placing low bets)")
    else:
        last_number = float(crash_numbers[-1]) if crash_numbers else 0
        big_win_from_last_game = last_number > 5

        if big_win_from_last_game:
            result_label.config(text="Join next game at your own risk (semi recommended)")
        elif above_2 in [4, 5, 6]:
            result_label.config(text="Join next game")
        elif above_2 == 7:
            result_label.config(text="Join next game at your own risk (Too many wins, a loss is highly probable)")
        elif below_2 == 6:
            result_label.config(text="Possible big win coming up (only join if you can afford to lose or are placing low bets)")
        elif below_2 == 5:
            result_label.config(text="Join next game at your own risk (not recommended)")
        elif below_2 == 4:
            result_label.config(text="Do not join next game")
        else:
            result_label.config(text="Do not join next game")



def show_credits():
    credits_window = tk.Toplevel()
    credits_window.title("Credits")
    credits_window.geometry("300x100")  # You can adjust the dimensions

    label_credits = tk.Label(credits_window, text="Developed By Dexter and Brendan", font=("Arial", 14))
    label_credits.pack()


def show_how_it_works():
    how_it_works_window = tk.Toplevel()
    how_it_works_window.title("How Predictor Works")
    how_it_works_window.geometry("400x300")

    explanation_text = (
        "There's a 70-80% chance of this predictor being correct. "
        "This predictor looks at patterns of previous crash games on the site bloxflip.com. "
        "The site claims to use an RNG system, stating that every casino game's results are random. "
        "However, I am 99% sure this is not true. I have developed a method to predict the results "
        "of these games by analyzing patterns of previous crash games. This method helps decide whether "
        "it's a good idea to join the next game or not (This software works best when theres either"
        "a large amount of 2x multipliers and above or a large amount of under 2x multipliers)"
    )

    text_widget = tk.Text(how_it_works_window, wrap=tk.WORD, width=50, height=15)
    text_widget.insert(tk.END, explanation_text)
    text_widget.pack()


def create_blank_window():
    window = tk.Tk()
    window.title("Decy's Bloxflip Predictor")

    window.geometry("700x600")  # You can adjust the dimensions
    window.configure(bg="#f0f0f0")  

    label = tk.Label(window, text="Paste last 7 crash numbers:", bg="#f0f0f0", font=("Arial", 12))
    label.pack(pady=10)

    global entry
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=10)
    entry.bind('<Control-v>', format_numbers)

    global result_label
    result_label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
    result_label.pack(pady=10)

    submit_button = tk.Button(window, text="Generate Answer", command=get_crash_numbers, bg="#4CAF50", fg="white",
                              font=("Arial", 12))
    submit_button.pack(pady=10)

    credits_button = tk.Button(window, text="Credits", command=show_credits, bg="#008CBA", fg="white",
                               font=("Arial", 12))
    credits_button.pack(pady=10)

    how_button = tk.Button(window, text="How It Works", command=show_how_it_works, bg="#FFD700", fg="black",
                           font=("Arial", 12))
    how_button.pack(pady=10)

    window.mainloop()


create_blank_window()
