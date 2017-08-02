from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404
from django.template.context import RequestContext
from urllib import unquote
import datetime
import time
from django.db.models import Q
from scriptsports.models import*
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

def mainecho(request):
    try:
        now=datetime.datetime.now()
        dt1=datetime.timedelta(hours=3)
        news_oneraw=News.objects.filter(important=1)
        news_mraw=News.objects.filter().exclude(id=news_oneraw[0].id)
        tvshow=Gameshow.objects.filter(game_time__gte=(now-dt1))
        news_craw=News.objects.filter(newsleixin=6)
        video_list=Regame.objects.filter()
        sharing=Sharing.objects.filter()
        talk=Talk.objects.filter()
    except IndexError:
        raise Http404
    return render_to_response('ssmain.html',{'onetitle':news_oneraw[0],'p_mraw1':news_mraw[0:5],'p_mraw2':news_mraw[5:10],\
                                             'p_mraw3':news_mraw[10:15],'tvshow':tvshow[0:9],'p_craw':news_craw[0:6],\
                                             'video_list':video_list[0:50],'sharing':sharing[0:9],'talk':talk[0:9],\
                                             'user':request.user})

def livekanecho(request):
    try:
        tv=request.GET.get('tv')
        pd=int(request.GET.get('pd'))
    except ValueError:
        raise Http404()
    adr=Tv.objects.get(id=tv)
    return render_to_response('live/live1.html',{'adr':adr,"pd":pd,'user':request.user})

def jijinecho(request):
    idj=int(request.GET.get('idj'))
    idr=int(request.GET.get('idr'))
    ss=int(request.GET.get('ss'))
    jijinstream=Regame.objects.get(id=idr)
    jis=Jijin.objects.get(id=idj)
    return render_to_response('video_list/jijin.html',{'jjs':jijinstream,'jis':jis,'ss':ss,'user':request.user})


def videolistecho(request):
    if request.is_ajax():
        x=int(request.GET.get('action'))
        y=int(request.GET.get('action1'))
        if(x):
            if(y):
                video_list=Regame.objects.filter(game_bigleixin_id=x).order_by("-important",'-game_time')
            else:
                video_list=Regame.objects.filter(game_bigleixin_id=x)
        else:
            if(y):
                video_list=Regame.objects.filter().order_by("-important",'-game_time')
            else:
                video_list=Regame.objects.all()
        return render_to_response('video_list/changelist.html',{'video_list':video_list[0:100],},context_instance = RequestContext(request))
    else:
        video_list=Regame.objects.all()
        return render_to_response('video_list/video_list.html',{'video_list':video_list,},context_instance = RequestContext(request))


def streamecho(request):
    gid=int(request.GET.get('gid'))
    idd=int(request.GET.get('id'))
    sga=Regame.objects.filter(id=idd)
    stream=Stream.objects.filter(id=gid)
    return render_to_response('video_list/restream.html',{'stream':stream[0],'sga':sga[0],'user':request.user})

def streamextrecho(request):
    eid=int(request.GET.get('eid'))
    xdd=int(request.GET.get('id'))
    extstream=Stream.objects.filter(id=eid)
    extvideo=Regame.objects.filter(id=xdd)
    return render_to_response("video_list/restream_extr.html",{'extstream':extstream[0],'extvideo':extvideo[0],'user':request.user})


def videoecho(request):
    iid=int(request.GET.get('xid'))
    iiid=int(request.GET.get('zid'))
    tts=Regame.objects.filter(id=iid)
    video=Video.objects.filter(id=iiid)
    return render_to_response('video_list/video.html',{'video':video[0],'tts':tts[0],'user':request.user})

def newsecho(request):
    id=int(request.GET.get('nd'))
    news=News.objects.filter(id=id)
    return render_to_response('news/news_detail.html',{'news':news[0],'user':request.user})

