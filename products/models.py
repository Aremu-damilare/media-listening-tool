from django.db import models

# Create your models here.


from django.conf import settings
import uuid


class UserSearchID(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)    
    search_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    searched_word =  models.JSONField() 
    searched_sources =  models.JSONField()
    search_name =  models.CharField(max_length=40, null=True, blank=False) 

    total_mentions = models.IntegerField(default=0, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add= True, null=True, blank=False) 
    
    
    def __str__(self):
        return f'{self.user} + {self.search_id}'


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)   
    searched_word =  models.CharField(max_length=40, null=True, blank=False) 

    source_name = models.CharField(max_length=60, null=True, blank=False, default='twitter') 
    source_id =  models.CharField(max_length=40, null=True, blank=False) 
    search_id = models.CharField(max_length=40, null=True, blank=False)     
    
    review_user = models.JSONField()
    review_date = models.JSONField()
    review_source = models.JSONField()
    review_sentiment = models.JSONField()
    review_text = models.JSONField()
    
    timestamp = models.DateTimeField(auto_now_add= True, null=True)
    
    def __str__(self):
        return f'{self.user}, {self.source_name}'

    def save(self, *args, **kwargs):                
        super(Product, self).save(*args, **kwargs)