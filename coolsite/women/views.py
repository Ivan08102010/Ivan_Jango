from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
from django.urls import reverse
def index(request):
    return render(request, 'women/index.html')

def d(request):
    return HttpResponse('1234567890')

def a(request):
    return HttpResponse('AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa')

def b(request):
    return HttpResponse('BbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBbBb')

def c(request):
    return HttpResponse('CcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCcCc')



def gim1(request):
    return HttpResponse('<img src= "https://bryansktoday.ru/uploads/common/091b388af452bef4_XL.jpg"</img ><h1> Gimnazia1</h1><img src= "https://www.gimn-1.ru/about/nasha-gordost/13.jpg"</img ><h1>')

def categories(request, cat_id):
    if cat_id == 1:
        return HttpResponse('<img src= "https://cf.ppt-online.org/files/slide/q/qo6WGyPDH8Z0aOzlRhtCwi3LVIdpeTx9jQksKv/slide-9.jpg"</img ><h1></h1> Аэробы - бактерии нуждающиеся в воздухе')

    elif cat_id == 2:
        return HttpResponse('<img src= "https://cf.ppt-online.org/files/slide/5/5GSMvQRln2BqO69m3Ko7PLHjp1ZaxeiEzNtu8V/slide-55.jpg"</img ><h1></h1> Анаэробы - бактерии не нуждающиеся в воздухе или погибающие от него')

    elif cat_id == 3:
        return HttpResponse('<img src= "https://druzhniy-center.ru/wp-content/uploads/7/c/5/7c5b5c720664e2970545805ff34e4e3e.jpeg"</img ><h1></h1> Гетротрофы - существа питающиеся готовыми питательными веществами ')

    elif cat_id == 4:
        return HttpResponse('<img src= "http://cdn01.ru/files/users/images/68/ce/68ce378c39850dce64c1ac6130ef75c3.jpg"</img ><h1></h1>Автотрофы - существа сами создающаи питательные вещества')

    elif cat_id == 5:
        return HttpResponse('<img src= "https://kevin-seoshnik.ru/wp-content/uploads/2021/09/carstva-zhivoj-prirody.jpg"</img ><h1></h1>Царства: Вирусы, Бактерии, Грибы, Растения, Животные.')

    elif cat_id == 6:
        return HttpResponse('<img src= "https://druzhniy-center.ru/wp-content/uploads/d/3/f/d3f14b7c732246264c33935d7e1158d6.jpeg"</img ><h1></h1> Сапротрофы или сапрофиты подвид гетротрофоф организмы, питающиеся отмершими останками других существ')

    elif cat_id == 7:
        return HttpResponse('<img src= "http://cf2.ppt-online.org/files2/slide/k/K4DweSYqzCjMgFQOP5hRIH7BmkLcWZ8tJG06dA1uEl/slide-28.jpg"</img ><h1></h1> Паразиты питаются защёт живого организма бывают паразитами грибы, животные, бактерии.')

    elif cat_id == 8:
        return HttpResponse('<img src= "http://images.myshared.ru/10/980867/slide_7.jpg"</img ><h1></h1>')

    elif cat_id == 9:
        return HttpResponse('<img src= "https://rodinkam.net/wp-content/uploads/2021/05/img_16200883403630-1-1024x576.jpg"</img ><h1></h1>Хемотрофы питаются организмы, получающие энергию в результате окислительно-восстановительных реакций, в которых они окисляют химические соединения, богатые энергией')

    elif cat_id == 10:
        return HttpResponse('''<img src= "https://cf.ppt-online.org/files/slide/j/jkYHRZ9gvrauh5UNB03omqiT8nwCGKfPFzDeVE/slide-7.jpg"</img ><h1></h1> В настоящее время в состав биологии включают ботанику (растения), зоологию (животные), микробиологию (микр оорганизмы),
         микологию (грибы), систематику, биохимию (химический состав живой материи и химические процессы в ней), цитологию (клетка), гистологию (ткани), анатомию (внутреннее строение),
         физиологию (процессы жизнедеятельности), эмбриологию (индивидуальное развитие), этологию (поведение).''')
    else:
        uri = reverse('home')
        return redirect(uri)