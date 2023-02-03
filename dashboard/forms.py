from django.forms import ModelForm
from dashboard.models import Barang,Pinjam,Kembali

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

class FormPinjam(ModelForm):
    class Meta :
        model=Pinjam
        fields='__all__'

class FormKembali(ModelForm):
    class Meta :
        model=Kembali
        fields='__all__'