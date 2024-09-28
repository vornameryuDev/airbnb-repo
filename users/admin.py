from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User



@admin.register(User)
class UserAdmin(UserAdmin):
	
	fieldsets = [
		(
			'Profile',
			{
				'fields': (
					'username',
					'password',
					'email',
					# 'first_name',
					# 'last_name',
				)
			}
		),
		(
			'Permissions',
			{
				'description': 'Permission of UserModel',
				'fields': (
					'is_active',
					'is_staff',
					'is_superuser',
					'groups',
					'user_permissions'
				),
				'classes': ('collapse',)
			}
		),
		(
			'Important Dates',
			{
				'description': 'Date',
				'fields': (
					'last_login',
					'date_joined',
				),
				'classes': ('collapse',)
			}
		)
	]
