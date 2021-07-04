import datetime
from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "post1",
        "image": "post1.png",
        "author": "Túlio Farias",
        "date": date(2021, 7, 4),
        "title": "Post 1 Title",
        "summary": "Post 1 summary",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Beatae quisquam laboriosam rerum ipsam quasi mollitia,
            cumque blanditiis ratione facilis totam dicta ipsa fugiat libero sequi perferendis perspiciatis porro fuga
            harum.

            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Beatae quisquam laboriosam rerum ipsam quasi mollitia,
            cumque blanditiis ratione facilis totam dicta ipsa fugiat libero sequi perferendis perspiciatis porro fuga
            harum.
            
        """
    },
    {
        "slug": "post2",
        "image": "post2.jpg",
        "author": "Túlio Farias",
        "date": date(2021, 7, 4),
        "title": "Post 2 Title",
        "summary": "Post 2 summary asdhnasdh asduihauis hdi asuih has ",
        "content": """
            parara pururu            
        """
    }
]
def get_date(post):
    return post['date']

def get_post(post_slug):
    post=all_posts
    return 
    

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:] #pega os 3 últimos
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })
