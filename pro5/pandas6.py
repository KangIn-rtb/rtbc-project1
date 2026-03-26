import pandas as pd
items = {
    'apple' : {'count' : 10, 'price':1500},
    'orange' : {'count' : 5, 'price':800}
}
df = pd.DataFrame(items)
print(df)
df.to_clipboard()
print(df.to_html)
print(df.to_json())
df3 = pd.DataFrame({
    'name' : ['Alice','Bob','oscar'],
    'age' : [23,22,29],
    'city':['seoul','suwoin','incheon']
})
df3.to_excel('result.xlsx',index=False,sheet_name='sheettest') # 엑셀 저장
exdf = pd.ExcelFile('result.xlsx')
print(exdf.sheet_names)
df4 = exdf.parse("sheettest")
print(df4)