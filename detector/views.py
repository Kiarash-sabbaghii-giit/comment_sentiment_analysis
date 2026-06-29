# detector/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .ml_utils import detector


def index(request):
    return render(request, 'detector/index.html')


def predict(request):
    if request.method == 'POST':
        # Check if batch mode
        batch_comments = request.POST.get('batch_comments', '')
        single_comment = request.POST.get('comment', '')

        # If batch mode
        if batch_comments:
            comments = [c.strip() for c in batch_comments.split('\n') if c.strip()]
            results = []
            for comment in comments:
                result = detector.predict(comment)
                results.append({
                    'comment': comment,
                    'result': result
                })

            return render(request, 'detector/result.html', {
                'batch_results': results,
                'batch_mode': True
            })

        # Single mode
        comment = single_comment
        if not comment.strip():
            return render(request, 'detector/index.html', {
                'error': 'Please enter a comment!'
            })

        result = detector.predict(comment)
        return render(request, 'detector/result.html', {
            'comment': comment,
            'result': result,
            'batch_mode': False
        })

    return render(request, 'detector/index.html')


def history(request):
    return render(request, 'detector/history.html')


def about(request):
    return render(request, 'detector/about.html')


def history_count(request):
    # This would normally read from a database
    # For demo, we'll return a simple count
    return JsonResponse({'count': 0})