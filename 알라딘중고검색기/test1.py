import pandas as pd
import requests
"""
1. 개별로 정리해서 데이터 프레임에 넣기,
 이름만 검색해도 알수 있도록// 아이템아이디를 직접해야 할까.
 그걸 만드는 건// 향후 다른 git을 참고

2. 검색(종류)
    1정리된 데이터 프레임으로 최저가 검색
        맨위에 것들만 선택해서 총가격과 가격 검색
    2판매자가 같은 경우 최저가 검색
        같은 경우 찾아서 총가격과 가격
    3최고등급에서 최저가 검색


"""
def get_dvide(dft, i): ## 1부터 시작해야함
    df_1 = dft.drop([0], axis=0)
    na = df_1[1][i]
    title = na.split(' ')[1] ## 상품이름
    grd = df_1[2][i]         ## 등급
    a = df_1[3][i]
    prod = a.split(' ')[0]  ## 상품가격
    deli =a.split(' ')[7]   ## 배송비
    seller = df_1[4][i]      ## 배송지
    alist = [title, grd, prod, deli, seller]
    return (alist)


url = 'https://www.aladin.co.kr/shop/UsedShop/wuseditemall.aspx?ItemId=14906714&TabType=0'
tlist = pd.read_html(url,encoding='utf-8')
dft = tlist[-2]
df_1 = dft.drop([0], axis=0)
na = df_1[1]
a = get_dvide(dft, 1)


glist = []
for i in range(1, len(df_1)+1):
    m = get_dvide(dft, i)
    glist.append(m)
dff = pd.DataFrame(glist, columns=['title', 'grade', 'price', 'charge', 'seller'])
## 일단 데이터 프레이 넣기 완료, 기본기가 없으니까 너무 멍청하게 하고 있다..
## 애초에 원을 제외하고  .astype(float) 해볼까.