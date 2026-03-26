# 한글 형태소 분석
# 형태소는 의미를 가지는 가장 작은 단위를 의미
from konlpy.tag import Okt,Kkma,Komoran

text = "나는 오늘 아침에 학교에 갔다. 가는 길에 벚꽃이 피어 너무 아름다웠다."
okt = Okt()
print(okt.morphs(text))
print(okt.pos(text))
print(okt.pos(text,stem=True))
print(okt.nouns(text))
