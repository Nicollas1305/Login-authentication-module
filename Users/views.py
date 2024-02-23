from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from Users.models import CustomUser
import json

User = get_user_model()
@csrf_exempt
def criar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        foto_perfil = request.FILES.get('foto_perfil')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        if nome and email and senha:
            try:
                user = CustomUser.objects.create_user(nome=nome, email=email, senha=senha, foto_perfil=foto_perfil,
                                                data_nascimento=data_nascimento, telefone=telefone, endereco=endereco)
                return JsonResponse({'message': 'Usuário criado com sucesso!'}, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'Nome, email e senha são campos obrigatórios'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        senha = data.get('senha')
        user = authenticate(request, email=email, password=senha)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Credenciais inválidas'}, status=401)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def perfil_usuario(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_data = {
                'id': request.user.id,
                'nome': request.user.nome,
                'email': request.user.email,
                'foto_perfil': request.user.foto_perfil.url if request.user.foto_perfil else None,
                'data_nascimento': request.user.data_nascimento,
                'telefone': request.user.telefone,
                'endereco': request.user.endereco,
            }
            return JsonResponse(user_data)
        else:
            return JsonResponse({'error': 'Usuário não autenticado'}, status=401)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
