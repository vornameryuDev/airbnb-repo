from django.db import models



class CommomModel(models.Model):
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	#추상 클래스로만 설정
	class Meta:
		abstract = True 

