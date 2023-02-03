from django.db import models

# Create your models here.

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return "{}. {}" .format(self.nama,self.ket)

class Barang(models.Model):
    kodebuku=models.CharField(max_length=8, default="Jdl")
    judul=models.CharField(max_length=50)
    stok=models.IntegerField()

    def __str__(self):
        return "{}. {}. {}" .format(self.kodebuku,self.judul,self.stok)


class Pinjam(models.Model):
    id_buku=models.CharField(max_length=10)
    nama=models.CharField(max_length=50)
    tgl_pinjam=models.CharField(max_length=10)
    tgl_kembali=models.CharField(max_length=10)
    judul_id=models.ForeignKey(Barang, on_delete=models.CASCADE,null=True)

    def __str__(self):
       return "{}. {}. {}. {}" .format(self.id_buku,self.nama,self.tgl_pinjam,self.tgl_kembali)

class Kembali(models.Model):
    id_buku=models.CharField(max_length=10)
    nama=models.CharField(max_length=8)
    tgl_pinjam=models.DateTimeField(auto_now_add=True)
    tgl_kembali=models.DateTimeField(auto_now_add=True)
    kondisi=models.CharField(max_length=15)
    
    def __str__(self):
        return "{}. {}. {}" .format(self.id_buku,self.nama,self.kondisi)

class Member(models.Model):
    idmember=models.CharField(max_length=10)
    nama=models.CharField(max_length=25)
    alamat=models.CharField(max_length=30)

    def __str__(self):
        return "{}. {}. {}" .format(self.idmember,self.nama,self.alamat)