from django.shortcuts import render, redirect
import openai

openai.api_key = "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"

messages = []

def home(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1,
        )
        answer = response.choices[0].text.strip()
        messages.append({'sender': 'user', 'message': prompt})
        messages.append({'sender': 'bot', 'message': answer})
        return redirect('home')
    else:
        return render(request, 'chatgpt_app/home.html', {'messages': messages})