from django.db import models



class FlashCard(models.Model):
    question = models.TextField(max_length=100,verbose_name='سوال')
    answer = models.TextField(max_length=100 , verbose_name='پاسخ')
    create_at = models.DateTimeField(auto_now_add= True, verbose_name= 'ساخته شده در')
    update_at = models.DateTimeField(auto_now=True, verbose_name='اپدیت شده در')

    def __str__(self):
        return f'{self.question[:10]}...'
    class Meta:
        verbose_name = 'فلش کارت'
        verbose_name_plural = 'فلش کارتها'
