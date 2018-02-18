from django.contrib import admin

# Register your models here.
from .models import Stocksdetail, Stockslist

class StocksModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'symbol', 'open', 'close', 'low', 'high', 'volume')
    list_filter = ['symbol']
    search_fields = ['=symbol']

    class Meta:
        model=Stocksdetail

class StockslistModelAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'marketcap', 'sector', 'industry')
    list_filter = ('industry', 'symbol')
    search_fields = ['=symbol', '=name']

    class Meta:
        model=Stockslist


admin.site.register(Stocksdetail, StocksModelAdmin)
admin.site.register(Stockslist, StockslistModelAdmin)
