from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    rating = models.IntegerField(default=0)
    posts = models.Manager
    
    
        
class Category(models.Model):
    categories = models.CharField(max_length=100, unique=True)
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')
    article_or_news = models.IntegerField(default= 0)
    automatic_data_time = models.DateTimeField(auto_now_add= True)
    post_category = models.ManyToManyField(Category, through= 'Post_Category')
    article_title_news = models.CharField(max_length= 255, db_index=True) #добавлено индексирование
    text_title_news = models.TextField()
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()
        
    def dislike(self):
        self.rating -=1
        self.save()
    
    def preview(self):
        return f"{self.text[:124]}..."
    
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    automatic_data_time = models.DateTimeField(auto_now_add= True)
    rating = models.IntegerField(default=0)
    
    def like(self):
        self.rating += 1
        self.save()
        
    def dislike(self):
        self.rating -=1
        self.save()