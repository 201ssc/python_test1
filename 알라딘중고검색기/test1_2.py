"""
1. 원을 제거 하고
총 가격을 구한다.

2. 동일 판매자를 찾는다.
if== 총 가격을 더한다.
else== 가장 위에 가격을 합친다.


"""
import pandas as pd
import locale ## "," 천단위 문자열 float 변환 오류 제거
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def get_dvide(dft, i): ## 1부터 시작해야함
    df_1 = dft.drop([0], axis=0)
    na = df_1[1][i]
    title = na.split(' ')[1] ## 상품이름
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


url = 'https://www.aladin.co.kr/shop/UsedShop/wuseditemall.aspx?ItemId=14906714&TabType=0'
tlist = pd.read_html(url,encoding='utf-8')
dft = tlist[-2]
df_1 = dft.drop([0], axis=0)



glist = []
for i in range(1, len(df_1)+1):
    m = get_dvide(dft, i)
    glist.append(m)
dff = pd.DataFrame(glist, columns=['title', 'grade', 'price', 'charge', 'seller'])
# dff["price"] = dff["price"].astype(float)
# dff["charge"] = dff["charge"].astype(float)