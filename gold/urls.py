from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    
    path('otp/', views.OTP, name='otp'),
    
    path('agreement/', views.agreement, name='agreement'),
    
    path('verify_agreement_otp/', views.verify_agreement_otp, name='verify_agreement_otp'),
    
    path('transaction_seprate/<str:number>/', views.transaction_seprate, name='transaction_seprate'),
    
    path('receipt_data/<str:number>/', views.receipt_data, name='receipt_data'),
    
    path('pdf_specific/', views.pdf_specific, name='pdf_specific'),

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
    
    path('user_nominee_details/', views.user_nominee_details, name='user_nominee_details'),
    
    path('check-account-status/<str:crn_no>/', views.check_account_status, name='check_account_status'),

    ######################ShowDeals#########################
    path('showDeals/',views.showDeals,name='showDeals'),
    
    path('handle_deal_action/',views.handle_deal_action, name='handle_deal_action'),
    
    path('chatbot/', views.chatbot, name='chatbot'),
    
    path('termcondition/', views.termcondition, name='termcondition'),
    
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    
    path('nominee_mandiates/<str:id>/', views.nominee_mandiates, name='nominee_mandiates'),
    
    path('deactivate/', views.deactivate, name='deactivate'),
    
    path('nach_response/', views.nach_response, name='nach_response'),

    path('nach_form/', views.nach_form, name='nach_form'),
    
    path('deactivates/<str:id>/', views.deactivates, name='deactivates'),
    
    path('plan/', views.GPlan, name='plan'),
    
    path('agreement_otp/<str:id>/', views.agreement_otp, name='agreement_otp'),
    
    path('deposite_agreement/', views.deposite_agreement, name='deposite_agreement'),
    
    path('verify_deposite_agreement_otp/', views.verify_deposite_agreement_otp, name='verify_deposite_agreement_otp'),
    
    path('deposite_agreement_otp/<str:id>/', views.deposite_agreement_otp, name='deposite_agreement_otp'),
    # path('verify_agreement_otp/', views.verify_agreement_otp, name='verify_agreement_otp'),
    
    path('payment/', views.payment, name='payment'), 
    
    # path('regular_payment/<str:id>/', views.regular_payment, name='regular_payment'), 
    
        # AFTER (no parameter)
    path('regular_payment/', views.regular_payment, name='regular_payment'),
    
    path('installment_op/', views.installment_op, name='installment_op'), 
    
    path('payment_status/<str:id>/', views.payment_status, name='payment_status'),
]