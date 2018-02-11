"""Render thecraiglist."""
from django.shortcuts import render

# Create your views here.


def index(request):
    """Return a copy that is easily postable."""

    return render(request, 'thecraiglist/index.html')
