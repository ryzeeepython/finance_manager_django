from .models import *
import datetime 
from .models import *

class Logic:
    def get_expenses(user, date, form):
        
        user_acc = UserAccount.objects.get(user_id = user.pk)

        if date == "МЕСЯЦ": 
            data = user_acc.data.filter(date__month=datetime.datetime.now().month)
            limit = int(user_acc.limit_per_month)
        else:
            limit = int(user_acc.limit_per_day)
            if date == str(datetime.datetime.now().date()):
                data = user_acc.data.filter(date = date)
                date = 'СЕГОДНЯ'
            else: 
                try:
                    data = user_acc.data.filter(date = date)
                except:
                    data = user_acc.data.get(pk = 0)


        sum = 0
        over_limit = False
        for i in data:
            sum += i.cost

        if sum > limit: 
            over_limit = True

        context = {
            'data': data, 
            'limit': limit,
            'sum': sum,
            'date': date,
            'over_limit': over_limit,  
            'form': form
        }

        return context


    def save_expense(user, form):
        date = form['date']
        if not(date): 
            date = datetime.datetime.today()
        user_acc = UserAccount.objects.get(user_id = user.id)
        new_exp = user_acc.data.create(title=form['title'], cost = form['cost'], date = date)

    def save_limits(user, data): 
        user_acc = UserAccount.objects.get(user_id = user.id)
        if data:
            user_acc.limit_per_day = data['day_limit']
            user_acc.limit_per_month = data['month_limit']
            user_acc.save()


