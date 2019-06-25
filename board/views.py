from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board


def index(request):
    board_list = Board.objects.all().order_by('-regdate')
    data = {'board_list': board_list}
    print(data)
    return render(request, 'board/list.html', data)


def write(request):
    print('Write View Called Method =', request.method)
    if request.method == "POST":
        board = Board()
        board.title = request.POST['title']
        board.contents = request.POST['contents']
        board.hit = 0
        board.group_no = 0
        if Board.objects.all().order_by("-group_no") is not None:
            board.group_no = Board.objects.all().order_by("-group_no")[0].group_no + 1
        else:
            board.group_no = 1
        board.order_no = 1
        board.depth = 0
        board.user_id = request.session['authuser']['id']
        board.save()
        # print(request.session['authuser']['id'])
        # print(request.session['authuser'])
        # print(request.POST['title'])
        # print(board)
        return HttpResponseRedirect('/board')
    else:
        return render(request, 'board/write.html')


def view(request, board_id):
    board = Board.objects.extra(where=[f'board_board.id={board_id}'])[0]
    print(board)
    data = {'board': board}
    print(data)
    return render(request, 'board/view.html', data)


def add(request):
    board = Board()
    board.name = request.POST['name']
    board.password = request.POST['password']
    board.message = request.POST['message']

    board.save()

    return HttpResponseRedirect('/Board')




def deleteform(request, no=0):
    data = {'no': no}
    return render(request, 'board/deleteform.html', data)


def delete(request):
    board = Board.objects.filter(id=request.POST['no']).filter(password=request.POST['password'])
    board.delete()

    return HttpResponseRedirect('/board')


