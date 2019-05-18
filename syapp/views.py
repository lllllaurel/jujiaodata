from django.shortcuts import render

# jujiaodata.com.
# 生成列表页
 
from django.http import HttpResponse
import json

# def index(request):
#     diariesDic = [{
#     "cover":"http://m.chanyouji.cn/index-cover/64695-2679221.jpg?imageView2/1/w/620/h/330/format/jpg",
#     "title":"此刻静好，愿幸福长存.py",
#     "meta": "2016.10.17"
#     }]*10
#     lastId=request.GET.get('lastid',default='3')
#     once=request.GET.get('one',default='3')
#     try:
#         last = int(lastId)
#         one = int(once)
#     except:
#         last = 3
#     return HttpResponse(json.dumps(diariesDic[last-one:last]))
#
# def detail(request):
#     context = {}
#     context['htmlBody'] = "helllo world"
#     return render(request, 'detail.html', context)
#
# def admin(request):
#     return render(request, 'admin.html')