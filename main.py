from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # get dataframe => dictionary
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # 定位 orient 设置成 records 可生成每行列1对应的列2的值 {column -> value}
    to_learn = data.to_dict(orient="records")


# ---------------------------- 2. Next CARD ------------------------------- #
def next_card():
    # df = pandas.DataFrame(data)
    global current_card, flip_timer, to_learn
    # 每次点击都是开启新的 flip （避免累积导致的不到 3 秒就反转）
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- 3. FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- 4. WORD TO LEARN ------------------------------- #

def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    df = pandas.DataFrame(to_learn)
    # index=False 不会每次读取 csv 时都增加索引
    df.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- 1. UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# word = Label(text="trouve", font=("Ariel", 60, "bold"))
# word.grid(column=0, row=1, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()


window.mainloop()
