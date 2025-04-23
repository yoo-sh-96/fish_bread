#주문, 관리자 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만든다
# input()을 통해서 3가지 중 한가지를 입력 받아서 작동시킬 수가 있다

stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵": 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵": 0,
    "초코붕어빵" : 0
}

price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵" : 1500
}

def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택해 주세요.(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 눌러주세요.")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: "))
            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f'{bread_type} {bread_count}개가 판매되었습니다.')
            else:
                print(f"재고가 부족합니다. 현재{stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("다시")

# 붕어빵 admin 기능
def admin_mode():
    while True:
        bread_type = input("추가 주문하시겠습니까?(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 없으시면 뒤로가기를 눌러주세요.")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("창고에 채워넣을 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고가 {bread_count}개 추가되어, 현재 {stock[bread_type]}개 있습니다.')
        else:
            print("다시")

# 붕어빵 계산 기능
def calculation_sales():
    total = 0
    for key in sales:
    #total_sales = sum(sales[key] * price[key] for key in sales
        total += (sales[key] * price[key])
    print(f'오늘의 총 매출은 {total}원 입니다.')

 
# 붕어빵 메인 화면
while True:
    mode = input("원하는 모드를 선택하세요.(주문, 관리자, 종료): ")
    if mode == "종료":
        calculation_sales()
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()