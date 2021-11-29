import datetime


class PastDate:
    def is_past_date(self, date):
        result_flag = True
        today = datetime.date.today()
        if date >= today:
            result_flag = False
        return result_flag
