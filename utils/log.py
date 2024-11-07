import traceback
from pytz import timezone
from datetime import datetime

def write(message, error_mode=False):
    time_zone = timezone("America/Sao_Paulo")
    current_date = datetime.now(tz=time_zone)
    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_hour = current_date.strftime(f"%H:%M:%S({time_zone})")

    formatted_message = f"{formatted_hour}: {message}\n"

    print(formatted_message)
    if error_mode:
            traceback.print_exc()

def error(error):
    error_message = f"ERROR: type: {type(error)}, description: {error}."
    write(error_message, error_mode=True)

if __name__ == '__main__':
    write("Testing log system.")
    error_handler(NameError("TestError", "Only testing the log system."))