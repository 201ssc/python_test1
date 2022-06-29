"""
df =pd.concat([a,b], ignore_index=True)
df['seller'].value_counts()
여러권 3권이상일 경우도 중복 판매자 확인쉽게 가능

    과제
    1종류를 여러권 하는 경우 필터링 필요
    계산은 다른 방식적용해야함

condition = (df.sex == 'female') & (df.survived ==1)
aa =df[condition]
활용해보기

"""

import pandas as pd
import locale ## "," 천단위 문자열 float 변환 오류 제거
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def get_dvide(dft, i): ## 1부터 시작해야함
    df_1 = dft.drop([0], axis=0)
    na = df_1[1][i]
    title = na.split(' ')[1] ## 상품이름    ## 오류발견, 띄어쓰기 시 오류 {진보와 빈곤} > {진보와}
    grd = df_1[2][i]         ## 등급
    a = df_1[3][i]
    prod = a.split(' ')[0]  ## 상품가격
    pp = prod.strip("원")
    p = locale.atof(pp)
    deli = a.split(' ')[7]  ## 배송비
    dd = deli.strip("원")
    d = locale.atof(dd)
    seller = df_1[4][i]      ## 배송지
    alist = [title, grd, p, d, seller]
    return (alist)

def get_al_df(itemId):
    url = 'https://www.aladin.co.kr/shop/UsedShop/wuseditemall.aspx?ItemId={}&TabType=0'.format(itemId)
    tlist = pd.read_html(url,encoding='utf-8')
    dft = tlist[-2]

    glist = []
    for i in range(1, len(dft)):
        m = get_dvide(dft, i)
        glist.append(m)
    dff = pd.DataFrame(glist, columns=['title', 'grade', 'price', 'charge', 'seller'])

    return (dff)

## 중고책의 경우 일반 검색에서 나오는 id 코드와 다르기에 주의해야 한다.
a = get_al_df("877643")
b = get_al_df("6766101")

df =pd.concat([a,b], ignore_index=True)
df['seller'].value_counts()
