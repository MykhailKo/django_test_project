import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	art_title = models.CharField("название статьи", max_length = 200)
	art_text = models.TextField("текст статьи")
	pub_date = models.DateTimeField("дата публикации")
	preview = models.ImageField(blank = True, upload_to = "images/articles/", help_text = "150px150px")

	def __str__(self):
		return self.art_title

	def recent_pub(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"


class Comment(models.Model):
	art_id = models.ForeignKey(Article, on_delete = models.CASCADE)
	author = models.CharField("имя автора", max_length = 50)
	com_text = models.CharField("тект комментария", max_length = 300)	

	def __str__(self):
		return self.author

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"