from django.db import models

from .enums import TerritoryTypes

# Create your models here.
class Territory(models.Model):
    """Representation of a `Territory`.
    Attributes:
        code (`str`): Code of the territory.
        name (`str`): Name of the territory.
        kind (`str`): Kind of territory among [FRCOMM, FREPCI, FRDEPA, FRCANT]
        updated_at (`datetime`): Update date of the territory.
        created_at (`datetime`): Creation date of the territory.
        is_current (`boolean`)
        population (`int`): population number
        official_website_url (`str`): official website url
        articles_count (`integer`): count of articles
        admin_docs_count (`integer`): count of admin docs
        impacters_count (`integer`): count of impacters
        websites_count (`integer`): count of websites 
        sources_count (`integer`): count of sources
        
    """
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50, choices=TerritoryTypes.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_current = models.BooleanField(null=True)
    population = models.IntegerField(null=True)
    official_website_url = models.CharField(max_length=50, null=True)
    articles_count = models.IntegerField(default=0)
    admin_docs_count = models.IntegerField(default=0)
    impacters_count = models.IntegerField(default=0)
    websites_count = models.IntegerField(default=0)
    sources_count = models.IntegerField(default=0)
    