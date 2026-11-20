from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from .models import Education, Experience, ExperiencePoint, Language, Profile, Project, SkillCategory, Skill

# Register your models here.
@admin.register(Education)
class EducationAdmin(TabbedTranslationAdmin):
    list_display = ("title", "organization", "start_date", "end_date", "is_visible")

class ExperiencePointInline(TranslationStackedInline):
    model = ExperiencePoint
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(TabbedTranslationAdmin):
    list_display = ("position", "organization", "start_date", "end_date", "is_visible")
    inlines = [ExperiencePointInline]

@admin.register(Language)
class LanguageAdmin(TabbedTranslationAdmin):
    list_display = ("name", "level")

@admin.register(Profile)
class ProfileAdmin(TabbedTranslationAdmin):
    list_display = ("name", "job_title", "email")

@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ("title", "is_visible")

@admin.register(SkillCategory)
class SkillCategoryAdmin(TabbedTranslationAdmin):
    list_display = ("name",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")