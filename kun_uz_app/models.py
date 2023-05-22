from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    type_of_news = models.CharField(max_length=256)
    #ЎЗБЕКИСТОН,ЖАҲОН,ИҚТИСОДИЁТ,ЖАМИЯТ,ФАН-ТЕХНИКА,СПОРТ,НУҚТАЙИ,НАЗАР,АУДИО
    def __str__(self):
        return self.type_of_news

class Language(models.Model):
    tillar=models.CharField(max_length=50)
#   rus  uzb eng

    def __str__(self):
        return self.tillar


class Viloyatlar(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hashtag(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




#############################################
class Post(models.Model):


    title = models.CharField(max_length=256)
    briefly = models.CharField(max_length=256)
    content = models.TextField()

    Category_of_content = models.ForeignKey(Category, on_delete=models.CASCADE)
    # lang =models.ForeignKey(Language, on_delete=models.CASCADE)
    

    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')    

    
    regions = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag)

    
    
    by_who = models.ForeignKey(User, on_delete=models.CASCADE)
    is_advertising = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.title}: || Publeshed BY {self.by_who}"




