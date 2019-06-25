from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=2000)
    hit = models.PositiveIntegerField()
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_no = models.PositiveIntegerField()
    order_no = models.PositiveIntegerField()
    depth = models.PositiveIntegerField()

    def __str__(self):
        return f'Board{self.title}, {self.contents}, {self.hit}, {self.regdate}, {self.user}, {self.group_no}, ' \
            f'{self.order_no}, {self.depth})'


