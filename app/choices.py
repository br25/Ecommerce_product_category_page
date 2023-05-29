from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.TextChoices):
    SMARTPHONE = 'Smartphone', _('Smartphone')
    EARPHONE = 'Earphone', _('Earphone')
    POWER_BANK = 'Power Bank', _('Power Bank')


class ProductWarranty(models.TextChoices):
    ONE_YEAR = '1', _('1')
    TWO_YEAR = '2', _('2')


class ProductBrand(models.TextChoices):
    ANKER = 'Anker', _('Anker')
    AWEI = 'Awei', _('Awei')
    GEECO = 'Geeco', _('Geeco')
    HAYLOU = 'Haylou', _('Haylou')
    HOCO = 'Hoco', _('Hoco')
    XIAOMI = 'Xiaomi', _('Xiaomi')
