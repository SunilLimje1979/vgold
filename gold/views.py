from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, 'gold/login.html')

# Create your views here.
def OTP(request):
    return render(request, 'gold/otp.html')

# Create your views here.
def Registration(request):
    return render(request, 'gold/registration.html')

# Create your views here.
def Dashboard(request):
    return render(request, 'gold/dashboard.html')

def Loan(request):
    return render(request, 'gold/loan.html')

def Withdraw(request):
    return render(request, 'gold/withdraw.html')

def Sell_gold(request):
    return render(request, 'gold/sell_gold.html')

def Add_gold(request):
    return render(request, 'gold/add_gold.html')

def Gold_plan(request):
    return render(request, 'gold/gold_plan.html')

def Our_vendors(request):
    return render(request, 'gold/our_vendors.html')

def Gold_wallet(request):
    return render(request, 'gold/gold_wallet.html')

def Profile(request):
    return render(request, 'gold/profile.html')

def Update_profile(request):
    return render(request, 'gold/update_profile.html')

def Certificate(request):
    return render(request, 'gold/certificate.html')

def Gbooking_history(request):
    # Dummy JSON data
    dummy_data = [
        {
            "number": "VG124356",
            "status": "Active",
            "logo_url": "{% static 'assets/img/vgold.jpg' %}",
            "today_gain": "125",
            "paid_amount": "13000",
            "emi_date": "25-02-2024",
            "booking_date": "25-02-2024",
            "weight": "20.00 gm",
            "rate": "123654",
            "value": "13000",
            "tenure": "60 Month",
            "booking_amount": "2000.00",
            "booking_charge": "125",
            "balance_amount": "13000",
            "closing_date": "25-02-2024"
        },
         {
            "number": "VG124356",
            "status": "Closed",
            "logo_url": "{% static 'assets/img/vgold.jpg' %}",
            "today_gain": "125",
            "paid_amount": "13000",
            "emi_date": "25-02-2024",
            "booking_date": "25-02-2024",
            "weight": "20.00 gm",
            "rate": "123654",
            "value": "13000",
            "tenure": "60 Month",
            "booking_amount": "2000.00",
            "booking_charge": "125",
            "balance_amount": "13000",
            "closing_date": "25-02-2024"
        },
          {
            "number": "VG124356",
            "status": "Closed",
            "logo_url": "{% static 'assets/img/vgold.jpg' %}",
            "today_gain": "125",
            "paid_amount": "13000",
            "emi_date": "25-02-2024",
            "booking_date": "25-02-2024",
            "weight": "20.00 gm",
            "rate": "123654",
            "value": "13000",
            "tenure": "60 Month",
            "booking_amount": "2000.00",
            "booking_charge": "125",
            "balance_amount": "13000",
            "closing_date": "25-02-2024"
        },
         
          {
            "number": "VG124356",
            "status": "Closed",
            "logo_url": "{% static 'assets/img/vgold.jpg' %}",
            "today_gain": "125",
            "paid_amount": "13000",
            "emi_date": "25-02-2024",
            "booking_date": "25-02-2024",
            "weight": "20.00 gm",
            "rate": "123654",
            "value": "13000",
            "tenure": "60 Month",
            "booking_amount": "2000.00",
            "booking_charge": "125",
            "balance_amount": "13000",
            "": "25-02-2024"
        },
        # Add more dummy data as needed
    ]
    return render(request, 'gold/gbooking_history.html', {'dummy_data': dummy_data})

def Gold_booking(request):
    return render(request, 'gold/gold_booking.html')

def Booking_details(request): 
    return render(request, 'gold/booking_details.html')

def Gdeposit_history(request):
    # Dummy JSON data
    dummy_data = [
         {
            "number": "VG124356",
            "status": "Active",
            "booking_date": "January 1, 2024",  # Gold Deposit Date
            "weight": "50 grams",  # Gold Deposit Weight
            "booking_charge": "$50",  # Processing Fees
            "rate": "99.9%",  # Gold Purity
            "tenure": "12 months",  # Tenure
            "remark": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",  # Remark
            "closing_date": "December 31, 2024",  # Gold Maturity Date
            "gold_maturity_weight": "50 grams",  # Gold Maturity Weight
            "todays_deposit_weight": "5 grams",  # Today's Deposit Weight
            "todays_deposit_value": "$500"  # Today's Deposit Value
        },
        # Add more dummy data as needed
    ]
    return render(request, 'gold/gdeposit_history.html', {'dummy_data': dummy_data})

def Gold_deposit(request):
    return render(request, 'gold/gold_deposit.html')

def Membership(request):
    return render(request, 'gold/membership.html')

def Money_wallet(request):
    return render(request, 'gold/money_wallet.html')

def Pay_installment(request):
    return render(request, 'gold/pay_installment.html')

def Add_money(request):
    return render(request, 'gold/add_money.html')

def Add_bank(request):
    return render(request, 'gold/add_bank.html')

def Channel_partner(request):
    return render(request, 'gold/channel_partner.html')

def Review(request):
    return render(request, 'gold/review.html')

def Complaint(request):
    return render(request, 'gold/complaint.html')

def Feedback(request):
    return render(request, 'gold/feedback.html')

def Refer(request):
    return render(request, 'gold/refer.html')

