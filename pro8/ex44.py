from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# 다항 나이브 베이즈
# 텍스트에서 가장 많이 쓰이는 NB모델

texts = [
    '무료 쿠폰 지금 무료 클릭',
    '한번만 클릭하면 무료',
    '오늘 회의는 2시야',
    '지금 할인 행사 진행 중',
    '회의 자료는 메일로 보내주세요',
    '지금 바로 쿠폰 확인'
]
labels = ['spam','spam','ham','spam','ham','spam']
vect = CountVectorizer()
x = vect.fit_transform(texts)
print(vect.get_feature_names_out())
print(x)
print(x.toarray())
print(vect.vocabulary_)
print(x)
# 모델
from sklearn.metrics import accuracy_score
model = MultinomialNB()
model.fit(x, labels)
pred = model.predict(x)
print(accuracy_score(labels,pred))

# 새로운 문장 테스트
test_text = ["무료 쿠폰 지금 발급","간부 회의는 언제 시작 하나요?"]
x_test = vect.transform(test_text)
print(x_test)

preds = model.predict(x_test)
probs = model.predict_proba(x_test)
class_names = model.classes_ 
for text, pred, prob in zip(test_text, preds, probs):
    prob_str = ", ".join([f"{cls}:{p:.4f}" for cls, p in zip(class_names, prob)])
    print(f"'{text}' -> 예측:{pred}/확률:[{prob_str}]")