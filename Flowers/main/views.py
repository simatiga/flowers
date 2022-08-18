from sqlite3 import connect

from django.db.models.aggregates import Avg, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import plant_ctg, plant_income
from audioop import avg


# Create your views here.
def index(request):
    # msg = 'Hello, World. views.index~~~~~~.'
    # print(msg)
    # return render(request, 'main/index.html', {'message': msg})
    datas = plant_ctg.objects.all()
    datas2 = plant_income.objects.all()
    # datas2 = plant_income.objects.aggregate(sum('col3')) 
    # datas2 = User.objects.raw('select col1, 0 as col2, sum(col3) as col3, sum(col4) as col4, sum(col5) as col5, sum(col6) as col6 , avg(col7) as col7 from main_plant_income group by col1;')
    # sql = 'select col1, 0 as col2, sum(col3) as col3, sum(col4) as col4, sum(col5) as col5, sum(col6) as col6 , avg(col7) as col7 from main_plant_income group by col1;'
    datasAnno = plant_income.objects.values('col1').order_by('col1').annotate(col3=Sum('col3'),col4=Sum('col4'),col5=Sum('col5'),col6=Sum('col6'),col7=Avg('col7'))
    
    # rel_chart = plant_rel.objects.all()
    
    print(datasAnno)
    # print(plant_income.objects.all().aggregate(col3=Avg('col3')))
    # print(datasAnno)
    # return render(request, 'main/dashboard.html')
    # return render(request, 'main/dashboard.html', {'plant_ctg':datas})
    # return render(request, 'main/dashboard.html', {'plant_income':datas2})
    return render(request, 'main/dashboard.html', {'plant_ctg':datas,'plant_income':datasAnno})
    # return render(request, 'main/dashboard.html', {'plant_ctg':datas,'plant_income':datas2,'plant_rel':rel_chart})

    # test sample
    # return HttpResponse("Hello, World. You're at the main views~~~~~~.")
    # return render(request, 'main/main.html')
    # return render(request, 'app1/')
    # return redirect('app1/') # view_name ���
    # return redirect('https://finviz.com/map.ashx?t=sec')# ���� ���
    # return redirect('view-name') # view_name ���
    # return redirect('/some/url/') # ��� ���
    
# def contents(request):
#     # return render(request, 'main/contents.html')
#     return HttpResponse("Hello, World. You're at contents views.")

def test(request):
    print('in view.test......#######')
    return render(request, 'main/contents5.html', {'test_value':'testdata'})
    
    
    # return redirect('https://www.youtube.com/watch?v=XndAdqnWHyQ&list=PLWYhpUYIuW3Z65_zoei2H05rbemhjZltY&index=3&ab_channel=%EC%9E%A0%EB%B0%95%EC%82%ACN%EC%9E%90%EC%97%B0%EC%86%8C%EB%A6%ACJAMBAKSANature')

    # print("LOG:::::views.ListFunc")
    # datas = plant_ctg.objects.all()
    # print(datas[1]['col1'])

    # (������ ���� �� Ʃ�÷� �޾ƾ� ��)
    # sql = "select * from plant_ctgry"
    # cursor = connect.cursor()
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # return render(request, 'list.htlm', {'plant_ctgry':datas})

def timeline(request):
    return render(request, 'main/timeline.html')


