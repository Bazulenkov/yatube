import datetime as dt


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    year_now = dt.datetime.now().date().year
    return {
        'year' : year_now
    }
