# 8. 파이썬 웹 프론트엔드 기초 (JavaScript - Ajax)

## 1. Ajax (Asynchronous JavaScript and XML)의 개념

Ajax는 자바스크립트를 사용하여 클라이언트(브라우저)와 서버 간에 데이터를 **비동기적**으로 주고받는 기술이다. 과거에는 XML 포맷을 주로 썼으나, 현재는 가볍고 다루기 쉬운 **JSON** 포맷을 훨씬 많이 사용한다.

* **동기식(Synchronous)**: 서버에 요청을 보내면 응답이 올 때까지 브라우저가 다른 작업을 하지 못하고 멈춰있는 방식이다. 데이터가 오면 페이지 전체가 새로고침된다.
* **비동기식(Asynchronous)**: 서버에 요청을 보낸 후에도 브라우저가 다른 작업을 계속할 수 있다. 페이지 전체를 새로고침하지 않고 필요한 부분의 데이터만 몰래 받아와 화면을 업데이트한다.
* **SPA (Single Page Application)**: 구글 검색 자동완성이나 지도 앱처럼, 페이지 이동 없이 한 화면 내에서 Ajax를 통해 요소만 동적으로 갈아끼우는 웹 애플리케이션 형태이다.


## 2. 전통적인 Ajax 처리 방식 (XMLHttpRequest)
가장 원시적인 형태의 객체(`XMLHttpRequest`)를 생성하여 서버와 통신하는 방법이다. 코드가 길고 콜백 지옥에 빠지기 쉬워 최근 실무에서는 잘 쓰이지 않지만, 내부 원리를 이해하기 위해 알아둘 필요가 있다.

### 1) GET 방식과 POST 방식의 차이
```javascript
// 1. GET 방식 요청 설정
let xhr = new XMLHttpRequest();
// url 뒤에 쿼리 스트링으로 데이터를 붙여 전송한다. (true: 비동기 설정)
xhr.open("GET", "js16.py?irum=tom&nai=33", true); 
xhr.send();

// 2. POST 방식 요청 설정
let xhr2 = new XMLHttpRequest();
xhr2.open("POST", "js16.py", true);
// POST는 Body 영역에 데이터를 숨겨 보내므로 헤더 설정이 필수이다.
xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xhr2.send("irum=tom&nai=33"); 
```

### 2) JSON 및 CSV 데이터 수신 및 파싱
서버에서 받아온 문자열 형태의 데이터를 자바스크립트 객체나 배열로 변환(Parsing)하여 화면에 출력한다.

```javascript
xhr.onreadystatechange = function() {
    // readyState 4: 통신 완료, status 200: 정상 응답
    if(xhr.readyState === 4 && xhr.status === 200) { 
        
        // 1. JSON 파싱
        // xhr.responseText(문자열)를 자바스크립트 객체(JSON)로 변환한다.
        let jsonData = JSON.parse(xhr.responseText); 
        console.log(jsonData[0].code);

        // 2. CSV 파싱 (줄바꿈 기호와 쉼표로 수동 분리)
        let csvText = xhr.responseText.trim();
        let lines = csvText.split("\n"); // 줄바꿈 단위로 쪼개기
        for(let i=0; i<lines.length; i++) {
            let parts = lines[i].split(","); // 쉼표 단위로 쪼개기
            console.log("코드:" + parts[0] + " 이름:" + parts[1]);
        }
    }
}
```


## 3. 실무에서 사용하는 최신 Ajax 방식 3가지

과거의 복잡한 `XMLHttpRequest`를 대체하기 위해 등장한 직관적인 비동기 통신 방법들이다. 모두 **Promise** 기반으로 동작한다.

### 1) `fetch()` 와 `then()`
자바스크립트 내장 함수인 `fetch API`를 사용한다. 코드가 직관적이지만 `.then()`을 여러 번 체이닝해야 한다.
```javascript
function funcFetch() {
    fetch("sangpum.json")
    .then(response => {
        if(!response.ok) throw new Error("서버 오류");
        return response.json(); // 응답을 JSON 객체로 변환하여 다음 then으로 넘김
    })
    .then(data => {
        // data 처리를 여기서 수행
        console.log(data);
    })
    .catch(error => { // 통신 중 에러 발생 시 처리
        console.log("에러 발생 : " + error);
    });
}
```

### 2) `async / await` (가장 권장됨)
`fetch`를 사용하되, `then` 체이닝 대신 동기식 코드처럼 읽기 편하게 작성하는 최신 문법이다. 함수 앞에 `async`를 붙이고 통신 코드 앞에 `await`를 붙여 응답이 올 때까지 기다린다.
```javascript
async function funcAsync() {
    try {
        const response = await fetch("sangpum.json");
        if(!response.ok) throw new Error("서버 오류");
        
        const data = await response.json();
        console.log(data); // 데이터 처리
        
    } catch(error) { // 에러 처리는 try-catch 블록을 사용
        console.log("에러 발생 : " + error);
    }
}
```

