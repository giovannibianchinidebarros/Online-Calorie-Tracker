from django.core.management.base import BaseCommand
from trackerapp.models import Food
import pandas as pd
import os


'''
data source:
https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products
'''

PATH = os.path.dirname(__file__)
PATH_CSV = os.path.join(PATH, 'fooditems.csv')


class Command(BaseCommand):
    help = 'Populate Food model from a CSV file'

    def handle(self, *args, **kwargs):

        df = pd.read_csv(PATH_CSV)

        for _, row in df.iterrows():
            Food.objects.create(
                name=row['name'],
                calories=row['calories'],
                fat=row['fat'],
                protein=row['protein'],
                carbs=row['carbohydrate'],
                fiber=row['fiber'],
                sugars=row['sugars']
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated Food model'))
