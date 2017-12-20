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


def datetime_range(start_datetime, end_datetime=None, step_interval=None, n_steps=1, snap_to_date=False, 
                   return_pairs=False):
    """Return a list of dates inside the date range between ``start_datetime`` and ``end_datetime``,
    equally spaced in ``step`` time intervals.

    Args:
        start_datetime (datetime): Starting time of the range
        end_datetime (datetime): End of the time range (included if range is multiple of step). Defaults to today
        step_interval (timedelta,str): time interval of between list elements. Can be a ``datetime.timedelta`` 
            object or a string from ['day', 'second', 'microsecond', 'millisecond', 'minute', 'hour', 'week'].
            Defaults to 1 day.
        n_steps (int): number of steps to be applied between list elements (default=1)
        snap_to_date (bool): Whether to disregard hour, minutes and seconds information (as a date object, 
            default=False)
        return_pairs (bool): Whether to return a simple list or a list of pairs with edge dates for each 
            interval (default=False)

    Returns:
        (list): List of ``datetime.dateitme`` objects (or tuples of two ``datetime.dateitme`` if ``return_pairs=True``)

    Examples:
        >>> datetime_range(datetime.datetime(2017,1,1), datetime.datetime(2017,1,3))
        [datetime.datetime(2017, 1, 1, 0, 0), datetime.datetime(2017, 1, 2, 0, 0), datetime.datetime(2017, 1, 3, 0, 0)]
        >>> datetime_range(datetime.datetime(2017,1,1,10,21,45), datetime.datetime(2017,1,3,10,30,54), snap_to_date=True)
        [datetime.datetime(2017, 1, 1, 0, 0), datetime.datetime(2017, 1, 2, 0, 0), datetime.datetime(2017, 1, 3, 0, 0)]
        >>> datetime_range(datetime.datetime(2017,1,1,11,0,0), datetime.datetime(2017,1,1,11,2,0), step_interval='minute')
        [datetime.datetime(2017, 1, 1, 11, 0), datetime.datetime(2017, 1, 1, 11, 1), datetime.datetime(2017, 1, 1, 11, 2)]
        >>> datetime_range(datetime.datetime(2017,1,1,11,0,0), datetime.datetime(2017,1,1,11,20,0), step_interval='minute', n_steps=10)
        [datetime.datetime(2017, 1, 1, 11, 0), datetime.datetime(2017, 1, 1, 11, 10), datetime.datetime(2017, 1, 1, 11, 20)]
        >>> datetime_range(datetime.datetime(2017,1,1), datetime.datetime(2017,1,3), return_pairs=True)
         [(datetime.datetime(2017, 1, 1, 0, 0), datetime.datetime(2017, 1, 2, 0, 0)), (datetime.datetime(2017, 1, 2, 0, 0), datetime.datetime(2017, 1, 3, 0, 0))]
    """

    if end_datetime is None:
        end_datetime = datetime.datetime.today()

    if step_interval is None:
        step_interval = datetime.timedelta(days=1)
    else:
        if not isinstance(step_interval, datetime.timedelta):
            if step_interval.lower() == 'day':
                step_interval = datetime.timedelta(days=n_steps)
            elif step_interval.lower() == 'second':
                step_interval = datetime.timedelta(seconds=n_steps)
            elif step_interval.lower() == 'microsecond':
                step_interval = datetime.timedelta(microseconds=n_steps)
            elif step_interval.lower() == 'millisecond':
                step_interval = datetime.timedelta(milliseconds=n_steps)
            elif step_interval.lower() == 'minute':
                step_interval = datetime.timedelta(minutes=n_steps)
            elif step_interval.lower() == 'hour':
                step_interval = datetime.timedelta(hours=n_steps)
            elif step_interval.lower() == 'week':
                step_interval = datetime.timedelta(weeks=n_steps)

    if snap_to_date:
        start_datetime = start_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        end_datetime = end_datetime.replace(hour=0, minute=0, second=0, microsecond=0)

    dates = []
    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        dates.append(current_datetime)
        current_datetime += step_interval

    if return_pairs:
        return list(zip(dates[:-1], dates[1:]))
    else:
        return dates
