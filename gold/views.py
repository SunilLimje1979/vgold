from django.http import HttpResponse
import requests
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
###################################### Log in #############################################
def Login(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        response = requests.get("https://www.vgold.co.in/dashboard/webservices/webappversion.php", headers=headers)
        response.raise_for_status()
        
        # Parse the JSON response
        appversion = response.json()
        
        # Extract the 'appVersionJson' value
        serverappversion = appversion['appVersionJson']
        
        # Print the extracted version
        print(serverappversion)
        
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the API: {str(e)}")

    if request.method == 'POST':
        mobile_number = request.POST.get('mobileNumber')
        
        api_url = "https://www.vgold.co.in/dashboard/webservices/login.php"
        payload = {'email': mobile_number}  # Assuming the API expects the mobile number as email
        
        try:
            response = requests.post(api_url, data=payload, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            
            data = response.json()
            if data.get("status") == "200":
                request.session['mobile_number'] = mobile_number
                return redirect('otp')
            else:
                messages.error(request, "This mobile number is not registered with VGold. Please contact the support team.")
                return render(request, 'gold/login.html')
        
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Failed to connect to the API: {str(e)}")
            return render(request, 'gold/login.html')
    
    return render(request, 'gold/login.html' , {'serverappversion':serverappversion})


###################################### OTP #############################################
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

def OTP(request):
    if request.method == 'GET':
        mobile_number = request.session.get('mobile_number', '')
        context = {'mobile_number': mobile_number}
        return render(request, 'gold/otp.html', context)
    else:
        otp0 = request.POST.get('otp0', '')
        otp1 = request.POST.get('otp1', '')
        otp2 = request.POST.get('otp2', '')
        otp3 = request.POST.get('otp3', '')

        otp_combined = otp0 + otp1 + otp2 + otp3
        mobile_number = request.session.get('mobile_number', '')

        login_api_url = "https://www.vgold.co.in/dashboard/webservices/login.php"
        payload = {'email': mobile_number, 'otp': otp_combined}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = requests.post(login_api_url, data=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            # print (response.text)

            if data.get("status") == 200:
                # Store user data in session
                request.session['user_data'] = data

                # Make the second API call to get purchase rate
                purchase_rate_api_url = "https://www.vgold.co.in/dashboard/webservices/get_purchase_rate.php"
                purchase_rate_payload = {}  # Add any required parameters here
                purchase_rate_response = requests.post(purchase_rate_api_url, data=purchase_rate_payload, headers=headers)
                purchase_rate_response.raise_for_status()
                purchase_rate_data = purchase_rate_response.json()

                # Store purchase rate data in session
                request.session['purchase_rate_data'] = purchase_rate_data

                # Print session data for debugging
                # print(request.session['user_data'])
                # print(request.session['purchase_rate_data'])
                
                # Redirect to the dashboard
                return redirect('dashboard')
            else:
                return HttpResponse("Login Failed")
        
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to connect to the API: {str(e)}"
            return HttpResponse(error_message)


###################################### Registration #############################################
def Registration(request):
    return render(request, 'gold/registration.html')

###################################### Dashboard #############################################
def Dashboard(request):
    user_data = request.session.get('user_data')
    # print(user_data)
    
    if user_data and 'data' in user_data and len(user_data['data']) > 0:
        user_info = user_data['data'][0]
        first_name = user_info.get('First_Name', 'User')
        user_id = user_info.get('User_ID')
        context = {'first_name': first_name}
    else:
        context = {'first_name': 'User'}
        user_id = None
    
    if user_id:
        # API call to get total gold booking gain
        gold_gain_url = 'https://www.vgold.co.in/dashboard/webservices/total_gold_booking_gain.php'
        gold_post_data = {'user_id': user_id}
        gold_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        gold_response = requests.post(gold_gain_url, data=gold_post_data, headers=gold_headers)
        
        # Check if gold API call is successful
        if gold_response.status_code == 200:
            gold_api_response = gold_response.json()
            total_gain = gold_api_response['Data']['gain']
            context['total_gain'] = total_gain  # Add total gain to context
        else:
            print("Failed to fetch gold API data")
        
        # API call to get user loan eligibility
        loan_eligibility_url = 'https://www.vgold.co.in/dashboard/webservices/get_user_loan_eligiblity.php'
        loan_post_data = {'user_id': user_id}
        loan_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        loan_response = requests.post(loan_eligibility_url, data=loan_post_data, headers=loan_headers)
        
        # Check if loan API call is successful
        if loan_response.status_code == 200:
            loan_api_response = loan_response.json()
            # Extract loan amount from API response and add it to the context
            loan_amount = loan_api_response['data']['loan_amount']
            context['loan_amount'] = loan_amount
            
            request.session['loan_api_response'] = loan_api_response
        else:
            print("Failed to fetch loan API data")
    
    return render(request, 'gold/dashboard.html', context)

###################################### Loan #############################################

def Loan(request):
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    # print(user_data)
    user_id = user_data.get('data', [{}])[0].get('User_ID')
    First_Name = user_data.get('data', [{}])[0].get('First_Name')

    if not user_id:
        return HttpResponse("User ID not found in session data.")
    
    # Retrieve loan API response from session
    loan_api_response = request.session.get('loan_api_response')
    
    # Print the loan API response to verify it
    # print(loan_api_response)
    
    # Extract the loan amount from the loan API response
    loan_amount = None
    if loan_api_response and 'data' in loan_api_response:
        loan_amount = loan_api_response['data'].get('loan_amount')
    
    # If you need to pass the response to the template, prepare the context
    context = {
        'First_Name': First_Name,
        'loan_amount': loan_amount,
    }
    
    # Render the template with the context
    return render(request, 'gold/loan.html', context)

###################################### Withdraw #############################################

def Withdraw(request):
    return render(request, 'gold/withdraw.html')
###################################### Withdraw #############################################
def Sell_gold(request):
    return render(request, 'gold/sell_gold.html')
###################################### Add Gold #############################################
def Add_gold(request):
    if request.method == 'POST':
        gold_amount = request.POST.get('goldAmount')
        gold_weight = request.POST.get('goldWeight')
        payment_method = request.POST.get('depositor')
        bank_details = request.POST.get('bankDetails')
        transaction_id = request.POST.get('transactionId')
        cheque_number = request.POST.get('chequeNumber')

        # Retrieve purchase rate data from session
        purchase_rate_data = request.session.get('purchase_rate_data', {})
        gold_purchase_rate = purchase_rate_data.get('Gold_purchase_rate', 'N/A')

        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('data', [{}])[0].get('User_ID')

        if not user_id:
            return HttpResponse("User ID not found in session data.")

        # Prepare the data for the API request
        data = {
            'user_id': user_id,
            'gold': gold_weight,
            'amount': gold_amount,
            'payment_option': payment_method,
            'bank_details': bank_details,
            'tr_id': transaction_id,
            'cheque_no': cheque_number
        }

        # Set the headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Make the API call
        response = requests.post('https://www.vgold.co.in/dashboard/webservices/add_gold.php', data=data, headers=headers)

        # Handle the API response
        if response.status_code == 200:
            response_data = response.json()
            status = response_data.get('status')
            message = response_data.get('Message')
            if status == '200':
                messages.success(request, f"Form submitted successfully! {message}")
                return redirect('add_gold')  # Redirect to the same page to clear form fields
            else:
                return HttpResponse(f"Form submission failed! {message}")
        else:
            return HttpResponse("Form submission failed due to a network error.")
    else:
        # Retrieve purchase rate data from session
        purchase_rate_data = request.session.get('purchase_rate_data', {})
        gold_purchase_rate = purchase_rate_data.get('Gold_purchase_rate', 'N/A')

        context = {
            'gold_purchase_rate': gold_purchase_rate
        }

        return render(request, 'gold/add_gold.html', context)



###################################### Withdraw #############################################
def Gold_plan(request):
    return render(request, 'gold/gold_plan.html')

###################################### Our Vendors #############################################
def Our_vendors(request):
    return render(request, 'gold/our_vendors.html')

###################################### Gold Wallet #############################################

def Gold_wallet(request):
    return render(request, 'gold/gold_wallet.html')

###################################### Profile #############################################

def Profile(request):
    # Retrieve the user_data from the session
    user_data = request.session.get('user_data', {})
    user_info = user_data.get('data', [{}])[0]  # Access the first element in the data list

    # Print the user_data (for debugging purposes)
    print(user_info)

    # Pass the user_info to the template context
    context = {'user_info': user_info}

    return render(request, 'gold/profile.html', context)



###################################### Update Profile #############################################

def Update_profile(request):
    return render(request, 'gold/update_profile.html')

###################################### Certificate #############################################
import requests
from django.http import HttpResponse
from django.shortcuts import render

def Certificate(request):
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('data', [{}])[0].get('User_ID')

    if not user_id:
        return HttpResponse("User ID not found in session data.")
    
    # print(user_id)

    # Set the API URL
    api_url = "https://www.vgold.co.in/dashboard/vgold_accnt_certificate/get_certificate.php"

    # Set the headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Call the API
    response = requests.post(api_url, data={'userid': user_id}, headers=headers)
    # print(response.text)

    if response.status_code == 200:
        api_response = response.json()
        if api_response.get("status") == "400" and api_response.get("Message") == "sucess":
            image_path = api_response.get("image_path")
            download_image_path = api_response.get("download_image_path")
        else:
            return HttpResponse("Failed to fetch certificate data from the API.")
    else:
        return HttpResponse("Error occurred while calling the API.")

    context = {
        'image_path': image_path,
        'download_image_path': download_image_path
    }

    return render(request, 'gold/certificate.html', context)


###################################### Gold Booking History #############################################
def Gbooking_history(request):
    api_url = "https://www.vgold.co.in/dashboard/webservices/gold_booking_history.php"
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('data', [{}])[0].get('User_ID')

    if not user_id:
        return HttpResponse("User ID not found in session data.")
    
    payload = {'user_id': user_id}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.post(api_url, data=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "200":
            bookings = data.get("Data", [])
        else:
            bookings = []
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the API: {str(e)}")
        bookings = []

    # Ensure all fields are populated with a default value if missing
    for booking in bookings:
        booking['number'] = booking.get('gold_booking_id', "N/A")
        booking['account_status'] = booking.get('account_status', "0")  # Default to "0" for closed
        booking['today_gain'] = booking.get('todays_gain', "0")
        booking['paid_amount'] = booking.get('total_paid_amount1', "0")
        booking['monthly_installment'] = booking.get('monthly_installment', "N/A")  # Update with appropriate key if exists in API response
        booking['booking_date'] = booking.get('added_date', "N/A")
        booking['weight'] = booking.get('gold', "0 gm")
        booking['rate'] = booking.get('rate', "0")
        booking['value'] = booking.get('booking_amount', "0")
        booking['tenure'] = f"{booking.get('tennure', '0')} Month"
        booking['booking_amount'] = booking.get('down_payment', "0")
        booking['booking_charge'] = booking.get('booking_charge', "0")
        booking['balance_amount'] = booking.get('total_balance_amount', "0")
        booking['closing_date'] = booking.get('closing_date', "N/A")

    return render(request, 'gold/gbooking_history.html', {'bookings': bookings})



def BookingReceipt(request):
    user_data = request.session.get('user_data')
    if user_data and 'data' in user_data and len(user_data['data']) > 0:
        user_id = user_data['data'][0].get('User_ID', 'User')
    else:
        user_id = None  
        
    if request.method == "POST":
        number = request.POST.get('number')
        if user_id:
            # Prepare data to post to the API
            data = {
                'bid': number,
                'user_id': user_id
            }
            # print(data)
            
            # pdf_link = f"https://www.vgold.co.in/dashboard/user/module/goldbooking/booking_receipt.php?bid={number}&user_id={user_id}"
            
            # response = HttpResponse(pdf_link, content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="booking_receipt.pdf"'
            
            # return response
            
            link = f"https://www.vgold.co.in/dashboard/user/module/goldbooking/booking_receipt.php?bid={number}&user_id={user_id}"
            
            return JsonResponse({'link' : link})

    #         # Make a POST request to the API
    #         response = requests.post('https://www.vgold.co.in/dashboard/user/module/goldbooking/booking_receipt.php', data=data)

    #         # Check if the request was successful
    #         if response.status_code == 200:
    #             # Check if response content type is PDF
    #             if 'application/pdf' in response.headers.get('Content-Type', ''):
    #                 # Set response headers to force download
    #                 response['Content-Disposition'] = 'attachment; filename="booking_receipt.pdf"'
    #                 hello=response['Content-Disposition'] 
                    
    #                 return JsonResponse({"hello" : hello})
    #             else:
    #                 return HttpResponse("Unexpected response content. Unable to download PDF.")
    #         else:
    #             # Handle errors appropriately
    #             return HttpResponse("Failed to post data to the API.")

    # return HttpResponse("GET request received. No action taken.")

###################################### Gold Boking #############################################
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def Gold_booking(request):
    
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('data', [{}])[0].get('User_ID')

    if not user_id:
        return HttpResponse("User ID not found in session data.")
        
    if request.method == "POST":
        gold_in_gm = request.POST.get('quantity')
        tenure = request.POST.get('tensure')
        promo_code = request.POST.get('inputField')
        
        # Prepare the data to be sent to the API
        data = {
            'quantity': gold_in_gm,
            'tennure': tenure,
            'pc': promo_code,
            'user_id': user_id
        }

        # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            # Send a POST request to the API endpoint
            response = requests.post('https://www.vgold.co.in/dashboard/webservices/booking_details.php', data=data, headers=headers)
            response.raise_for_status()

            # Check the API response status
            response_data = response.json()
            if response_data.get("status") == "200":
                # Print the response data
                # print("API Response:", response_data)
                
                request.session['api_response'] = response_data
                
                print("API Response:", request.session['api_response'])
                # Redirect to the booking details page
                return redirect('booking_details')
            else:
                # Handle the case where the status is not 200
                error_message = response_data.get("Message", "An error occurred")
                print("API Error:", error_message)
                return render(request, 'gold/gold_booking.html', {'error_message': error_message})
        except requests.exceptions.RequestException as e:
            error_message = f"Failed to connect to the API: {str(e)}"
            print(error_message)
            return render(request, 'gold/gold_booking.html', {'error_message': error_message})

    return render(request, 'gold/gold_booking.html')

######################################Booking Details #############################################
   
from django.shortcuts import render
from django.http import HttpResponse

def Booking_details(request):
    if request.method == 'GET':
        # Retrieve the API response from the session
        api_response = request.session.get('api_response')
        print(api_response)

        if api_response:
            # Render the template with API response data
            return render(request, 'gold/booking_details.html', {'api_response': api_response})
        else:
            return HttpResponse("No API response found in session.", status=404)

    elif request.method == 'POST':
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('data', [{}])[0].get('User_ID')
        # Retrieve form data
        payment_option = request.POST.get('dropdown2')
        bank_details = request.POST.get('bankDetails')
        tr_id = request.POST.get('transactionId')
        cheque_no = request.POST.get('chequeNo')
        
        # # Dynamically set the label for additional information based on payment option
        # additional_info_label = "Cheque No" if payment_option == 'cheque' else "Transaction ID"
        # additional_info = request.POST.get('chequeNo') if payment_option == 'cheque' else request.POST.get('transactionId')
        
        # Retrieve the API response from POST data and parse it
        api_response = request.POST.get('api_response')
        if api_response:
            api_response = eval(api_response)  # Convert string representation of dict to dict

        # Retrieve additional form data

        # Ensure the API response has the necessary fields
        booking_value = api_response.get('Booking_value')
        gold_rate = api_response.get('Gold_rate')
        down_payment = api_response.get('Down_payment')
        booking_charges_discount = api_response.get('Booking_charges_discount')
        monthly = api_response.get('Monthly')
        pc = api_response.get('pc')
        Initial_Booking_charges = api_response.get('Initial_Booking_charges')
        Booking_charges = api_response.get('Booking_charges')
        
        
        payload={
            "user_id":user_id,
            "booking_value":booking_value,
            "down_payment" :down_payment,
            "monthly":monthly,
            "rate":gold_rate,
            "pc":pc,
            # "gold_weight":gold_weight, 
            # "tennure":tennure,
            "payment_option":payment_option,
            "bank_details":bank_details,
            "cheque_no" :cheque_no,
            "tr_id":tr_id,
            "initial_booking_charges":Initial_Booking_charges,
            "booking_charges_discount":booking_charges_discount,
            "booking_charges":Booking_charges,
            "confirmed":0                  
        }
        
        
         # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        res=requests.post("https://www.vgold.co.in/dashboard/webservices/gold_booking.php", data= payload ,headers=headers)
        print(res.text)
        
        if res.json().get('status') == '200':
            messages.success(request, res.json().get('Message'))             
        else:
            messages.error(request, res.json().get('Message'))
       
        return redirect(Booking_details)
       
    else:
        return HttpResponse("Invalid request method.", status=405)


###################################### Gold Deposite History #############################################
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

###################################### Gold Deposite #############################################
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

from django.shortcuts import render
from django.http import HttpResponse

def Add_bank(request):
    if request.method == "POST":
        bank_name = request.POST.get('bankName')
        branch = request.POST.get('branch')
        account_number = request.POST.get('accountNumber')
        account_type = request.POST.get('accountType')
        ifsc_code = request.POST.get('ifscCode')
        account_holder = request.POST.get('accountHolder')

        # Print the received data
        print("Bank Name:", bank_name)
        print("Branch:", branch)
        print("Account Number:", account_number)
        print("Account Type:", account_type)
        print("IFSC Code:", ifsc_code)
        print("Account Holder:", account_holder)

        # Here, you can process the data further, save it to the database, etc.

        return HttpResponse("Form submitted successfully!")

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
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('data', [{}])[0].get('User_ID')

    if not user_id:
        return HttpResponse("User ID not found in session data.")
    
    if request.method == 'POST':
        # Retrieve form data
        enterName = request.POST.get('enterName', '')
        enter_email = request.POST.get('enter_email', '')
        enter_mobileno = request.POST.get('enter_mobileno', '')

        # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Make the POST request to the external API
        api_url = 'https://www.vgold.co.in/dashboard/webservices/send_refer_link.php'
        payload = {
            'user_id': user_id,
            'name': enterName,
            'email': enter_email,
            'mobile_no': enter_mobileno
        }
        
        try:
            response = requests.post(api_url, data=payload, headers=headers)
            # Ensure response content is not empty
            if response.content:
                try:
                    response_data = response.json()
                    # print(response_data)
                    
                    if response_data.get('status') == '200':
                        messages.success(request, "Refer link sent successfully.")
    
                      
                    else:
                        messages.error(request, "Failed to send refer link.")
                    
                    return redirect(Refer)
                except ValueError:
                    message = "Received invalid JSON response."
            else:
                message = "Received empty response from the API."
        except requests.exceptions.RequestException as e:
            message = f"An error occurred while making the request: {e}"
        
        return HttpResponse(message)

    return render(request, 'gold/refer.html')


