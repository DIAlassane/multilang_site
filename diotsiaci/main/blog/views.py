from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Document
import openai

api_key = 'sk-proj-RVdItmDxN14DhXGVOgifT3BlbkFJ8CxeucIFBYTABhRm9lee'

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
        prompt = user_input

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5
        )

        response_text = response['choices'][0]['text'].strip()

    return render(request, 'blog/ExtendedFront.html', {'posts': posts, 'response': response_text})
def search_documents(query):
    documents = Document.objects.all()
    results = []
    for doc in documents:
        if query.lower() in doc.content.lower():
            results.append(doc)
    return results
