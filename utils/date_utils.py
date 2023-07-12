from datetime import datetime


class DateTransformer:

    def __init__(self, data) -> None:
        self.data = data

    def convert_to_days(self) -> int:

        date_obj: datetime = datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S')
        return date_obj.day

    def convert_to_weekdays(self) -> int:
        date_obj: datetime = datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S')
        return date_obj.weekday()

    def convert_to_hours(self) -> int:
        date_obj: datetime = datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S')
        return date_obj.hour

    def convert_to_minutes(self) -> int:
        date_obj: datetime = datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S')
        return date_obj.minute

    def convert_to_sec(self) -> int:
        date_obj: datetime = datetime.strptime(self.data, '%Y-%m-%d %H:%M:%S')
        return date_obj.second
