from django.db import models


from django.db import models


status_choices = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
)


class Book(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, default=status_choices[0][0], verbose_name='Статус', choices=status_choices)

    def __str__(self):
        return self.author
# Create your models here.
