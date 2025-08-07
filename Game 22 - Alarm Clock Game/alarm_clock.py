import datetime
import time

def get_alarm_time():
    print("🕰️ Set your alarm:")
    hour = input("Hour (HH - 12-hour format): ")
    minute = input("Minute (MM): ")
    second = input("Second (SS): ")
    am_pm = input("AM or PM: ").strip().upper()

    alarm_time = f"{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)} {am_pm}"
    print(f"✅ Alarm set for {alarm_time}")
    return alarm_time

def start_alarm(alarm_time):
    print("⏳ Waiting for the alarm time...")
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        if current_time == alarm_time:
            print("\n⏰⏰⏰ WAKE UP! TIME'S UP! ⏰⏰⏰")
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm = get_alarm_time()
    start_alarm(alarm)
