# pandas의 DataFrame의 자료를 원격 DB 테이블에 저장
import pandas as pd
from sqlalchemy import create_engine

data = {
    'code':[6,7,8],
    'sang':['사이다','맥주','와인'],
    'su': [20,22,25],
    'dan':[5000,3000,60000]
    
}
try:
    frame = pd.DataFrame(data)
    print(frame)
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8")
    # 저장
    frame.to_sql(name='sangdata',con=engine,if_exists='append',index=False)
    # 읽기
    df = pd.read_sql("select * from sangdata",engine)
    print(df)
except Exception as e:
    print(e)

"""
.env 파일
DB_USER = root
DB_PASS = 123

from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:\
        {os.getenv('DB_PASS)}@127.0.0.1:3306/test?charset=utf8mb4"
)
"""


