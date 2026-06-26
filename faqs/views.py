# Custom app - original work by Yemi Alade

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FAQ
from .forms import FAQForm


def faqs(request):
    """ Display all FAQs grouped by category """
    faqs = FAQ.objects.all()
    template = 'faqs/faqs.html'
    context = {
        'faqs': faqs,
        'on_faqs_page': True,
    }
    return render(request, template, context)


@login_required
def add_faq(request):
    """ Add a FAQ - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('faqs'))
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ added successfully!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to add FAQ. Please check the form.')
    else:
        form = FAQForm()
    template = 'faqs/add_faq.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Edit a FAQ - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('faqs'))
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ updated successfully!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to update FAQ. Please check the form.')
    else:
        form = FAQForm(instance=faq)
        messages.info(request, f'You are editing: {faq.question}')
    template = 'faqs/edit_faq.html'
    context = {'form': form, 'faq': faq}
    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a FAQ - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('faqs'))
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        faq.delete()
        messages.success(request, 'FAQ deleted!')
        return redirect(reverse('faqs'))
    template = 'faqs/delete_faq.html'
    context = {'faq': faq}
    return render(request, template, context)