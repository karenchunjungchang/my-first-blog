from django.db import models
from django.utils import timezone # All of the stable modules are included in django.utils and designed for internal use.

class MyPost(models.Model): # Model is defined in (or in fact introduced to) django.db.models as mentioned in the first line.
    author = models.ForeignKey('auth.User') # The ForeignKey is a data type with a datum or data pointing to a column of a table with a datum or data defined as the PrimaryKey
                                            # The ForeignKey is used to confirm the referential integrity of a datum or data.,
    title = models.CharField(max_length=200) # The CharField is used to define text with a limitation on the number of characters.
    text = models.TextField() # The TextField is used to define text without a limitation on the number of characters.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) # The blank is used to confirm whether a datum or data should be included in the column.
                                                                 # The column can be blank as blank=True and vice versa.
                                                                 # The null is used to confirm whether a datum or data should be included in the database.
                                                                 # The database can be null as null=True and vice versa.
    def publish(self): # The def is used to define a function or method.
                       # The def should be indented inside the class which it belongs to.
                       # Please refer to page 17 and page 18 of the PDF file titled "Object Oriented Programming in Python" under D:\From '170810\My Course\Django.
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # The __str__ is used to print the string, by print() whenever necessary, as returned.
                       # Please refer to the PDF files titled "Special Method Names" and "10.3 Operator - Standard Operators as Functions" under D:\From '170810\My Course\Django.
        return self.title
