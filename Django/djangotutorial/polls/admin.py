from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    show_change_link = True  # tiện mở form chi tiết Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    date_hierarchy = "pub_date"
    list_per_page = 25

    # Nếu bạn CHƯA thêm @admin.display ở models.py, dùng wrapper sau:
    # @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    # def was_published_recently(self, obj):
    #     return obj.was_published_recently()

# (Tùy chọn) Đăng ký Choice để có màn hình riêng quản lý Choice
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "question", "votes"]
    search_fields = ["choice_text", "question__question_text"]
    list_select_related = ["question"]
