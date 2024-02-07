from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext as _
# primary_key=True

#AVB_CURRENCY = [
#    ('USD','USD'),
#   ('EUR','EUR'),
#    ('SEK','SEK'),
#    ('XXX','XXX'),
#]

class Currency(models.Model):
     name = models.CharField(max_length=60)
     
     class Meta:
         verbose_name = _("currency")
         verbose_name_plural = _("currencies")
 
     def __str__(self):
         return self.name
 
     def get_absolute_url(self):
         return reverse("currency_detail", kwargs={"pk": self.pk})

class Industry(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
         verbose_name = _("industry")
         verbose_name_plural = _("industries")
         
 
    def __str__(self):
         return self.name
 
    def get_absolute_url(self):
         return reverse("industry_detail", kwargs={"pk": self.pk})   


class Ticker(models.Model):
    symbol = models.CharField(max_length=6)
    name = models.CharField(max_length=60)
    currency = models.ForeignKey(Currency, default=Currency, on_delete=models.SET_NULL, blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
         verbose_name = _("ticker")
         verbose_name_plural = _("tickers")
         ordering = ["symbol"]
 
    def ticker_field(self):
         return self.name + ' (' + self.symbol +')'
 
    def get_absolute_url(self):
         return reverse("ticker_detail", kwargs={"pk": self.pk})

class PortfolioItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    ticker = models.ManyToManyField(Ticker)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = _("portfolio item")
        verbose_name_plural = _("portfolio items")
    
    def __str__(self):
        return self.ticker

    def ticker_name(self):
        return self.ticker.name
    
    def ticker_symbol(self):
        return self.ticker.symbol
 
    def bought_price(self):
        return round(self.amount*self.avg_price,2)
 
    def stock(self):
         return self.ticker.name + ' (' + self.ticker.symbol  + ')'
 
    def get_absolute_url(self):
         return reverse("portfolioitem_detail", kwargs={"pk": self.pk}) 
    