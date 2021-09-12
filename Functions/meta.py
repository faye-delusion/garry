import datetime
async def log(log):

    return print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {log}")