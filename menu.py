import expense_manager
import datetime

class CLI_menu:

    def __init__(self) -> None:
        self.manager = expense_manager.ExpenseManager()
        self.menu_item = ["exit",
                          "add expense",
                          "delete expense",
                          "get expenses by category",
                          "get all expenses",
                          "get total money spend on expenses",
                          "get_expense_by_date",
                          "get_total_expense_by_category",
                          "update_expense"]
        pass

    def user_input(self,prompt: str,prefix="") -> str:
        while True:
            full_prompt = f"\n{prompt} (or type cancel to go back) : {prefix}".title()
            user_input = input(full_prompt).strip()
            if not user_input :
                print("❌ Input cannot be empty! Please try again.")
                continue
            elif user_input.lower() == "cancel" :
                return "cancel"
            else :
                return user_input
            
    def add_data(self):
        category = self.user_input("which category did you spend your money : ").lower()
        if category == "cancel" :
            return
        while True :
            amount = self.user_input("how much money did you spend on it : ",prefix="🤑")
            if amount == "cancel":
                return
            elif amount < 0:
                print("spending amount can't be zero".title())
                continue
            elif not amount.isdigit() :
                print("Please Enter a valid amount ")
                continue
            else :
                amount = int(amount)
                break
        description = self.user_input("describe about where the spending gone : ")
        if  description == 'cancel':
            return
        success = self.manager.add_expense(amount, category, description)
        if success:
            print("✅ Expense added successfully!")
        else:
            print("❌ Failed to add expense.")
    
    def delete_data(self):
        while True:
            index = self.user_input("enter the the index you want to delete \nif dont know the index first see all expense for be sure : ")
            if index == 'cancel':
                return
            elif index.isdigit(): 
                index = int(index)
                success = self.manager.delete_expense(index)
                if success:
                    print(f"✅ Expense Number {index} Deleted successfully!")
                else:
                    print(f"❌ Failed to Delete This Index {index} not available in the data")
                break
            else :
                print("Please Inter A Valid Index")
                continue

    def expense_by_category(self) :
        category = self.user_input("which category did spends do you want find out : ")
        if category == "cancel":
            return
        else:
            success = self.manager.get_expenses_by_category(category)
            if success:
                print(f"\n✅ Expense Category {category} Here You GO!\n")
                for item in success:
                    print(f"|| {item} ||")
            else:
                print(f"❌ Failed to Fetch Category {category} not Available in the data")

    def expense_by_date(self) :
        format_rule = "%d-%m-%Y"
        date = self.user_input("enter the date in [01-01-2026] format : ")
        if date == "cancel":
            return    
        else :
            try :
                valditions = datetime.datetime.strptime(date , format_rule)
                if valditions:
                    found = self.manager.get_expense_by_date(date)
                    if found :
                        print(f"\n✅ Expense on {date} Here You GO!\n")
                        for item in found:
                            print(f"|| {item} ||")
                    else:
                        print(f"❌ Failed to Fetch Not any expense on this  {date}")
            except ValueError :
                print("please enter a correct fromat of date [dd-mm-yyyy]")
            except Exception  as e:
                print(e)

    def get_all_expenses(self) :
        data = self.manager.get_all_expenses()
        if not data:
            print("NO DATA Available ##")
        else:
            print(f"\n✅ All Expense Here You GO!\n")
            for item in data :
                print(f" || {item} ||")

    def get_total_expenses(self) :
        amount = self.manager.get_total_expenses()
        print(f"\nthis is the total ₹{amount} you spent till now!!🤯")

    def total_expense_by_category(self):
        category = self.user_input("which category did spends do you want find out : ")
        if category == "cancel":
            return
        else :
            amount,cat_name = self.manager.get_total_expense_by_category(category)
            if amount == 0:
                print(f"\n this {cat_name} category has not been created yet !!❌")
            else :
                print(f"\nthe total ₹{amount} till now you spent this category : {cat_name}!!🤯")

    def update_expense(self) :
        while True :
            index = self.user_input("index of expense you want to edit : ")
            if index == 'cancel':
                return
            elif index.isdigit():
                index = int(index)
                break
            else :
                print("if you don't know the index first see all expenses for find it ".title())
                continue
        while True :
            part = self.user_input("which thing you want edit [[1-Category],[2-Money][3-Description]]")
            if part == 'cancel' :
                return 
            elif part in ['1','2','3'] :
                break
            else :
                print("please give input only [1] or [2] or [3]".title())
                continue
        if part in ['1','3'] :
            if part == '1':
                part = "category"
            else :
                part = 'description'
            changed = self.user_input("what to changed with :")
        elif part == '2':
            part = "Amount"
            while True :
                        changed = self.user_input("new amount : ",prefix="🤑")
                        if changed == "cancel":
                            return
                        elif changed.isdigit():
                            changed = int(changed)
                            break
                        elif not changed.isdigit() :
                            print("Please Enter a valid amount ")
                            continue
        self.manager.update_expense(index,part,changed)
        


    def start_app(self) :
        self.menu_dict = {1 : self.add_data,
                          2 : self.delete_data,
                          3 : self.expense_by_category,
                          4 : self.get_all_expenses,
                          5 : self.get_total_expenses,
                          6 : self.expense_by_date,
                          7 : self.total_expense_by_category,
                          8 : self.update_expense}
        UIlen = len(max(self.menu_item,key=len))+10
        while True:
            print("\n")
            print("₹".center(60,"₹"))
            print("   |||    Welcome to Expense Tracker! 🚀   |||     ".center(60,"₹"))
            print("₹".center(60,"₹"))
            print("="*UIlen)
            for index,item in enumerate(self.menu_item):
                print(f"|  {index} : {item}  ".ljust(UIlen-1)+"|")
            print("="*UIlen,end="\n\n")
            options = input("Enter from the following option : ".title()).strip()
            if options.isdigit():
                options = int(options)
                if options == 0:
                    print("\nGoodbye! 👋\n")
                    break
                elif options < len(self.menu_item) :
                    go = self.menu_dict[options]
                    go()
                    continue
                else :
                    print("\nInvalid choice, please try again.")
                    continue
            else :
                print(f"\nPlease Enter a valid option from the choice not {options} !!!")


