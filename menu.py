import expense_manager

class CLI_menu:

    def __init__(self) -> None:
        self.manager = expense_manager.ExpenseManager()
        self.menu_item = ["exit",
                          "add expense",
                          "delete expense",
                          "get expenses by category",
                          "get all expenses",
                          "get total money spend on expenses",
                          "get_expense_by_date"]
        pass

    def add_data(self):
        while True:
            category = input("which category did you spend your money : ".title()).strip()
            if not category:
                continue
            else:
                break
        while True:
            amount = input("how much money did you spend on it : ₹".title()).strip()
            if amount.isdigit() :
                amount = int(amount)
                break
            else :
                continue
        while True :
            description = input("describe about where the spending gone : ".title())
            if  not description :
                continue
            else : 
                break
        success = self.manager.add_expense(amount, category, description)
        if success:
            print("✅ Expense added successfully!")
        else:
            print("❌ Failed to add expense.")
    
    def delete_data(self):
        while True:
            index = input('enter the the index you want to delete \n if dont know the index first see all expense for be sure : '.title()).strip()
            if index.isdigit(): 
                index = int(index)
                success = self.manager.delete_expense(index)
                if success:
                    print(f"✅ Expense Number {index} Deleted successfully!")
                else:
                    print(f"❌ Failed to Delete This Index {index} not avlible in the data")
                break
            else :
                continue

    def expanse_by_category(self) :
        while True:
            category = input("which category did you spend your money : ".title()).strip()
            if not category:
                continue
            else:
                success = self.manager.get_expenses_by_category(category)
                if success:
                    print(f"✅ Expense Category {category} Here You GO!")
                    for item in success:
                        print(f"|| {item} ||")
                else:
                    print(f"❌ Failed to Feach Category {category} not avlible in the data")
                break
    def expense_by_date(self) :
        while True:
            date = input("enter the date in [01-01-2026] format : ").title().strip()
            if not date:
                continue
            elif None :
                pass # dont know the regex yet to use at this place 
            else :
                found = self.manager.get_expense_by_date(date)
                if found :
                   print(f"✅ Expense on {date} Here You GO!")
                   for item in found:
                       print(f"|| {item} ||")
                else:
                    print(f"❌ Failed to Feach Not any expense on this  {date}")
                break
    def get_all_expenses(self) :
        data = self.manager.get_all_expenses()
        if not data:
            print("NO DATA Avlible ##")
        else:
            for item in data :
                print(f" || {item} ||")

    def get_total_expenses(self) :
        amount = self.manager.get_total_expenses()
        print(f"this is the total amount {amount} you spent till now!!🤯")

    def start_app(self) :
        self.menu_dict = {1 : self.add_data,
                          2 : self.delete_data,
                          3 : self.expanse_by_category,
                          4 : self.get_all_expenses,
                          5 : self.get_total_expenses,
                          6 : self.expense_by_date}

        while True:
            print("| Welcome to Expense Tracker! 🚀 |".center(50,"$"))
            for index,item in enumerate(self.menu_item):
                print(f"| {index} : {item} |")
        
            options = input("Enter from the following option : ".title()).strip()
            if options.isdigit():
                options = int(options)
                if options == 0:
                    print("Goodbye! 👋")
                    break
                elif options < len(self.menu_item) :
                    go = self.menu_dict[options]
                    go()
                    continue
                else :
                    print("Invalid choice, please try again.")
                    continue



