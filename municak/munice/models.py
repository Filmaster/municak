from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.

class Kategorie(models.Model):
    oznaceni_kategorie = models.CharField(max_length=50, unique=True, verbose_name="Označení kategorie produktů",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    TYP = (
        ('pušky', 'Pušky'),
        ('samopaly', 'Samopaly'),
        ('pistole', 'Pistole'),
        ('brokovnice', 'Brokovnice'),
        ('pláty', 'Pláty'),
        ('helmy', 'Helmy'),
    )
    typ = models.CharField(max_length=20, choices=TYP, blank=True, default='pušky', verbose_name="Typ", help_text='Vyberte označení typu')

    class Meta:
        ordering = ["oznaceni_kategorie"]
        verbose_name = 'Typy produktů'
        verbose_name_plural = 'Typy produktů'

    def __str__(self):
        return f"{self.oznaceni_kategorie}, {self.typ}"


class Prukaz(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název zboží", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis produktu")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    SKUPINY = (
        ('A', 'Skupina A'),
        ('B', 'Skupina B'),
        ('C', 'Skupina C'),
        ('D', 'Skupina D'),
        ('E', 'Skupina E'),
    )
    skupiny = models.CharField(max_length=20, choices=SKUPINY, blank=True, default='A', verbose_name="Skupiny zbrojního průkazu", help_text='Vyberte označení průkazu')
    foto = models.ImageField(upload_to='Prukaz/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka produktu")
    kategorie = models.ForeignKey(Kategorie, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["cena", "nazev"]
        verbose_name = 'Zbozi'
        verbose_name_plural = 'Zboží'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])