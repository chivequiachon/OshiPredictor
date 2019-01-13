from django.db import models

class IdolInformation(models.Model):
    romaji_name = models.CharField(max_length=60, default="NULL")
    kanji_name = models.CharField(max_length=10, default="NULL")
    generation = models.CharField(max_length=5, default="1st")
    image_url = models.CharField(max_length=100)

    anime_manga_fan_score = models.IntegerField(default=0)
    eat_score = models.IntegerField(default=0)
    artistic_score = models.IntegerField(default=0)
    music_fan_score = models.IntegerField(default=0)
    travel_score = models.IntegerField(default=0)
    athletic_score = models.IntegerField(default=0)
    animal_like_score = models.IntegerField(default=0)
    caring_score = models.IntegerField(default=0)
    read_score = models.IntegerField(default=0)
    cook_score = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return "%s (%s)" % (self.romaji_name, self.kanji_name)
