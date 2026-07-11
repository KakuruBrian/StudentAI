from django.db import models

class Prediction(models.Model):

    gender=models.CharField(max_length=10)

    age=models.IntegerField()

    studytime=models.IntegerField()

    failures=models.IntegerField()

    absences=models.IntegerField()

    g1=models.IntegerField()

    g2=models.IntegerField()

    higher=models.CharField(max_length=5)

    prediction=models.CharField(max_length=20)

    confidence=models.FloatField()

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} ({self.confidence}%)"