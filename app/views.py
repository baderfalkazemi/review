from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from app.models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleCreateSerializer


# Create your views here.

def create_view(request):
    form = ArticleForm()

    context = {
        "form":form
    }
    return render(request, 'create_page.html', context)



class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer




class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'article_id'


class ArticleCreateView(CreateAPIView):
    serializer_class = ArticleCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)