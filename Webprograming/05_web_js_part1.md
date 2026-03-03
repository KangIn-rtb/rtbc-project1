# 5. 파이썬 웹 프론트엔드 기초 (JavaScript - Part 1)

## 1. 자바스크립트(JavaScript) 개요 및 기본 출력

자바스크립트는 기본적으로 HTML에 종속된 스크립트 언어이므로, 특별한 설정이 없는 한 HTML 문서 내의 `<script>` 태그 안에서 사용 가능하다. 

클라이언트(웹 브라우저) 측에서 작동하기 때문에 직접 SQL문을 사용하여 서버의 데이터베이스(DB)에 접근할 수 없다. (만약 자바스크립트를 서버 사이드에서 구동하여 DB를 다루고 싶다면 **Node.js** 환경을 사용해야 한다.)

### 기본 출력 방법
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>JS 기초</title>
</head>
<body>
    ** 자바스크립트 : 클라이언트 사이드 스크립트 ** <br>
    <script>
        // 1. 브라우저 화면에 직접 HTML 요소로 출력
        window.document.write("환영합니다 Js<br>"); 
        document.write("<h2>브라우저에 문자열 출력</h2>");
        
        // 2. 개발자 도구(F12)의 콘솔창에 출력 (디버깅 용도)
        console.log("개발자를 위해 표준 출력 장치로 출력");
        
        let b = 10;
        let a = b + 10;
        document.write("a는 ", a);
    </script>
</body>
</html>
```

## 2. 변수 선언과 자료형 (Scope & Types)
자바스크립트는 변수 선언 시 데이터 타입을 명시하지 않으며, 할당되는 값에 따라 타입이 결정된다. 정수와 실수를 구분하지 않고 모두 `number` 타입으로 취급한다.

* **`let`**: 블록 스코프(Block Scope)를 가지는 변수 선언 방식이다. (최신 표준 권장)
* **`const`**: 블록 스코프를 가지며, 한 번 할당하면 값을 변경할 수 없는 상수이다.
* **`var`**: 전역(Global) 또는 함수 스코프를 가지는 과거의 선언 방식이다. (현재는 사용을 지양함)

```javascript
let aa = 100;
let bb = 20.5; 
const cc = 300; // 상수 선언
// cc = cc + 10; -> 상수의 값을 변경하려 하면 TypeError 발생

let dd = false; // 파이썬과 달리 소문자 false/true 사용
let msg = "변수 선언 이해";

// 자료형 확인 (typeof)
document.write("bb:", typeof(bb), " cc:", typeof(cc), " dd:", typeof(dd), "<br>"); 
// 결과: number, number, boolean

document.write("msg:", typeof(msg), " null:", typeof(null), " undefined:", typeof(undefined), "<br>");
// 결과: string, object, undefined
```

### [주의] 부동 소수점 연산 오차
자바스크립트는 소수를 2진법으로 변환하여 계산하기 때문에 무한 소수가 발생하면 미세한 연산 오차가 생길 수 있다. 따라서 소수를 비교할 때는 `==` 연산자보다 부등호나 특정 오차 범위를 설정하는 것이 안전하다.
```javascript
document.write(0.1 + 0.2); // 결과: 0.30000000000000004
```


## 3. 연산자와 조건문 (if, switch)

### 주요 연산자
* **논리 연산자**: `&&` (AND), `||` (OR)
* **비교 연산자**: 
  * `==`: 값만 비교한다. (자동 형변환 일어남)
  * `===`: 값과 자료형(Type)까지 엄격하게 비교한다. (권장)
  * `!==`: 값 또는 자료형이 다른지 확인한다.
* **삼항 연산자**: `(조건) ? 참일_때_값 : 거짓일_때_값`

```javascript
let x = 5, y = 2;
document.write("논리 연산: ", x > y && x <= y, "<br>");
document.write("삼항 연산: ", (x > y) ? 1000 : 3000, "<br>");

// 다중 할당 연산
let m, b, c;
m = b = c = 6 + 5; // 우측부터 계산되어 모두 11이 할당됨
```

### 조건 판단문

```javascript
let ave = 85;

// if - else if - else 문
if (ave >= 90) {
    document.write("<b style='color:blue'>우수</b>");
} else if (ave >= 70) {
    document.write("<b style='color:black'>보통</b>");
} else {
    document.write("<b style='color:crimson'>저조</b>");
}

