from django.db import models


class Carrer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CourseTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    class Meta:
        unique_together = ('course_template', 'carrer')

    course_template = models.ForeignKey(
        'CourseTemplate',
        on_delete=models.CASCADE,
    )
    carrer = models.ForeignKey(
        'Carrer',
        on_delete=models.CASCADE,
    )

    get_dynamic_natural_key = lambda self: '{0}:{1}:{2}'.format(
            self.id,
            self.course_template.code,
            self.carrer.code
        )
