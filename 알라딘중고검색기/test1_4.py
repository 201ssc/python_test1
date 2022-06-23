"""
기존 test1_3 def에 하나로 넣어서 보기좋게 하기
+ 복표시, 중복과 개별 가격 비교해서 추천해주기, 그 경우 등급 표지
> 향후 등급 최소치를 넣어서 필터링 하여 기준 비교하기
> 값 3개 이상 비교도 가능하게 하기
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

df = pd.DataFrame(columns=['cost', 'seller','grade1', 'grade2'])
for i in range(0, len(a)):
    aa = a["seller"][i]
    for j in range(0, len(b)):
        bb = b["seller"][j]
        if aa == bb:
           print(aa)
           alco =a["price"][i] + a["charge"][i]+ b["price"][j] # 총가격
           alse = a["seller"][i]  # 판매자
           ag = a["grade"][i]
           bg = b["grade"][i]
           all = [alco,alse,ag,bg]
           df= df.append(pd.Series(all, index=df.columns), ignore_index=True)
        else:
            pass
indc = a['price'][0] + a["charge"][0] + b['price'][0] + b["charge"][0] # 개별가격 최저가
indse = a["seller"][0], b["seller"][0]
indgr = a["grade"][0], b["grade"][0]
print("\n개별로 구매할 실 경우 가격은 총 '{}원' 입니다."
      "\n 판매자:{}, 등급:{}".format(indc,indse,indgr))