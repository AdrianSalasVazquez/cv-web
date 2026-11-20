from modeltranslation.translator import register, TranslationOptions
from .models import Education, Experience, ExperiencePoint, Language, Profile, Project, SkillCategory

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ("title", "description")

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ("position",)

@register(ExperiencePoint)
class ExperiencePointTranslationOptions(TranslationOptions):
    fields = ("text",)

@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ("job_title", "summary", "location")

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("description",)

@register(SkillCategory)
class SkillCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)