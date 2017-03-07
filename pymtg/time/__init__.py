import time
import datetime


def time_stats(done, total, starttime):
    """
    TODO: document that function
    """
    nowtime = time.time()
    position = done*1.0 / total
    duration = round(nowtime - starttime)
    durdelta = datetime.timedelta(seconds=duration)
    remaining = round((duration / position) - duration)
    remdelta = datetime.timedelta(seconds=remaining)

    return str(durdelta), str(remdelta)
