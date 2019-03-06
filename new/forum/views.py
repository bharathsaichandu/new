from urllib.parse import quote_plus
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django import http
from . forms import questionForm,ImageForm,UserRegisterForm,sharedroomform,\
    shareImageForm,privateImageForm,privateroomform,entirehouseform,entirehouseImageForm,SearchForm#,ModuleForm
from .models import question,Images,share_room_Images,private_room_Images,entire_house_Images,shared_room,private_room,entire_house
from django.http import Http404,HttpResponseRedirect
from django.contrib import messages
from django.forms import modelformset_factory
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def searchview(request):
    if request.method == 'GET':

        form = SearchForm(request.GET)
        if form.is_valid():
            state = form.cleaned_data['state']
            area = form.cleaned_data['area']
            #module_name = form.cleaned_data['module_name']
            #results = Module.objects.all()
            '''if release_num:
                results = results.filter(metamodule__release__number=release_num)
            if metamodule_name:
                result = results.filter(metamodule__name=metamodule_name)
            if module_name:
                result = results.filter(name=module_name)'''
            #return render(request, 'search/search_result.html', {'form': form, 'results': results})
            return render(request,'search.html',{'form':form})
    else:
        form = SearchForm()
        return render(request, 'search_form.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def ask_question(request):

     ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=6 )
     print("hrllo")
     if request.method == 'POST':
        print("jnkjnkjnjkj k")
        question_Form = questionForm(request.POST or None,request.FILES or None)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if question_Form.is_valid():
            print("coming")
            question_Form = question_Form.save(commit=False)
            question_Form.user = request.user
            question_Form.save()

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return http.HttpResponseRedirect('/')
        else:
            print("in else")
            print
            question_Form.errors#, formset.errors
     else:
        question_Form = questionForm()
        formset = ImageFormSet(queryset=Images.objects.none())
     context={'postForm': question_Form}
     return render(request, 'ask_question.html',context)


def question_detail_view(request,my_id):
    obj=question.objects.get(id=my_id)
    imag=Images.objects.all()
    try :
        obj =question.objects.get(id=my_id)
        #imag = Images.objects.all()
        imag=question.image1
    except question.DoesNotExist:
        raise Http404
    share_string = quote_plus(obj.description)
    a=[]
    '''for i in imag:
        if i.questionn == obj:
            if i.image:
                a.append(i.image)'''
    a=[]
    a.append(obj.image1.url)
    length=len(a)
    one=1
    print(obj.image1.url)
    context={'object':obj,"share_string":share_string,'imag':imag,'a':a,'range':range(length),'one':one}
    return render(request,'question_detail.html',context)

def house_detail_view(request,my_id):
    obj=shared_room.objects.get(id=my_id)
    imag=share_room_Images.objects.all()
    try :
        obj =shared_room.objects.get(id=my_id)
        imag = share_room_Images.objects.all()
    except question.DoesNotExist:
        raise Http404
    share_string = quote_plus(obj.Area)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    value = 0
    if username == obj.user_name:
        value = 1
    a=[]
    '''for i in imag:
        if i.sharedroom == obj:
            if i.image:
                a.append(i.image)'''
    print(obj.image1)
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)
    if len(a)==0:
        a.append('../../static/noimage.png')

    some_var = str(obj.essentialamenities)
    some_var=some_var.split(',')
    print(some_var)
    print(type(some_var))
    optional = str(obj.optionalamenities)
    optional = optional.split(',')
    length=len(a)
    one=1
    lengthofessential=len(some_var)
    lengthofoptional=len(optional)
    context={'optional':optional,'value':value,'lenofoptional':lengthofoptional,'object':obj,"share_string":share_string,'imag':imag,'a':a,'range':range(length),'one':one,'essential':some_var,'lenofessential':lengthofessential}
    return render(request,'house_detail.html',context)


def privateroom_detail_view(request,my_id):
    obj=private_room.objects.get(id=my_id)
    imag=share_room_Images.objects.all()
    try :
        obj =private_room.objects.get(id=my_id)
        imag = share_room_Images.objects.all()
    except question.DoesNotExist:
        raise Http404
   # share_string = quote_plus(obj.Area)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    value = 0
    if username == obj.user_name:
        value = 1
    a=[]
    '''for i in imag:
        if i.sharedroom == obj:
            if i.image:
                a.append(i.image)'''
    print(obj.image1)
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)
    if len(a)==0:
        a.append('../../static/noimage.png')

    some_var = str(obj.essentialamenities)
    some_var=some_var.split(',')
    print(some_var)
    print(type(some_var))
    optional = str(obj.optionalamenities)
    optional = optional.split(',')
    length=len(a)
    one=1
    lengthofessential=len(some_var)
    lengthofoptional=len(optional)
    context={'optional':optional,'value':value,'lenofoptional':lengthofoptional,'object':obj,'imag':imag,'a':a,'range':range(length),'one':one,'essential':some_var,'lenofessential':lengthofessential}
    return render(request,'privateroomdetail.html',context)

