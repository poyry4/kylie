from django.db import models

class categorys(models.Model):
    categoryName = models.CharField(max_length=40)

    def __str__(self):
        return self.categoryName

class image(models.Model):
     imges = models.ImageField(default='default.png', blank=True)

class product(models.Model):
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=250)
    productName = models.TextField(null=False)
    img = models.ForeignKey(image, on_delete=models.CASCADE, default=None)
    cat = models.ForeignKey(categorys, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.productName    
