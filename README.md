롯데월드타워 SKY31 점심메뉴 추출기 (unmaintained)
================

롯데월드타워에 재직중인 직장인이 점심메뉴 매번 확인하기 귀찮아서 만듦

메뉴데이터가 더이상 제공되지 않아 업데이트되지 않음

메뉴파일을 구할수 있다면 동작은 할지도...?


사용법
================
2021년 3월 메뉴라면, `202103.pptx` 혹은 `202103.pdf` 파일로 저장하고 아래 코드 사용

```python
# 오늘의 메뉴 얻기
SKY31().get_today_menus()

# 오늘의 메뉴 출력 예시
today_menu = SKY31().get_today_menus()
    print('오늘의 SKY 31 점심메뉴')
    for menu in today_menu:
        print(f'{menu.menu} ({menu.price:,d}원)')

# 월간 메뉴 얻기
SKY31().get_monthly_menus()
```
