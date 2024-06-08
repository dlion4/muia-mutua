from ..forms import SubscriptionForm


def lns_context_processors(request):
    return {
        "subscription_form": SubscriptionForm(),
    }