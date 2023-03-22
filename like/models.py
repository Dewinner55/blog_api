from django.db import models, migrations

from post.models import Post

class Like(models.Model):
    owner = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'post']
                            # 7          14
                            # 7          14 нельзя

class Favorites(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='favorites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['owner', 'post']

class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'), # замените на последнюю существующую миграцию в приложении like
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # добавьте поля модели
            ],
        ),
    ]

