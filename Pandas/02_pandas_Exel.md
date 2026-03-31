# 파이썬 데이터 분석 (Pandas와 엑셀 연동)

## 1. 데이터프레임 변환 및 기본 엑셀 입출력
Pandas 데이터프레임은 `.to_` 형태의 메서드를 사용하여 클립보드, HTML, JSON, 엑셀 등 다양한 포맷으로 쉽게 변환하고 내보낼 수 있다.

```python
import pandas as pd

# 1. 딕셔너리를 활용한 데이터프레임 생성
items = {
    'apple' : {'count' : 10, 'price':1500},
    'orange' : {'count' : 5, 'price':800}
}
df = pd.DataFrame(items)
print(df)

# 2. 다양한 포맷으로 내보내기
df.to_clipboard()      # 클립보드에 복사 (엑셀 등에 Ctrl+V로 붙여넣기 가능)
print(df.to_html())    # HTML 테이블 태그로 변환하여 문자열 반환
print(df.to_json())    # JSON 포맷 문자열로 변환

# 3. 데이터프레임을 엑셀 파일로 저장 (.to_excel)
df3 = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'oscar'],
    'age' : [23, 22, 29],
    'city' : ['seoul', 'suwon', 'incheon']
})
# index=False: 행 인덱스 번호는 제외하고 저장
df3.to_excel('result.xlsx', index=False, sheet_name='sheettest') 

# 4. 저장된 엑셀 파일 읽어오기 (ExcelFile & parse)
exdf = pd.ExcelFile('result.xlsx')
print(exdf.sheet_names) # 엑셀 파일 내의 시트 이름 목록 확인

df4 = exdf.parse("sheettest") # 특정 시트의 데이터를 읽어 데이터프레임으로 파싱
print(df4)
```


## 2. 엑셀 고급 포맷팅 (`openpyxl` 연동)

Pandas의 기본 내보내기 기능에 `openpyxl` 엔진을 결합하면 엑셀 셀의 폰트, 배경색, 정렬, 표(Table) 스타일 적용, 엑셀 함수(SUM) 삽입 등 세밀한 서식 지정이 가능해져 자동화된 보고서를 생성하기 좋다.

```python
import pandas as pd 
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo

# 1. 원본 데이터프레임 생성 및 파생 변수 추가
df = pd.DataFrame({
    '상품명': ['Mouse', 'Keyboard', 'Monitor'],
    '수량': [10, 5, 2],
    '가격': [12000, 25000, 300000]
})

df['총금액'] = df['수량'] * df['가격'] # 총금액 컬럼 추가

# 2. ExcelWriter와 openpyxl 엔진을 사용하여 엑셀 파일 생성
with pd.ExcelWriter('report.xlsx', engine='openpyxl') as writer:
    # DataFrame을 엑셀로 저장 (startrow=2 설정으로 3행부터 데이터 출력)
    df.to_excel(writer, sheet_name='Report', index=False, startrow=2)

    # 활성화된 워크시트 객체 가져오기
    ws = writer.sheets['Report']

    # 3. 최상단 제목 추가 및 스타일 적용
    ws['A1'] = '상품 판매 보고서'  
    ws['A1'].font = Font(bold=True, size=14) # 굵게 + 글자 크기 14

    # 4. 헤더(컬럼명) 영역 스타일 설정
    header_font = Font(bold=True, color='FFFFFF') # 흰색 굵은 글씨
    header_fill = PatternFill(start_color='4F81BD', fill_type='solid') # 파란색 배경

    # 3행이 헤더이므로 ws[3]의 셀들을 순회하며 스타일 적용
    for cell in ws[3]:
        cell.font = header_font              
        cell.fill = header_fill                  
        cell.alignment = Alignment(horizontal='center') # 가운데 정렬

    # 5. 데이터 값의 길이에 맞춰 컬럼 너비 자동 조정
    for col in ws.columns:  
        max_length = 0
        col_letter = col[0].column_letter  # 컬럼 문자 추출 (A, B, C...)

        for cell in col:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        # 최대 길이에 여유값(+2)을 주어 너비 설정
        ws.column_dimensions[col_letter].width = max_length + 2

    # 6. 숫자 포맷 적용 (천 단위 콤마)
    # 4행부터 데이터 영역이므로 이 구역의 셀들을 순회
    for row in ws.iter_rows(min_row=4, min_col=2, max_col=4):
        for cell in row:
            if isinstance(cell.value, (int, float)):
                cell.number_format = '#,##0'

    # 7. 엑셀 표(Table) 서식 추가
    # A3부터 데이터가 끝나는 행까지 범위 지정
    tab = Table(displayName="Table1", ref=f"A3:D{len(df)+3}")

    # 줄무늬가 있는 엑셀 기본 테이블 스타일(TableStyleMedium9) 지정
    style = TableStyleInfo(
        name="TableStyleMedium9",   
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,        
        showColumnStripes=False
    )
    tab.tableStyleInfo = style  
    ws.add_table(tab)           

    # 8. 최하단에 합계 행 추가 및 엑셀 함수 연동
    total_row = len(df) + 4  
    ws[f'A{total_row}'] = '합계'  

    # 총금액 합계를 구하는 엑셀 SUM 함수를 수식 문자열로 직접 삽입
    ws[f'D{total_row}'] = f'=SUM(D4:D{len(df)+3})'

    # 9. 전체 데이터 영역 가운데 정렬
    for row in ws.iter_rows(min_row=4, max_row=ws.max_row):
        for cell in row:
            cell.alignment = Alignment(horizontal='center')
```