def entirehouse_detail_view(request,my_id):
    obj=entire_house.objects.get(id=my_id)
    imag=share_room_Images.objects.all()
    try :
        obj =entire_house.objects.get(id=my_id)
        imag = share_room_Images.objects.all()
    except question.DoesNotExist:
        raise Http404
   # share_string = quote_plus(obj.Area)
    print(obj.user_name)
    print(request.user.is_authenticated)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    value=0
    if username==obj.user_name:
        value=1
    a=[]
    '''for i in imag:
        if i.sharedroom == obj:
            if i.image:
                a.append(i.image)'''
    print(obj.image1)
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)
    if len(a)==0:
        a.append('../../static/noimage.png')

    some_var = str(obj.essentialamenities)
    some_var=some_var.split(',')
    print(some_var)
    print(type(some_var))
    optional = str(obj.optionalamenities)
    optional = optional.split(',')
    length=len(a)
    one=1
    lengthofessential=len(some_var)
    lengthofoptional=len(optional)
    context={'optional':optional,'value':value,'lenofoptional':lengthofoptional,'object':obj,'imag':imag,'a':a,'range':range(length),'one':one,'essential':some_var,'lenofessential':lengthofessential}
    return render(request,'entirehousedetail.html',context)


@login_required
def question_edit_view(request,my_id=None):
    obj = question.objects.get(id=my_id)
    imag = Images.objects.all()
    a = []
    a.append(obj.image1.url)
    form = questionForm(request.POST or None,request.FILES or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "updated")
        return HttpResponseRedirect(obj.get_absolute_url())
    try:
        obj = question.objects.get(id=my_id)
    except question.DoesNotExist:
        raise Http404

    edit = 'edit'
    context = {'object': obj, "form": form, "send": edit}
    return render(request, 'questionupdate.html', context)
    pass

def question_delete_view(request,my_id):
    obj=get_object_or_404(question,id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context={'object':obj}
    return render(request,'delete.html',context)

def question_list_view(request):
    queryset_list=question.objects.all()

    query=request.GET.get("city")
    query1=request.GET.get("area")
    if query!=None:
        query=" ".join(query.split())
    if query1!=None:
        query1=" ".join(query1.split())
    if query:
        print('here')
        queryset_list=queryset_list.filter(title__icontains=query)|queryset_list.filter(title__icontains=query1)
    if query1:
        print(queryset_list)
    paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context={
        'object_list':queryset,
        "page_request_var":page_request_var,
    }
    return render(request,'question_list.html',context)

def sharedroom_list_view(request):
    print("dklmlkm")
    queryset_list=shared_room.objects.all()
    imag = share_room_Images.objects.all()
    try:
        #obj = question.objects.get(id=my_id)
        imag = Images.objects.all()
    except question.DoesNotExist:
        raise Http404
    query=request.GET.get("city")
    query1=request.GET.get("area")
    query2 = request.GET.get("gender")
    query3=request.GET.get("rent")
    query=str(query)
    query1=str(query1)
    query2=str(query2)
    query3 = str(query3)
    print(query2)
    query = " ".join(query.split())
    query1 = " ".join(query1.split())
    #print(queryset_list.filter( Area__icontains=query1))
    print(query)
   # print(queryset_list.filter(City__icontains=query))
    query_param=""
    query_param = "city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
    print(len(query))
    print(len(query1))
    if query1==None:
        print("mkmkfm")
    if query!="None" or query1!="None":
        query_param="city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
        print('here')
        print(query)
        print(query1)
        queryset_list=queryset_list.filter( Area__icontains=query1)&queryset_list.filter(City__icontains=query)
        if query2=='boys':
            print('enter')
            queryset_list=queryset_list.filter(gender="boys")
        elif query2=='girls':
            queryset_list=queryset_list.filter(gender='girls')
        elif query2=='family':
            queryset_list=queryset_list.filter(gender='family')
        if query3=='small':
            queryset_list = queryset_list.filter(rent__gte= 1)&queryset_list.filter(rent__lte=5000)
        elif query3=='medium':
            queryset_list = queryset_list.filter(rent__gte= 5000)&queryset_list.filter(rent__lte=10000)
        elif query3=='more':
            queryset_list = queryset_list.filter(rent__gte= 10000)&queryset_list.filter(rent__lte=20000)
        elif query3=='lot':
            queryset_list=queryset_list.filter(rent__gte=20000)

    if query1:
        print(queryset_list)

    final_list=[]

    print(queryset_list)
   # print(queryset_list[3].id)
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context={
        'object_list':queryset,
        "page_request_var":page_request_var,
        "query":query_param
    }
    return render(request,'house_list.html',context)

def privateroom_list_view(request):
    print("dklmlkm")
    queryset_list=private_room.objects.all()
    imag = share_room_Images.objects.all()
    try:
        #obj = question.objects.get(id=my_id)
        imag = Images.objects.all()
    except question.DoesNotExist:
        raise Http404
    query=request.GET.get("city")
    query1=request.GET.get("area")
    query2 = request.GET.get("gender")
    query3=request.GET.get("rent")
    query=str(query)
    query1=str(query1)
    query2=str(query2)
    query3 = str(query3)
    print(query2)
    query = " ".join(query.split())
    query1 = " ".join(query1.split())
    #print(queryset_list.filter( Area__icontains=query1))
    print(query)
   # print(queryset_list.filter(City__icontains=query))
    query_param=""
    query_param = "city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
    print(len(query))
    print(len(query1))
    if query1==None:
        print("mkmkfm")
    if query!="None" or query1!="None":
        query_param="city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
        print('here')
        print(query)
        print(query1)
        queryset_list=queryset_list.filter( Area__icontains=query1)&queryset_list.filter(City__icontains=query)
        if query2=='boys':
            print('enter')
            queryset_list=queryset_list.filter(gender="boys")
        elif query2=='girls':
            queryset_list=queryset_list.filter(gender='girls')
        elif query2=='family':
            queryset_list=queryset_list.filter(gender='family')
        if query3=='small':
            queryset_list = queryset_list.filter(rent__gte= 1)&queryset_list.filter(rent__lte=5000)
        elif query3=='medium':
            queryset_list = queryset_list.filter(rent__gte= 5000)&queryset_list.filter(rent__lte=10000)
        elif query3=='more':
            queryset_list = queryset_list.filter(rent__gte= 10000)&queryset_list.filter(rent__lte=20000)
        elif query3=='lot':
            queryset_list=queryset_list.filter(rent__gte=20000)

    if query1:
        print(queryset_list)

    final_list=[]

    print(queryset_list)
   # print(queryset_list[3].id)
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context={
        'object_list':queryset,
        "page_request_var":page_request_var,
        "query":query_param
    }
    return render(request,'privateroomlist.html',context)


def entirehouse_list_view(request):
    print("dklmlkm")
    queryset_list=entire_house.objects.all()
    imag = share_room_Images.objects.all()
    try:
        #obj = question.objects.get(id=my_id)
        imag = Images.objects.all()
    except question.DoesNotExist:
        raise Http404
    query=request.GET.get("city")
    query1=request.GET.get("area")
    query2 = request.GET.get("gender")
    query3=request.GET.get("rent")
    query=str(query)
    query1=str(query1)
    query2=str(query2)
    query3 = str(query3)
    print(query2)
    query = " ".join(query.split())
    query1 = " ".join(query1.split())
    #print(queryset_list.filter( Area__icontains=query1))
    print(query)
   # print(queryset_list.filter(City__icontains=query))
    query_param=""
    query_param = "city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
    print(len(query))
    print(len(query1))
    if query1==None:
        print("mkmkfm")
    if query!="None" or query1!="None":
        query_param="city=" + query + "&area=" + query1+"&gender=" + query2+"&rent=" + query3
        print('here')
        print(query)
        print(query1)
        queryset_list=queryset_list.filter( Area__icontains=query1)&queryset_list.filter(City__icontains=query)
        if query2=='boys':
            print('enter')
            queryset_list=queryset_list.filter(gender="boys")
        elif query2=='girls':
            queryset_list=queryset_list.filter(gender='girls')
        elif query2=='family':
            queryset_list=queryset_list.filter(gender='family')
        if query3=='small':
            queryset_list = queryset_list.filter(rent__gte= 1)&queryset_list.filter(rent__lte=5000)
        elif query3=='medium':
            queryset_list = queryset_list.filter(rent__gte= 5000)&queryset_list.filter(rent__lte=10000)
        elif query3=='more':
            queryset_list = queryset_list.filter(rent__gte= 10000)&queryset_list.filter(rent__lte=20000)
        elif query3=='lot':
            queryset_list=queryset_list.filter(rent__gte=20000)

    if query1:
        print(queryset_list)

    final_list=[]

    print(queryset_list)
   # print(queryset_list[3].id)
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)
    context={
        'object_list':queryset,
        "page_request_var":page_request_var,
        "query":query_param
    }
    return render(request,'entirehouselist.html',context)



@login_required
def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    try:
        querylist=entire_house.objects.all()
        querylist=querylist.filter(user_name=username)
    except:
        querylist=[]
    try:
        querylist1=private_room.objects.all()
        querylist1=querylist1.filter(user_name=username)
    except:
        querylist1=[]
    try:
        querylist2=shared_room.objects.all()
        querylist2=querylist2.filter(user_name=username)
    except:
        querylist2=[]
    print(querylist1)
    print(querylist2)
    print(querylist)
    context={'query1':querylist,'query2':querylist1,'query3':querylist2}
    return render(request, 'profile.html',context)




@login_required
def sharedroompost(request):
    ImageFormSet = modelformset_factory(share_room_Images,
                                        form=shareImageForm, extra=6 )

    if request.method == 'POST':

        question_Form = sharedroomform(request.POST or None,request.FILES or None)
        #formset = ImageFormSet(request.POST, request.FILES,
         #                      queryset=share_room_Images.objects.none())

        if question_Form.is_valid() :#and formset.is_valid():
            question_Form = question_Form.save(commit=False)
            question_Form.user_name = request.user
            question_Form.save()


            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print (question_Form.errors)#, formset.errors)
    else:
        question_Form = sharedroomform()
    context={'postForm': question_Form}#, 'formset': formset}

    return render(request, 'post_share_room.html',context)
@login_required
def sharedroompostedit(request,my_id=None):
    obj = shared_room.objects.get(id=my_id)

    a = []
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)

    formset = modelformset_factory(Images,
                                   form=ImageForm, extra=6)  # queryset=Images.objects.all().filter(id=my_id))

    form = sharedroomform(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "updated")
        return HttpResponseRedirect(obj.get_absolute_url())
    try:
        obj = shared_room.objects.get(id=my_id)
    except question.DoesNotExist:
        raise Http404

    edit = 'edit'
    context = {'object': obj, "postForm": form, "send": edit}
    return render(request, 'post_share_room.html', context)

@login_required
def privateroompostedit(request,my_id=None):
    obj = private_room.objects.get(id=my_id)

    a = []
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)

    formset = modelformset_factory(Images,
                                   form=ImageForm, extra=6)  # queryset=Images.objects.all().filter(id=my_id))

    form = privateroomform(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "updated")
        return HttpResponseRedirect(obj.get_absolute_url())
    try:
        obj = private_room.objects.get(id=my_id)
    except question.DoesNotExist:
        raise Http404

    edit = 'edit'
    context = {'object': obj, "postForm": form, "send": edit}
    return render(request, 'post_private_room.html', context)

@login_required
def privateroompost(request):
    ImageFormSet = modelformset_factory(share_room_Images,
                                        form=shareImageForm, extra=6)

    if request.method == 'POST':

        question_Form = privateroomform(request.POST or None, request.FILES or None)
        # formset = ImageFormSet(request.POST, request.FILES,
        #                      queryset=share_room_Images.objects.none())

        if question_Form.is_valid():  # and formset.is_valid():
            question_Form = question_Form.save(commit=False)
            question_Form.user_name = request.user
            question_Form.save()

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(question_Form.errors)  # , formset.errors)
    else:
        question_Form = privateroomform()
    context = {'postForm': question_Form}  # , 'formset': formset}

    return render(request, 'post_private_room.html', context)
    return render(request, 'post_private_room.html',context)

@login_required
def entirehousepost(request):
    ImageFormSet = modelformset_factory(share_room_Images,
                                        form=shareImageForm, extra=6)

    if request.method == 'POST':

        question_Form = entirehouseform(request.POST or None, request.FILES or None)
        # formset = ImageFormSet(request.POST, request.FILES,
        #                      queryset=share_room_Images.objects.none())

        if question_Form.is_valid():  # and formset.is_valid():
            question_Form = question_Form.save(commit=False)
            question_Form.user_name = request.user
            question_Form.save()

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(question_Form.errors)  # , formset.errors)
    else:
        question_Form = entirehouseform()
    context = {'postForm': question_Form}  # , 'formset': formset}

    #return render(request, 'post_entire_room.html', context)

    return render(request, 'post_entire_house.html',context)

@login_required
def entirehousepostedit(request,my_id=None):
    obj = entire_house.objects.get(id=my_id)

    a = []
    if obj.image1:
        a.append(obj.image1.url)
    if obj.image2:
        a.append(obj.image2.url)
    if obj.image3:
        a.append(obj.image3.url)
    if obj.image4:
        a.append(obj.image4.url)
    if obj.image5:
        a.append(obj.image5.url)
    if obj.image6:
        a.append(obj.image6.url)

    formset = modelformset_factory(Images,
                                   form=ImageForm, extra=6)  # queryset=Images.objects.all().filter(id=my_id))

    form = entirehouseform(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "updated")
        return HttpResponseRedirect(obj.get_absolute_url())
    try:
        obj = entire_house.objects.get(id=my_id)
    except question.DoesNotExist:
        raise Http404

    edit = 'edit'
    context = {'object': obj, "postForm": form, "send": edit}
    return render(request, 'post_entire_house.html', context)