def newschecho(request):
    if request.is_ajax():
        act=int(request.GET.get('action'))
        news_oneraw=News.objects.filter(important=1)
        if (act==0):
            news_mraw=News.objects.filter().exclude(id=news_oneraw[0].id)
        elif (act==3):
            news_mraw=News.objects.filter(important=1)[1:15]
        else:
            news_mraw=News.objects.filter(sportsleixin_id=act).exclude(id=news_oneraw[0].id)
        return render_to_response('news/newsch.html',{'p_mraw1':news_mraw[0:5],'p_mraw2':news_mraw[5:10],'p_mraw3':news_mraw[10:15],})


def newslistecho(request):
    if request.is_ajax():
        searchtype=int(request.GET.get('x'))
        if(searchtype):
            newslist=News.objects.filter(sportsleixin_id=searchtype)
        else:
            newslist=News.objects.all()
        return render_to_response('news/news1234ch.html',{'newslist':newslist[0:200]},context_instance = RequestContext(request))
    else:
        search=request.GET.get('search')
        if (search):
            newslist=News.objects.filter(Q(tag1__icontains=search) |Q(tag2__icontains=search)| Q(title__icontains=search))
        else:
            newslist=News.objects.all()
        return render_to_response('news/news.html',{'newslist':newslist},context_instance = RequestContext(request))

def liveecho(request):
    day=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    if (request.GET.get('dateid')):
        dateid=int(request.GET.get('dateid'))
        mday=datetime.timedelta(days=dateid)
        llist=Gameshow.objects.filter(game_time__gte=(day+mday),game_time__lt=(day+oneday+mday))
        return render_to_response('live/live_list.html',{'day':day+mday,'llist':llist,'day1':day+oneday,'day2':day+2*oneday,'day3':day+3*oneday,'day4':day+4*oneday,'day5':day+5*oneday,'day6':day+6*oneday,'day7':day+7*oneday,'day8':day+8*oneday,'user':request.user})
    else:
        llist=Gameshow.objects.filter(game_time__gte=day,game_time__lt=(day+oneday))
        return render_to_response('live/live_list.html',{'day':day,'llist':llist,'day1':day+oneday,'day2':day+2*oneday,'day3':day+3*oneday,'day4':day+4*oneday,'day5':day+5*oneday,'day6':day+6*oneday,'day7':day+7*oneday,'day8':day+8*oneday,'user':request.user})

def showchecho(request):
    if request.is_ajax():
        now=datetime.datetime.now()
        dt2=datetime.timedelta(hours=3)
        ch=int(request.GET.get('showch'))
        if ch!=0:
            tvshow=Gameshow.objects.filter(sports_leixin_id=ch,game_time__gte=(now-dt2))
        else:
            tvshow=Gameshow.objects.filter(game_time__gte=(now-dt2))
        return render_to_response('live/showch.html',{'tvshow':tvshow[0:9],})

def dataecho(request):
    if request.is_ajax():
        dax=request.GET.get('datateam')
        search=request.GET.get('search')
        if(dax):
            cht=Team.objects.filter(english_name=dax)[0]
            chcoach=Man.objects.filter(club_id=cht.id,career_id=2)
            chkeep=Man.objects.filter(club_id=cht.id,position_id=1)
            chdef=Man.objects.filter(club_id=cht.id,position_id=2)
            chmid=Man.objects.filter(club_id=cht.id,position_id=3)
            chforw=Man.objects.filter(club_id=cht.id,position_id=4)
            chhire=Man.objects.filter(club_id=cht.id,position_id=5)
            return render_to_response('data/datachange.html',{'cht':cht,'chcoach':chcoach[0],'chkeep':chkeep,'chdef':chdef,'chmid':chmid,'chforw':chforw,'chhire':chhire})
        if(search):
            sea=unquote(request.GET.get('search'))
            if (Team.objects.filter(chinese_name__icontains=sea)):
                cht=Team.objects.filter(chinese_name__icontains=sea)[0]
                chcoach=Man.objects.filter(club_id=cht.id,career_id=2)
                chkeep=Man.objects.filter(club_id=cht.id,position_id=1)
                chdef=Man.objects.filter(club_id=cht.id,position_id=2)
                chmid=Man.objects.filter(club_id=cht.id,position_id=3)
                chforw=Man.objects.filter(club_id=cht.id,position_id=4)
                chhire=Man.objects.filter(club_id=cht.id,position_id=5)
                return render_to_response('data/searchdata.html',{'cht':cht,'chcoach':chcoach[0],'chkeep':chkeep,'chdef':chdef,'chmid':chmid,'chforw':chforw,'chhire':chhire})
            else:
                cht1=Man.objects.filter(Q(chinese_name__icontains=sea))[0]
                return render_to_response('data/searchdataman.html',{'cht':cht1,})
    else:
        return render_to_response('data/data.html',{'user':request.user})


