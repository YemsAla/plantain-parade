from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RipenessGuide
from .forms import RipenessGuideForm


def ripeness_guide(request):
    """ Display all ripeness stages """
    stages = RipenessGuide.objects.all()
    template = 'plantain_ripeness_guide/ripeness_guide.html'
    context = {
        'stages': stages,
    }
    return render(request, template, context)


def ripeness_detail(request, stage_id):
    """ Display a single ripeness stage """
    stage = get_object_or_404(RipenessGuide, pk=stage_id)
    template = 'plantain_ripeness_guide/ripeness_detail.html'
    context = {
        'stage': stage,
    }
    return render(request, template, context)


@login_required
def add_ripeness(request):
    """ Add a ripeness stage - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('ripeness_guide'))
    if request.method == 'POST':
        form = RipenessGuideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ripeness stage added successfully!')
            return redirect(reverse('ripeness_guide'))
        else:
            messages.error(request, 'Failed to add stage. Please check the form.')
    else:
        form = RipenessGuideForm()

    template = 'plantain_ripeness_guide/add_ripeness.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def edit_ripeness(request, stage_id):
    """ Edit a ripeness stage - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('ripeness_guide'))
    stage = get_object_or_404(RipenessGuide, pk=stage_id)
    if request.method == 'POST':
        form = RipenessGuideForm(request.POST, request.FILES, instance=stage)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ripeness stage updated successfully!')
            return redirect(reverse('ripeness_guide'))
        else:
            messages.error(request, 'Failed to update stage. Please check the form.')
    else:
        form = RipenessGuideForm(instance=stage)
        messages.info(request, f'You are editing {stage.stage}')

    template = 'plantain_ripeness_guide/edit_ripeness.html'
    context = {'form': form, 'stage': stage}
    return render(request, template, context)


@login_required
def delete_ripeness(request, stage_id):
    """ Delete a ripeness stage - superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('ripeness_guide'))
    stage = get_object_or_404(RipenessGuide, pk=stage_id)
    if request.method == 'POST':
        stage.delete()
        messages.success(request, 'Ripeness stage deleted!')
        return redirect(reverse('ripeness_guide'))
    template = 'plantain_ripeness_guide/delete_ripeness.html'
    context = {'stage': stage}
    return render(request, template, context)