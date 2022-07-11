from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(Timestamp):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Category(Timestamp):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(Timestamp):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_date = models.DateField()
    project_url = models.URLField(max_length=255)

    def __str__(self):
        return self.title


class ProjectImage(Timestamp):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    file_url = models.URLField(max_length=255)
    is_poster = models.BooleanField(default=False)

    def __str__(self):
        return self.file_url
