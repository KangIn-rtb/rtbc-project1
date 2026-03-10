#  3. Flask 템플릿 엔진 심화 (조건, 반복, 필터, 상속)

## 1. Jinja2 템플릿 처리 원리

웹 브라우저는 기본적으로 `{% %}`나 `{{ }}` 같은 템플릿 엔진 특유의 기호를 해석하지 못한다.
따라서 Flask 서버 내부에 있는 **Jinja2**가 먼저 해당 기호들 안의 파이썬 코드(조건문, 반복문, 변수 등)를 실행하여 **순수한 HTML로 변환**한 뒤, 완성된 HTML 문서만 브라우저로 보내는 방식으로 동작한다.


## 2. 템플릿 상속 (Template Inheritance)

모든 웹 페이지에 공통으로 들어가는 레이아웃(상단 헤더, 하단 푸터 등)을 매번 작성하지 않도록, 기본 틀(`base.html`)을 만들어 두고 다른 HTML 파일들이 이를 상속(`extends`)받아 특정 부분만 갈아끼우는 방식이다.

### 1) 부모 템플릿 (`base.html`)
뼈대가 되는 기본 틀이다. `{% block 블록명 %}`으로 공간을 만들어 두면 자식 템플릿에서 해당 영역을 덮어쓸 수 있다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}기본 제목{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <h2>공통 상단 메뉴(header)</h2>
    <hr>
    
    {% block content %}
        기본 내용
    {% endblock %}
    
    <hr>
    <footer class="bg-light text-center">
        <span class="text-muted">작성자 : 홍길동 (주)에이콘 (전화)02-111-1234</span><br>
        공통 바닥글
    </footer>
</body>
</html>
```

### 2) 자식 템플릿 1 (`index.html` - 메인 화면)
`base.html`을 상속받아 메뉴 리스트를 렌더링하는 페이지이다. (※ 코드 최상단에 반드시 `{% extends %}`를 명시해야 한다.)
```html
{% extends "base.html" %}

{% block title %}메인 : Jinja2{% endblock %}

{% block content %}
    <h3>메인 : 템플릿 엔진의 조건문, 반복문, 필터, 상속</h3>
    <ul>
        <li><a href="/condition">조건문</a></li>
        <li><a href="/loop">반복문</a></li>
        <li><a href="/filter">필터</a></li>
        <li><a href="/base">base 틀 확인하기</a></li>
    </ul>
{% endblock %}
```


## 3. 필터 (Filter) 사용
템플릿 내에서 파이썬 서버로부터 넘겨받은 변수 값을 화면에 출력하기 직전에 원하는 형태로 가공할 수 있다. 변수명 뒤에 파이프(`|`) 기호를 붙여 사용한다.

### 자식 템플릿 2 (`filter.html`)
```html
{% extends "base.html" %}

{% block title %}필터 : Jinja2{% endblock %}

{% block content %}
    <h3>필터 옵션 사용 예제</h3>
    
    원본 메세지 : {{message}}<br>
    대문자로 : {{message | upper}}<br>
    첫 글자만 대문자로 : {{message | capitalize}}<br>
    단어별 첫 글자 대문자로 : {{message | title}}<br>
    가격 : {{price}}<br>
{% endblock %}
```


## 4. 조건문 (Condition)
서버에서 넘겨준 데이터(예: 점수)에 따라 화면에 렌더링할 HTML 태그를 동적으로 다르게 분기 처리할 때 사용한다. 파이썬의 `if-elif-else` 문법과 유사하나, 마지막에 반드시 `{% endif %}`로 닫아주어야 한다.

### 자식 템플릿 3 (`condition.html`)
```html
{% extends "base.html" %}

{% block title %}조건문 : Jinja2{% endblock %}

{% block content %}
    <h3>조건 연습</h3>

    {% if score >= 90 %}
        <p>성적 : {{score}} -> a등급</p>
    {% elif score >= 80 %}
        <p>성적 : {{score}} -> b등급</p>
    {% else %}
        <p>성적 : {{score}} -> c등급</p>
    {% endif %}
{% endblock %}
```


## 5. 반복문 (Loop)
서버에서 리스트나 배열 형태의 데이터를 넘겨주었을 때, 이를 순회하며 반복적인 HTML 태그(예: `<li>`, `<tr>` 등)를 생성할 때 사용한다.

### 자식 템플릿 4 (`loop.html`)
`loop.index` 변수를 사용하면 현재 반복이 몇 번째 진행 중인지 번호(1부터 시작)를 매길 수 있다.
```html
{% extends "base.html" %}

{% block title %}반복문 : Jinja2{% endblock %}

{% block content %}
    <h3>반복문 예제</h3>
    <ul>
        {% for i in user %}
            <li>{{loop.index}}번째 사람 : {{i}}</li>
        {% endfor %}
    </ul>

    <p>총 인원 : {{user | length}}</p> 
{% endblock %}
```