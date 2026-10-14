from .models import Category, About, SocialLink

# gate categories function:
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

# get about and socil link function:
def get_social_links(request):
    social_links = SocialLink.objects.all()
    about = About.objects.first()  # first entry nikal lega
    return dict(social_links=social_links, about=about)