// switch 문
let result = "A";
switch(result) {
    case "A":
        document.write("매우 우수");
        break; // break가 없으면 아래 case까지 모두 실행됨 (Fall-through)
    case "B":
        document.write("우수"); break;
    case "D": 
    case "F": // D 이거나 F 일 때 '불량' 출력
        document.write("불량"); break;
    default:
        document.write("기타");
}
```


## 4. 반복문 (for, while)과 템플릿 리터럴

### 템플릿 리터럴 (Template Literal)
백틱(`` ` ``) 기호와 `${변수명}`을 사용하면 파이썬의 f-string처럼 문자열 내부에 변수나 수식을 쉽게 삽입할 수 있다.

```javascript
// for문과 템플릿 리터럴을 활용한 구구단 테이블 생성
document.write("<table border='1'>");
for(let i = 1; i <= 9; i++) {
    document.write("<tr>");
    for(let j = 2; j <= 9; j++) {
        // 백틱(`)을 사용하여 변수와 수식을 직관적으로 배치
        document.write(`<td>${j} x ${i} = ${j * i}&nbsp;&nbsp;</td>`); 
    }
    document.write("</tr>");
}
document.write("</table>");
```

### while 문과 continue
```javascript
let k = 0;
while(k < 10) {
    k++;
    if(k === 3 || k === 5) continue; // 3과 5는 건너뛰고 다음 반복 진행
    document.write(k + " ");
}
```


## 5. 배열 (Array) 기초와 활용

자바스크립트의 배열은 크기가 가변적이며, 하나의 배열 안에 숫자, 문자열, 논리형, 객체(JSON), 심지어 함수(Function)까지 다양한 타입의 데이터를 섞어서 담을 수 있다.

### 배열 선언과 접근
```javascript
let aa = new Array(); // 방법 1
let cc = [];          // 방법 2 (주로 사용)

cc.push("seoul"); // 맨 뒤에 요소 추가
cc.push(82, 1234, 5678); // 여러 개 동시 추가
cc[99] = 'wow'; // 인덱스를 지정하여 추가하면 중간의 빈 공간(empty)은 자동으로 확보됨

document.write(`cc 배열의 전체 크기는 ${cc.length}이다.`); // 결과: 100

// 배열에 함수를 담고 실행하기
let myarr = [
    '안녕', true, 3.5, {name: '신기해'}, // {키: 값} 형태의 JSON(객체)
    function() {
        document.write('난 배열 안의 함수');
    }
];
document.write(myarr[3].name); // '신기해' 출력
myarr[4](); // 배열의 4번 인덱스에 있는 함수 실행
```

### 배열 순회 방법
```javascript
let korea = ['연필', '지우개', '노트'];

// 방법 1: 고전적인 for 루프
for(let i = 0; i < korea.length; i++) {
    document.write(korea[i] + " ");
}

// 방법 2: for...of (파이썬의 for i in korea 와 유사하게 요소 값을 꺼냄)
for(let item of korea) {
    document.write(item + " ");
}

// 방법 3: for...in (요소의 '인덱스' 번호를 꺼냄)
for(let idx in korea) {
    document.write(korea[idx] + " ");
}
```

### 배열 요소 제어 (삭제, 구조 분해, 전개 연산자)
```javascript
// 1. 요소 삭제 (delete vs splice)
let ar = ['i', 'go', 'home'];
delete ar[1]; 
// 결과: ['i', empty, 'home'] -> 값만 지워지고 공간(길이)은 그대로 유지됨

ar = ['i', 'go', 'home'];
ar.splice(1, 1); // 1번 인덱스부터 1개 삭제
// 결과: ['i', 'home'] -> 공간 자체가 완전히 삭제되어 배열 길이가 줄어듦

// 2. 구조 분해 할당 (Destructuring Assignment)
// 배열의 값들을 추출하여 한 번에 여러 변수에 깔끔하게 할당한다.
let nums = [1, 2, 3, 4];
let [a1, a2, a3] = nums; // 4개의 값 중 앞에서부터 3개만 변수에 할당됨

// 3. 전개 연산자 (Spread Operator)
// 배열 앞이나 내부에 '...' 을 붙여 괄호를 벗기고 내부 요소를 펼쳐준다.
const fruits = ['apple', 'peach', 'melon'];
const imsi = [...fruits]; // fruits의 값들을 그대로 펼쳐서 새로운 배열 imsi에 깊은 복사(할당)
```