# 외국인(미,중,일) 국내 관광지 5개 방문
# 나라별 관광지 상관관계 확인하기
import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 산점도 그리기 
def setScatterGraph(tour_table,m_table,tourpoint):
    pass

def procssFunc():
    # 서울시 관광지 정보 파일
    fname = "서울특별시_관광지입장정보_2011_2016.json"
    jsonTP = json.loads(open(fname, 'r',encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm','resNm','ForNum'))
    tour_table = tour_table.set_index('yyyymm')
    # print(tour_table)
    resNm = tour_table.resNm.unique()
    
    # 중국인 관광지 정보 파일 DataFrame에 저장 
    cdf = "중국인방문객.json"
    jdata = json.loads(open(cdf,'r',encoding='utf-8').read())
    china_table = pd.DataFrame(jdata, columns=('yyyymm','visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])
    
    # 일본인 관광지 정보 파일 DataFrame에 저장 
    jdf = "일본인방문객.json"
    jdata = json.loads(open(jdf,'r',encoding='utf-8').read())
    j_table = pd.DataFrame(jdata, columns=('yyyymm','visit_cnt'))
    j_table = j_table.rename(columns={'visit_cnt':'japan'})
    j_table = j_table.set_index('yyyymm')
    print(j_table[:2])
    
    # 미국인 관광지 정보 파일 DataFrame에 저장 
    adf = "미국인방문객.json"
    adata = json.loads(open(adf,'r',encoding='utf-8').read())
    a_table = pd.DataFrame(adata, columns=('yyyymm','visit_cnt'))
    a_table = a_table.rename(columns={'visit_cnt':'america'})
    a_table = a_table.set_index('yyyymm')
    print(a_table[:2])
    
    m_table = pd.merge(china_table,j_table,left_index=True,right_index=True)
    m_table = pd.merge(m_table,a_table,left_index=True,right_index=True)
    print(m_table)


if __name__ == "__main__":
    procssFunc()