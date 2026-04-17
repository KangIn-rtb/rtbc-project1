# 작업 결과를 간단하게 웹으로 출력하기

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer 
texts = [
    '광고성 메일을 확인하세요',
    '회의 일정 변경 공지'
    '무료 쿠폰 지금 무료 클릭',
    '한번만 클릭하면 무료',
    '오늘 회의는 2시야',
    '지금 할인 행사 진행 중',
    '회의 자료는 메일로 보내주세요',
    '지금 바로 쿠폰 확인',
    '오늘 바로 확인하세요',
    '사내 공지입니다'
]
labels = ['ham','spam','spam','ham','spam','ham','spam','spam','ham']

vect = CountVectorizer()
x = vect.fit_transform(texts)

model = MultinomialNB()
model.fit(x, labels)

# ---Streamil UI---
import streamlit as st
st.title("스팸 메일 분류기")
user_input = st.text_input("메일 내용을 입력하세요:")
if user_input:
    x_new = vect.transform([user_input])
    pred = model.predict(x_new)[0]
    prob = model.predict_proba(x_new)[0]
    spam_prob = prob[model.classes_.tolist().index('spam')]
    ham_prob = prob[model.classes_.tolist().index('ham')]
    
    st.write(f'예측 결과 : {pred}')
    st.progress(spam_prob if pred == 'spam' else ham_prob)
    st.write(f'확률 결과 → spam:{spam_prob:.2%}, ham:{ham_prob:.2%}')
    