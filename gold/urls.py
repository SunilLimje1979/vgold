from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    
    path('otp/', views.OTP, name='otp'),
    
    path('registration/', views.Registration, name='registration'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),
    
    path('loan/', views.Loan, name='loan'),
      
    path('add_gold/', views.Add_gold, name='add_gold'),
    
    path('withdraw/', views.Withdraw, name='withdraw'),
    
    path('sell_gold/', views.Sell_gold, name='sell_gold'),
    
    path('gold_plan/', views.Gold_plan, name='gold_plan'),
    
    path('our_vendors/', views.Our_vendors, name='our_vendors'),
    
    path('imagespecific/', views.Imagespecific, name='imagespecific'),
    
    path('gold_wallet/', views.Gold_wallet, name='gold_wallet'),
    
    path('gbooking_history/', views.Gbooking_history, name='gbooking_history'),
    
    path('transection_pdf/', views.transection_pdf, name='transection_pdf'),
    
    path('gold_booking/', views.Gold_booking, name='gold_booking'),
    
    path('booking_details/', views.Booking_details, name='booking_details'),
    
    path('gdeposit_history/', views.Gdeposit_history, name='gdeposit_history'),
    
    path('gold_deposit/', views.Gold_deposit, name='gold_deposit'),
    
    path('calculate_gold_deposite/', views.calculate_gold_deposite, name='calculate_gold_deposite'),
    
    path('cgold_mature_weight/', views.cgold_mature_weight, name='cgold_mature_weight'),
    
    path('membership/', views.Membership, name='membership'),
    
    path('money_wallet/', views.Money_wallet, name='money_wallet'),
    
    path('pay_installment/', views.Pay_installment, name='pay_installment'),
    
    path('add_money/', views.Add_money, name='add_money'),
    
    path('add_bank/', views.Add_bank, name='add_bank'),
    
    path('channel_partner/', views.Channel_partner, name='channel_partner'),
    
    path('review/', views.Review, name='review'),
        
    path('profile/', views.Profile, name='profile'),  
      
    path('update_profile/', views.Update_profile, name='update_profile'),
    
    path('certificate/', views.Certificate, name='certificate'),
    
    path('complaint/', views.Complaint, name='complaint'),
    
    path('feedback/', views.Feedback, name='feedback'),
    
    path('refer/', views.Refer, name='refer'),
    
    path('booking_receipt/', views.BookingReceipt, name='booking_receipt'),

    path('logout/', views.Logout, name='logout'),
    
    path('handle_selection/', views.handle_selection, name='handle_selection'),
    
    path('dashb/', views.dashb, name='dashb'),
    
    path('nc_login/', views.nc_login, name='nc_login'),
    
    path('nc_booking/', views.nc_booking, name='nc_booking'),
    
    path('nc_deposit/', views.nc_deposit, name='nc_deposit'),
    
    path('nc_wallet/', views.nc_wallet, name='nc_wallet'),
    
    path('nc_loan/', views.nc_loan, name='nc_loan'),
    
    path('nc_vendors/', views.nc_vendors, name='nc_vendors'),

    ######################ShowDeals#########################
    path('showDeals/',views.showDeals,name='showDeals'),
    path('handle_deal_action/',views.handle_deal_action, name='handle_deal_action'),
    
]