# admin.py (inside the aptitude_test app)

from django.contrib import admin
from .models import Section, Question, Option, UserScore, UserAnswer

# Register the Section model
admin.site.register(Section)

# Create an admin class for the Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'section', 'score', 'is_multiple_choice')
    list_filter = ('section',)
    search_fields = ('text',)
    list_per_page = 20

# Register the Question model with its admin class
admin.site.register(Question, QuestionAdmin)

# Create an admin class for the Option model
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('question__section',)
    search_fields = ('text',)
    list_per_page = 20

# Register the Option model with its admin class
admin.site.register(Option, OptionAdmin)

# Register the UserScore model
admin.site.register(UserScore)

# Register the UserAnswer model
admin.site.register(UserAnswer)
