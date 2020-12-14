from tkinter import Tk, Entry, Button, Canvas, PhotoImage, Label
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
plus_check = []

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count():
    global timer
    global REPS
    global plus_check
    window.after_cancel(timer)

    # reset time to 00:00
    canvas.itemconfig(time_text, text="00:00")

    # reset label
    label_timer.config(text="Timer", font=(
        FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)

    # reset check mark
    label_check.config(text="")

    REPS = 0
    plus_check = []

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    global REPS
    REPS += 1

    print(REPS)
    if REPS == 8:
        label_timer.config(text="Break", font=(
            FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
        count_down(20)

    if REPS % 2 == 0 and REPS != 8:
        label_timer.config(text="Break", font=(
            FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
        count_down(3)
    elif REPS % 2 != 0:
        label_timer.config(text="Work", font=(
            FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
        count_down(2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def double_digit_check(n):
    return f"0{n}" if n < 10 else n


def count_down(count):
    global plus_check
    check = "✔"
    count_minute = double_digit_check(count//60)
    count_second = double_digit_check(count % 60)

    canvas.itemconfig(time_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if REPS % 2 != 0:
            plus_check.append(check)
            label_check.config(
                text=f"{' '.join([str(check) for check in plus_check])}")


            # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas estate
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(102, 112, image=tomato_img)
time_text = canvas.create_text(103, 130, text="00:00", fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label estate
# Title timeer
label_timer = Label(text="Timer", font=(
    FONT_NAME, 28, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

# check mark
label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(column=1, row=3)


# buttom estate
# start btm
bt_start = Button(text="Start", command=start_count)
bt_start.grid(column=0, row=2)

# reset btm
bt_reset = Button(text="Reset", command=reset_count)
bt_reset.grid(column=2, row=2)


window.mainloop()
