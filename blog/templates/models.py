from django.db import models

#class 이름 = table 이름
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성

    #self - post에 의해서 만들어지는 data - primary key 값은 자동 생성됨
    def __str__(self):
        return f'[{self.pk}] {self.title}  - {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'