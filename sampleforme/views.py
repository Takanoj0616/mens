from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import PostForm
from .models import Post


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'myapp/post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            # フォームの有効なデータを取得
            post_data = form.cleaned_data
            # データをセッションに保存（キーと値をすべて文字列に変換）
            request.session['post_data'] = {
                str(key): str(value) for key, value in post_data.items()
            }
            return redirect('post_confirm')
        return render(request, 'myapp/post_create.html', {'form': form})

class PostConfirmView(View):
    def get(self, request):
        post_data = request.session.get('post_data')
        if not post_data:
            return redirect('post_create')
        return render(request, 'myapp/post_confirm.html', {'post_data': post_data})

    def post(self, request):
        post_data = request.session.get('post_data')
        if not post_data:
            return redirect('post_create')
        # 保存処理
        Post.objects.create(**post_data)
        del request.session['post_data']  # セッションデータを削除
        return redirect('post_complete')


class PostCompleteView(View):
    def get(self, request):
        return render(request, 'myapp/post_complete.html')


class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'
    context_object_name = 'posts'