# 6. 파이썬 웹 프론트엔드 기초 (JavaScript - Part 2 심화)

자바스크립트는 브라우저에서 동작하며, HTML 문서(DOM)를 동적으로 제어하기 위한 핵심 언어이다. VSC의 Live Server를 이용하면 코드를 수정할 때마다 즉시 브라우저에서 테스트할 수 있다.


## 1. 함수 (Function)의 이해와 활용
함수는 특정한 목적의 작업을 수행하도록 설계된 독립적인 코드 블록(`{}`)이다. 자바스크립트는 HTML 문서 내 어디서든 작성할 수 있지만, 일반적으로 `<head>` 태그 내에 함수를 정의하고 `<body>`에서 호출하는 방식을 많이 사용한다.

### 내장 함수 (Built-in Function)
자바스크립트 엔진이 기본적으로 지원하는 함수들이다.
```javascript
let str = "Java script Language";
document.write(str.charAt(2));   // 'v' 출력 (인덱스 2번 문자 추출)
document.write(str.bold());      // 문자열을 <b> 태그로 감싼 효과
document.write(Math.abs(-7));    // 7 출력 (절대값 계산)
```

### 사용자 정의 함수 (User-defined Function)
개발자가 직접 `function` 키워드를 사용해 만든 함수이다. 자바스크립트에서 함수는 **참조형(Reference) 타입**으로 취급된다.
```javascript
let count = 0;
function aa() { // 매개변수 없는 함수
    count += 1;
    document.write(count + "번 수행<br>");
}
aa(); // 함수 호출

function cc(para) { // 매개변수와 반환값(return)이 있는 함수
    let kk = para + 10;
    return kk;
}
let re = cc(5); // re에는 15가 저장됨
```


## 2. 대화상자 관련 함수
사용자에게 메시지를 보여주거나 입력을 받을 때 브라우저 팝업창을 띄우는 함수들이다.

* **`alert("메시지")`**: 단순한 확인 버튼만 있는 경고창을 띄운다. 반환값은 없다.
* **`confirm("메시지")`**: [확인]과 [취소] 버튼이 있는 창을 띄운다. 사용자가 확인을 누르면 `true`, 취소를 누르면 `false`를 반환하므로 결과를 변수에 저장해 분기 처리에 사용할 수 있다.
* **`prompt("메시지", "기본값")`**: 텍스트를 입력받을 수 있는 창을 띄운다. 입력된 문자열을 반환한다.

```javascript
let irum = "홍길동";
alert("이름은 " + irum); 

let result = confirm("계속할까요?"); 
document.write("선택한 값은 " + result); // true 또는 false 출력

let juso = prompt("사는 곳을 입력", "테헤란로"); 
document.write("사는 곳 : " + juso);
```


## 3. ES6 화살표 함수 (Arrow Function)
ES6(ECMAScript 2015)부터 도입된 문법으로, `function` 키워드를 생략하고 `=>` 기호를 사용하여 코드를 훨씬 간결하게 작성할 수 있다.

> **`'use strict';`**: 스크립트 최상단에 선언하면, ES6 이후의 엄격한 문법 검사를 적용하겠다는 의미이다. (구형 문법 사용 시 에러 발생)

```javascript
'use strict';

// 1. 기존 함수 표현식
let sum1 = function(a, b) { return a + b; };

// 2. 화살표 함수 기본 구문
let sum2 = (a, b) => { return a + b; };

// 3. 중괄호와 return 생략 (코드가 한 줄일 때)
let sum3 = (a, b) => a + b;

// 4. 매개변수가 하나일 때는 괄호도 생략 가능
let double1 = n => n * 2;

// 5. 삼항 연산자와 화살표 함수의 결합
let age = 25;
let welcome = (age < 30) ? () => document.write(`안녕<br>`) : () => document.write(`반가워<br>`);
welcome(); // '안녕' 출력
```


## 4. DOM (문서 객체 모델) 요소 탐색과 내용 제어

자바스크립트를 이용해 실행 중인 HTML 태그를 동적으로 참조하고, 내용을 추가하거나 수정할 수 있다.

### DOM 요소 선택 (Query)
* `document.getElementById("아이디")`: 특정 ID를 가진 요소 1개를 찾는다.
* `document.getElementsByName("이름")`: 특정 name을 가진 요소들을 **배열** 형태로 모두 찾는다.
* `document.getElementsByTagName("태그명")`: 특정 태그들을 **배열** 형태로 찾는다.
* **`document.querySelector("#아이디 또는 .클래스")`**: CSS 선택자 방식으로 요소를 찾는다. (최근 가장 많이 사용됨)

