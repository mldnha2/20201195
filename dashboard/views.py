from django.shortcuts import render,redirect
from dashboard.forms import FormBarang, FormPinjam, FormKembali 
from dashboard.models import Barang,Member,Jenis,Kembali,Pinjam
from django.contrib import messages

# Create your views here.
def produk(request):
    titlenya="Produk"
    konteks={ 'title':titlenya, }
    return render(request,'produk.html',konteks)

def addbrg(request):
 if request.POST:
    form= FormBarang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        form = FormBarang()
        konteks = {
            'form' : form,
        }
    return render(request,'addbrg.html',konteks)
 else  :
    form = FormBarang()
    konteks = {
        'form':form,
    }
 return render(request,'addbrg.html',konteks)

def addpinjam(request):
 if request.POST:
    form= FormPinjam(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        form = FormPinjam()
        konteks = {
            'form' : form,
        }
    return render(request,'addpinjam.html',konteks)
 else  :
    form = FormPinjam()
    konteks = {
        'form':form,
    }
 return render(request,'addpinjam.html',konteks)

def addkembali(request):
 if request.POST:
    form= FormKembali(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        form = FormKembali()
        konteks = {
            'form' : form,
        }
    return render(request,'addkembali.html',konteks)
 else  :
    form = FormKembali()
    konteks = {
        'form':form,
    }
 return render(request,'addkembali.html',konteks) 

def Barang_View(request):
    barangs=Barang.objects.all()
    
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def member(request):
    members=Member.objects.all()
    
    konteks={
        'members':members,
    }
    return render(request,'member.html',konteks) 

def jenis(request):
    jeniss=Jenis.objects.all()
    
    konteks={
        'jeniss':jeniss,
    }
    return render(request,'jenis.html',konteks) 

def ubah_brg(request,id_barang):
 barangs=Barang.objects.get(id=id_barang)
 if request.POST:
    form= FormBarang(request.POST,instance=barangs)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        return redirect('ubah_brg',id_barang=id_barang)
 else  :
    form = FormBarang(instance=barangs)
    konteks = {
        'form':form,
        'barangs':barangs
    }
 return render(request,'ubah_brg.html',konteks)

def ubah_pinjam(request,id_pinjam):
 pinjams=Pinjam.objects.get(id=id_pinjam)
 if request.POST:
    form= FormPinjam(request.POST,instance=pinjams)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        return redirect('ubah_pinjam',id_pinjam=id_pinjam)
 else  :
    form = FormPinjam(instance=pinjams)
    konteks = {
        'form':form,
        'pinjams':pinjams
    }
 return render(request,'ubah_pinjam.html',konteks)

def ubah_kembali(request,id_kembali):
 kembalis=Kembali.objects.get(id=id_kembali)
 if request.POST:
    form= FormKembali(request.POST,instance=kembalis)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        return redirect('ubah_kembali',id_kembali=id_kembali)
 else  :
    form = FormKembali(instance=kembalis)
    konteks = {
        'form':form,
        'kembalis':kembalis
    }
 return render(request,'ubah_kembali.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data terhapus")
    return redirect('Vbrg') 

def hapus_pinjam(request,id_pinjam):
    pinjams=Pinjam.objects.filter(id=id_pinjam)
    pinjams.delete()
    messages.success(request,"Data terhapus")
    return redirect('pinjam') 

def hapus_kembali(request,id_kembali):
    kembalis=Kembali.objects.filter(id=id_kembali)
    kembalis.delete()
    messages.success(request,"Data terhapus")
    return redirect('kembali') 

def buku_kembali(request):
    kembalis=Kembali.objects.all()
    
    konteks={
        'kembalis':kembalis,
    }
    return render(request,'kembali.html',konteks)

def buku_pinjam(request):
    pinjams=Pinjam.objects.all()
    
    konteks={
        'pinjams':pinjams,
    }
    return render(request,'pinjam.html',konteks)
