from django.db import models
from django.utils import timezone

class Record(models.Model):

    my_string = models.CharField(max_length=200, default="new record")
    my_int = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Record from {} - my_string = {}, my_int = {}".format(self.created,
                                                                     self.my_string,
                                                                     self.my_int,)