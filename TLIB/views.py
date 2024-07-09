from django.shortcuts import redirect

def homePage(request):
    return (redirect("mangalib:manga"))