from django.db import models


class Player(models.Model):
    username = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Character(models.Model):
    name = models.CharField(max_length = 45)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    winner = models.ForeignKey(Player, related_name = 'won_match', on_delete=models.CASCADE)
    winner_char = models.ManyToManyField(Character, related_name = 'winning')
    loser = models.ForeignKey(Player, related_name = 'loss_match', on_delete=models.CASCADE)
    loser_char = models.ManyToManyField(Character, related_name = 'losing')
    tourney = models.CharField(max_length = 55)
    round = models.CharField(max_length = 60)
    date = models.DateField()
    video = models.URLField(max_length = 225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)