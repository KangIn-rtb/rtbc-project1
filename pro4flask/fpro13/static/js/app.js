const $ = (sel) => document.querySelector(sel); // 현재 작업중인 객체가 선택됨
// function $(sel){
//     return document.querySelector(sel);
// } 과 같은 의미
// ex) $("#sendBtn") 하면 doucment.querySelector(sel)가 실행 됨

$("#sendBtn").addEventListener("click", async() => {
    const name = $("#name").value.trim();
    const age = $("#age").value.trim();
    // const age = document.querySelector("#age").value.trim() 위랑 같은거 

    const params = new URLSearchParams({name, age}); // 홍길동 -> %ED%78%AD... 이런 변환을 해줌 -> 자동 인코딩
    const url = `/api/friend?${params.toString()}`; // 최종 URL 생성 : /api/friend?name=%ED%78%AD...&age=22 이런식으로 넘어감
    $("#result").textContent = "요청중...";

    try{
        const res = await fetch(url, {
            method:"GET",
            headers:{"Accept":"application/json"} // mime type
        });

        const data = await res.json(); // 응답 본문을 JSON으로 파싱해서 JS객체화
        if(!res.ok || data.ok === false){
            $("#result").innerHTML = `<span class="error">네트워크 패싱오류 : ${data.error}</span>`;
            return;
        }
        $("#result").innerHTML = `
            <div>이름 : ${data.name}</div>
            <div>나이 : ${data.age}</div>
            <div>연령대 : ${data.age_group}</div>
            <div>메세지 : ${data.msg}</div>
        `
    }catch(err){
        $("#result").innerHTML = `<span class="error">네트워크 패싱오류 : ${err}</span>`;
    }
});
