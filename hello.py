from datetime import datetime

def greeting():
    current_time = datetime.now().strftime("%H:%M")
    print(f"Powitanie! Aktualna godzina to {current_time}.")

if __name__ == "__main__":
    greeting()
