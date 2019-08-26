from django.db import models
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
# Create your models here.


class Home(models.Model):
    area = models.IntegerField()
    seria = models.IntegerField()
    region=models.IntegerField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    heating = models.IntegerField()
    price = models.IntegerField(null=True)

    def __str__(self):
        return 'price : ' + str(self.price)+' area_'+str(self.area)





