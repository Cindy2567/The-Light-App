
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sermon, Event, Devotional
import requests

def get_daily_verse():
    try:
        response = requests.get('https://beta.ourmanna.com/api/v1/get/?format=json')
        if response.status_code == 200:
            data = response.json()
            verse_text = data['verse']['details']['text']
            reference = data['verse']['details']['reference']
            return {'text': verse_text, 'reference': reference}
    except:
        return {'text': 'Error retrieving verse.', 'reference': ''}
    return {'text': 'No verse available.', 'reference': ''}


def home(request):
    verse = get_daily_verse()
    return render(request, 'home.html', {'verse': verse})

def register(request):
    return render(request, 'registration/register.html')




def base(request):
    return render(request, 'base.html')

def events(request):
    devotionals = Devotional.objects.order_by('-date')[:5]
    return render(request, 'events.html', {'devotionals': devotionals})

def sermons(request):
    return render(request, 'sermons.html')


def devotional_detail(request, pk):
    devotional = get_object_or_404(Devotional, pk=pk)
    return render(request, 'devotional_detail.html', {'devotional': devotional})

INSPIRATION_DATA = {
    'peace': {
        'verses': [
            "Philippians 4:7 – 'And the peace of God... will guard your hearts.'",
            "Isaiah 26:3 – 'You will keep in perfect peace...'",
        ],
        'songs': [
            {"title": "Koseunti – Sunmisola Agbebi", "url": "https://open.spotify.com/track/6IKW8iElgDeWsiFr0yD0rI?si=c352990983b549b8"},
            {"title": "You Are Great – Steve Crown", "url": "https://open.spotify.com/track/0BoMUR3WfVuGTSZ4DUEfnZ?si=8f4f2cc377a64023"},
        ]
    },
    'faith': {
        'verses': [
            "Hebrews 11:1 – 'Now faith is the substance of things hoped for...'",
            "Mark 11:24 – 'Whatever you ask in prayer, believe...'",
        ],
        'songs': [
            {"title": "Way Maker – Sinach", "url": "https://open.spotify.com/track/4jJ0CynHMdzrgK5IOVMX08?si=d3853d72f7b04f13"},
            {"title": "More Than Gold – Judikay ft. Mercy Chinwo", "url": "https://open.spotify.com/track/74xNLJNnHY9YDFRSi57UoI?si=451569c10f044b99"},
        ]
    },
    'joy': {
        'verses': [
            "Nehemiah 8:10 – 'The joy of the Lord is your strength.'",
            "Psalm 16:11 – 'In your presence there is fullness of joy.'",
        ],
        'songs': [
            {"title": "Victory – Eben", "url": "https://open.spotify.com/track/6GL0fX7lcTWiWqdCocOLk7?si=dd198a31078640d9"},
            {"title": "I Know Who I Am – Sinach", "url": "https://open.spotify.com/track/6UQrlKMYNcPhSFfW7bAnEd?si=7117537f4f684441"},
        ]
    },
    'strength': {
        'verses': [
            "Isaiah 40:31 – 'They that wait upon the Lord shall renew their strength.'",
            "Philippians 4:13 – 'I can do all things through Christ...'",
        ],
        'songs': [
            {"title": "Miracle Papa – Joe Praize", "url": "https://open.spotify.com/track/7d76M0MTPcdV9zn4EuQYhA?si=d8c074f0741c4f7f"},
            {"title": "B'ola – Sunmisola Agbebi", "url": "https://open.spotify.com/track/6JWWPQY2pxzIXt4lKqHSvh?si=4b15c513fa224831"},
        ]
    },
}


def sermons_view(request):
    theme = request.GET.get('theme', 'peace')
    content = INSPIRATION_DATA.get(theme, INSPIRATION_DATA['peace'])
    return render(request, 'sermons.html', {
        'theme': theme.capitalize(),
        'content': content
    })
