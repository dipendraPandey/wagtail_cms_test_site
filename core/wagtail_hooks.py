from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register("insert_global_admin_css",order=100)
def global_admin_css():
    """dddd"""
    return format_html('<link rel="stylesheet" href ="{}">', static("css/custom.css"))


@hooks.register("insert_global_admin_css", order=100)
def global_admin_js():
    """Some docstring in here"""
    return format_html('<script src={} ></script>', static("js/custom.js"))