# 3. 파이썬 웹 프론트엔드 기초 (HTML)

## 1. 개발 환경 설정 (VS Code & Live Server)
HTML과 CSS를 연습할 때 VS Code 에디터의 `Live Server` 익스텐션을 설치하면 매우 편리하다.
설치 후 우측 하단의 `Go Live` 버튼을 누르거나, 에디터에서 마우스 우클릭 후 `Open with Live Server`를 클릭하면 로컬 웹 서버가 구동되어 포트가 할당되고 브라우저에 실시간으로 결과가 반영된다.


## 2. HTML 기본 태그 및 특성

### 텍스트 및 서식 태그
* `<br>`: 줄바꿈 (Break)
* `&nbsp;`: 공백 (Non-breaking space)
* `<!---->`: HTML 주석 처리 (브라우저 화면에 표시되지 않음)
* `<hr>`: 문단 나누기용 가로 수평선
* `<b></b>`: 텍스트를 굵게(볼드체) 표시
* `<h1>` ~ `<h6>`: 제목 표시 (h1이 가장 크며, block 방식이라 자동으로 줄바꿈이 일어남)

### 색상 표현 (RGB)
* 16진수로 `R`, `G`, `B` 각각 2자리씩 할당하여 색상을 표현한다. (00 ~ FF)
* 예시: `#0000FF`는 파란색이다.

### 태그의 출력 형태 (Block vs Inline)
* **Block 방식**: 요소 전후로 자동 행 분리(줄바꿈)가 이루어지며, 가로 영역 전체를 차지한다. (`<p>`, `<h1>`, `<div>`, `<ol>`, `<li>` 등)
* **Inline 방식**: 줄바꿈 없이 같은 행에 계속 이어서 출력되며, 내용물 크기만큼만 영역을 차지한다. (`<b>`, `<i>`, `<span>` 등)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
</head>
<body>
    --출력 형태에 따른 태그 종류--<br>
    1) Block 방식 : 행 분리가 이루어짐 : p, h, div, ol, li ...<br>
    2) inline 방식 : 같은 행에 계속 출력 : b, i, span ...<br> <hr>
    
    <p><b>문단 나누기</b></p>
    <i>이텔릭으로 표기</i>
    <h1>표제용 제목 가장 큼</h1>
    
    <div style="background-color: yellow;">구역 설정 태그(행 전체)</div>
    <span style="background-color: silver;">구역 설정 태그(일부 영역)</span>
    
    <b>&lt;특수문자 표시&gt;</b><br>
    
    <hr size="10" width="200" color="blue"> <hr width="60%" color="#0000ff"> 
    
    <pre>
        입력한  그대로
    보여주는 
                태그이다.
    </pre>
    <br>
    
    --- 목록 만들기 --- <br>
    <ul> <li>파이썬</li>
        <li>DB</li>
    </ul>
    
    <ol> <li>파이썬</li>
        <li>DB</li>
        <ul> <li>파이썬 서브</li>
            <li>DB 서브</li>
        </ul>
    </ol>
</body>
</html>
```


## 3. 이미지와 링크 (img & a 태그)

* **`<img>` 태그**: 이미지를 삽입한다.
  * 속성: `src` (경로), `width`/`height` (크기), `title` (마우스 오버 시 이름), `alt` (이미지 엑스박스 시 대체 텍스트)
* **`<a>` 태그**: 하이퍼링크를 생성한다.
  * 브라우저가 해석하지 못하는 파일(예: `.zip`, `.dat`)이 연결되면 다운로드가 진행된다.

### 절대 경로 vs 상대 경로
* **절대 경로**: `/` 로 시작하며 최상위(Root) 디렉토리부터의 전체 경로를 명시한다. 중간 폴더 이름이 바뀌면 작동하지 않는다.
* **상대 경로**: 현재 자신의 위치를 기준으로 경로를 지정하므로 유지보수 및 이전에 유리하다. (`../` 는 상위 폴더로 이동을 의미)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>image and link</title>
</head>
<body>
    이미지 삽입 
    <img src="images/ramji.jpeg" width="30%" title="람쥐" alt="람쥐 이미지가 없습니다."/>
    <br>
    
    ** a tag 연습 **
    <br>
    <a href="a.html">a 문서 보기 (현재 탭)</a><br>
    <a href="a.html" target="_blank">a 문서 보기 (새 탭)</a><br>
    
    <a href="https://www.kbs.co.kr/" target="_blank">kbs GO</a><br>
    
    <a href="https://www.hyundai-rotem.co.kr/" target="_blank">
        <img src="images/rotem.png" width="30%" title="현대로템 마크"/>
    </a><br>
    
    <a href="mydb.dat">db 다운로드 (브라우저가 못 읽는 파일)</a><br>
    
    <a href="kbs/sbs/cc.html">상대 경로로 cc 보기</a><br> 
    <a href="/pro3web/pack1/kbs/sbs/cc.html">절대 경로로 cc 보기</a><br> 
</body>
</html>
```

