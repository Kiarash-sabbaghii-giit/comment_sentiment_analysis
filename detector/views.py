# detector/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .ml_utils import analyzer  # ← اسم کلاس رو عوض کن


def index(request):
    """
    صفحه اصلی - نمایش فرم تحلیل
    """
    return render(request, 'detector/index.html')


def predict(request):
    """
    پردازش و پیش‌بینی احساسات
    """
    if request.method == 'POST':
        # ===== دریافت متن =====
        comment = request.POST.get('comment', '').strip()

        # ===== اعتبارسنجی =====
        if not comment:
            return render(request, 'detector/index.html', {
                'error': 'لطفا یک متن وارد کنید!'
            })

        # ===== پیش‌بینی =====
        try:
            result = analyzer.predict(comment)
        except Exception as e:
            return render(request, 'detector/index.html', {
                'error': f'خطا در تحلیل: {str(e)}'
            })

        # ===== نمایش نتیجه =====
        return render(request, 'detector/result.html', {
            'comment': comment,
            'result': result
        })

    # GET request - برگشت به صفحه اصلی
    return render(request, 'detector/index.html')


def history(request):
    """
    صفحه تاریخچه
    """
    return render(request, 'detector/history.html')


def about(request):
    """
    صفحه درباره ما
    """
    return render(request, 'detector/about.html')


def history_count(request):
    """
    API برای گرفتن تعداد تاریخچه (برای نمایش در navbar)
    """
    # اینجا میتونی از دیتابیس یا localStorage استفاده کنی
    # برای نمونه، از localStorage استفاده میکنیم
    return JsonResponse({'count': 0})