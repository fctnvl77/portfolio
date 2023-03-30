from django.db import models

class Men(models.Model):
    ism = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='rasmlarim', null=True, blank=True)
    men_xaqimda = models.TextField()
    yil = models.DateField()
    manzil = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    
    tajriba_yil = models.IntegerField()
    loyihalar_soni = models.IntegerField()
    yutuqlar_soni = models.IntegerField()
    ish_vaqt = models.FloatField()
    
    def str(self):
        return f"{self.ism} | {self.manzil} | {self.email}"
    
    class Meta:
        verbose_name = "Men_haqimda"
        verbose_name_plural = "Men haqimda"



class Portfolio(models.Model):
    rasm = models.ImageField(upload_to='loyiha_rasmlar', null=True, blank=True)
    nomi = models.CharField(max_length=100)
    malumot = models.TextField(max_length=100)
    link = models.CharField(max_length=100)
    


    def str(self):
        return f"{self.nomi}"
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfoliolar"
        
        
class Blog(models.Model):
    rasm = models.ImageField(upload_to='blog_rasmlar', null=True, blank=True)
    mavzu = models.CharField(max_length=100)
    batafsil = models.TextField(max_length=100)
    blog_raqam = models.IntegerField(null=True, blank=True, default=0)
    


    def str(self):  
        return f"{self.mavzu} | {self.blog_raqam}"
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"




class Rezyume(models.Model):
    rezyume = models.FileField(upload_to="rezyumelarim")