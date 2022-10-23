from django.db import models, IntegrityError


class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'create_at'


class User(models.Model):
    name = models.CharField(max_length=50)
    user_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)


class Word(models.Model):
    word = models.CharField(max_length=50, )
    user_words = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, to_field='room_name')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('word', 'user_words',),
                name='unique_word',
            )
        ]


