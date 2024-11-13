class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: #allow age 0
            return 50
        elif 13 <= age <= 20:#allow age 20
            return 100
        elif 21 <= age <= 60:#count age 21
            return 150
        elif age > 60:#above 60 only
            return 100
        elif age < 0:#error if age < 0
            return ("Error")