### innerHTML vs innerText
* **`innerText`**: 요소 안의 텍스트 값만 대상으로 처리한다. HTML 태그를 넣어도 문자열 그대로 화면에 출력된다.
* **`innerHTML`**: 요소 안의 텍스트뿐만 아니라, **HTML 태그 구조까지 해석하여 렌더링**한다.

```javascript
function fun1() {
    // #test1 영역의 내용을 폼 태그가 포함된 HTML 코드로 완전히 덮어씌움
    let tag1 = "이름:<input type='text' name='irum'>";
    let tag2 = "나이:<input type='text' name='nai'>";
    document.querySelector("#test1").innerHTML = tag1 + "<br>" + tag2;
}
```


## 5. 이벤트(Event)와 핸들러 연결

이벤트란 클릭, 마우스 이동 등 브라우저에서 일어나는 모든 사건을 말한다. 이를 감지하고 실행될 함수를 **이벤트 핸들러**라고 한다.

### 1) 인라인 방식 및 프로퍼티 방식
```html
<a href="javascript:func()">이벤트 처리 함수 호출 (이벤트 핸들러 X)</a>
<button onclick="func()">클릭 이벤트 처리</button>
```

### 2) `window.onload`를 이용한 이벤트 동적 연결 (권장)
HTML 요소(DOM)가 메모리에 전부 로드되기 전에 자바스크립트가 실행되면 태그를 찾을 수 없어 에러가 발생한다. 따라서 `window.onload` 콜백 함수 내부에 이벤트를 연결하는 것이 안전하다.

```javascript
window.onload = function() { // 문서 수신 완료 후 1회 실행
    const exBtn1 = document.getElementById("btn1");
    exBtn1.onclick = function() {
        document.getElementById("show").innerHTML = "클릭1 선택";
    }

    // 배열 형태로 반환되므로 인덱스[0], [1]로 접근해야 함
    const exBtn2 = document.getElementsByName("myBtn");
    exBtn2[0].onclick = function() { alert("첫 번째 myBtn 클릭"); }

    // 가장 권장되는 방식: addEventListener
    // 하나의 요소에 여러 이벤트를 중첩하거나 제거하기 용이하다.
    document.getElementById("btn5").addEventListener("click", abcFunc);
}

function abcFunc() {
    document.getElementById("show").innerHTML = "클릭5 수행됨";
    // 1회 수행 후 이벤트 리스너 제거하기
    document.getElementById("btn5").removeEventListener("click", abcFunc);
}
```


## 6. 다양한 이벤트 종류와 실전 활용 (배경색 변경, a 태그 제어)
클릭 이외에도 다양한 이벤트가 존재하며, 이를 활용하여 동적인 웹페이지를 구축할 수 있다.

### 다양한 이벤트 모음
* `onclick`: 마우스 클릭 시
* `ondblclick`: 마우스 더블클릭 시
* `onmouseover`: 마우스 포인터가 요소 위에 올라갈 때
* `onmouseout`: 마우스 포인터가 요소 밖으로 나갈 때
* `onchange`: `<select>` 등 입력 요소의 값이 변경되었을 때

### [실습 1] Select 박스를 이용한 배경색/글자색 동적 변경
`onchange` 이벤트를 사용하면 선택한 드롭다운 옵션에 따라 즉각적으로 함수를 실행시킬 수 있다.
```html
<script>
    function colorFunc() {
        // frm 폼 안에 있는 bc(배경색)와 tc(글자색)의 value 값을 가져와 body에 적용
        document.body.bgColor = document.frm.bc.value;
        document.body.text = document.frm.tc.value;
    }
</script>

<form name="frm">
    배경색:
    <select name="bc" onchange="colorFunc()">
        <option value="white" selected>흰색</option>
        <option value="black">검은색</option>
        <option value="blue">파란색</option>
    </select>
</form>
```

### [실습 2] `event.preventDefault()` 고유 기능 억제
`<a>` 태그는 클릭 시 페이지를 이동하는 고유 기능을 가지고 있다. 자바스크립트에서 이 이벤트를 낚아채서 고유 기능을 막고 원하는 동작만 수행하게 할 수 있다.

```javascript
window.onload = () => {
    document.querySelector("#daum").onclick = (event) => {
        // <a> 태그의 본래 기능인 링크 이동을 취소(정지)시킴
        event.preventDefault(); 
        console.log(event);
        document.title = "새로운 제목으로 변경됨"; // 탭 제목만 바뀜
    }
}
```