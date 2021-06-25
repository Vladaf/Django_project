from django.db import models


class UserMessage(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="User name",
    )
    email = models.EmailField(
        verbose_name="User email",
    )
    subject = models.CharField(
        max_length=100,
        verbose_name="Message subject",
    )
    message = models.TextField(
        verbose_name="Message text",
    )
    is_worked = models.BooleanField(
        default=False,
        verbose_name="Is worked",
    )

    class Meta:
        db_table = "user_messages"
        verbose_name = "User message"
        verbose_name_plural = "User messages"

    def str(self) -> str:
        return self.name