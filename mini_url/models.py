from django.db import models
import random
import string


class MiniUrl(models.Model):
    """
    Classe pour minimiser les URLs
    """
    url = models.URLField(verbose_name="URL", unique=True)
    code = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    pseudo = models.CharField(max_length=50, blank=True, null=True)
    nb_acces = models.IntegerField(default=0, verbose_name="Nombre d'accès")

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.url)

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        return ''.join(aleatoire)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniUrl, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"
