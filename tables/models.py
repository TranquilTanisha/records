from django.db import models
from datetime import datetime, date
import uuid
# Create your models here.

class Table(models.Model):
    title=models.TextField("Title of the table")
    desc=models.TextField("Description",null=True, blank=True)
    col1=models.TextField("Column 1",null=True, blank=True)
    col2=models.TextField("Column 2",null=True, blank=True)
    col3=models.TextField("Column 3",null=True, blank=True)
    col4=models.TextField("Column 4",null=True, blank=True)
    col5=models.TextField("Column 5",null=True, blank=True)
    #date=models.DateField("Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False)
    #total=models.IntegerField(null=True, blank=True)
    column=models.ManyToManyField("Column", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    

    def __str__(self):
        return self.title

class Column(models.Model):
    #table=models.ForeignKey(Table, on_delete=models.CASCADE)
    col1=models.TextField("Column 1 entry",null=True, blank=True)
    col2=models.TextField("Column 2 entry",null=True, blank=True)
    col3=models.TextField("Column 3 entry",null=True, blank=True)
    col4=models.TextField("Column 4 entry",null=True, blank=True)
    col5=models.TextField("Column 5 entry",null=True, blank=True)
    date=models.DateField("Date (yyyy-mm-dd)",auto_now_add=False, auto_now=False)
    total=models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    

    def getTotal(self):
        total_c=date.count()
        self.total=total_c
        return self.total

    def __str__(self):
        return str(self.date)