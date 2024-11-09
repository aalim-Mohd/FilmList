from django.db import models

#title , year , language , , Director , Producer
class Film(models.Model):
    
    title=models.CharField(max_length=20)

    year=models.PositiveBigIntegerField()

    language=models.CharField(max_length=20)

    director=models.CharField(max_length=20)

    producer=models.CharField(max_length=20)
