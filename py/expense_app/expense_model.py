from datetime import datetime

class Expense: 
    def __init__(self, category: str, amount: float, date: str):
        self.category = category
        self.amount = amount
        self.date = self._validate_date(date)
        
    def _validate_date(self, date: str) -> datetime:
        try:
            return datetime.strptime(date, "%Y-%m-%d")  
        except:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date.strftime("%Y-%m-%d")
        }   
        
