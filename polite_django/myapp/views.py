from django.shortcuts import HttpResponse
from hanspell import spell_checker
from django.core import serializers
from django.http import JsonResponse

def index(request):
    return HttpResponse('''
    <h1>안녕하세요</h1>
    ''')

def polite(request, text_area):
    polite_list = {
    '있습니다':   '있다',
    '같습니다':   '같다',
    '입니다':    '이다',
    '기본서입니다': '기본서다',
    '했습니다':   '했다',
    '하였습니다':  '하였다',
    '익혔습니다':  '익혔다',
    '봤습니다':   '봤다',
    '됩니다':    '된다',
    '줍니다':    '준다',
    '합니다':    '한다',
    '쳤습니다':   '쳤다',
    '쌌습니다':   '쌌다',
    '해주세요':   '해요',
    '샀습니다':   '샀다',
    '었습니다':   '었다',
    '먹습니다':   '먹다',
    '좋습니다':   '좋다',
    '많습니다':   '많다',
    '없습니다':   '없다',
    '하겠습니다':  '하겠다',
    '다가옵니다':  '다가온다',
    '필수입니다':  '필수다',
    '생깁니다':   '생긴다',
    '않습니다':   '않는다',
    '보겠습니다':  '보겠다',
    '하십니다':   '하신다',
    '가능합니다':  '가능하다',
    '중요합니다':  '중요하다',
    '바랍니다':   '바란다',
    '나옵니다':   '나온다',
    '놓았습니다':  '놓았다',
    '어렵습니다':  '어렵다',
    '저는': '나는',
    '배웠습니다':  '배웠다',
    '저희 ':    '우리 ',
    '아닙니다':   '아니다',
    '쉽습니다':   '쉽다',
    '교과서입니다': '교과서다',
    '됐습니다':   '됐다',
    '학습서입니다': '학습서다',
    '없앴습니다':  '없앴다',
    '개념서입니다': '개념서다',
    '교재입니다':  '교재다',
    '안녕하십니까':	'안녕하세요',
    '반갑습니다':	'반가워요',
    '안녕하십니까':	'안녕',
    '반갑습니다':	'반가워',
      }

    for polite_a, short_b in polite_list.items():
        text = str(text_area).replace(short_b, polite_a)

    spelled_text = spell_checker.check(text)
    checked_text = spelled_text.checked

    return JsonResponse({"0": checked_text})