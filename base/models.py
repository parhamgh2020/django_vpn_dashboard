from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Verification(models.Model):
    verification_code = models.CharField(max_length=255)
    permission_num = models.PositiveIntegerField()

    def __str__(self):
        return f"identification_code: {self.verification_code}, permission_num: {self.permission_num}"


class User(AbstractUser):
    identification_code = models.ForeignKey(Verification,
                                            null=True,
                                            on_delete=models.PROTECT)


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk": self.pk})
