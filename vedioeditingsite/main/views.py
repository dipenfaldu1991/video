from django.shortcuts import render,redirect
from .models import Video
from .forms import VideoForm
from moviepy.editor import *
import moviepy
import moviepy.video.fx.all as vfx
from django.core.files.storage import FileSystemStorage
from vedioeditingsite import settings
from wsgiref.util import FileWrapper
from django.http import HttpResponse
import mimetypes
import datetime
def index(request):
    if request.method=='POST':
        if request.POST.get('trim')=='trim':
            request.session['type_']=request.POST.get('trim')
        elif request.POST.get('loop')=='looping':
            request.session['type_']=request.POST.get('loop')
        elif request.POST.get('clip_mirror_x')=='clip_mirror_x':
            request.session['type_']=request.POST.get('clip_mirror_x')
        elif request.POST.get('clip_mirror_y')=='clip_mirror_y':
            request.session['type_']=request.POST.get('clip_mirror_y')
        elif request.POST.get('clip_rotate')=='clip_rotate':
            request.session['type_']=request.POST.get('clip_rotate')
        elif request.POST.get('clip_freeze')=='clip_freeze':
            request.session['type_']=request.POST.get('clip_freeze')
        elif request.POST.get('clip_invertcolour')=='clip_invertcolour':
            request.session['type_']=request.POST.get('clip_invertcolour')
        elif request.POST.get('clip_blackandwhite')=='clip_blackandwhite':
            request.session['type_']=request.POST.get('clip_blackandwhite')
        return redirect('upload')
    return render(request,'index.html')
def showvideo(request):
    if request.method == 'POST'  and request.FILES['file1']:
        myfile = request.FILES['file1']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        request.session['uploaded_file_url']=uploaded_file_url
        return redirect(str(request.session['type_']))
    return render(request, 'videos.html',{})
# Create your views here.
def trim_view(request):
    dur=0
    a=str(request.session['uploaded_file_url'])
    uploaded_file_url = request.session['uploaded_file_url']
    a = str(uploaded_file_url)
    file_n=a.split('/')
    request.session['file_name']=str(file_n[2])
    uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
    video_clip = VideoFileClip(uploaded_file_url1)
    dur=int(video_clip.duration)
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        starttime= request.POST.get('start')
        lasttime = request.POST.get('end')
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        dur=int(video_clip.duration)
        print(dur)
        video_clip=video_clip.subclip(int(starttime), int(lasttime))
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        print(video_clip)
        return redirect('download')
    return render(request, 'tpe.html', {'video':str(a),'dur':dur})


def looping_view(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        starttime= request.POST.get('start')
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        tmp_list=[]
        for temp in range(int(starttime)):
            tmp_list.append(video_clip)
        video_clip=concatenate_videoclips(tmp_list)
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'loop.html', {'video':str(a)})




def clip_mirror_x(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        starttime= request.POST.get('start')
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.mirror_x(video_clip)        
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_mirror_x.html', {'video':str(a)})

def clip_mirror_y(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        starttime= request.POST.get('start')
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.mirror_x(video_clip)        
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_mirror_y.html', {'video':str(a)})


def clip_rotate(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        starttime= int(request.POST.get('start'))
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=video_clip.rotate(starttime)       
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_mirror_y.html', {'video':str(a)})


def clip_freeze(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        time_at= int(request.POST.get('time_at'))
        time_freeze_duration = int(request.POST.get('time_freeze_duration'))
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.freeze(video_clip, time_at, time_freeze_duration)
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        print(video_clip)
        return redirect('download')
    return render(request, 'clip_freeze.html', {'video':str(a)})

def clip_invertcolour(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.invert_colors(video_clip)        
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_invertcolour.html', {'video':str(a)})

def clip_invertcolour(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.invert_colors(video_clip)        
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_invertcolour.html', {'video':str(a)})

def clip_blackandwhite(request):
    a=str(request.session['uploaded_file_url'])
    a=settings.MEDIA_URL+a[7:]
    if request.method == 'POST':
        uploaded_file_url = request.session['uploaded_file_url']
        a = str(uploaded_file_url)
        file_n=a.split('/')
        request.session['file_name']=str(file_n[2])
        uploaded_file_url1=settings.BASE_DIR+uploaded_file_url
        video_clip = VideoFileClip(uploaded_file_url1)
        video_clip=moviepy.video.fx.all.blackwhite(video_clip)        
        video_clip=video_clip.write_videofile(settings.BASE_DIR+'/media/final/'+str(file_n[2]), codec="libx264", fps=20)
        request.session['video_clip'] = video_clip
        return redirect('download')
    return render(request, 'clip_blackandwhite.html', {'video':str(a)})



def download(request):
    file_name=request.session['file_name']
    file_path = settings.MEDIA_ROOT + file_name
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    a=file_name
    return render(request, 'Download_Video.html', {'file':a,'MEDIA_URL':settings.MEDIA_URL})
