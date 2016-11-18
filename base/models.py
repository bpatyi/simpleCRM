import datetime
from django.db import models
from base.abstracts import AbstractBaseModel


class GeoCoderLog(AbstractBaseModel):
    number_of_request = models.IntegerField(default=0)

    @classmethod
    def get_today_record(cls):
        record = cls.objects.filter(
            created_at__range=(
                datetime.datetime.combine(
                    datetime.date.today(),
                    datetime.time.min
                ),
                datetime.datetime.combine(
                    datetime.date.today(),
                    datetime.time.max
                )
            )
        )

        if record:
            return record[0]

        record = cls.objects.create()

        return record

    @classmethod
    def update_today_number_of_request(cls):
        record = cls.get_today_record()

        record.number_of_request += 1
        record.save()

        return record.number_of_request

    @classmethod
    def get_limit(cls):
        record = cls.get_today_record()

        return 2500 - record.number_of_request
