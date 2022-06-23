import pandas as pd
df = pd.DataFrame()

df1 = pd.DataFrame({'name':['Kim', 'Lee', 'Jeong'], 'price':[100, 200, 230]})
#df1.set_index('name', inplace=True)
df2 = pd.DataFrame({'name':['Choi', 'Lee', 'Dong'], 'price':[110, 210, 420]})
#df2.set_index('name', inplace=True)
df = pd.concat([df1,df2])
df = df.reset_index(drop=True)
##https://bio-info.tistory.com/25


## 특정조건 값 찾기 // 판매자가 같아야함
#df.loc[df['B'] == 19] # 데이터 프레임 형식
#df.index[df['B'] == 19].tolist() # 리스트로 인덱스만 받음
# df.loc[(df['Name'] == 'charlie') & (df['Type'] =='Raptors')]
## 찾은 값 구분해서(다른 책이름) 따로 넣기/ 가격만
