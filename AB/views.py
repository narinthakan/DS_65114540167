from django.shortcuts import render
from .models import A
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

# แสดงรายการทั้งหมด
def bb(req):
    n = A.objects.all()
    return render(req, "home.html", {"A1": n})

# ค้นหาตาม id
def cc(req):
    m = req.GET.get("id", "")
    n1 = A.objects.filter(id=m)
    return render(req, "home1.html", {"A2": n1})

# ค้นหาตามชื่อ
def dd(req):
    o = req.GET.get("name", "")
    n2 = A.objects.filter(name=o)
    return render(req, "home2.html", {"A3": n2})

# อัปเดตรายวิชา
class ss(UpdateView):
    model = A
    fields = ["name", "teacher"]
    template_name = "home3.html"
    success_url = reverse_lazy("bb")

# ลบรายวิชา
class yy(DeleteView):
    model = A
    template_name = "home4.html"
    success_url = reverse_lazy("bb")
