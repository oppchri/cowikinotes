import os
from siteStyle.models import SiteColor, SiteString, SiteRichText
from wiki.models import Category, Page


# List Button Container:
class ListButton:
    def __init__(self, label, state, link):
        self.label = label
        self.state = state
        self.link = link


class HtmlContext:

    def __init__(self, request, selected_category="") -> None:
        self.request = request
        self.context = {}
        self.selected_category = selected_category
        print(selected_category)

    def get(self) -> dict:
        self.__getSiteColors()
        self.__getListButtons(self.selected_category)

        # Set some default content:
        self.context["title"] = SiteString.objects.filter(key="title")[0].value
        self.context["pagenotfoundcontent"] = SiteRichText.objects.filter(
            name="PageNotFoundContent")[0].value
        self.context['GOOGLE_VERIFICATION'] = os.environ['GOOGLE_VERIFICATION']

        return self.context

    def set(self, key, value):
        # Add a key/value pair to context:
        self.context[key] = value

    def __getListButtons(self, selected_category):
        listbutton_list = []

        # Add home button (active if no category is selected):
        listbutton_list.append(ListButton(
            "Home", "active" if selected_category == "" else "inactive", "/"))

        categories = Category.objects.all()
        for c in categories:
            if self.request.user.is_authenticated:
                # Show all categories to authorized user:
                if len(Page.objects.filter(category=c)) > 0:
                    listbutton_list.append(ListButton(
                        c.label, "active" if selected_category == c.name else "inactive", f"/category/{c.name}"))
            else:
                # Show only categories with published pages to unauthorized user:
                if len(Page.objects.filter(category=c, published=True)) > 0:
                    listbutton_list.append(ListButton(
                        c.label, "active" if selected_category == c.name else "inactive", f"/category/{c.name}"))
        self.context["listbutton_list"] = listbutton_list

    def __getSiteColors(self):
        shadowcolor = SiteColor.objects.filter(name="shadow")[0]
        ribboncolor = SiteColor.objects.filter(name="ribbon")[0]
        footertext = SiteColor.objects.filter(name="footertext")[0]
        dimhighlight = SiteColor.objects.filter(name="dimhighlight")[0]
        brighthighlight = SiteColor.objects.filter(name="brighthighlight")[0]
        bodytext = SiteColor.objects.filter(name="bodytext")[0]
        background = SiteColor.objects.filter(name="background")[0]
        self.context["shadowcolor"] = shadowcolor.color
        self.context["ribboncolor"] = ribboncolor.color
        self.context["footertext"] = footertext.color
        self.context["dimhighlight"] = dimhighlight.color
        self.context["brighthighlight"] = brighthighlight.color
        self.context["bodytext"] = bodytext.color
        self.context["background"] = background.color
