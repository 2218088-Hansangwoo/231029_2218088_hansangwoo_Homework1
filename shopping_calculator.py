print("안녕하세요?")
profile = {'이름': input("이름:"), '몸무게': float(input("몸무게:")), '키': float(input("키:"))}
products = []
products_name =[]
coupon = [20,15,10,5]
while True:
    product_name = input("어떤 상품입니까? (끝내려면 'end'을 입력하세요): ")
    if product_name == 'end':
        break
    price = float(input(f"{product_name}의 가격: "))
    products.append({'이름': product_name, '가격': price})
    products_name.append(str(product_name))

CD = input("최대 쿠폰 적용하십니까? (yes or no): ")

class Shop:
    def __init__(self, name, weight, tall, cart, decision):
        self.name = name
        self.weight = weight
        self.tall = tall
        self.cart = cart
        self.decision = decision

    def recommend(self):
        if self.tall <= 170:
            if 50 <= self.weight <= 60:
                print("추천사이즈는 S입니다.")
            elif 60 < self.weight <= 70:
                print("추천사이즈는 M입니다.")
            else:
                print("추천사이즈는 L입니다.")
        elif 170 < self.tall <= 180:
            if 50 <= self.weight <= 60:
                print("추천사이즈는 M입니다.")
            elif 60 < self.weight <= 70:
                print("추천사이즈는 L입니다.")
            else:
                print("추천사이즈는 L입니다.")
        else:
            if 50 <= self.weight <= 60:
                print("추천사이즈는 L입니다.")
            elif 60 < self.weight <= 70:
                print("추천사이즈는 XL입니다.")
            else:
                print("추천사이즈는 XXL입니다.")

    def bill(self):
        total_price = 0
        for product in self.cart:
            price = product['가격']
            if 'yes' in self.decision:
                coupon_price = price - (price * max(coupon) / 100)
                total_price += coupon_price
                max_coupon = max(coupon)
                coupon.remove(max_coupon)
            else:
                total_price += price

        print(f"총 가격은 {total_price}원 입니다.")

cart = products
customer = Shop(profile['이름'], profile['몸무게'], profile['키'], cart, CD)
customer.recommend()
customer.bill()

print(f"총 구매 상품은 {products_name}이고 남은 쿠폰은{coupon}입니다.")



