from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 카테고리에 지출 추가")
        print("3. 지출 목록 보기")
        print("4. 총 지출 보기")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)
        
        elif choice == "2":
            category_list = list(budget.category_list)
            for i, c in enumerate(category_list, 1):
                print(f"{i}: {c}")
            print()
            try:
                category = category_list[int(input("카테고리를 선택하세요: "))-1]
            except ValueError:
                print("잘못된 번호입니다.\n")
                continue
            except Exception:
                print("잘못된 입력입니다.\n")
                continue
            
            print(f"{category}이(가) 선택되었습니다.")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.total_spent()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
