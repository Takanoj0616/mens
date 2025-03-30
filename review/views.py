from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from review.forms import ReviewForm
from .models import Review
from list.models import Therapist
"""
投稿画面を表示し、入力内容をセッションに保存して確認画面へ遷移
"""
class ReviewCreateView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'create_review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_data = form.cleaned_data
            request.session['review_data'] = {
                str(key): str(value) for key, value in review_data.items()
            }
            request.session.save()
            return redirect('review_confirm')
        return render(request, 'create_review.html', {'form': form})

class ReviewConfirmView(View):
    def get(self, request):
        review_data = request.session.get('review_data')
        if not review_data:
            return redirect('review_create')
        return render(request, 'review_confirm.html', {'review_data': review_data})

    def post(self, request):
        review_data = request.session.get('review_data')

        if not review_data:
            return redirect('review_create')

        try:
            # 外部キーの値をインスタンスに変換
            therapist_instance = Therapist.objects.get(name=review_data['girl'])
            review_data['girl'] = therapist_instance
            Review.objects.create(**review_data)
            print("データベースに保存されました:", review_data)
        except Therapist.DoesNotExist:
            return redirect('review_create')

        request.session.pop('review_data', None)
        print("セッションデータを削除しました。")
        return redirect('review_success')

class SuccessView(View):
    def get(self, request):
        return render(request, 'review_success.html')

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'