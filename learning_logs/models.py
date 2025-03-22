from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def __str__(self):
        return self.title



# class Topic(models.Model):
#     text = models.CharField(max_length=200)
#     date_add = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text
#
# class Entry(models.Model):
#     '''Inforamtion learned by user about topic'''
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta():
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         '''Returns string view of model'''
#         text_preview = f'{self.text[:50]}...' if len(self.text) > 50 else self.text
#         return text_preview
