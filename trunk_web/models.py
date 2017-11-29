from django.db import models

class Talkgroup(models.Model):
    name = models.CharField(max_length=50)
    dec_id = models.IntegerField()

    def __str__(self):
        return self.name


class Station(models.Model):
    number = models.CharField(max_length=3, help_text="fire station number")
    name = models.CharField(max_length=100, blank=True)
    disp_tg = models.ForeignKey(Talkgroup, on_delete=models.CASCADE, related_name='station_disp')
    tac_tg = models.ForeignKey(Talkgroup, on_delete=models.CASCADE, related_name='station_tac')

    def __str__(self):
        if self.name:
            return '{} ({})'.format(self.name, self.number)         
        else:
            return self.number
