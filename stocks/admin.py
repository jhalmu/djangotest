from django.contrib import admin
from .models import Currency, Ticker, Industry, Portfolio

# Register your models here.
admin.site.register(Currency)

@admin.register(Ticker)

class TickerAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name")
    list_display_links = ["name"]

admin.site.register(Industry)

@admin.register(Portfolio)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("ticker", "ticker_name", "amount", "avg_price", "bought_price")
    list_display_links = ["ticker_name"]