from django.contrib import admin

from LogAuth.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass
