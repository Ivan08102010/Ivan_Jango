from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

menu = [{'title':'главная страница', 'url_n' : 'home'},
        {'title': 'Гимназия', 'url_n': 'gim1'},
        {'title': 'a', 'url_n': 'a'},
        {'title': 'b', 'url_n': 'b'},
        {'title': 'c', 'url_n': 'c'},
        {'title': 'It-Cube', 'url_n': 'cube'},
        {'title': 'Котики', 'url_n': 'cats'},
        ]



cats1 = ['https://celes.club/uploads/posts/2022-10/1666808106_47-celes-club-p-krutoi-kot-v-ochkakh-pinterest-49.jpg',
         'https://zaebov.net/wp-content/uploads/2021/01/995/26.jpg',
         'https://www.necoichi.co.jp/files/topics/6701_ext_06_0.jpg',
         'https://fikiwiki.com/uploads/posts/2022-02/1644991784_25-fikiwiki-com-p-prikolnie-kartinki-pro-kotov-26.jpg',
         'https://pichold.ru/wp-content/uploads/2018/12/smeshnie-koshki.jpg,',
         'https://fikiwiki.com/uploads/posts/2022-02/1644991766_9-fikiwiki-com-p-prikolnie-kartinki-pro-kotov-10.jpg',
         'https://demotivation.ru/wp-content/uploads/2020/07/s1200-10-8-1024x1024.jpg',
         'https://proprikol.ru/wp-content/uploads/2019/08/kartinki-nyashnye-kotiki-9.jpg',
         'https://i.yapx.cc/WMaPg.jpg',
         'https://ferma-biz.ru/wp-content/uploads/2022/08/koty-50.jpg',
         'https://krot.club/uploads/posts/2022-03/1646806215_8-krot-info-p-kote-prikoli-smeshnie-foto-10.jpg',
         'https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666142156_11-mykaleidoscope-ru-p-zabavnie-kotiki-vkontakte-12.jpg']


title = ['Главная страница', 'AaAaАа', 'BbBbBb', 'CcCcCc', 'gim1', 'it-cube']


def index(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/index.html',context={'menu':menu})


def a(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/a.html', data)


def b(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/b.html',data)


def c(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/c.html',data)


def gim1(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/gim1.html',data)

def categories(request, cat_id):
    if cat_id == 1:
        return HttpResponse(
            '<img src= "https://cf.ppt-online.org/files/slide/q/qo6WGyPDH8Z0aOzlRhtCwi3LVIdpeTx9jQksKv/slide-9.jpg"</img ><h1></h1> Аэробы - бактерии нуждающиеся в воздухе')

    elif cat_id == 2:
        return HttpResponse(
            '<img src= "https://cf.ppt-online.org/files/slide/5/5GSMvQRln2BqO69m3Ko7PLHjp1ZaxeiEzNtu8V/slide-55.jpg"</img ><h1></h1> Анаэробы - бактерии не нуждающиеся в воздухе или погибающие от него')

    elif cat_id == 3:
        return HttpResponse(
            '<img src= "https://druzhniy-center.ru/wp-content/uploads/7/c/5/7c5b5c720664e2970545805ff34e4e3e.jpeg"</img ><h1></h1> Гетротрофы - существа питающиеся готовыми питательными веществами ')

    elif cat_id == 4:
        return HttpResponse(
            '<img src= "http://cdn01.ru/files/users/images/68/ce/68ce378c39850dce64c1ac6130ef75c3.jpg"</img ><h1></h1>Автотрофы - существа сами создающаи питательные вещества')

    elif cat_id == 5:
        return HttpResponse(
            '<img src= "https://kevin-seoshnik.ru/wp-content/uploads/2021/09/carstva-zhivoj-prirody.jpg"</img ><h1></h1>Царства: Вирусы, Бактерии, Грибы, Растения, Животные.')

    elif cat_id == 6:
        return HttpResponse(
            '<img src= "https://druzhniy-center.ru/wp-content/uploads/d/3/f/d3f14b7c732246264c33935d7e1158d6.jpeg"</img ><h1></h1> Сапротрофы или сапрофиты подвид гетротрофоф организмы, питающиеся отмершими останками других существ')

    elif cat_id == 7:
        return HttpResponse(
            '<img src= "http://cf2.ppt-online.org/files2/slide/k/K4DweSYqzCjMgFQOP5hRIH7BmkLcWZ8tJG06dA1uEl/slide-28.jpg"</img ><h1></h1> Паразиты питаются защёт живого организма бывают паразитами грибы, животные, бактерии.')

    elif cat_id == 8:
        return HttpResponse('<img src= "http://images.myshared.ru/10/980867/slide_7.jpg"</img ><h1></h1>')

    elif cat_id == 9:
        return HttpResponse(
            '<img src= "https://rodinkam.net/wp-content/uploads/2021/05/img_16200883403630-1-1024x576.jpg"</img ><h1></h1>Хемотрофы питаются организмы, получающие энергию в результате окислительно-восстановительных реакций, в которых они окисляют химические соединения, богатые энергией')

    elif cat_id == 10:
        return HttpResponse('''<img src= "https://cf.ppt-online.org/files/slide/j/jkYHRZ9gvrauh5UNB03omqiT8nwCGKfPFzDeVE/slide-7.jpg"</img ><h1></h1> В настоящее время в состав биологии включают ботанику (растения), зоологию (животные), микробиологию (микр оорганизмы),
         микологию (грибы), систематику, биохимию (химический состав живой материи и химические процессы в ней), цитологию (клетка), гистологию (ткани), анатомию (внутреннее строение),
         физиологию (процессы жизнедеятельности), эмбриологию (индивидуальное развитие), этологию (поведение).''')
    else:
        uri = reverse('home')
        return redirect(uri)


def itcube(request):
    data = {'title': title, 'menu':menu}
    return render(request, 'women/32.html',data)


def Cats(request):
    data = {'cats1': cats1, 'menu':menu
            }
    return render(request, 'women/Cats.html',data)
