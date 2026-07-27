# expense management file including method are :

'''
  1.  add_expense(amount, category, description)
  2.  get_all_expenses()
  3.  get_total_expenses()
  4.  delete_expense(expense_index)
  5.  get_expenses_by_category(category_name)
  6.  get_expense_by_date(date)
  7.  get_total_expense_by_category(category_name)'''
  
# progect import
import storage
import datetime

# module import




class ExpenseManager:

    def __init__(self) -> None:
        self.expense = storage.get_data()
        pass

    def get_date(self) -> str :
        self.date = datetime.datetime.now().strftime("%d-%m-%Y At %H:%M:%S")
        return self.date
    
    @property
    def index_no(self) -> int:
        if not self.expense:
            self.index = 1
            return self.index
        else:
            self.data_index = [index["index"] for index in self.expense]
            self.index = max(self.data_index) + 1
            return self.index

    def add_expense(self,amount, category, description) -> bool:
        data = {"date": self.get_date(),
                "index": self.index_no,
                "Amount": amount,
                "category" : category,
                "description" : description}
        self.expense.append(data)
        storage.save_data(self.expense)
        return True
    
    def get_all_expenses(self) -> list:
        return self.expense
    
    def get_total_expenses(self) -> int:
        total_money = [item["Amount"] for item in self.expense]
        return sum(total_money)
    
    def delete_expense(self,index) -> bool:
        before = len(self.expense)
        re_write = [expense for expense in self.expense if expense["index"] != index]
        self.expense = re_write
        if before > len(re_write):
            storage.save_data(self.expense)
            return True
        else :
            return False
        
    def get_expenses_by_category(self,category_name) -> list:
        if not self.expense:
            return []
        else: 
            found_category = [items for items in self.expense if items["category"] == category_name]
            return found_category
        
    def get_expense_by_date(self,date) -> list:
        if not self.expense:
            return []
        else :
            found = [item for item in self.expense if item['date'][0:10]==date]
            return found

    def get_total_expense_by_category(self,category_name) -> list:
        amount_list = self.get_expenses_by_category(category_name)
        if not amount_list:
            return [category_name]
        else :
            amount = [item["Amount"] for item in amount_list]
            return [sum(amount),category_name]



