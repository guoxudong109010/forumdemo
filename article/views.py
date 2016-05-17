#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from block.models import Block
from comment.models import Comment
from comment.views import create_comment
from comment.views import comment_list
from utils.paginator import paginate_queryset
from article.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request,block_id):
    block_id = int(block_id)
    page_no = int(request.GET.get("page_no", "1"))
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
   # p=Paginator(articles,1)
   # if page_no > p.num_pages:
   #     page_no = p.num_pages
   # if page_no <= 0:
   #     page_no = 1
  #  page_links=[i for i in range(page_no-5,page_no+6) if i > 0 and i < p.num_pages]
  #  page=p.page(page_no)
  #  previous_link=page_links[0]-1
  #  next_link=page_links[-1]+1
  #  return render_to_response("article_list.html", {"articles":page.object_list,"b":block,"has_previous":previous_link > 0,"has_next":next_link <= p.num_pages,"previous_link":previous_link,"next_link":next_link,"page_cnt":p.num_pages,"current_no":page_no,"page_links":page_links},context_instance=RequestContext(request))
    object_list, pagination_data = paginate_queryset(articles, page_no, cnt_per_page=1)
    return render_to_response("article_list.html", {"articles":object_list, "b":block, "pagination":pagination_data}, context_instance=RequestContext(request))
@login_required
def create_article(request, block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=="GET":
        return render_to_response("article_create.html", {"b":block}, context_instance=RequestContext(request))
    else: #request.method=="post"
        title=request.POST["title"].strip()
        content=request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题和内容均不能为空')
            return render_to_response("article_create.html", {"b":block,"title":title,"content":content},context_instance=RequestContext(request))
        owner=User.objects.all()[0]#TODO
        new_article=Article(block=block,owner=request.user,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'成功发布文章')
        return redirect(reverse("article_list",args=[block.id]))

def article_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    comment_page_no = int(request.GET.get("comment_page_no", "1"))
    comments = Comment.objects.filter(article=article).order_by("-last_update_timestamp")
    print comments
    object_list, pagination_data = paginate_queryset(comments, comment_page_no, cnt_per_page=1)
    return render_to_response("article_detail.html", {"comments":object_list, "article":article, "pagination":pagination_data}, context_instance=RequestContext(request))
   # return render_to_response("article_detail.html", {"article":article},context_instance=RequestContext(request))
        


