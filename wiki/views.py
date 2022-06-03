from django.shortcuts import render
from wiki.models import Category, Page, SubPage
from wiki.htmlContext import HtmlContext
from siteStyle.models import SiteRichText


def index(request):
    context = HtmlContext(request)

    homepagecontent = SiteRichText.objects.filter(name="HomePageContent")[0].value
    context.set("homepagecontent", homepagecontent)

    # Set context values:
    return render(request, 'index.html', context.get())


def getPage_Index(subpage):
    return subpage.page_index


def page(request, page_name):

    # Get page:
    pages = Page.objects.filter(name=page_name)

    context = HtmlContext(request, "" if len(pages) ==
                          0 else pages[0].category.name)
    if len(pages) > 0:
        if pages[0].published or request.user.is_authenticated:
            # Get subpages sorted by page_index:
            subpages = list(SubPage.objects.filter(page=page_name))
            subpages.sort(key=getPage_Index)

            context.set("page", pages[0])
            context.set("subpages", subpages)
            return render(request, 'view.html', context.get())
        else:
            context.set("object_name",
                        "Unauthorized to view page: " + page_name)
            return render(request, 'noview.html', context.get())
    else:
        context.set("object_name", "Page does not exist: " + page_name)
        return render(request, 'noview.html', context.get())


def category(request, category_name):
    context = HtmlContext(request, category_name)

    # Build list of pages in category:
    selected_categories = Category.objects.filter(name=category_name)

    if len(selected_categories) > 0:
        selected_category = selected_categories[0]
        if request.user.is_authenticated:
            # Show all pages to authenticated user:
            pages = Page.objects.filter(category=selected_category)
        else:
            # Show only published pages to unauthenticated user:
            pages = Page.objects.filter(
                category=selected_category, published=True)
    else:
        context.set("object_name", "Category does not exist: " + category_name)
        return render(request, 'noview.html', context.get())

    if len(pages) > 0:
        context.set("selected_category", selected_category)
        context.set("page_list", pages)
        return render(request, 'category.html', context.get())
    else:
        context.set("object_name", "No pages available in category: " + selected_category.label)
        return render(request, 'noview.html', context.get())
