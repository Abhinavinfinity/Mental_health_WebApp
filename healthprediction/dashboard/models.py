from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

# Create your models here.
GENDER=(
    (0,'Female'),
    (1,'Male'),
    (2,'Trans'),
)

FAMILY=(
    (0,'No'),
    (1,'Yes'),
)

class Data(models.Model):
    name=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    tech_company=models.CharField(max_length=100,null=True)
    student=models.CharField(max_length=100,null=True)
    physical_health=models.CharField(max_length=300,null=True)
    age=models.PositiveIntegerField(validators=[MinValueValidator(15),MaxValueValidator(60)],null=True)
    family_history=models.PositiveIntegerField(choices=FAMILY,null=True)
    sex=models.PositiveIntegerField(choices=GENDER,null=True)
    predictions=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        ml_model=joblib.load('model/model_project.joblib')
        self.predictions=ml_model.predict([[self.age,self.sex,self.family_history]])
        return super().save(*args,*kwargs)


    class Meta:
        ordering=['-date']

    def _str_(self):
        return self.name


