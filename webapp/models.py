from django.db import models

# Create your models here.
status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]
class GuestBook(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name="Name")
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name="Email")
    guest_note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Changed at')
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Status", default='new', choices=status_choices)

    def __str__(self):
        return f"{self.pk}. {self.name}-{self.email}-{self.created_at}-{self.changed_at}-{self.status}"

    class Meta:
        db_table = 'guestBook'
        verbose_name = 'Guest Book'
        verbose_name_plural = 'GuestBooks'