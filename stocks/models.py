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


class Ticker(models.Model):
    symbol = models.CharField(max_length=6)
    name = models.CharField(max_length=60)

    class Meta:
         verbose_name = _("ticker")
         verbose_name_plural = _("tickers")
         ordering = ["symbol"]
 
    def __str__(self):
         return self.symbol
 
    def get_absolute_url(self):
         return reverse("ticker_detail", kwargs={"pk": self.pk})   
    

class Industry(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
         verbose_name = _("industry")
         verbose_name_plural = _("industries")
 
    def __str__(self):
         return self.name
 
    def get_absolute_url(self):
         return reverse("industry_detail", kwargs={"pk": self.pk})   



class Portfolio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)
    ticker = models.OneToOneField(Ticker, unique=True, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)

    def ticker_name(self):
        return self.ticker.name
 
    def bought_price(self):
        return round(self.amount*self.avg_price,2)
 
    # def __str__(self):
    #     return self.ticker.name + ' (' + self.ticker.symbol  + ') Amount: ' + str(self.amount)
 
    def get_absolute_url(self):
         return reverse("portfolio_detail", kwargs={"pk": self.pk}) 
    