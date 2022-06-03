from django.contrib.sitemaps import Sitemap
from wiki.models import Page, Category

# Sitemap classes:


class PageSiteMap(Sitemap):
    # How frequently the page is expected to change:
    changefreq = "weekly"
    # The priority of these entries on the website:
    priority = 0.7

    # Return queryset of objects to map:
    def items(self):
        return Page.objects.filter(published=True)

    # Define the location of each entry:
    def location(self, item: Page) -> str:
        return f"/page/{item.name}/"


class CategorySiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return Category.objects.all()

    def location(self, item: Page) -> str:
        return f"/category/{item.name}/"


# Map to sitemaps:
SITEMAPS = {
    'page': PageSiteMap,
    'category': CategorySiteMap
}
