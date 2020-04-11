from django.conf import settings
from django.db import models
from django.utils import timezone


class Question(models.Model):
	''' Вопрос '''
	question_text = models.CharField('Вопрос', max_length=1500)
	question_author = models.CharField('Имя', max_length=100)
	question_created_date = models.DateTimeField('Время вопроса', default=timezone.now)
	''' Ответ '''
	question_answer = models.TextField('Ответ на вопрос', blank=True, null=True)
	question_answer_author = models.CharField('Имя отвечающего', max_length=100, blank=True)
	question_answer_date = models.DateTimeField('Время ответа', blank=True, null=True)

	def __str__(self):
		return self.question_text

	class Meta:
		verbose_name = "Вопрос"
		verbose_name_plural = "Вопросы"