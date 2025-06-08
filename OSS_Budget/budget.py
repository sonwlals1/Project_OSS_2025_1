import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.category_list = set()

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        self.category_list.add(category)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def category_list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        for category in self.category_list:
            print(f"[{category}]")
            for e in self.expenses:
                if e.category == category:
                    print(e)
            print()