### 아이프레임 (iframe)
현재 웹 페이지 안에 또 다른 웹 페이지를 삽입하는 프레임이다. `<a>` 태그의 `target` 속성과 `iframe`의 `name` 속성을 일치시키면 링크 클릭 시 해당 아이프레임 안에서 페이지가 열린다.
```html
    --- iframe 연습 ---<br>
    <a href="https://www.sbs.co.kr/" target="tiger">sbs 열기</a><br>
    <a href="https://www.kbs.co.kr/" target="tiger">kbs 열기</a>
    
    <iframe src="https://www.kbs.co.kr/" width="98%" height="500" name="tiger"></iframe>
```


## 4. 테이블 태그 (Table)
표 형태의 데이터를 표현할 때 사용한다. 과거에는 `border`나 `width` 속성을 HTML에 직접 넣었으나, 최근 웹 표준에서는 CSS로 꾸미는 것을 권장한다.
* `colspan`: 열(가로) 병합
* `rowspan`: 행(세로) 병합

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Table</title>
</head>
<body>
    --- table tag ---<br>
    <table border="1" width="200">
        <tr>
            <td colspan="2">a (가로 두 칸 병합)</td>
            <td>b</td>
            <td rowspan="2">c (세로 두 칸 병합)</td>
        </tr>
        <tr>
            <td>d</td>
            <td>cell(셀)</td>
            <td>
                <table border="1">
                    <tr>
                        <td>kor</td>
                        <td>eng</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```


## 5. 폼 태그 (Form)
사용자의 데이터를 입력받아 서버로 전송할 때 사용하는 태그이다.

* **`<input type="text">`**: 한 줄 텍스트 입력
* **`<input type="password">`**: 비밀번호 입력 (입력 문자가 가려짐)
* **`<textarea>`**: 여러 줄 텍스트 입력 (`cols`와 `rows`로 크기 지정)
* **`<input type="radio">`**: 같은 `name` 그룹 내에서 **단일 선택**만 가능하다. (반드시 `value` 지정 필요)
* **`<input type="checkbox">`**: 같은 `name` 그룹 내에서 **중복(다중) 선택**이 가능하다.
* **`<select>`**: 드롭다운 스크롤 목록 선택
* **`<input type="hidden">`**: 화면에는 보이지 않지만 폼 전송 시 서버로 넘기고 싶은 값이 있을 때 사용한다.
* **`<input type="submit">` / `<input type="reset">`**: 전송 및 폼 초기화 버튼이다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form</title>
</head>
<body>
    ---form 태그(자료 입력용 태그)---
    <form method="get" action="server_script.py">
        1. 이름 : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="text" name="name" id="irum" value="초기값" size="10"><br>
        
        2. 비밀번호 : <input type="password" name="pwd" size="10"><br>
        
        3. 메세지 :<br><textarea name="msg" cols="50" rows="10"></textarea><br>
        
        4. 학년 (단일 선택) :   
        <input type="radio" name="hak" value="1" checked>1학년
        <input type="radio" name="hak" value="2">2학년
        <input type="radio" name="hak" value="3">3학년
        <input type="radio" name="hak" value="4">4학년<br>
        
        5. 과목 (다중 선택) :   
        <input type="checkbox" name="gwa" value="python">파이썬&nbsp;&nbsp;&nbsp;
        <input type="checkbox" name="gwa" value="db">db&nbsp;&nbsp;&nbsp;
        <input type="checkbox" name="gwa" value="web">web&nbsp;&nbsp;&nbsp;
        <br>
        
        <input type="submit" value="전송">
    </form>
</body> 
</html>
```


## 6. DOM (Document Object Model) 문서 객체 모델

HTML 문서를 객체화한 것으로, 브라우저가 HTML 코드를 이해하고 조작할 수 있도록 만든 트리(Tree) 구조의 자료구조이다.
브라우저 내부의 렌더링 엔진이 전달받은 HTML 코드를 분석하여 DOM 트리를 구축한 뒤 화면에 요소를 그려낸다. 이후 자바스크립트(JS)를 통해 이 DOM 요소들에 접근하여 동적인 제어를 수행하게 된다.