### 3) Axios 라이브러리 활용
`Axios`는 브라우저와 Node.js 환경 모두에서 사용할 수 있는 강력한 서드파티 HTTP 클라이언트 라이브러리이다. 자동으로 JSON 변환을 해주어 코드가 더 짧아진다. HTML의 `<head>` 태그에 CDN 링크를 추가해야 사용할 수 있다.
`<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>`

```javascript
async function funcAxios() {
    try {
        const response = await axios.get("sangpum.json");
        const data = response.data; // axios는 자동으로 json 파싱을 완료하여 .data 속성에 담아준다.
        console.log(data);
    } catch(error) {
        console.log("에러 발생 : " + error);
    }
}
```

## 4. [실습] Ajax를 이용한 직원 부서별 검색기 (JSON 필터링)
JSON 데이터를 Ajax로 비동기 로드한 뒤, 입력한 키워드(부서명)를 바탕으로 데이터를 필터링하고 평균 연봉을 계산하여 동적으로 테이블을 렌더링하는 실무형 예제이다.

### HTML & JavaScript (검색 페이지)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ajax 부서별 검색</title>
    <style>
        .error { color: red; margin-top: 10px; }
        table { border-collapse: collapse; margin-top: 15px; width: 500px; }
        th, td { border: 1px solid #333; text-align: center; }
        th { background-color: #eee; }
    </style>
</head>
<body>
    <h3>직원 부서별 검색 (Ajax)</h3>
    <input type="text" id="deptKeyword" placeholder="부서명 입력">
    <button id="btnSearch">검색</button>

    <div id="loading"></div>
    <div id="message"></div>
    <div id="result"></div>

    <script>
        document.getElementById("btnSearch").addEventListener("click", loadJikwons);

        async function loadJikwons() {
            const keyword = document.getElementById("deptKeyword").value.trim();
            const loading = document.getElementById("loading");
            const message = document.getElementById("message");
            const resultDiv = document.getElementById("result");
            
            loading.innerHTML = "데이터 로딩 중...";
            message.innerHTML = "";
            resultDiv.innerHTML = "";

            try {
                // 1. JSON 데이터 비동기 호출
                const response = await fetch("js19jikwon.json");
                if(!response.ok) throw new Error("서버 오류 발생");
                
                const jsonData = await response.json();
                if(jsonData.status !== "success") throw new Error("서버 응답 오류 발생");
                
                const jikwons = jsonData.data; // 실제 데이터 배열 추출

                // 2. 부서 키워드 필터링 (배열.filter 메서드 활용)
                const filtered = jikwons.filter(jik => jik.dept.includes(keyword));
                
                if(filtered.length === 0) {
                    loading.innerHTML = "";
                    message.innerHTML = "<b>검색 결과가 없습니다.</b>";
                    return;
                }

                // 3. 필터링된 데이터로 화면에 테이블 그리기 함수 호출
                renderTableFunc(filtered);

                // 4. 검색 인원수와 연봉 평균 계산 
                // 배열.reduce(): 배열 요소를 순회하며 누적 합계를 구한다.
                const avgSalary = filtered.reduce((sum, emp) => sum + emp.salary, 0) / filtered.length;
                message.innerHTML = `검색 인원 : ${filtered.length}명 / 평균 연봉 : ${avgSalary.toFixed(2)}만원`;
                
            } catch(error) {
                loading.innerHTML = "";
                message.innerHTML = `<span class='error'>${error.message}</span>`;
            }
        }

        // 받아온 데이터 배열을 HTML 테이블 태그 문자열로 조립하여 출력하는 함수
        function renderTableFunc(data) {
            let table = "<table>";
            table += "<tr><th>ID</th><th>이름</th><th>부서</th><th>연봉</th></tr>";
            
            data.forEach(emp => {
                table += `<tr>
                            <td>${emp.id}</td>
                            <td>${emp.name}</td>
                            <td>${emp.dept}</td>
                            <td>${emp.salary}</td>
                          </tr>`;
            });
            table += "</table>";
            
            document.getElementById("result").innerHTML = table;
            document.getElementById("loading").innerHTML = ""; // 로딩 텍스트 지우기
        }
    </script>
</body>
</html>
```

### JSON 데이터 (js19jikwon.json)
```json
{
    "status": "success",
    "count": 5,
    "data": [
        {"id": 1, "name": "홍길동", "dept": "영업부", "salary": 6500},
        {"id": 2, "name": "이순신", "dept": "총무부", "salary": 4200},
        {"id": 3, "name": "강감찬", "dept": "전산부", "salary": 5900},
        {"id": 4, "name": "강나루", "dept": "인사부", "salary": 6700},
        {"id": 5, "name": "신선해", "dept": "영업부", "salary": 7900}
    ]
}
```