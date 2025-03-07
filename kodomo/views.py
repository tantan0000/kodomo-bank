from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Ticket


class HomeTemplateView(TemplateView):
    template_name = "kodomo/home.html"


class TicketListView(ListView):
    template_name = "kodomo/tickets/list.html"
    model = Ticket


# class UseTicketView(TemplateView):
#     template_name = "kodomo/tickets/use.html"


# class BuyTicketView(TemplateView):
#     template_name = "kodomo/tickets/by.html"


# class BankView(Detail):
#     template_name = "kodomo/banks/detail.html"

