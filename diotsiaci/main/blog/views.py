from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Document
import openai

api_key = 'sk-proj-TthpmGB9V2JyshHARmH4T3BlbkFJpndemZAZM0ALVDcO4ErS'

def switch_to_french(request):
    activate('fr')
    return redirect('/')

def switch_to_english(request):
    activate('en')
    return redirect('/')

@csrf_exempt
def ExtendedFront(request):
    posts = Post.objects.all()
    response_text = None

    if request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a master poet. Craft beautiful, emotive, and lyrical poems on any topic."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.5
        )

        response_text = response['choices'][0]['message']['content'].strip()

    return render(request, 'blog/ExtendedFront.html', {'posts': posts, 'response': response_text})

def search_documents(query):
    documents = Document.objects.all()
    results = []
    for doc in documents:
        if query.lower() in doc.content.lower():
            results.append(doc)
    return results
