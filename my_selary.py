def calculate(selary, work_hour, premium):
    try:
        return (selary * work_hour) + premium
    except TypeError:
        return

def hello(name):
    print(f"Привет, {name}")
