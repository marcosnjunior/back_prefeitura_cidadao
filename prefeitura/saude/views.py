from django.shortcuts import render, redirect

from .forms.vigilancia_sanitaria import DenunciaForm
from .forms.vacina import VacinacaoDomiciliarForm
from .forms.lgbt_igualdade import ConsultaGinecologistaLGBTForm, ExameCitopatologicoForm, GastroenterologistaForm, ExameEndocrinologiaForm
from .forms.remedio_em_casa import RemedioEmCasaForm, RenovacaoReceitaForm
from .forms.opera_mais import SoliciteCirurgiaForm, ExamesForm
from .forms.cartao_sus import CartaoSUSForm

# categoria de saúde
def vigilancia_sanitaria(request):
    return render(request, 'vigilancia-sanitaria.html')

def vacina(request):
    return render(request, "vacina-domiciliar.html")

def lgbt_igualdade(request):
    return render(request, 'lgbt-igualdade.html') 

def remedio_em_casa(request):
    return render(request, 'remedio-em-casa.html')

def opera_mais(request):
    return render(request, 'opera-mais.html')

def cartao_sus(request):
    return render(request, 'cartao-sus.html')


def denuncias(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/vigilancia-sanitaria')
    else:
        form = DenunciaForm()
    return render(request, 'categoria/denuncia.html', {'form': form})

def vacinacao(request):
    if request.method == 'POST':
        form = VacinacaoDomiciliarForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/vacina')
    else:
        form = VacinacaoDomiciliarForm()
    return render(request, 'categoria/vacinacao.html', {'form': form})

# LGBT
def consulta_ginecologista_lgbt(request):
    if request.method == 'POST':
        form = ConsultaGinecologistaLGBTForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/lgbt-igualdade')
    else:
        form = ConsultaGinecologistaLGBTForm()
    return render(request, 'categoria/consulta-ginecologista-lgbt.html', {'form': form})

def exame_citopatologico(request):
    if request.method == 'POST':
        form = ExameCitopatologicoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/lgbt-igualdade')
    else:
        form = ExameCitopatologicoForm()
    return render(request, 'categoria/exame-citopatologico.html', {'form': form})

def gastroenterologista(request):
    if request.method == 'POST':
        form = GastroenterologistaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/lgbt-igualdade')
    else:
        form = GastroenterologistaForm()
    return render(request, 'categoria/gastroenterologista.html', {'form': form})

def exame_endocrinologia(request):
    if request.method == 'POST':
        form = ExameEndocrinologiaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/lgbt-igualdade')
    else:
        form = ExameEndocrinologiaForm()
    return render(request, 'categoria/exame-endocrinologia.html', {'form': form})


# remedio_em_casa

def pedidos_remedios(request):
    if request.method == 'POST':
        form = RemedioEmCasaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/remedio-em-casa')
    else:
        form = RemedioEmCasaForm()
    return render(request, 'categoria/pedidos-remedios.html', {'form': form})

def renovacao_receita(request):
    if request.method == 'POST':
        form = RenovacaoReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/remedio-em-casa')
    else:
        form = RenovacaoReceitaForm()
    return render(request, 'categoria/renovacao-receita.html', {'form': form})

# opera_mais

def solicite_cirurgia(request):
    if request.method == 'POST':
        form = SoliciteCirurgiaForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/opera-mais')
    else:
        form = SoliciteCirurgiaForm()
    return render(request, 'categoria/solicite-cirurgia.html', {'form': form})

def solicete_exames(request):
    if request.method == 'POST':
        form = ExamesForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/opera-mais')
    else:
        form = ExamesForm()
    return render(request, 'categoria/solicite-exames.html', {'form': form})


def solicite_cartao_sus(request):
    if request.method == 'POST':
        form = CartaoSUSForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('/saude/cartao-sus')
    else:
        form = CartaoSUSForm()
    return render(request, 'categoria/solicite-cartao-sus.html', {'form': form})