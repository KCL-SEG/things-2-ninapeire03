from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if request.thing.is_authenticated:
            current_thing = request.thing

            if form.is_valid():
                text = form.cleaned_data.get('text')
                form.save(current_form)
                #request_lesson = RequestLesson.objects.create()
                return redirect('home')
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
