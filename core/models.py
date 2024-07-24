from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)

    class Meta:
        ordering = ['done', '-created_at']

    def __str__(self):
        return (
            f"{self.content} (completed: {self.done})"
            f"Created at: {self.content}"
            f"Deadline: {self.deadline}"
        )