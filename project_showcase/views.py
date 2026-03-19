"""
Views for the SI3DR Project Showcase Website

This module contains all view functions for rendering the promotional website pages
and handling form submissions.
"""

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import (
    ProjectInfo, Objective, TeamMember, Supervisor, Technology,
    SystemPhase, Feature, Screenshot, Result, FutureScope,
    ContactSubmission, Methodology, Limitation
)
from .forms import ContactForm
from .museum_data import get_museum_artifacts


def get_project_context():
    """
    Returns common context data used across all pages.
    """
    try:
        project_info = ProjectInfo.objects.first()
    except ProjectInfo.DoesNotExist:
        project_info = None
    
    return {
        'project_info': project_info,
        'project_title': project_info.title if project_info else "Single Image 3D Reconstruction",
        'institution': project_info.institution if project_info else "Tribhuvan University, IOE Pulchowk Campus",
    }


def home(request):
    """
    Renders the homepage with hero section and project overview.
    """
    context = get_project_context()
    context['objectives'] = Objective.objects.all()[:4]
    context['features'] = Feature.objects.all()[:6]
    context['team_members'] = TeamMember.objects.all()
    context['technologies'] = Technology.objects.all()[:8]
    context['results'] = Result.objects.all()[:4]
    return render(request, 'project_showcase/home.html', context)


def about(request):
    """
    Renders the About Project page with abstract, problem statement, and objectives.
    """
    context = get_project_context()
    context['objectives'] = Objective.objects.all()
    context['team_members'] = TeamMember.objects.all()
    context['supervisors'] = Supervisor.objects.all()
    return render(request, 'project_showcase/about.html', context)


def technology(request):
    """
    Renders the Technology Stack page.
    """
    context = get_project_context()
    
    # Group technologies by category
    context['languages'] = Technology.objects.filter(category='language')
    context['frameworks'] = Technology.objects.filter(category='framework')
    context['tools'] = Technology.objects.filter(category='tool')
    context['models'] = Technology.objects.filter(category='model')
    context['hardware'] = Technology.objects.filter(category='hardware')
    context['all_technologies'] = Technology.objects.all()
    
    return render(request, 'project_showcase/technology.html', context)


def architecture(request):
    """
    Renders the System Architecture page with workflow diagrams.
    """
    context = get_project_context()
    context['phases'] = SystemPhase.objects.all()
    context['methodology_steps'] = Methodology.objects.all()
    return render(request, 'project_showcase/architecture.html', context)


def features(request):
    """
    Renders the Features/Modules page.
    """
    context = get_project_context()
    context['features'] = Feature.objects.all()
    return render(request, 'project_showcase/features.html', context)


def screenshots(request):
    """
    Renders the Screenshots/Demo page with virtual museum gallery.
    """
    context = get_project_context()
    context['screenshots'] = Screenshot.objects.all()
    
    # Group screenshots by category
    categories = Screenshot.objects.values_list('category', flat=True).distinct()
    context['categories'] = categories
    context['screenshots_by_category'] = {
        cat: Screenshot.objects.filter(category=cat)
        for cat in categories
    }
    
    # Load museum artifacts for the gallery
    context['artifacts'] = get_museum_artifacts()
    
    return render(request, 'project_showcase/screenshots.html', context)


def results(request):
    """
    Renders the Results & Outcomes page.
    """
    context = get_project_context()
    context['results'] = Result.objects.all()
    context['limitations'] = Limitation.objects.all()
    
    # Group limitations by category
    context['reconstruction_limitations'] = Limitation.objects.filter(category='reconstruction')
    context['editing_limitations'] = Limitation.objects.filter(category='editing')
    context['system_limitations'] = Limitation.objects.filter(category='system')
    
    # Load museum artifacts for reconstruction results
    context['artifacts'] = get_museum_artifacts()
    
    return render(request, 'project_showcase/results.html', context)


def future_scope(request):
    """
    Renders the Future Scope page with possible enhancements.
    """
    context = get_project_context()
    context['future_items'] = FutureScope.objects.all()
    
    # Group by category
    context['reconstruction_future'] = FutureScope.objects.filter(category='reconstruction')
    context['editing_future'] = FutureScope.objects.filter(category='editing')
    context['system_future'] = FutureScope.objects.filter(category='system')
    context['research_future'] = FutureScope.objects.filter(category='research')
    
    return render(request, 'project_showcase/future_scope.html', context)


def contact(request):
    """
    Renders the Contact page with contact form.
    """
    context = get_project_context()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('project_showcase:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context['form'] = form
    context['team_members'] = TeamMember.objects.all()
    context['supervisors'] = Supervisor.objects.all()
    
    return render(request, 'project_showcase/contact.html', context)


@require_POST
@csrf_protect
def contact_submit(request):
    """
    AJAX endpoint for contact form submission.
    """
    form = ContactForm(request.POST)
    if form.is_valid():
        submission = form.save()
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.'
        })
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)


def team(request):
    """
    Renders the Team page with team members and supervisors.
    """
    context = get_project_context()
    context['team_members'] = TeamMember.objects.all()
    context['supervisors'] = Supervisor.objects.all()
    return render(request, 'project_showcase/team.html', context)


def virtual_museum(request):
    """
    Renders the Virtual Museum page for visualizing GLB files.
    """
    context = get_project_context()
    # Optionally, add a list of models if you want to make it dynamic
    return render(request, 'project_showcase/virtual_museum.html', context)
