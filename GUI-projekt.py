from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI Projekt")
username = StringVar()
password = StringVar()


def close(key=None):  # Just simple function to close program
    if key is None:  # To prevent PyCharm from complaining
        pass
    root.quit()


def reset_status_bar():  # Resets the status bar text to it's default text & colour
    status_bar_message["fg"] = "black"
    status_bar_message["text"] = "Welcome. Enter username and password."


def secret_hint(key=None):  # Hint to find secret key
    if key is None:  # To prevent PyCharm from complaining
        pass
    messagebox.showinfo("", "TrY pressing different keYs to find a secret keY.")


def secret_key(key=None):  # If player presses secret key (see keybindings) this happens
    if key is None:  # To prevent PyCharm from complaining
        pass
    messagebox.showinfo("You did it!", "You have pressed the secret key.")


def change_text(key=None):
    if key is None:  # To prevent PyCharm from complaining
        pass
    button_dont_press["text"] = "You pressed it anyway."


def do_nothing(key=None):
    if key is None:  # To prevent PyCharm from complaining
        pass
    messagebox.showinfo("", "This button doesn't do anything.")


def verify_login(key=None):
    if key is None:  # To prevent PyCharm from complaining
        pass
    if username.get() == "abc" and password.get() == "123":
        status_bar_message["text"] = "Welcome,", username.get()
        status_bar_message["fg"] = "darkgreen"
        status_bar_message.after(1, login_process)
    else:
        login_fail()


def login_fail():
    status_bar_message["fg"] = "red"
    status_bar_message["text"] = "Wrong username or password. Try again."


def exit_print(key=None):
    if key is None:  # To prevent PyCharm from complaining
        pass
    print("exit print")


def login_process():
    frame_username.destroy()
    frame_password.destroy()
    frame_newusername = Frame(frame_canvas, bg="white")
    label_newusername = Label(frame_newusername, text="Username")
    entry_newusername = Entry(frame_newusername, text=username)
    frame_newusername.pack(side=TOP)
    label_newusername.pack(side=LEFT)
    entry_newusername.pack()
    open_success_window()


def delay_login_attempt():
    status_bar_message["text"] = status_bar_message["text"] + "."


def open_success_window():
        success_window = Tk()
        success_frame_create(success_window)
        success_window.mainloop()


def success_frame_create(success_window):
    success_frame = Frame(success_window, bg="gold", bd=20)
    success_frame.pack()
    global success_button
    success_button = Button(success_frame, text="You did it",
                            command=success_button_press)
    success_button.pack()
    success_button_quit = Button(success_frame, text="Quit", command=success_window.quit)
    success_button_quit.pack(side=BOTTOM)
    success_button_quit.bind("<Return>", close)


def success_button_press():
    if success_button["text"] == "You did it":
        success_button["text"] = "Woohooo!"
    else:
        success_button["text"] = success_button["text"][:6] + "o" + success_button["text"][6:]


main_frame = Frame(root, bg="orange", height=505, width=405)
main_frame.pack()

main_canvas = Canvas(main_frame, bg="darkgreen", height=500, width=400)
main_canvas.pack()

frame_canvas = Frame(main_canvas, bd=200, bg="orange")
frame_canvas.pack()

frame_username = Frame(frame_canvas, bg="white")
label_username = Label(frame_username, text="Username")
entry_username = Entry(frame_username, text=username)
frame_username.pack(side=TOP)
label_username.pack(side=LEFT)
entry_username.pack()
entry_username.bind("<Return>", verify_login)

frame_password = Frame(frame_canvas, bg="yellow")
label_password = Label(frame_password, text="Password")
entry_password = Entry(frame_password, text=password, show="*")
frame_password.pack()
label_password.pack(side=LEFT)
entry_password.pack()
entry_password.bind("<Return>", verify_login)

other_frame = Frame(main_frame, bd=1)
other_frame.pack(side=BOTTOM)

button_frame = Frame(main_frame, bd=1)
button_frame.pack(side=BOTTOM)


button_login = Button(button_frame, text="Log In", bg="orange",
                      activebackground="blue",
                      activeforeground="red",
                      command=verify_login)
button_login.pack(side=LEFT)
button_login.bind("<Return>", verify_login)

button_hello = Button(button_frame, text="Hint", bg="orange",
                      activebackground="red",
                      activeforeground="white",
                      highlightcolor="gray",
                      command=secret_hint)
button_hello.pack(side=LEFT)
button_hello.bind("<Return>", secret_hint)

button_dont_press = Button(button_frame, text="Don't press this button.", bg="orange",
                           activebackground="gray", command=change_text)
button_dont_press.pack(side=BOTTOM)
button_dont_press.bind("<Return>", change_text)

button4 = Button(other_frame, text="Quit", bg="orange",
                 activebackground="gray", command=root.quit)
button4.pack(side=TOP)
button4.bind("<Return>", close)


############
# Menu bar #
############

menubar = Menu(root)

settings_bar = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=settings_bar)
settings_bar.add_command(label="Change stat bar", command=reset_status_bar)
settings_bar.add_command(label="Do nothing", command=do_nothing)
settings_bar.add_command(label="Hint", command=secret_hint)


def make_canvas_red():
    frame_canvas.configure(background="red")
    main_frame["bg"] = frame_canvas["bg"]


def make_canvas_blue():
    frame_canvas.configure(background="blue")
    main_frame["bg"] = frame_canvas["bg"]


def make_canvas_green():
    frame_canvas.configure(background="green")
    main_frame["bg"] = frame_canvas["bg"]


def make_canvas_purple():
    frame_canvas.configure(background="purple")
    main_frame["bg"] = frame_canvas["bg"]


colour_menu = Menu(menubar, tearoff=0)
colour_menu.add_command(label="Red", command=make_canvas_red)
colour_menu.add_command(label="Blue", command=make_canvas_blue)
colour_menu.add_command(label="Green", command=make_canvas_green)
colour_menu.add_command(label="Purple", command=make_canvas_purple)
settings_bar.add_cascade(label="Change background colour", menu=colour_menu)

settings_bar.add_command(label="Quit", command=root.quit)

############
# Stat bar #
############


status_bar = Label(root, bd=2, anchor=W, text="")
status_bar.pack(side=BOTTOM, fill=X)
status_bar_message = Label(status_bar, text="Welcome. Enter username and password.")
status_bar_message.pack()


############
# Keybinds #
############

root.bind("<Escape>", close)
root.bind("<Alt-Key-F4>", exit_print)
root.bind("<y>", secret_key)  # Secret key accepts both lower- and upper-case character
root.bind("<Y>", secret_key)


root.config(menu=menubar)

root.mainloop()