def aboutecho(request):
    if(request.GET.get('a')):
        return render_to_response('about/aboutadv.html',{})
    else:
        return render_to_response('about/aboutus.html',{})

def bbs(request):
    if request.is_ajax():
        x=request.GET.get('x')
        if(x=='talk'):
            talkbbs=Talk.objects.filter()
            return render_to_response('bbs/tlist.html',{"Sharebbs":talkbbs[0:200]},context_instance = RequestContext(request))
        elif(x=='share'):
            Sharebbs1=Sharing.objects.all()
            return render_to_response('bbs/slist.html',{"Sharebbs":Sharebbs1[0:200]},context_instance = RequestContext(request))
        else:
            talkbbs1=Talk.objects.filter(tname=x)
            return render_to_response('bbs/tlist.html',{"Sharebbs":talkbbs1[0:200]},context_instance = RequestContext(request))

    else:
        sn=request.GET.get('sname')
        if(sn):
            Sharebbs=Sharing.objects.filter(sname=sn)
        else:
            Sharebbs=Sharing.objects.all()
        return render_to_response('bbs/main_bbs.html',{"Sharebbs":Sharebbs[0:200]},context_instance = RequestContext(request))

def bbstalk(request):
    talk=int(request.GET.get('talk'))
    bbstalk=Talk.objects.get(id=talk)
    return render_to_response('bbs/bbs_talk.html',{'bbstalk':bbstalk})

@csrf_exempt
def sharing(request):
    if request.method=='POST':
        title = request.POST.get('bbs_sharing1', '')[0:80]
        address = request.POST.get('bbs_sharing2', '')
        s_user = request.user.username
        try:
            s1=Sharing(sname=s_user,title=title,address=address,imp=0,share_time=datetime.datetime.now(),like_count=1)
            s1.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),{'user':request.user})
        except Exception:
            return HttpResponse('<p style="font-size:40px">Sharing lose!!!</p>')

@csrf_exempt
def ttalk(request):
    if request.method=='POST':
        title = request.POST.get('bbs_ttalk1', '')[0:80]
        bbstext = request.POST.get('bbs_ttalk2', '')
        s_user = request.user.username
        try:
            s1=Talk(tname=s_user,title=title,bbstext=bbstext,ttop=0,ttime=datetime.datetime.now())
            s1.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),{'user':request.user})
        except Exception:
            return HttpResponse('<p style="font-size:40px">discussing lose!!!</p>')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('ss_username', '')
        passwordi = request.POST.get('passwordi', '')
        passwordk = request.POST.get('passwordk', '')
        email=request.POST.get('email', '')
        if passwordi==passwordk:
            try:
                user=User.objects.create_user(username=username,email=email,password=passwordi)
                user.is_active=True
                user.save()
                return HttpResponse('<p style="font-size:20px;text-align:center">Congratulations! Register is Success</p>')
            except Exception:
                return HttpResponse('<p style="font-size:20px">Username already exists! </p>')
        else:
            return HttpResponse('<p style="font-size:20px;text-align:center">Enter password twice inconsistent!</p>')
    else:
        return HttpResponse('<p style="font-size:20px;text-align:center">invalid register</p>')

@csrf_exempt
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        user_login(request, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),{'user':request.user})
    else:
        return HttpResponse('<p style="font-size:20px;text-align:center">Logining account or password is wrong</p>')


def loginout(request):
    user_logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@csrf_exempt
def changeps(request):
    password = request.POST.get('passwordnew', '')
    password1 = request.POST.get('passwordnew1', '')
    if password==password1:
        user = User.objects.get(username=request.user)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponse('<p>Enter the new password twice inconsistent!</p>')