from django.contrib import admin
from .models import Currency, Ticker, Industry, PortfolioItem

# Register your models here.
admin.site.register(Currency)
admin.site.register(Industry)

@admin.register(Ticker)

class TickerAdmin(admin.ModelAdmin):
    list_display = ("ticker_field", "currency", "symbol", "industry")
    list_display_links = ["ticker_field", "currency"]

@admin.register(PortfolioItem)

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("ticker_name", "ticker_symbol", "industry", "amount", "avg_price", "bought_price")
    list_display_links = ["ticker_name"] 