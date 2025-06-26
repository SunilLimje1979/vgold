from django.http import HttpResponse
import requests
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.decorators import api_view

###################################### Log in #############################################
# def Login(request):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }

#     # Fetch the app version
#     try:
#         response = requests.get("https://www.vgold.co.in/dashboard/webservices/webappversion.php", headers=headers)
#         response.raise_for_status()
        
#         # Parse the JSON response and extract app version
#         appversion = response.json()
#         serverappversion = appversion.get('appVersionJson', None)
        
#     except requests.exceptions.RequestException as e:
#         messages.error(request, f"Failed to retrieve app version: {str(e)}")
#         serverappversion = None  # Default value in case of failure

#     # Handle POST login request
#     if request.method == 'POST':
#         username = request.POST.get('mobileNumber')
#         password = request.POST.get('password')
        
#         api_url = "https://vgold.app/vgold_admin/m_api/m_login/"
#         payload = {'username': username, 'password': password}

#         try:
#             response = requests.post(api_url, data=payload)
#             response.raise_for_status()  # Raise an error for HTTP issues
            
#             data = response.json()

#             # Check if login was successful (status == "1000")
#             if data.get("message_code") == 1000:
#                 user_data = data.get("message_data", {})
#                 # Store user_data in session
#                 request.session['user_data'] = user_data
#                 request.session['user_mobile'] = user_data.get('UserMobileNo')
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, data.get("message_text", "Login failed. Please try again."))
#                 return render(request, 'gold/login.html', {'serverappversion': serverappversion})

#         except requests.exceptions.RequestException as e:
#             messages.error(request, f"Failed to connect to the API: {str(e)}")
#             return render(request, 'gold/login.html', {'serverappversion': serverappversion})

#     return render(request, 'gold/login.html', {'serverappversion': serverappversion})

# def Login(request):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }
    
#         # Fetch the app version
#     try:
#         response = requests.get("https://www.vgold.co.in/dashboard/webservices/webappversion.php", headers=headers)
#         response.raise_for_status()
        
#         # Parse the JSON response and extract app version
#         appversion = response.json()
#         serverappversion = appversion.get('appVersionJson', None)
        
#     except requests.exceptions.RequestException as e:
#         messages.error(request, f"Failed to retrieve app version: {str(e)}")
#         serverappversion = None  # Default value in case of failure

#     if request.method == 'POST':
#         step = request.POST.get('step')
        
#         # Step 1: Send OTP
#         if step == 'send_otp':
#             mobile_number = request.POST.get('mobileNumber')
            
#             if mobile_number in ['9657965188', '9881136531', '9763583584', '8087699949']:
#                 request.session['otp_data'] = {'otp':9999,'mobile_no':mobile_number}
#                 mobile_number = mobile_number # Get mobile number from message_data

#                  # messages.success(request, "OTP sent successfully to your mobile number.")
#                 return render(request, 'gold/logiin.html', {'show_otp_form': True, 'mobile_number': mobile_number, 'step': 'verify_otp','serverappversion': serverappversion})
#             else:    
            
#                 api_url = "https://vgold.app/vgold_admin/m_api/login_verify/"
#                 payload = {"mobileno": mobile_number}

#                 try:
#                     response = requests.post(api_url, json=payload)
#                     response.raise_for_status()
#                     data = response.json()

#                     if data.get('message_code') == 1000:  # OTP generated successfully
#                         # Store OTP data in session
#                         request.session['otp_data'] = data['message_data']
#                         mobile_number = data['message_data'].get('mobile_no', '')  # Get mobile number from message_data

#                         # messages.success(request, "OTP sent successfully to your mobile number.")
#                         return render(request, 'gold/logiin.html', {'show_otp_form': True, 'mobile_number': mobile_number, 'step': 'verify_otp','serverappversion': serverappversion})
#                     else:
#                         messages.error(request, data.get('message_text', 'Failed to generate OTP.'))

#                 except requests.exceptions.RequestException as e:
#                     messages.error(request, f"Error communicating with API: {str(e)}")
#                     return redirect('login')

#         elif step == 'verify_otp':
#             # Fetch OTP from the form and session data
#             user_otp = request.POST.get('otp')
#             session_data = request.session.get('otp_data')
#             mobile_number = session_data.get('mobile_no') if session_data else ''  
#             # print(user_otp)
#             # print(mobile_number)
            
#             # Validate the OTP
#             # if user_otp and user_otp == str(session_data.get('otp')):  # Comparing OTP from user input with the one from API response
#             if user_otp:
#                 # OTP matches, call the external API to verify OTP
#                 api_url = "https://vgold.app/vgold_admin/m_api/verifyotp/"
#                 payload = {
#                     "mobileno": mobile_number,
#                     "otp": user_otp
#                 }
#                 try:
#                     response = requests.post(api_url, data=payload)
#                     response_data = response.json()
#                     # print(response.text)

#                     if response_data.get('message_code') == 1000:
#                         user_data = response_data.get("message_data", {})  # Fetching from response_data, not data
#                         request.session['user_data'] = user_data
#                         request.session['user_mobile'] = user_data.get('UserMobileNo') 
#                         request.session['flag']=True
#                         # messages.success(request, "Login successful.")
#                         return redirect('dashboard')
#                     else:
#                         # OTP verification failed, show error message
#                         messages.error(request, "Incorrect OTP. Please try again.")
#                         return redirect('login')  # Replace with your OTP verification page URL
#                 except requests.exceptions.RequestException as e:
#                     messages.error(request, f"Error communicating with API: {str(e)}")
#                     return redirect('login')

#             else:
#                 # OTP does not match, show error message
#                 messages.error(request, "Invalid OTP. Please try again.")
#                 return redirect('login')  # Replace with your OTP verification page URL

#     source = request.GET.get('source',None)
#     # print(request.GET)
#     print(source)
#     if(source):
#         request.session['source']=source
        
#     return render(request, 'gold/logiin.html',{'serverappversion': serverappversion,'source':source})

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
        appversion = response.json()
        serverappversion = appversion.get('appVersionJson', None)
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Failed to retrieve app version: {str(e)}")
        serverappversion = None
    
    source = request.GET.get('source', None)
    if source:
        request.session['source'] = source
    else:
        source = request.session.get('source', None)
    
    if request.method == 'POST':
        step = request.POST.get('step')
        
        if step == 'send_otp':
            mobile_number = request.POST.get('mobileNumber')
            
            if mobile_number in ['9657965188', '9881136531', '9763583584', '8087699949','9850180648','8600672101']:
                request.session['otp_data'] = {'otp': 9999, 'mobile_no': mobile_number}
                return render(request, 'gold/logiin.html', {
                    'show_otp_form': True,'mobile_number': mobile_number,'step': 'verify_otp','serverappversion': serverappversion,'source': source
                })
            else:
                api_url = "https://vgold.app/vgold_admin/m_api/login_verify/"
                # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/login_verify/"
                
                payload = {"mobileno": mobile_number}
                
                try:
                    response = requests.post(api_url, json=payload)
                    response.raise_for_status()
                    data = response.json()
                    
                    if data.get('message_code') == 1000:
                        request.session['otp_data'] = data['message_data']
                        mobile_number = data['message_data'].get('mobile_no', '')
                        return render(request, 'gold/logiin.html', {
                            'show_otp_form': True,
                            'mobile_number': mobile_number,
                            'step': 'verify_otp',
                            'serverappversion': serverappversion,
                            'source': source
                        })
                    else:
                        messages.error(request, data.get('message_text', 'Failed to generate OTP.'))
                except requests.exceptions.RequestException as e:
                    messages.error(request, f"Error communicating with API: {str(e)}")
                    return redirect('login')
        
        elif step == 'verify_otp':
            user_otp = request.POST.get('otp')
            session_data = request.session.get('otp_data')
            mobile_number = session_data.get('mobile_no') if session_data else ''
            
            if user_otp:
                api_url = "https://vgold.app/vgold_admin/m_api/verifyotp/"
                payload = {
                    "mobileno": mobile_number,
                    "otp": user_otp
                }
                try:
                    response = requests.post(api_url, data=payload)
                    response_data = response.json()
                    
                    if response_data.get('message_code') == 1000:
                        user_data = response_data.get("message_data", {})
                        request.session['user_data'] = user_data
                        request.session['user_mobile'] = user_data.get('UserMobileNo')
                        request.session['flag'] = True

                        # 🔻 Fetch gold rate and store in session
                        try:
                            gold_rate_response = requests.post("https://vgold.app/vgold_admin/m_api/get_gold_rate/")
                            gold_rate_response.raise_for_status()
                            gold_rate_data = gold_rate_response.json()

                            if gold_rate_data.get('message_code') == 1000:
                                request.session['gold_rate_data'] = gold_rate_data.get('message_data', {})
                        except requests.exceptions.RequestException as e:
                            messages.warning(request, f"Gold rate fetch failed: {str(e)}")
                            request.session['gold_rate_data'] = {}

                        return redirect('dashboard')
                    else:
                        messages.error(request, "Incorrect OTP. Please try again.")
                        return redirect('login')
                except requests.exceptions.RequestException as e:
                    messages.error(request, f"Error communicating with API: {str(e)}")
                    return redirect('login')
            else:
                messages.error(request, "Invalid OTP. Please try again.")
                return redirect('login')

    
    return render(request, 'gold/logiin.html', {'serverappversion': serverappversion,'source': source})

###################################### Verify Mobile No ##################################################


###################################### OTP #############################################

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
import hashlib
from cryptography.fernet import Fernet
import base64
from django.shortcuts import render, redirect

# Convert the given key to a valid Fernet key
key_val = "k2hLr4X0ozNyZByj5DT66edtCEee1x+6"
key_bytes = base64.urlsafe_b64encode(key_val.encode()[:32])
cipher = Fernet(key_bytes)

# Function to encrypt data
def encrypt_data(data):
    if data is None:
        return ''
    return cipher.encrypt(data.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data.encode()).decode()

def Registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        pancard_number = request.POST.get('pancard_number')
        aadhar_number = request.POST.get('aadhar_number')
        address = request.POST.get('address')
        refer_code = request.POST.get('refer_code')
        dob = request.POST.get('dob')
        
        payload = {
            "first": encrypt_data(first_name),
            "middle": encrypt_data(middle_name),
            "last": encrypt_data(last_name),
            "email": encrypt_data(email),
            "no": encrypt_data(mobile_no),
            "pancard": encrypt_data(pancard_number),
            "aadhar_number": encrypt_data(aadhar_number),
            "refer_code": encrypt_data(refer_code),
            "address": encrypt_data(address),
            "dob": encrypt_data(dob),
        }
        print(payload)
        

        api_url="https://vgold.app/vgold_admin/m_api/register_user/"
        # api_url="http://127.0.0.1:8000/vgold_admin/m_api/register_user/"
        
        try:
            response = requests.post(api_url, json=payload)  # Use params parameter
            if response.content:
                try:
                    response_data = response.json()
                    
                    if response_data.get('message_code') == 1000:
                        messages.success(request, "User registration successful")
                    else:
                        messages.error(request, response_data.get('Message', 'Something went wrong or filed missing.'))
                        
                    return redirect(Registration)  # Assuming 'Registration' is the URL name
                except ValueError:
                    messages.error(request, "Received invalid JSON response.")
            else:
                messages.error(request, "Received empty response from the API.")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"An error occurred while making the request: {e}")

        return redirect(Registration)
    
    return render(request, 'gold/registration.html')

###################################### Dashboard #############################################
def Dashboard(request):
    # Retrieve user data from the session
    user_data = request.session.get('user_data')
    
    if user_data and isinstance(user_data, dict):
        # Extract the user's first name and user id from the dictionary
        first_name = user_data.get('UserFirstname', 'User')  # Get the user's first name
        user_id = user_data.get('User_Id')  # Get the user's ID
        
        # Pass the first name into the context for rendering
        # context = {'first_name': first_name}
        context = {
            'first_name': first_name,
            'user_id': user_id
        }
    else:
        # Default values if no user data is found
        # context = {'first_name': 'User'}
        context = {
            'first_name': "User",
            'user_id': 404
        }
        return redirect('login') 

    if user_id:
        # **Initialize loan_api_response to avoid UnboundLocalError**
        loan_api_response = {}

        # **New API endpoint for total gold booking gain**
        gold_gain_url = 'https://vgold.app/vgold_admin/m_api/total_gain/'
        gold_post_data = {'user_id': user_id}

        try:
            gold_response = requests.post(gold_gain_url, json=gold_post_data)
            gold_response_data = gold_response.json()

            # Check if gold API call is successful
            if gold_response_data.get('message_code') == 1000:
                context['total_gain'] = gold_response_data['message_data'].get('total_gain_all_bookings', 0)
            else:
                context['total_gain'] = 0
        except requests.RequestException:
            context['total_gain'] = 0

        # **API call to get user loan eligibility**
        loan_eligibility_url = 'https://vgold.app/vgold_admin/m_api/check_loan_eligibility/'
        loan_post_data = {'user_id': user_id}

        try:
            loan_response = requests.post(loan_eligibility_url, json=loan_post_data)
            if loan_response.status_code == 200:
                loan_api_response = loan_response.json()
                if loan_api_response.get('message_code') == 1000 and loan_api_response.get('message_data', {}).get('is_eligible'):
                    loan_amount = loan_api_response['message_data'].get('net_amount_85_percent', 0)
                else:
                    loan_amount = 0
            else:
                loan_amount = 0
        except requests.RequestException:
            loan_amount = 0

        # Add loan amount to the context
        context['loan_amount'] = loan_amount
        request.session['loan_api_response'] = loan_api_response

        # **NEW API: Get Pending Agreement List**
        if request.session['flag']:
            request.session['flag']=False
            agreement_url = 'https://vgold.app/vgold_admin/m_api/get_pending_agreement_list/'
            agreement_post_data = {'GBUserId': user_id}

            try:
                agreement_response = requests.post(agreement_url, json=agreement_post_data)
                if agreement_response.status_code == 200:
                    agreement_api_response = agreement_response.json()
                    if agreement_api_response.get('message_code') == 1000:
                        context['pending_agreements'] = agreement_api_response.get('message_data', [])
                    else:
                        context['pending_agreements'] = []
                else:
                    context['pending_agreements'] = []
            except requests.RequestException:
                context['pending_agreements'] = []

    return render(request, 'gold/dashboard.html', context)

###################################### Loan #############################################

# def Loan(request):
#     if request.method=='GET':
#         # Retrieve user data from session
#         user_data = request.session.get('user_data', {})
#         # print(user_data)
#         user_id = user_data.get('data', [{}])[0].get('User_ID')
#         First_Name = user_data.get('data', [{}])[0].get('First_Name')

#         if not user_id:
#             return HttpResponse("User ID not found in session data.")
        
#         # Retrieve loan API response from session
#         loan_api_response = request.session.get('loan_api_response')
        
#         # Print the loan API response to verify it
#         # print(loan_api_response)
        
#         # Extract the loan amount from the loan API response
#         loan_amount = None
#         if loan_api_response and 'data' in loan_api_response:
#             loan_amount = loan_api_response['data'].get('loan_amount')
        
#         # If you need to pass the response to the template, prepare the context
#         context = {
#             'First_Name': First_Name,
#             'loan_amount': loan_amount,
#         }
        
#         # Render the template with the context
#         return render(request, 'gold/loan.html', context)
    
#     else:
#         user_data = request.session.get('user_data', {})
#         user_id = user_data.get('data', [{}])[0].get('User_ID')

#         if not user_id:
#             return HttpResponse("User ID not found in session data.")
        
        
#         amount = request.POST.get('goldWeight')
#         comment = request.POST.get('depositor')
        
#         payload = {
#             "user_id": user_id,
#             "amount": amount,
#             "comment": comment  
#         }

#         print("Payload:", payload)

#         # return HttpResponse("Data")
#         return redirect(Loan)
    
def Loan(request):
    if request.method == 'GET':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')

        if not user_id:
            return redirect('login')

        # Call the new API
        api_url = 'https://vgold.app/vgold_admin/m_api/check_loan_eligibility/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/json'  # Ensure JSON content type
        }
        api_data = {
            "user_id": user_id
        }

        try:
            response = requests.post(api_url, headers=headers, json=api_data)
            response.raise_for_status()  # Raise exception for HTTP errors
            loan_api_response = response.json()

            # Extract the required fields from the API response
            message_text = None
            if loan_api_response and 'message_code' in loan_api_response and loan_api_response['message_code'] == 1000:
                message_text = loan_api_response.get('message_text', "You are not eligible for a loan.")

        except requests.exceptions.RequestException as e:
            message_text = "Error retrieving loan eligibility data."

        # Prepare context
        context = {
            'message_text': message_text
        }

        # Render the template
        return render(request, 'gold/loan.html', context)

    if request.method == 'POST':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')

        if not user_id:
            return redirect('login')

        # Get form data
        amount = request.POST.get('goldWeight')
        comment = request.POST.get('depositor')

        if not amount:
            messages.error(request, 'Amount is required.')
            return redirect('loan')

        # API request
        # api_url = 'http://127.0.0.1:8000/vgold_admin/m_api/loan_request/'
        api_url = 'https://vgold.app/vgold_admin/m_api/loan_request/'
        payload = {"LRUserId": user_id, "LRAmount": amount, "LRComment": comment}

        try:
            response = requests.post(api_url, json=payload)
            api_response = response.json() if response.status_code == 200 else {}

            if api_response.get('message_code') == 1000:
                request.session['loan_api_response'] = api_response.get('message_data')
                messages.success(request, api_response.get('message_text'))
            else:
                messages.error(request, api_response.get('message_text', 'An error occurred.'))
        except requests.exceptions.RequestException:
            messages.error(request, "Failed to connect to the server.")

        return redirect('loan')
    else:
        messages.success(request, api_response.get('message_text'))
        return redirect('dashboard') 

###################################### Withdraw #############################################

def Withdraw(request):
    if request.method == 'GET':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')

        if not user_id:
            return redirect('login') 

        # API URL and data for wallet balance
        # wallet_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_wallet_balances/"
        wallet_api_url = "https://vgold.app/vgold_admin/m_api/get_wallet_balances/"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        wallet_payload = {
            "user_id": user_id
        }

        try:
            # Make a POST request to get wallet balance
            wallet_response = requests.post(wallet_api_url, json=wallet_payload, headers=headers)
            wallet_response_data = wallet_response.json()

            if wallet_response_data['message_code'] == 1000:
                wallet_balance = wallet_response_data['message_data'].get('GoldWalletBalance', 0.0)
                return render(request, 'gold/withdraw.html', {'wallet_balance': wallet_balance})
            else:
                return HttpResponse(f"API Error: {wallet_response_data.get('message_text', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Failed to connect to the API: {e}")
    
    elif request.method == 'POST':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        # user_id = user_data.get('data', [{}])[0].get('User_ID')
        user_id = user_data.get('User_Id')  #

        if not user_id:
            return HttpResponse("User ID not found in session data.")
        
        amount = request.POST.get('bankName')  # Adjust to match your form field names
        comment = request.POST.get('comment')
        
        # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/json',  # Specify content type as JSON
        }
        
        api_url = "https://www.vgold.co.in/dashboard/webservices/add_withdraw_request.php"
        
        # Data to be sent as JSON
        data = {
            "user_id": user_id,
            "amount": amount,
            "comment": comment
        }
        
        # print(data)
        
        try:
            response = requests.post(api_url, json=data, headers=headers)
            # print(response.text)
            
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('status') == '200':
                    messages.success(request, "Request for withdraw amount has been sent successfully.")
                else:
                    messages.error(request, response_data.get('Message', 'An error occurred.'))
            else:
                messages.error(request, f"Failed to connect to the API. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"An error occurred while making the request: {e}")
        
        return redirect('withdraw')  # Redirect back to the withdraw page
    
    return render(request, 'gold/withdraw.html')
   
###################################### Withdraw #############################################

def Sell_gold(request):
    if request.method == 'GET':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')  #

        if not user_id:
            return redirect('login') 

        # First API endpoint and headers for getting gold wallet balance
        # wallet_url = 'http://127.0.0.1:8000/vgold_admin/m_api/get_wallet_balances/'
        wallet_url = 'https://vgold.app/vgold_admin/m_api/get_wallet_balances/'
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        wallet_data = {'user_id':994 }

        # Fetch gold sale rate from session
        gold_rate_data = request.session.get('gold_rate_data', {})
        gold_sale_rate = gold_rate_data.get('Gold_sale_rate', 'N/A')

        try:
            # Fetch gold wallet balance data
            response_wallet = requests.post(wallet_url, json=wallet_data, headers=headers)
            wallet_response_data = response_wallet.json()

            # Check if API request was successful
            if wallet_response_data.get('message_code') == 1000:
                gold_balance = wallet_response_data['message_data'].get('GoldWalletBalance', 'N/A')
                # Render your template with the retrieved data
                return render(request, 'gold/sell_gold.html', {'gold_balance': gold_balance, 'gold_sale_rate': gold_sale_rate})
            else:
                return HttpResponse(f"Failed to fetch data: {wallet_response_data.get('message_text', 'Unknown error')}")

        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error: {str(e)}")
        
    elif request.method == 'POST':
        # Handle POST request data
        gold_weight = request.POST.get('gold_weight')
        gold_amount = request.POST.get('gold_amount')

        # Print the posted data for demonstration
        print(f"Gold Weight: {gold_weight}")
        print(f"Gold Amount: {gold_amount}")

        # Return a response or redirect as necessary
        return redirect(Sell_gold)

    return HttpResponse("Unsupported HTTP method.")

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
        user_id = user_data.get('User_Id')  #

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



###################################### Gold Plan #############################################
def Gold_plan(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')

        # Set the headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Make the API request
        api_url = "https://vgold.app/vgold_admin/m_api/get_gold_plans/"
        response = requests.post(api_url, data={'quantity': quantity}, headers=headers)
        
        # Check if the API request was successful
        if response.status_code == 200:
            api_response = response.json()
            if api_response.get("status") == "200":
                data = api_response.get("Data", {})
                # Pass the API response data to the template
                return render(request, 'gold/gold_plan.html', {'data': data})
            else:
                # Handle the case where the API response status is not 200
                return render(request, 'gold/gold_plan.html', {'error': api_response.get("Message")})
        else:
            # Handle the case where the API request failed
            return render(request, 'gold/gold_plan.html', {'error': 'Failed to retrieve gold plan data'})
    
    # For GET requests, just render the template without any data
    return render(request, 'gold/gold_plan.html')

###################################### Our Vendors #############################################

def Our_vendors(request):
    # URL of the API
    api_url = "https://www.vgold.co.in/dashboard/webservices/vendor_upload.php"

    # Set the headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a GET request to the API with headers
    response = requests.get(api_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if data['status'] == '200':
            # Extract vendor details and prepend the base URL
            base_url = "https://www.vgold.co.in"
            vendors = [
                {
                    'vendor_id': vendor['vendor_id'],
                    'logo_path': base_url + vendor['logo_path'],
                    'letter_path': base_url + vendor['letter_path'],
                    'advertisement_path': base_url + vendor['advertisement_path']
                }
                for vendor in data['Data']
            ]
        else:
            vendors = []
    else:
        vendors = []

    context = {
        'vendors': vendors,
    }
    return render(request, 'gold/our_vendors.html', context)

###################################### Image Specific #############################################

from django.shortcuts import render

def Imagespecific(request):
    # Get the vendor_id and logo_path from the query parameters
    vendor_id = request.GET.get('vendor_id', None)
    logo_path = request.GET.get('logo_path', None)
    
    context={'vendor_id': vendor_id, 'logo_path': logo_path}
    # print(context)
   
    return render(request, 'gold/imagespecific.html',context)


###################################### Gold Wallet #############################################

def Gold_wallet(request):
    # Retrieve gold rate data from session
    gold_rate_data = request.session.get('gold_rate_data', {})
    gold_purchase_rate = gold_rate_data.get('Gold_purchase_rate', 'N/A')
    
    print(gold_purchase_rate)

    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')

    if not user_id:
        return redirect('login')

    # API endpoint for wallet balance
    # wallet_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_wallet_balances/"
    wallet_api_url = "https://vgold.app/vgold_admin/m_api/get_wallet_balances/"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    wallet_payload = {
        "user_id": user_id
    }

    try:
        # API request to get wallet balance
        wallet_response = requests.post(wallet_api_url, json=wallet_payload, headers=headers)
        wallet_response_data = wallet_response.json()

        if wallet_response_data['message_code'] == 1000:
            gold_balance = wallet_response_data['message_data'].get('GoldWalletBalance', 0.0)
        else:
            return HttpResponse(f"Error: {wallet_response_data.get('message_text', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"API request failed: {e}")

    # API endpoint for transactions
    # transactions_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_gw_transection/"
    transactions_api_url = "https://vgold.app/vgold_admin/m_api/get_gw_transection/"
    transactions_payload = {
        "user_id": user_id
    }
    # transactions_payload = {
    #     "user_id": 491
    # }


    try:
        # API request to get transaction data
        transactions_response = requests.post(transactions_api_url, json=transactions_payload, headers=headers)
        transactions_response_data = transactions_response.json()

        if transactions_response_data['message_code'] == 1000:
            transactions = transactions_response_data['message_data']
        else:
            return HttpResponse(f"Error: {transactions_response_data.get('message_text', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"API request failed: {e}")

    context = {
        'gold_purchase_rate': gold_purchase_rate,
        'gold_balance': gold_balance,
        'transactions': transactions,
    }

    return render(request, 'gold/gold_wallet.html', context)
###################################### Profile #############################################

def Profile(request):
    # Retrieve the user_data from the session
    user_data = request.session.get('user_data', {})
    print(user_data)
    user_info = user_data  # Access the first element in the data list

    # Print the user_data (for debugging purposes)
    # print(user_info)

    # Pass the user_info to the template context
    context = {'user_info': user_info}

    return render(request, 'gold/profile.html', context)



###################################### Update Profile #############################################
from django.shortcuts import render, redirect
from django.urls import reverse

def Update_profile(request):
    if request.method == 'GET':
        user_data = request.session.get('user_data', {})
        user_info = user_data
        context = {'user_info': user_info}
        return render(request, 'gold/update_profile.html', context)

    elif request.method == 'POST':
        # Retrieve user data from session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')
        
        input_email = request.POST.get('inputEmail')
        input_mobile = request.POST.get('inputMobile')
        input_address = request.POST.get('inputAddress')
        # input_city = request.POST.get('inputCity')
        # input_state = request.POST.get('inputState')
        input_adhar = request.POST.get('inputAdhar')
        input_pan = request.POST.get('inputPan')
       
        payload={
            "User_Id":user_id,
            "UserMobileNo": input_mobile,
            "UserAddress": input_address,
            # "city": input_city,
            # "state": input_state,
            "UserEmail": input_email,
            "UserAadharNumber": input_adhar,
            "UserPannumber": input_pan
        }

        # print(payload)
         # Set the headers for the API request
         
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # }
        
        api_url="https://vgold.app/vgold_admin/m_api/update_user_details/"
        
        try:
            response = requests.post(api_url, json=payload)  # Use params parameter
            #print(response.text)
            # Ensure response content is not empty
            if response.content:
                try:
                    response_data = response.json()
                    # print(response_data)
                    
                    if response_data.get('message_code') == 1000:
                        user_data = response_data.get("message_data", {})
                        request.session['user_data'] = user_data
                        messages.success(request, "User profile updated")
                    else:
                        messages.error(request, response_data.get('Message', response_data.get('message_text')))
                    
                    return redirect('update_profile')  # Assuming 'complaint' is the URL name for the complaint view
                except ValueError:
                    message = "Received invalid JSON response."
            else:
                message = "Received empty response from the API."
        except requests.exceptions.RequestException as e:
            message = f"An error occurred while making the request: {e}"

    return redirect(reverse('update_profile'))

###################################### Certificate #############################################
import requests
from django.http import HttpResponse
from django.shortcuts import render

def Certificate(request):
    user_data = request.session.get('user_data', {})
    # user_id = user_data.get('data', [{}])[0].get('User_ID')
    user_id = user_data.get('User_Id') 

    if not user_id:
        return redirect('login') 
    
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
    # API URL for local gold booking history endpoint
    # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/gold_booking_history/"
    api_url = "https://vgold.app/vgold_admin/m_api/gold_booking_history/"
    
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    
    # Extract user_id from the session data
    user_id = user_data.get('User_Id')  # Correct key for 'User_Id'
    print(user_id)

    # If user_id is not found in the session data, return an error message
    if not user_id:
        return redirect('login') 
    
    # Prepare the payload for the API call
    payload = {'user_id': user_id}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Send the POST request to the local API
        response = requests.post(api_url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the response JSON
        
        # Check if the response is successful
        if data.get("message_code") == 1000:  # Success code is 1000
            bookings = data.get("message_data", [])
        else:
            bookings = []  # Default to empty list if unsuccessful
    except requests.exceptions.RequestException as e:
        # Print the error if the API request fails
        print(f"Failed to connect to the API: {str(e)}")
        bookings = []

    # Process each booking and ensure fields have default values if missing
    for booking in bookings:
        booking['number'] = booking.get('gold_booking_id', "N/A")
        booking['account_status'] = booking.get('account_status', "0")  # Default to "0" for closed
        booking['today_gain'] = booking.get('todays_gain', "0")
        booking['paid_amount'] = booking.get('total_paid_amount', "0")
        booking['monthly_installment'] = booking.get('monthly_installment', "0")  # Assuming monthly_installment exists in response
        booking['booking_date'] = booking.get('added_date', "N/A")
        booking['weight'] = f"{booking.get('gold', 0)}"
        booking['rate'] = booking.get('rate', "0")
        booking['value'] = booking.get('booking_amount', "0")
        booking['tenure'] = f"{booking.get('tennure', '0')} Month"
        booking['down_payment'] = booking.get('down_payment', "0")
        booking['booking_charge'] = booking.get('booking_charge', "0")
        booking['balance_amount'] = booking.get('down_payment', "0")
        booking['closing_date'] = booking.get('closing_date', "N/A")
        booking['booking_percentage'] = booking.get('percentage_paid', "60")

    # Render the template and pass the processed bookings data
    return render(request, 'gold/gbooking_history.html', {'bookings': bookings})

##############################################################################################
from django.http import JsonResponse

def transection_pdf(request):
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')  # Correct key for 'User_Id'

    # If user_id is not found in the session data, return an error message
    if not user_id:
        return redirect('login') 

    # Retrieve 'number' from POST request
    number = request.POST.get('number')
    print(number)
    if not number:
        return JsonResponse({"error": "Number is required."}, status=400)

    # Mocking API response with generated PDF link
    response_data = {
        "bid": number,
        "user_id": user_id,
        "link": f"https://vgold.app/vgold_admin/generate_booking_statement/{number}/"  # Use 'number' here
    }

    # Return JSON response with link
    return JsonResponse(response_data)

####################################### Agreement ######################################################

def agreement(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        
        # Prepare the data to send to the API
        payload = {
            "GBAccountDisplayId": number
        }
        
        # API URL
        api_url = "https://vgold.app/vgold_admin/m_api/get_agreement_copy/"

        try:
            # Send a POST request to the API
            response = requests.post(api_url, json=payload)
            response_data = response.json()  # Parse the JSON response

            if response_data.get('message_code') == 1000:  # Check for success
                agreement_data = response_data.get('message_data', {})
                gb_agreement_seen = agreement_data.get('GBAgreement_Seen')
                gb_agreement_url = agreement_data.get('GBAgreement_Url')
                
                if gb_agreement_seen == 1:
                    otp_api_url = "https://vgold.app/vgold_admin/m_api/send_agreement_otp/"
                    otp_response = requests.post(otp_api_url, json=payload).json()

                    if otp_response.get('message_code') == 1000:
                        return JsonResponse({
                            'message': 'OTP verification required',
                            'otp_required': True,
                            'GBAccountDisplayId': number
                        })
                    return JsonResponse({'error': 'Failed to send OTP'}, status=400)
                
                elif gb_agreement_seen == 2:
                    # Directly show the PDF
                    return JsonResponse({
                        'message': 'PDF available',
                        'pdf_url': gb_agreement_url,
                        'otp_required': False
                    })
                else:
                    return JsonResponse({'error': 'Unexpected GBAgreement_Seen value'}, status=400)
            else:
                return JsonResponse({
                    'error': 'Failed to fetch agreement details from API',
                    'message_text': response_data.get('message_text')
                }, status=400)
                
        except requests.exceptions.RequestException as e:
            # Handle API request exceptions
            return JsonResponse({'error': 'API request failed', 'details': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
################################# Transection Seprate ############################################    
def transaction_seprate(request, number):
    # API endpoint and payload
    api_url = "https://vgold.app/vgold_admin/m_api/get_transaction_list/"
    
    # print(type(number),number)
    payload = {
        "GBAccountDisplayId": number
    }
    
    # print(payload)
    
    try:
        # Send POST request to the API
        response = requests.post(api_url, json=payload)
        response_data = response.json()  # Parse the response as JSON
        
        # print(response_data)
        
        if response_data.get("message_code") == 1000:
            # Success - extract transaction data
            transactions = response_data.get("message_data", [])
        else:
            # Handle API response error
            transactions = []
            messages.error(request, response_data.get("message_text", "Failed to fetch transactions."))
    except requests.RequestException as e:
        # Handle request errors
        transactions = []
        messages.error(request, f"An error occurred while connecting to the API: {str(e)}")
    
    # Pass the transactions data to the template
    return render(request, 'gold/transaction_list.html', {"transactions": transactions,"number": number,})

################################# Transection Seprate ############################################    
def receipt_data(request, number):
    api_url = "https://vgold.app/vgold_admin/m_api/get_details_transection/"
    payload = {
        "GBT_Id": number
    }

    try:
        # Send POST request to the API
        response = requests.post(api_url, json=payload)
        response_data = response.json()  # Parse the response as JSON
        
        # print(response_data)
        
        if response_data.get("message_code") == 1000:
            # Success - extract transaction data
            transactions = response_data.get("message_data", [])
        else:
            # Handle API response error
            transactions = []
            messages.error(request, response_data.get("message_text", "Failed to fetch transactions."))
    except requests.RequestException as e:
        # Handle request errors
        transactions = []
        messages.error(request, f"An error occurred while connecting to the API: {str(e)}")
    
    # Pass the transactions data to the template
    return render(request, 'gold/receipt_data.html', {"transactions": transactions,"number": number,})


######################################################################################
def pdf_specific(request):
    if request.method == "POST":
        # Retrieve user session data
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')  # Get User_Id from session

        if not user_id:
            return redirect('login')  # Redirect to login if user is not authenticated

        # Get 'number' from POST request
        number = request.POST.get('number')
        if not number:
            return JsonResponse({"error": "Number is required."}, status=400)

        # Generate PDF link dynamically
        response_data = {
            "bid": number,
            "link": f"https://vgold.app/vgold_admin/booking_statement_specific/{number}/"
        }

        return JsonResponse(response_data)
    return JsonResponse({"error": "Invalid request method."}, status=405)
    
####################################### Verify Agreement #########################################################
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def verify_agreement_otp(request):
    if request.method == 'POST':
        try:
            # Parse the request data
            data = json.loads(request.body)
            gb_account_display_id = data.get('GBAccountDisplayId')
            gb_agreement_otp = int(data.get('GBAgreement_Otp'))
            
            print(gb_account_display_id)
            print(gb_agreement_otp)
            
            # Ensure the required fields are provided
            if not gb_account_display_id or not gb_agreement_otp:
                return JsonResponse({'success': False, 'message': 'Missing required fields.'}, status=400)
            
            # Prepare the payload for the external API
            payload = {
                "GBAgreement_Otp": gb_agreement_otp,
                "GBAccountDisplayId":gb_account_display_id,
            }

            # Call the external API
            external_api_url = "https://vgold.app/vgold_admin/m_api/verify_agreement_otp/"
            response = requests.post(external_api_url, json=payload)
            response_data = response.json()
            
            # print(response_data)
            
            # Process the response from the API
            if response_data.get('message_code') == 1000:  # Success case
                message_data = response_data.get('message_data', {})
                pdf_url = message_data.get('GBAgreement_Url')
                
                return JsonResponse({
                    'success': True,
                    'pdf_url': pdf_url,
                    'message': response_data.get('message_text', 'Success')
                })
            else:
                # Handle error from the API
                return JsonResponse({
                    'success': False,
                    'message': response_data.get('message_text', 'Retry again')
                }, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
        except requests.RequestException as e:
            return JsonResponse({'success': False, 'message': 'Error connecting to the API.', 'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An unexpected error occurred.', 'error': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
    
#############################################################################################
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
            
            link = f"https://www.vgold.co.in/dashboard/user/module/goldbooking/transaction_pdf.php?bid={number}&user_id={user_id}"
            
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
    user_id = user_data.get('User_Id')  # Assuming 'User_Id' is the correct key

    if not user_id:
        return redirect('login') 

    if request.method == "POST":
        # Retrieve POST data from form
        gold_in_gm = request.POST.get('quantity')
        print(gold_in_gm)
        tenure = request.POST.get('tensure')  # Make sure the name matches the form field
        
         # Store quantity and tenure in session
        request.session['gold_in_gm'] = gold_in_gm
        request.session['tenure'] = tenure
        
        # Prepare the data to be sent to the API
        data = {
            'quantity': gold_in_gm,
            'tenure': tenure,  # Updated key to 'tenure' as per the new API
            'user_id': user_id
        }
        
        # print(data)

        # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            # Send a POST request to the local API endpoint
            response = requests.post('https://vgold.app/vgold_admin/m_api/booking_details/', data=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the API response
            response_data = response.json()
            if response_data.get("message_code") == 1000:
                # Extract the necessary booking details from the API response
                booking_details = response_data.get("message_data", {})
                
                # Save booking details in session or pass to the template
                request.session['api_response'] = booking_details
                
                # print("API Response:", request.session['api_response'])

                # Redirect to a booking details page (ensure this view exists)
                return redirect('booking_details')
            else:
                # Handle the case where the status is not 1000
                error_message = response_data.get("message_text", "An error occurred")
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
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id') 
        # Retrieve the API response from the session
        api_response = request.session.get('api_response')
        # print(api_response)

        if api_response:
            # Render the template with API response data
            return render(request, 'gold/booking_details.html', {'api_response': api_response,"user_id":user_id})
        else:
            return HttpResponse("No API response found in session.", status=404)

    elif request.method == 'POST':
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id') 
        user_crn= user_data.get('UserCRNno') 
        payment_option = request.POST.get('dropdown2')
        bank_details = request.POST.get('bankDetails')
        tr_id = request.POST.get('transactionId')
        cheque_no = request.POST.get('chequeNo')
        gold_in_gm = request.session.get('gold_in_gm')
        tenure = request.session.get('tenure')
        
        print(f"User ID: {user_id}")
        print(f"User CRN: {user_crn}")
        print(f"Payment Option: {payment_option}")
        print(f"Bank Details: {bank_details}")
        print(f"Transaction ID: {tr_id}")
        print(f"Cheque No: {cheque_no}")
        print(f"Quantity (Gold in GM): {gold_in_gm}")
        print(f"Tenure: {tenure}")

        # Retrieve the API response from POST data and parse it
        api_response = request.POST.get('api_response')
        if api_response:
            api_response = eval(api_response)  # Convert string representation of dict to dict
            print("DEBUG: Extracted API response data:")
            print(f"Booking Value: {api_response.get('Booking_value')}")
            print(f"Gold Rate: {api_response.get('Gold_rate')}")
            print(f"Down Payment: {api_response.get('Down_payment')}")
            print(f"Booking Charges Discount: {api_response.get('Booking_charges_discount')}")
            print(f"Monthly: {api_response.get('Monthly')}")
            print(f"PC: {api_response.get('pc')}")
            print(f"Initial Booking Charges: {api_response.get('Initial_Booking_charges')}")
            print(f"Booking Charges: {api_response.get('Booking_charges')}")

        # Ensure the API response has the necessary fields
        booking_value = api_response.get('Booking_value')
        gold_rate = api_response.get('Gold_rate')
        down_payment = api_response.get('Down_payment')
        booking_charges_discount = api_response.get('Booking_charges_discount')
        monthly = api_response.get('Monthly')
        pc = api_response.get('pc')
        Initial_Booking_charges = api_response.get('Initial_Booking_charges')
        Booking_charges = api_response.get('Booking_charges')
        
        # payload={
        #     "user_id":user_id,
        #     "booking_value":booking_value,
        #     "down_payment" :down_payment,
        #     "monthly":monthly,
        #     "rate":gold_rate,
        #     "pc":pc,
        #     "gold_weight":gold_in_gm, 
        #     "tennure":tenure,
        #     "payment_option":payment_option,
        #     "bank_details":bank_details,
        #     "cheque_no" :cheque_no,
        #     "tr_id":tr_id,
        #     "initial_booking_charges":Initial_Booking_charges,
        #     "booking_charges_discount":booking_charges_discount,
        #     "booking_charges":Booking_charges,
        #     "confirmed":0                  
        # }
        payload = {
            "user_id": user_id,
            "booking_value": booking_value,
            "down_payment": down_payment,
            "monthly": monthly,
            "rate": gold_rate,
            "pc": pc,
            "gold_weight": gold_in_gm,
            "tennure": tenure,
            "payment_option": payment_option,
            "bank_details": bank_details if payment_option != "PG" else "",
            "cheque_no": cheque_no if payment_option == "Cheque" else "",
            "tr_id": tr_id if payment_option == "Online" else "",
            "initial_booking_charges": Initial_Booking_charges,
            "booking_charges_discount": booking_charges_discount,
            "booking_charges": Booking_charges,
            "confirmed": 0
        }

        api_url = "https://vgold.app/vgold_admin/m_api/create_gold_booking/"
        # api_url = "http://127.0.0.1:8001/vgold_admin/m_api/create_gold_booking/"

        # Send POST request to the API
        # try:
        #     response = requests.post(api_url, json=payload)
        #     response_data = response.json()

        #     if response.status_code == 200 and response_data.get('message_code') == 1000:
        #         # Success: Save booking ID or other details if needed
        #         booking_id = response_data['message_data']['booking_id']
        #         messages.success(request, f"Booking successful! Booking ID: {booking_id}")
        #         return redirect('gold_booking')  # Redirect to a success page
        #     else:
        #         # Handle API error
        #         error_message = response_data.get('message_text', 'An error occurred during booking.')
        #         messages.error(request, error_message)
        #         return redirect('booking_details') 
            
        #     # Redirect to the same page
        # except requests.exceptions.RequestException as e:
        #     # Handle request exceptions
        #     messages.error(request, "Failed to connect to the booking API. Please try again later.")
        #     return redirect('booking_details')
        
        try:
            response = requests.post(api_url, json=payload)
            response_data = response.json()

            if response.status_code == 200 and response_data.get('message_code') == 1000:
                booking_id = response_data['message_data']['booking_id']
                
                if payment_option == "PG":
                    partial_amount = float(down_payment) + float(Booking_charges)
                    # partial_amount = down_payment  # or monthly or whatever value you'd use
                    return redirect('regular_payment', id=partial_amount)
                else:
                    messages.success(request, f"Booking successful! Booking ID: {booking_id}")
                    return redirect('gold_booking')
            else:
                error_message = response_data.get('message_text', 'An error occurred during booking.')
                messages.error(request, error_message)
                return redirect('booking_details')
        except requests.exceptions.RequestException:
            messages.error(request, "Failed to connect to the booking API. Please try again later.")
            return redirect('booking_details')
       
    else:
        return HttpResponse("Invalid request method.", status=405)


###################################### Gold Deposite History #############################################
import requests
from django.shortcuts import render
from django.http import HttpResponse

def Gdeposit_history(request):
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')
    print(user_id)

    if not user_id:
        return redirect('login') 

    # Updated API endpoint and parameters
    api_url = "https://vgold.app/vgold_admin/m_api/m_gdeposite_history/"
    api_params = {
        'user_id': user_id
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Make the API request with headers
        response = requests.post(api_url, json=api_params, headers=headers)
        response_data = response.json()

        # Check if the API response status is success
        if response_data.get('message_code') == 1000:
            # Parse the data
            api_data = response_data.get('message_data', [])
            deposit_history = [
                {
                    "number": entry["gold_deposite_id"],
                    "status": entry["account_status"],
                    "booking_date": entry["added_date"],
                    "maturity_date": entry["maturity_date"],
                    "weight": f"{entry['gold']} gm",
                    "booking_charge": f"{entry['processing_fee']} INR",
                    "rate": f"{entry['addpurity']}%",
                    "tenure": f"{entry['tennure']} months",
                    "remark": entry["remark"],
                    "closing_date": entry["closing_date"],
                    "gold_maturity_weight": f"{entry['maturity_weight']} gm",
                    "todays_deposit_weight": f"{entry['gold_quality']} gm",
                    "todays_deposit_value": f"{entry['todays_deposit_value']} INR"
                }
                for entry in api_data
            ]
        else:
            # Handle the case when the API response status is not success
            deposit_history = []
    except Exception as e:
        # Handle exceptions such as network errors
        print(f"An error occurred: {e}")
        deposit_history = []

    return render(request, 'gold/gdeposit_history.html', {'deposit_history': deposit_history})


###################################### Gold Deposite #############################################
def Gold_deposit(request):
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')

    if not user_id:
        return redirect('login') 

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Fetch vendor data from the API endpoint
    try:
        vendor_response = requests.post('https://vgold.app/vgold_admin/m_api/m_vendor_upload/')
        if vendor_response.status_code == 200:
            vendor_data = vendor_response.json().get('message_data', [])
        else:
            vendor_data = []
            messages.error(request, "Failed to fetch vendor data.")
    except requests.exceptions.RequestException as e:
        vendor_data = []
        messages.error(request, f"Error while fetching vendor data: {e}")

    if request.method == "POST":
        gold_weight = request.POST.get('goldWeight')
        deposit_charges = request.POST.get('depositCharges')
        tenure = request.POST.get('tenure')
        maturity_weight = request.POST.get('maturityWeight')
        depositor = request.POST.get('depositor')
        purity = request.POST.get('purity')
        remark = request.POST.get('remark')

        # Print all the data
        # print("Gold Weight:", gold_weight)
        # print("Deposit Charges:", deposit_charges)
        # print("Tenure:", tenure)
        # print("Maturity Weight:", maturity_weight)
        # print("Depositor:", depositor)
        # print("Purity:", purity)
        # print("Remark:", remark)

        payload = {
            "user_id": user_id,
            "gw": gold_weight,
            "deposite_charges": deposit_charges,
            "tennure": tenure,
            "cmw": maturity_weight,
            "vendor_id": depositor,
            "addpurity": purity,
            "remark": remark,
            "guarantee": "no"
        }

        try:
            # Make the POST request to the new API
            response = requests.post('https://vgold.app/vgold_admin/m_api/m_gold_deposite/', json=payload, headers=headers)

            if response.content:
                try:
                    response_data = response.json()

                    # Check if message_code is 1000 for a successful request
                    if response_data.get('message_code') == 1000:
                        # Handle successful response
                        messages.success(request, response_data.get('message_text'))
                    else:
                        # If message_code is not 1000, display the message_text
                        messages.error(request, response_data.get('message_text'))

                    return redirect('gold_deposit')  # Redirect to the 'Gold_deposit' page

                except ValueError:
                    # If the response is not in valid JSON format
                    message = "Received invalid JSON response."
            else:
                # Handle empty response from the API
                message = "Received empty response from the API."

        except requests.exceptions.RequestException as e:
            # Handle errors during the API request
            message = f"An error occurred while making the request: {e}"

            return HttpResponse(message)

    # Render the HTML template with vendor data
    return render(request, 'gold/gold_deposit.html', {'vendor_data': vendor_data})


 ###################################### calculate_gold_deposite #############################################   
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.shortcuts import render

def calculate_gold_deposite(request):
    if request.method == 'POST':
        gold_weight = request.POST.get('gold_weight')
        
        # Headers for the API requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # New API endpoint and payload
        api_url = 'https://vgold.app/vgold_admin/m_api/gold_deposite_charges/'
        payload = {'gold_weight': gold_weight}

        try:
            # Make a POST request to the external API with headers
            response = requests.post(api_url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                
                # Check if the API response is successful
                if data.get('message_code') == 1000:
                    charges = data['message_data'].get('charges')
                    deposite_charges_rate = data['message_data'].get('deposite_charges_rate')
                    
                    # Prepare JSON response to send back to frontend
                    json_response = {
                        'gold_weight': gold_weight,
                        'charges': charges,
                        'deposite_charges_rate': deposite_charges_rate,
                        'message': data.get('message_text', 'Received Gold Weight successfully.')
                    }
                    
                    # print(json_response)
                    return JsonResponse(json_response)
                else:
                    return JsonResponse({'error': 'Failed to calculate charges.'}, status=400)
            else:
                return JsonResponse({'error': 'Failed to fetch charges from API.'}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request.'}, status=400)

###################################### cgold_mature_weight #############################################
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use only for demonstration; CSRF should be handled properly in production
def cgold_mature_weight(request):
    if request.method == 'POST':
        gold_weight = request.POST.get('gold_weight')
        tenure = request.POST.get('tenure')
        
        # Headers for the API requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Make a POST request to the external API with headers
        api_url = 'https://www.vgold.co.in/dashboard/webservices/calculate_gold_mature_weight.php'
        
        payload = {
            'gold_weight': gold_weight,
            'tennure': tenure,
            'guarantee': "no"
        }
        
        # print(payload)
        
        # Send the POST request
        response = requests.post(api_url, headers=headers, data=payload)

        if response.status_code == 200:
            response_data = response.json()
            # print(response_data)
            
            # Check if the response is successful and contains the expected data
            if response_data.get('status') == '200':
                context = {
                    'status': response_data.get('status'),
                    'message': response_data.get('Message'),
                    'data': response_data.get('Data')
                }
                return JsonResponse(context)  # Send context as JSON response
            else:
                return JsonResponse({'error': 'API response was unsuccessful.'}, status=400)
        else:
            return JsonResponse({'error': 'Failed to connect to the external API.'}, status=400)
    
    # Handle non-POST requests
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


###################################### Membership #############################################
def Membership(request):
    return render(request, 'gold/membership.html')
###################################### Money Wallet #############################################
# def Money_wallet(request):
#     # Retrieve user data from session
#     user_data = request.session.get('user_data', {})
#     # user_id = user_data.get('data', [{}])[0].get('User_ID')
#     user_id = user_data.get('User_Id') 

#     if not user_id:
#         return redirect('login') 

#     # API endpoint and headers
#     api_url = "https://www.vgold.co.in/dashboard/webservices/money_wallet_transactions.php"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     payload = {'user_id': user_id}

#     try:
#         response = requests.post(api_url, headers=headers, data=payload)
#         response_data = response.json()
#         # print(response_data)

#         if response_data['status'] == "200":
#             Wallet_Balance = response_data.get('Wallet_Balance')
#             transactions = response_data.get('Data', [])
#         else:
#             return HttpResponse(f"Error: {response_data.get('Message', 'Unknown error')}")

#     except requests.exceptions.RequestException as e:
#         return HttpResponse(f"API request failed: {e}")

#     context = {
#         'Wallet_Balance': Wallet_Balance,
#         'transactions': transactions,
#     }
#     print(context)
#     return render(request, 'gold/money_wallet.html' , context)

def Money_wallet(request):
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id') 
    print(user_id)

    if not user_id:
        return redirect('login') 

    # API endpoints
    # balance_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_wallet_balances/"
    # transactions_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_mw_transection/"
    
    balance_api_url = "https://vgold.app/vgold_admin/m_api/get_wallet_balances/"
    transactions_api_url = "https://vgold.app/vgold_admin/m_api/get_mw_transection/"

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }

    payload = {'user_id': user_id}
    # payload = {'user_id': 491}

    try:
        # Wallet balance request
        balance_response = requests.post(balance_api_url, headers=headers, json=payload)
        balance_data = balance_response.json()

        if balance_data['message_code'] != 1000:
            return HttpResponse(f"Balance API Error: {balance_data.get('message_text', 'Unknown error')}")

        Wallet_Balance = balance_data['message_data'].get('MoneyWalletBalance', 0)

        # Transactions request
        transaction_response = requests.post(transactions_api_url, headers=headers, json=payload)
        transaction_data = transaction_response.json()

        if transaction_data['message_code'] == 1000:
            transactions = transaction_data.get('message_data', [])
        else:
            transactions = []  # fallback to empty list if error in transactions API

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"API request failed: {e}")

    context = {
        'Wallet_Balance': Wallet_Balance,
        'transactions': transactions,
    }
    print(context)
    return render(request, 'gold/money_wallet.html', context)

###################################### Pay Installment #############################################
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import requests

@csrf_exempt
@require_POST
def handle_selection(request):
    try:
        # Fetch user data from session
        user_data = request.session.get('user_data', {})
        # user_id = user_data.get('data', [{}])[0].get('User_ID')
        user_id = user_data.get('User_Id') 

        # Check if user ID is available in session
        if not user_id:
            return HttpResponse("User ID not found in session data.", status=400)
        
        # print(user_id)  # Print user ID to server logs for debugging
    
        # Parse the JSON body of the request
        data = json.loads(request.body)
        selected_value = data.get('selected_value')
        print(selected_value)  # Print selected value to server logs for debugging
        
        # Headers for the API requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # First API call to fetch down payment details
        api_url_down_payment = 'https://www.vgold.co.in/dashboard/webservices/fetch_down_payment.php'
        api_data_down_payment = {'gbid': selected_value}
        response_down_payment = requests.post(api_url_down_payment, data=api_data_down_payment, headers=headers)

        response_data = {}
        
        if response_down_payment.status_code == 200:
            api_response_down_payment = response_down_payment.json()
            monthly_installment = api_response_down_payment.get('monthly_installment', 'N/A')
            response_data['monthly_installment'] = monthly_installment
            
            # print(f"Monthly Installment: {monthly_installment}") 

            message = api_response_down_payment.get('Message', 'Data fetched successfully')
            response_data['message'] = message
        else:
            return JsonResponse({'error': 'Failed to fetch data from the down payment API'}, status=response_down_payment.status_code)
        
        # Second API call to fetch money wallet transactions
        api_url_wallet_transactions = 'https://www.vgold.co.in/dashboard/webservices/money_wallet_transactions.php'
        api_data_wallet_transactions = {'user_id': user_id}
        response_wallet_transactions = requests.post(api_url_wallet_transactions, data=api_data_wallet_transactions, headers=headers)

        if response_wallet_transactions.status_code == 200:
            api_response_wallet_transactions = response_wallet_transactions.json()
            Wallet_Balance = api_response_wallet_transactions.get('Wallet_Balance', 'N/A')
            response_data['wallet_balance'] = Wallet_Balance
            
            # print(f"Wallet Balance: {Wallet_Balance}")  # Print the wallet balance
        else:
            return JsonResponse({'error': 'Failed to fetch data from the wallet transactions API'}, status=response_wallet_transactions.status_code)
                
        # Third API call to fetch gold wallet transactions
        api_url_gold_wallet_transactions = 'https://www.vgold.co.in/dashboard/webservices/gold_wallet_transactions.php'
        api_data_gold_wallet_transactions = {'user_id': user_id}
        response_gold_wallet_transactions = requests.post(api_url_gold_wallet_transactions, data=api_data_gold_wallet_transactions, headers=headers)
        
        if response_gold_wallet_transactions.status_code == 200:
            api_response_gold_wallet_transactions = response_gold_wallet_transactions.json()
            gold_Balance = api_response_gold_wallet_transactions.get('gold_Balance', 'N/A')
            response_data['gold_balance'] = gold_Balance
            
            # print(f"Gold Balance: {gold_Balance}")  # Print the wallet balance
        else:
            return JsonResponse({'error': 'Failed to fetch data from the gold wallet transactions API'}, status=response_gold_wallet_transactions.status_code)
        
        # Return the combined response data as JSON
        return JsonResponse(response_data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

###################################### Pay Installment #############################################

def Pay_installment(request):
    # Retrieve user data from session
    purchase_rate_data = request.session.get('purchase_rate_data', {})
    gold_purchase_rate = purchase_rate_data.get('Gold_purchase_rate', 'N/A')
    
    # Fetch user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')
    
    if not user_id:
        return redirect('login')

    # New API endpoint
    # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/installment_booking_id/"
    
    api_url = "https://vgold.app/vgold_admin/m_api/installment_booking_id/"
    
    # JSON payload for the API
    post_data = {'user_id': user_id}
    
    try:
        # Make the POST request to the local API
        response = requests.post(api_url, json=post_data)
        response.raise_for_status()
        response_data = response.json()
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred while calling the API: {e}")

    # Check the response code and message
    if response_data.get('message_code') == 1000 and response_data.get('message_text') == 'success':
        installment_data = response_data.get('message_data', [])
    else:
        return HttpResponse("Failed to retrieve installment data from the new API.")
    
    # Handle form submission
    if request.method == 'POST':
        # Retrieve form data from POST request
        gbid = request.POST.get('gbid')
        payment_options = request.POST.get('paymentOptions')
        minimumamt = request.POST.get('minimumamt')
        other_amount_input = request.POST.get('otherAmountInput')
        payment_option = request.POST.get('depositor')  # Default value if not 'moneyWallet' or 'goldWallet'
        bank_details = request.POST.get('bankName')
        tr_id = request.POST.get('transactionId')
        cheque_no = request.POST.get('chequeNumber')
        payable_amount = request.POST.get('payableAmount')
        
        # Determine payment_option and amountr based on payment_options
        if payment_options == 'moneyWallet':
            payment_option = 'MONEY WALLET'
            amountr = payable_amount  # Use payable_amount if payment_options is 'moneyWallet'
            other_amount_input = payable_amount
            confirmed = 0
        elif payment_options == 'goldWallet':
            payment_option = 'GOLD WALLET'
            amountr = payable_amount
            other_amount_input = payable_amount# Use payable_amount if payment_options is 'goldWallet'
            confirmed = 1
        elif payment_options == 'minimumAmount':
            # payment_option = 'MINIMUM AMOUNT'
            amountr = minimumamt 
            confirmed = 0
            other_amount_input = minimumamt# Use minimumamt if payment_options is 'minimumAmount'
        else:
            # Default case (if payment_options is not 'moneyWallet', 'goldWallet', or 'minimumAmount')
            amountr = 0  # Set a default value, adjust as per your application logic
            confirmed = 0  # Default confirmed value for other cases
       
        # Prepare payload for the installment payment API request
        payload = {
            "user_id": user_id,
            "gbid": gbid,
            "amountr": amountr,
            "payment_option": payment_option,
            "bank_details": bank_details if bank_details else 0,  # Default value for bank_details if not provided
            "amount_other": other_amount_input if other_amount_input else 0,  # Default value for amount_other if not provided
            "tr_id": tr_id,
            "cheque_no": cheque_no,
            "confirmed": confirmed, 
        }
        # print(payload)
        
        # Make POST request to installment payment API
        try:
            if(payment_option=="GOLD WALLET"):
                res = requests.post("https://www.vgold.co.in/dashboard/webservices/installment.php", data=payload, headers=headers)
            else:
                res = requests.post("https://www.vgold.co.in/dashboard/webservices/installment.php", data=payload, headers=headers)
            res.raise_for_status()  # Raise HTTPError for bad responses
            api_response = res.json()
            # print(api_response )
            
            # Handle success or failure based on API response
            if api_response.get('status') == '200':
                messages.success(request, api_response.get('Message'))
            else:
                messages.success(request, api_response.get('Message'))
        
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"An error occurred: {e}")
       
        return redirect(Pay_installment)  # Redirect back to Pay_installment view after form submission
    
    # Render the template with installment data in context
    # context = {'gold_purchase_rate': gold_purchase_rate}
    context = {'installment_data': installment_data, 'gold_purchase_rate': gold_purchase_rate}
    return render(request, 'gold/pay_installment.html', context)

###################################### Add Money #############################################
def Add_money(request):
    if request.method == 'POST':
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')  #

        if not user_id:
            return redirect('login') 
        
        # Accessing the 'amount' and 'depositor' fields from the POST data
        amount = request.POST.get('amount')
        depositor = request.POST.get('depositor')
        bankDetails = request.POST.get('bankDetails')
        transactionId = request.POST.get('transactionId')
        chequeNumber = request.POST.get('chequeNumber')
        
        payload={
            "user_id":user_id,
            "amount":amount,
            "payment_option":depositor,
            "bank_details":bankDetails,
            "tr_id":transactionId,
            "cheque_no":chequeNumber,
        }
        
        # print("Payload:", payload)
        
        # Headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            res = requests.post("https://www.vgold.co.in/dashboard/webservices/add_money.php", data=payload, headers=headers)
            res.raise_for_status()  # Raises an exception for HTTP errors
            response_data = res.json()

            if response_data.get('status') == '200':
                messages.success(request, response_data.get('Message'))             
            else:
                messages.error(request, response_data.get('Message'))
        except requests.exceptions.RequestException as e:
            messages.error(request, f"An error occurred while processing your request: {str(e)}")
        
        return redirect('add_money')

    return render(request, 'gold/add_money.html')

###################################### Add Bank #############################################

def Add_bank(request):
    if request.method == "POST":
        # Retrieve user data from the session
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id')
        if not user_id:
            return redirect('login') 
        
        bank_name = request.POST.get('bankName')
        branch = request.POST.get('branch')
        account_number = request.POST.get('accountNumber')
        account_type = request.POST.get('accountType')
        ifsc_code = request.POST.get('ifscCode')
        account_holder = request.POST.get('accountHolder')
        
        # Print debug information
        # print(f"User Data from Session: {user_data}")
        # print(f"Form Data: {bank_name}, {branch}, {account_number}, {account_type}, {ifsc_code}, {account_holder}")
        
        # Payload for the API
        payload = {
            "user_id": user_id,
            "bank_name": bank_name,
            "branch": branch,
            "acc_no": account_number,
            "account_type": account_type,
            "ifsc": ifsc_code,
            "name": account_holder
        }
        
        # print(f"Payload to be sent: {payload}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # API URL
        api_url = "https://vgold.app/vgold_admin/m_api/bank_details/"
        
        try:
            # Sending POST request to the API
            response = requests.post(api_url, json=payload, headers=headers)
            response_data = response.json()  # Parse JSON response
            
            # print(f"API Response: {response_data}")
            
            # Handle API response
            if response_data.get("message_code") == 1000:
                messages.success(request, "Bank detail added successfully.")
            else:
                messages.error(request, response_data.get("message_text", "An error occurred."))
        
        except requests.exceptions.RequestException as e:
            # print(f"Error while making API request: {e}")
            messages.error(request, "Failed to connect to the API. Please try again.")
        
        # Redirect to the add bank view
        return redirect('add_bank')

    return render(request, 'gold/add_bank.html')

###################################### Channel_partner #############################################
def Channel_partner(request):
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')
    UserCRNno = user_data.get('UserCRNno')
    
    if not user_id:
        return redirect('login') 
    
    api_url = "https://vgold.app/vgold_admin/m_api/get_cp_list/"
    post_data = {'GBAccountDisplayId': UserCRNno}
    
    data = []  # Ensure data is always initialized

    try:
        response = requests.post(api_url, data=post_data)
        response_data = response.json()

        if response_data.get('message_code') == 1000:
            data = response_data.get('message_data', [])
        else:
            messages.error(request, response_data.get('Message', 'An error occurred.'))

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")

    return render(request, 'gold/channel_partner.html', {'data': data})

###################################### Review #############################################
def Review(request):
    return render(request, 'gold/review.html')

###################################### Complaint #############################################

def Complaint(request):
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id') 

    if not user_id:
        return redirect('login') 
    
    if request.method == 'POST':
        # Retrieve form data
        complaint = request.POST.get('description')

        # Headers for the API request
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        #     'Content-Type': 'application/json'  # Specify that the data is JSON
        # }
        
        api_url="https://vgold.app/vgold_admin/m_api/add_feedback/"
        
        # Prepare query parameters for the API request
        params = {
            "user_id": user_id,
            "feedback_detail": complaint
        }
        # print(params)
        
        try:
            response = requests.post(api_url, json=params)  # Use params parameter
            # print(response.text)
            # Ensure response content is not empty
            if response.content:
                try:
                    response_data = response.json()
                    # print(response_data)
                    
                    if response_data.get('message_code') == 1000:
                        messages.success(request, "Complaint/Feedback registered.")
                    else:
                        messages.error(request, response_data.get('Message', 'An error occurred.'))
                    
                    return redirect('complaint')  # Assuming 'complaint' is the URL name for the complaint view
                except ValueError:
                    message = "Received invalid JSON response."
            else:
                message = "Received empty response from the API."
        except requests.exceptions.RequestException as e:
            message = f"An error occurred while making the request: {e}"
        
        messages.error(request, message)
        return redirect('complaint')  # Redirect back to the complaint form page

    return render(request, 'gold/complaint.html')

###################################### Feedback #############################################
def Feedback(request):
    return render(request, 'gold/feedback.html')
###################################### Refer #############################################
def Refer(request):
    # Retrieve user data from session
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id') 

    if not user_id:
        return redirect('login') 
    
    if request.method == 'POST':
        # Retrieve form data
        enterName = request.POST.get('enterName', '')
        enter_email = request.POST.get('enter_email', '')
        enter_mobileno = request.POST.get('enter_mobileno', '')

        # New API URL
        api_url = 'https://vgold.app/vgold_admin/m_api/referal_link/'

        # Payload with the updated structure
        payload = {
            'user_id': user_id,
            'name': enterName,
            'email': enter_email,
            'mobile_no': enter_mobileno
        }
        
        try:
            response = requests.post(api_url, json=payload)
            # Ensure response content is not empty
            if response.content:
                try:
                    response_data = response.json()

                    if response_data.get('message_code') == 1000:
                        messages.success(request, "Refer link sent successfully.")
                    else:
                        messages.error(request, f"Failed to send refer link: {response_data.get('message_text')}")
                    
                    return redirect(Refer)
                except ValueError:
                    message = "Received invalid JSON response."
            else:
                message = "Received empty response from the API."
        except requests.exceptions.RequestException as e:
            message = f"An error occurred while making the request: {e}"
        
        return HttpResponse(message)

    return render(request, 'gold/refer.html')
###################################### Logout #############################################
def Logout(request):
    # Clear all sessions
    request.session.clear()
    # Redirect to the login page
    return redirect('login')

###################################### NC Login #############################################
def nc_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        
        payload = {
            "name": name,
            "mobile": mobile
        }
        
        # Store payload in session
        request.session['payload'] = payload
        
        # Redirect to the dashb view
        return redirect('dashb')  # Use the name of the URL pattern for dashb
    
    return render(request, 'gold/nc_login.html')

###################################### NC Dashboard #############################################
def dashb(request):
    # Retrieve payload from session
    payload = request.session.get('payload', {})
    
    # Extract name and mobile from payload
    name = payload.get('name', '')
    mobile = payload.get('mobile', '')
    
    # Truncate name to 10 characters and add ellipsis if it exceeds
    truncated_name = name if len(name) <= 10 else name[:10] + '...'
    
    # Print the payload for debugging
    print(payload)
    
    # Pass truncated name and mobile to the template context
    context = {
        'name': truncated_name,
        'mobile': mobile
    }
    
    return render(request, 'gold/dashb.html', context)


###################################### NC Booking #############################################
def nc_booking(request):
    # First API endpoint and parameters
    api_url1 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params1 = {
        "App_Id": 1,
        "Script_Code": 19
    }
    
    # Second API endpoint and parameters
    api_url2 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params2 = {
        "App_Id": 1,
        "Script_Code": 20
    }
    
    # Headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make POST request to the first API with headers
    response1 = requests.post(api_url1, json=api_params1, headers=headers)
    
    # Check if first request was successful
    if response1.status_code == 200:
        api_data1 = response1.json()
        message_html1 = api_data1.get('message_text', '')
    else:
        message_html1 = "<p>First API request failed. Please try again later.</p>"
    
    # Make POST request to the second API with headers
    response2 = requests.post(api_url2, json=api_params2, headers=headers)
    
    # Check if second request was successful
    if response2.status_code == 200:
        api_data2 = response2.json()
        message_html2 = api_data2.get('message_text', '')
    else:
        message_html2 = "<p>Second API request failed. Please try again later.</p>"
    
    # Pass both message_html to the template context
    context = {
        'message1': message_html1,
        'message2': message_html2
    }
    
    # Render the template with the messages in the context
    return render(request, 'gold/nc_booking.html', context)


###################################### NC Booking #############################################
def nc_deposit(request):
    # First API endpoint and parameters
    api_url1 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params1 = {
        "App_Id": 1,
        "Script_Code": 27
    }
    
    # Second API endpoint and parameters
    api_url2 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params2 = {
        "App_Id": 1,
        "Script_Code": 28
    }
    
    # Headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make POST request to the first API with headers
    response1 = requests.post(api_url1, json=api_params1, headers=headers)
    
    # Check if first request was successful
    if response1.status_code == 200:
        api_data1 = response1.json()
        message_html1 = api_data1.get('message_text', '')
    else:
        message_html1 = "<p>First API request failed. Please try again later.</p>"
    
    # Make POST request to the second API with headers
    response2 = requests.post(api_url2, json=api_params2, headers=headers)
    
    # Check if second request was successful
    if response2.status_code == 200:
        api_data2 = response2.json()
        message_html2 = api_data2.get('message_text', '')
    else:
        message_html2 = "<p>Second API request failed. Please try again later.</p>"
    
    # Pass both message_html to the template context
    context = {
        'message1': message_html1,
        'message2': message_html2
    }
    
    # Render the template with the messages in the context
    return render(request, 'gold/nc_deposit.html', context)

###################################### NC Wallet #############################################
def nc_wallet(request):
    # First API endpoint and parameters
    api_url1 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params1 = {
        "App_Id": 1,
        "Script_Code": 31
    }
    
    # Second API endpoint and parameters
    api_url2 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params2 = {
        "App_Id": 1,
        "Script_Code": 32
    }
    
    # Headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make POST request to the first API with headers
    response1 = requests.post(api_url1, json=api_params1, headers=headers)
    
    # Check if first request was successful
    if response1.status_code == 200:
        api_data1 = response1.json()
        message_html1 = api_data1.get('message_text', '')
    else:
        message_html1 = "<p>First API request failed. Please try again later.</p>"
    
    # Make POST request to the second API with headers
    response2 = requests.post(api_url2, json=api_params2, headers=headers)
    
    # Check if second request was successful
    if response2.status_code == 200:
        api_data2 = response2.json()
        message_html2 = api_data2.get('message_text', '')
    else:
        message_html2 = "<p>Second API request failed. Please try again later.</p>"
    
    # Pass both message_html to the template context
    context = {
        'message1': message_html1,
        'message2': message_html2
    }
    
    # Render the template with the messages in the context
    return render(request, 'gold/nc_wallet.html', context)


####################################################################
def GPlan(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')

        # Set the headers for the API request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Make the API request
        api_url = "https://vgold.app/vgold_admin/m_api/get_gold_plans/"
        response = requests.post(api_url, data={'quantity': quantity}, headers=headers)
        
        # Check if the API request was successful
        if response.status_code == 200:
            api_response = response.json()
            if api_response.get("status") == "200":
                data = api_response.get("Data", {})
                # Pass the API response data to the template
                return render(request, 'gold/plan.html', {'data': data})
            else:
                # Handle the case where the API response status is not 200
                return render(request, 'gold/plan.html', {'error': api_response.get("Message")})
        else:
            # Handle the case where the API request failed
            return render(request, 'gold/plan.html', {'error': 'Failed to retrieve gold plan data'})
    
    # For GET requests, just render the template without any data
    return render(request, 'gold/plan.html')
###################################### NC Loan #############################################
def nc_loan(request):
    # First API endpoint and parameters
    api_url1 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params1 = {
        "App_Id": 1,
        "Script_Code": 29
    }
    
    # Second API endpoint and parameters
    api_url2 = "https://www.gyaagl.app/apis/chatbot/chatscripttext"
    api_params2 = {
        "App_Id": 1,
        "Script_Code": 30
    }
    
    # Headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make POST request to the first API with headers
    response1 = requests.post(api_url1, json=api_params1, headers=headers)
    
    # Check if first request was successful
    if response1.status_code == 200:
        api_data1 = response1.json()
        message_html1 = api_data1.get('message_text', '')
    else:
        message_html1 = "<p>First API request failed. Please try again later.</p>"
    
    # Make POST request to the second API with headers
    response2 = requests.post(api_url2, json=api_params2, headers=headers)
    
    # Check if second request was successful
    if response2.status_code == 200:
        api_data2 = response2.json()
        message_html2 = api_data2.get('message_text', '')
    else:
        message_html2 = "<p>Second API request failed. Please try again later.</p>"
    
    # Pass both message_html to the template context
    context = {
        'message1': message_html1,
        'message2': message_html2
    }
    
    # Render the template with the messages in the context
    return render(request, 'gold/nc_loan.html', context)

############################################################################################
def nc_vendors(request):
    # URL of the API
    api_url = "https://www.vgold.co.in/dashboard/webservices/vendor_upload.php"

    # Set the headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a GET request to the API with headers
    response = requests.get(api_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if data['status'] == '200':
            # Extract vendor details and prepend the base URL
            base_url = "https://www.vgold.co.in"
            vendors = [
                {
                    'vendor_id': vendor['vendor_id'],
                    'logo_path': base_url + vendor['logo_path'],
                    'letter_path': base_url + vendor['letter_path'],
                    'advertisement_path': base_url + vendor['advertisement_path']
                }
                for vendor in data['Data']
            ]
        else:
            vendors = []
    else:
        vendors = []

    context = {
        'vendors': vendors,
    }
    return render(request, 'gold/nc_vendors.html', context)


###############################Deal#########################
from time import time
def showDeals(request):
    if('user_data' in request.session):
        user_data = request.session.get('user_data', {})
        user_id = user_data.get('User_Id') 
        res = requests.post('https://vgold.app/vgold_admin/m_api/get_active_deals_by_visible_to/',json={"visible_to":"1","user_id":user_id}) #here '1' pass as a doctor==all user for vgold
        # print(res.text)
        if(res.json().get('message_code')==1000):
            alldeals = res.json().get('message_data')
        
        else:
            alldeals = []
        
        return render(request,'gold/showDeals.html',{'alldeals':alldeals,"timestamp":int(time())})
    
    else:
        return redirect(Login)

@csrf_exempt
def handle_deal_action(request):
    if request.method == 'POST':
        deal_id = request.POST.get('deal_id')
        DealAction_id = request.POST.get('DealAction_id')
        action_type = request.POST.get('action_type')
        #user_id = request.session.get('doctor_id')  # Assuming 'doctor_id' is stored in the session
        # print(deal_id,DealAction_id,action_type,user_id)
        
        # Make request to external API
        response = requests.post(
            'https://vgold.app/vgold_admin/m_api/update_deal_action_type_by_DealactionId/',
            json={"deal_id":deal_id,"dealaction_id":DealAction_id,"dealactiontype":action_type}
        )
        # print(response.text)

        # Check response status
        if response.status_code == 200 and response.json().get('message_code') == 1000:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "message": "Unable to perform action."})
    
    return JsonResponse({"success": False, "message": "Invalid request method."})

###################################### Nominee Details Form #############################################
import time
from datetime import datetime
def user_nominee_details(request):
    user_data = request.session.get('user_data', {})
    NomieeForUserId = user_data.get('User_Id')

    if not NomieeForUserId:
        return redirect('login')

    if request.method == "POST":
        # Retrieve form data
        NomieeForAccountType = request.POST.get("accountType")
        NomineeFirstName = request.POST.get("firstName")
        NomieeLastname = request.POST.get("lastName")
        NomieeEmail = request.POST.get("email")
        NomieeMobileNo = request.POST.get("mobileNo")
        NomieeDateofBirth = request.POST.get("dob")  # Already in "YYYY-MM-DD" format
        NomieeOccupation = request.POST.get("occupation")
        NomieePanNo = request.POST.get("panCard")
        NomieeRelation = request.POST.get("relation")
        NomieeIsMinorYN = request.POST.get("minor")

        print(NomieeDateofBirth)  # Ensure it's correctly formatted

        # Validate date format
        try:
            datetime.strptime(NomieeDateofBirth, "%Y-%m-%d")
        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return render(request, 'gold/user_nominee_details.html')

        # Prepare data for API request
        # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/user_nominee_insert/"
        api_url = "https://vgold.app/vgold_admin/m_api/user_nominee_insert/"
        
        post_data = {
            "NomieeForUserId": NomieeForUserId,
            "NomineeForAccountId": 10,  # Change dynamically if needed
            "NomieeForAccountType": NomieeForAccountType,
            "NomineeFirstName": NomineeFirstName,
            "NomieeLastname": NomieeLastname,
            "NomieeOccupation": NomieeOccupation,
            "NomieeMobileNo": NomieeMobileNo,
            "NomieePanNo": NomieePanNo,
            "NomieeEmail": NomieeEmail,
            "NomieeRelation": NomieeRelation,
            "NomieeDateofBirth": NomieeDateofBirth,  # Send as "YYYY-MM-DD"
            "NomieeIsMinorYN": NomieeIsMinorYN,
            "NomieeStatus": 0
        }

        try:
            response = requests.post(api_url, json=post_data)
            response_data = response.json()
            print(response_data)

            if response_data.get("message_code") == 1000:
                messages.success(request, "Nominee added successfully!")
            else:
                messages.error(request, response_data.get("message_text", "Failed to add nominee."))

        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error communicating with API: {str(e)}")

    return render(request, 'gold/user_nominee_details.html')

###################################### Feedback #############################################
def chatbot(request):
    
    return render(request, 'gold/chatbot.html')

###################################################################################
def check_account_status(request, crn_no):
    # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/check_account_status_mobile/"
    api_url = "https://vgold.app/vgold_admin/m_api/check_account_status_mobile/"
    payload = {"crn_no": crn_no}
    
    try:
        response = requests.post(api_url, json=payload)
        response_data = response.json()
        
        if response_data.get("message_code") == 1000:
            account_details = response_data.get("message_data", [])
        else:
            account_details = []

    except requests.exceptions.RequestException as e:
        account_details = []
        print("Error fetching data:", e)

    return render(request, 'gold/check_account_status.html', {'crn_no': crn_no, 'account_details': account_details})

###################################### Feedback #############################################
def termcondition(request):
    
    return render(request, 'gold/termcondition.html')

###################################### privacypolicy #############################################
def privacypolicy(request):
    return render(request, 'gold/privacypolicy.html')

###################################### Feedback #############################################
def deactivate(request):
    user_data = request.session.get('user_data', {})
    User_Id = user_data.get('User_Id')

    if not User_Id:
        return redirect('login')

    try:
        response = requests.post(
            # 'http://127.0.0.1:8000/vgold_admin/m_api/deactivate_account/',
            'https://vgold.app/vgold_admin/m_api/deactivate_account/',
            json={"user_id": User_Id}
        )
        data = response.json()
        if data.get("message_code") == 1000:
            request.session.clear()
            return redirect('login')
        else:
            return redirect('dashboard')
    except Exception as e:
        print("Error calling deactivate API:", e)
        return redirect('dashboard')
    
#####################################################################################  
def deactivates(request, id):
    # api_url = f'http://127.0.0.1:8000/vgold_admin/m_api/deactivate_user/{id}/'
    api_url = f'https://vgold.app/vgold_admin/m_api/deactivate_user/{id}/'
    
    try:
        response = requests.get(api_url)
        data = response.json()

        context = {}
        if data.get("message_code") == 1000:
            context["user_info"] = data.get("message_data", {})
            context["message_text"] = data.get("message_text", "")
        else:
            context["error_message"] = f"Deactivation failed: {data.get('message_text', 'Unknown error')}"

        return render(request, "gold/deactivate.html", context)

    except Exception as e:
        print("Error calling deactivate API:", e)
        return render(request, "gold/deactivate.html", {
            "error_message": "An error occurred while trying to deactivate the account."
        })
        
#######################################################################       
    
# @api_view(["POST"])
# @csrf_exempt
# def nach_response(request):
#     if request.method=="POST":
#         # print(request.data)
#         print(request.POST)
#         post_data = request.POST
        
#         # return redirect('dashboard')
#         return render(request, 'gold/nach_response.html', {'post_data': post_data})

# @csrf_exempt
# def nach_response(request):
#     if request.method == "POST":
#         post_data = request.POST.dict()

#         mandate_resp_raw = post_data.get("MandateRespDoc", "{}")
#         print(mandate_resp_raw)

#         try:
#             mandate_resp_json = json.loads(mandate_resp_raw)
#         except json.JSONDecodeError:
#             mandate_resp_json = {"error": "Invalid JSON in MandateRespDoc"}

#         is_success = mandate_resp_json.get("Status", "").lower() == "success"

#         context = {
#             "post_data": post_data,
#             "mandate_resp": mandate_resp_json,
#             "is_success": is_success,
#         }

#         return render(request, 'gold/nach_response.html', context)

# @csrf_exempt
# def nach_response(request):
#     if request.method == "POST":
#         post_data = request.POST.dict()

#         # Convert single quotes to double for JSON parsing
#         mandate_resp_raw = post_data.get("MandateRespDoc", "{}").replace("'", '"')

#         try:
#             mandate_resp_json = json.loads(mandate_resp_raw)
#         except json.JSONDecodeError:
#             mandate_resp_json = {"Status": "Failed", "Error": "Invalid JSON in MandateRespDoc"}

#         is_success = (
#             mandate_resp_json.get("Status", "").lower() == "success" and
#             mandate_resp_json.get("Errors", [{}])[0].get("Error_Code") == "000"
#         )

#         context = {
#             "post_data": post_data,
#             "mandate_resp": mandate_resp_json,
#             "is_success": is_success,
#         }

#         return render(request, 'gold/nach_response.html', context)

ERROR_CODE_MAPPING = {
    "000": "No Error",

    # AP (Bank) Errors
    "AP01": "Account blocked",
    "AP02": "Account closed",
    "AP03": "Account frozen",
    "AP04": "Account Inoperative",
    "AP05": "No such account",
    "AP06": "Not a CBS act no.or old act no.represent with CBS no",
    "AP07": "Refer to the branch - KYC not completed",
    "AP10": "Amount Exceeds E mandate Limit",
    "AP11": "Authentication Failed",
    "AP14": "Invalid User Credentials",
    "AP15": "Mandate Not Registered - Not maintaining required balance",
    "AP16": "Mandate Not Registered - Minor Account",
    "AP17": "Mandate Not Registered - NRE Account",
    "AP18": "Mandate registration not allowed for CC account",
    "AP19": "Mandate registration not allowed for PF account",
    "AP20": "Mandate registration not allowed for PPF account",
    "AP23": "Transaction rejected or cancelled by the customer",
    "AP24": "Withdrawal stopped owing to death of account holder",
    "AP28": "Mandate registration failed. Please contact your home branch",
    "AP29": "Technical errors or connectivity issue at bank end",
    "AP30": "Browser closed by the customer in mid transaction",
    "AP31": "Mandate registration not allowed for joint account",
    "AP32": "Mandate registration not allowed for wallet account",
    "AP33": "User rejected the transaction on pre-Login page",
    "AP34": "Account number not registered for net-banking facility",
    "AP35": "Invalid card number",
    "AP36": "Invalid expiry date",
    "AP37": "Invalid PIN",
    "AP38": "Invalid CVV",
    "AP39": "OTP invalid",
    "AP40": "Maximum tries exceeded for OTP",
    "AP41": "Time expired for OTP",
    "AP42": "Debit card not activated",
    "AP43": "Debit card blocked",
    "AP44": "Debit card hot listed",
    "AP45": "Debit card expired",
    "AP46": "No response received from customer while performing mandate registration",
    "AP47": "Account number registered for only view rights in net-banking facility",

    # IM (Merchant) Errors
    "IM01": "Merchant account is not valid",
    "IM02": "Merchant IFSC code is not valid",
    "IM03": "Merchant category code is not valid",
    "IM04": "Merchant category description is not valid",
    "IM05": "Merchant account name is not valid",
    "IM06": "Duplicate msgid found",

    # IC (Customer) Errors
    "IC01": "All contact fields (Email, Mobile, Telephone) cannot be empty",
    "IC04": "Expiry date should be greater than Start date",
    "IC06": "InstructedMember Bank is not available",
    "IC11": "Mandate cannot be registered with Inactive account",
    "IC13": "Mandate registration is not allowed with provided relationship type",
    "IC14": "Mandate registration is not allowed with provided relationship type",

    # I (Common) Errors
    "I001": "Invalid JSON",
    "I002": "Invalid Token",
    "I003": "Invalid Merchant",
    "I004": "Invalid Account",
    "I005": "Key is not provided",
    "I006": "Field cannot be empty",
    "I007": "Value exceeds maximum length",
    "I008": "Value below minimum length",
    "I009": "Invalid value",
    "I010": "Request is not valid",
    "I011": "All keys not provided in the form",
    "I012": "Session expired",
    "I013": "Request and Response checksum do not match",

    # ONMAGS/NPCI/Bank Errors (partial, extend as needed)
    "151": "Merchant xmlns name empty or incorrect",
    "152": "Merchant MsgId empty or incorrect",
    "153": "Merchant CreDtTm empty or incorrect",
    "154": "Merchant ReqInitPty Id empty or incorrect",
    "155": "Merchant CatCode empty or incorrect",
    "156": "Merchant UtilCode empty or incorrect",
    "157": "Merchant CatDesc empty or incorrect",
    "158": "Merchant ReqInitPty name empty or incorrect",
    "159": "Merchant MndtReqId empty or incorrect",
    "160": "Merchant SeqTp empty or incorrect",
    "161": "Merchant Frequency empty or incorrect",
    "162": "First collection date empty or incorrect",
    "163": "Final collection date empty or incorrect",
    "164": "Collection Amount currency type empty or incorrect",
    "165": "Collection Amount empty or incorrect",
    "166": "Max Amount currency type empty or incorrect",
    "167": "Max Amount empty or incorrect",
    "168": "Creditor name empty or incorrect",
    "169": "Creditor account number empty or incorrect",
    "170": "Creditor Member ID empty or incorrect",
    "171": "MandateReqId empty or incorrect",
    "172": "Creditor Account No empty",
    "173": "Merchant Info not available",
    "174": "ReqInitPty not available",
    "175": "Creditor Account Details not available",
    "176": "Group Header not available",
    "177": "Mandate not available",
    "178": "MandateAuthReq empty or not available",
    "179": "Checksum validation failed",
    "180": "Signature validation failed",
    "181": "Error in decrypting Creditor Acc No",
    "182": "Error in decrypting First Collection Date",
    "183": "Error in decrypting Final Collection Date",
    "184": "Error in decrypting Collection Amount",
    "185": "Error in decrypting Max Amount",
    "186": "Invalid request",
    "187": "Merchant ID empty or incorrect",
    "188": "MandateReqDoc incorrect",
    "189": "Checksum empty or not available",
    "190": "Signature not found",
    "191": "Group Header missing tags",
    "192": "ReqInitPty missing tags",
    "193": "Mandate missing tags",
    "194": "Creditor Account Details missing tags",
    "195": "Certificate not found",
    "196": "Signature algorithm incorrect",
    "197": "Signature Digest algorithm incorrect",
    "198": "First date is after final date",
    "199": "Creditor Account Details not available",
    "200": "First date not available",
    "201": "Final date not available",
    "202": "First date empty",
    "203": "Final date empty",
    "204": "MandateReqDoc empty or not available",
    "205": "MerchantId not in approved list",
    "206": "Both ColltnAmt and MaxAmt empty",
    "207": "Both ColltnAmt and MaxAmt present (conflict)",
    "208": "Category code not in approved list",
    "209": "MsgId is duplicate",
    "210": "Frequency type is invalid",
    "211": "Sequence type is invalid",
    "212": "Category description not in approved list",
    "213": "UtilCode not in approved list",
    "214": "Req Pay ID not in approved list",
    "215": "Creditor Account name not in approved list",
    "216": "Occurrences is empty",
    "217": "Debitor name empty or incorrect",
    "218": "Debitor account number empty or incorrect",
    "219": "Debitor tags missing",
    "220": "Debitor Account No empty",
    "221": "Debitor Account not available",
    "222": "Creditor and Debitor account number are the same",
    "251": "Bank Request is invalid",
    "252": "Bank xmlns is empty or incorrect",
    "253": "Bank Response type not available or empty",
    "254": "Bank Check sum is not available or empty",
    "255": "Mandate request document is incorrect",
    "256": "Bank ID not available or empty",
    "257": "Error decrypting Accepted value",
    "258": "Error decrypting Accepted Ref Number",
    "259": "Error decrypting Reason Code",
    "260": "Error decrypting Reason Description",
    "261": "Error decrypting Rejected By",
    "262": "NPCI Ref ID empty or incorrect",
    "263": "Error code not available in Error XML",
    "264": "Error description not available in Error XML",
    "265": "Rejected By not available in Error XML",
    "266": "Mandate Error Response not available in Error XML",
    "267": "Checksum validation failed",
    "268": "UndrlygAccptncDtls not available",
    "269": "GrpHdr empty or not available",
    "270": "MsgId empty or incorrect",
    "271": "CreDtTm empty or incorrect",
    "272": "ReqInitPty empty or incorrect",
    "273": "OrgnlMsgInf not available",
    "274": "MndtReqId empty or incorrect",
    "275": "UndrlygAccptncDtls CreDtTm empty or incorrect",
    "276": "Accptd empty",
    "277": "AccptRefNo empty or incorrect",
    "278": "RjctRsn not available",
    "279": "RjctRsn ReasonCode not empty",
    "280": "RjctRsn ReasonDesc not empty",
    "281": "RjctRsn RejectBy not empty",
    "282": "RjctRsn ReasonCode empty or incorrect",
    "283": "RjctRsn ReasonDesc empty or incorrect",
    "284": "RjctRsn RejectBy empty or incorrect",
    "285": "Certificate not found",
    "286": "IFSC Code incorrect",
    "287": "RespType is incorrect",
    "288": "GrpHdr missing some tags",
    "289": "UndrlygAccptncDtls missing some tags",
    "290": "OrgnlMsgInf missing some tags",
    "291": "IFSC tag is missing",
    "292": "DBTR not available",
    "293": "AccptncRslt not available",
    "294": "RjctRsn missing some tags",
    "295": "ManReqDoc not available or empty",
    "296": "Accptd type incorrect",
    "297": "Signature not available",
    "298": "Signature Digest algorithm incorrect",
    "299": "Signature validation failed",
    "300": "Signature algorithm incorrect",
    "301": "BankId not in approved list",
    "302": "MsgId is duplicate",
    "303": "Accepted Ref number is duplicate",
    "305": "Response timeout",
    "474": "Returning Error XML",
    "475": "Invalid JSON Structure",
    "497": "SpnBank not certified for the variant",
}

# @csrf_exempt
# def nach_response(request):
#     if request.method == "POST":
#         post_data = request.POST.dict()
#         mandate_resp_raw = post_data.get("MandateRespDoc", "{}").replace("'", '"')

#         try:
#             mandate_resp_json = json.loads(mandate_resp_raw)
#         except json.JSONDecodeError:
#             mandate_resp_json = {"Status": "Failed", "Errors": [{"Error_Code": "I001", "Error_Message": "Invalid JSON"}]}

#         status = mandate_resp_json.get("Status", "")
#         error_code = mandate_resp_json.get("Errors", [{}])[0].get("Error_Code", "")
#         error_desc = ERROR_CODE_MAPPING.get(error_code, "Unknown error")

#         is_success = (status.lower() == "success" and error_code == "000")

#         context = {
#             "post_data": post_data,
#             "mandate_resp": mandate_resp_json,
#             "is_success": is_success,
#             "error_description": error_desc,
#         }

#         return render(request, 'gold/nach_response.html', context)

@csrf_exempt
def nach_response(request):
    if request.method == "POST":
        post_data = request.POST.dict()
        mandate_resp_raw = post_data.get("MandateRespDoc", "{}").replace("'", '"')

        try:
            mandate_resp_json = json.loads(mandate_resp_raw)
        except json.JSONDecodeError:
            mandate_resp_json = {
                "Status": "Failed",
                "Errors": [{"Error_Code": "I001", "Error_Message": "Invalid JSON"}]
            }
            messages.error(request, "Invalid JSON received in Mandate Response.")

        # Extract high-level response details
        status_value = mandate_resp_json.get("Status", "")
        error_code = mandate_resp_json.get("Errors", [{}])[0].get("Error_Code", "")
        error_desc = ERROR_CODE_MAPPING.get(error_code, "Unknown error")
        is_success = (status_value.lower() == "success" and error_code == "000")

        msgid = ""
        mandate_data = {}

        # Extract Msgid
        if "d" in mandate_resp_json and "tranStatus" in mandate_resp_json["d"]:
            tran_status_list = mandate_resp_json["d"]["tranStatus"]
            if tran_status_list and isinstance(tran_status_list, list):
                msgid = tran_status_list[0].get("Msgid", "")
                print(f"Msgid from NACH response: {msgid}")

                if msgid:
                    # Extract Filler fields from top-level JSON
                    filler8 = mandate_resp_json.get("Filler8", "")
                    filler9 = mandate_resp_json.get("Filler9", "")
                    filler10 = mandate_resp_json.get("Filler10", "")

                    # Determine final values based on status
                    if status_value.lower() == "success":
                        nm_status = 1
                        nm_error_code = "000"
                        nm_error_message = "N/A"
                    else:
                        nm_status = 2
                        nm_error_code = error_code
                        nm_error_message = error_desc

                    # 🔁 Call the update mandate API
                    update_url = "https://vgold.app/vgold_admin/m_api/update_nach_mandate/"
                    update_payload = {
                        "Msgid": msgid,
                        "Filler8": filler8,
                        "Filler9": filler9,
                        "Filler10": filler10,
                        "NMStatus": nm_status,
                        "NMErrorCode": nm_error_code,
                        "NMErrorMessage": nm_error_message
                    }

                    try:
                        update_response = requests.post(update_url, json=update_payload)
                        update_json = update_response.json()
                        if update_json.get("message_code") == 1000:
                            messages.success(request, "NACH mandate updated successfully.")
                        else:
                            messages.error(request, "Failed to update NACH mandate.")
                    except requests.RequestException as e:
                        print(f"Error calling update API: {e}")
                        messages.error(request, "Error occurred during mandate update API call.")

                    # ✅ Fetch mandate details
                    try:
                        api_url = f"https://vgold.app/vgold_admin/m_api/get_mandate_data/{msgid}/"
                        api_response = requests.get(api_url, timeout=10)

                        if api_response.status_code == 200:
                            mandate_api_data = api_response.json()
                            if mandate_api_data.get("message_code") == 1000:
                                mandate_data = mandate_api_data.get("message_data", {})

                                # ✅ Call update_nach_status API if success
                                if is_success:
                                    display_id = mandate_data.get("NMCustomer_Reference2")
                                    user_id = request.session.get("user_id")

                                    if display_id and user_id:
                                        update_status_url = "https://vgold.app/vgold_admin/m_api/update_nach_status/"
                                        update_status_payload = {
                                            "display_id": display_id,
                                            "user_id": user_id
                                        }

                                        try:
                                            status_response = requests.post(update_status_url, json=update_status_payload, timeout=10)
                                            status_json = status_response.json()

                                            if status_json.get("message_code") == 1000:
                                                messages.success(request, "NACH status updated successfully.")
                                            else:
                                                messages.error(request, f"Failed to update NACH status: {status_json.get('message_text', '')}")
                                        except requests.RequestException as e:
                                            print(f"Error calling NACH status update API: {e}")
                                            messages.error(request, "An error occurred while calling NACH status update API.")
                                    else:
                                        messages.error(request, "Display ID or User ID not found for NACH status update.")
                            else:
                                messages.error(request, "Mandate data not found for the given Msgid.")
                        else:
                            messages.error(request, "Failed to fetch mandate details from server.")
                    except requests.RequestException as e:
                        print(f"Error calling mandate API: {e}")
                        messages.error(request, "An error occurred while calling mandate API.")

        # Prepare and render context
        context = {
            "post_data": post_data,
            "mandate_resp": mandate_resp_json,
            "is_success": is_success,
            "error_description": error_desc,
            "msgid": msgid,
            "mandate_data": mandate_data,
        }

        return render(request, 'gold/nach_response.html', context)

###################################################################################

import hashlib
from cryptography.fernet import Fernet
import base64
from django.shortcuts import render, redirect

# Function to generate SHA256 CheckSumVal
def generate_checksum(data_list):
    combined_data = ''.join(data_list)
    checksum = hashlib.sha256(combined_data.encode()).hexdigest()
    return checksum

# def encrypt_text_using_api(text):
#     try:
#         url = 'http://127.0.0.1:8000/vgold_admin/api/encrypt_text/'
#         # url = 'https://vgold.app/vgold_admin/api/encrypt_text/'
#         response = requests.post(url, json={"text": text})
#         if response.status_code == 200:
#             result = response.json()
#             return result.get('message_data', {}).get('encrypted_text', '')
#     except Exception as e:
#         print("Encryption API error:", str(e))
#     return ''
from Crypto.Cipher import AES

BLOCK_SIZE = 16

def pad(data):
    padding_length = BLOCK_SIZE - len(data.encode('utf-8')) % BLOCK_SIZE
    return data + chr(padding_length) * padding_length

def encrypt_data_aes256_ecb(data, key="k2hLr4X0ozNyZByj5DT66edtCEee1x+6"):
    try:
        padded_data = pad(data)
        key_bytes = key.encode('utf-8')
        if len(key_bytes) != 32:
            raise ValueError("Key must be exactly 32 bytes for AES-256 encryption.")
        cipher = AES.new(key_bytes, AES.MODE_ECB)
        encrypted_bytes = cipher.encrypt(padded_data.encode('utf-8'))
        return "\\x" + encrypted_bytes.hex()
    except Exception as e:
        return str(e)

def encrypt_text_using_api(text):
    try:
        encrypted_text = encrypt_data_aes256_ecb(text)
        return encrypted_text
    except Exception as e:
        print("Encryption error:", str(e))
        return ''

########################### Nominee Mandiate #########################################
import requests
from decimal import Decimal, ROUND_DOWN, InvalidOperation
# def nominee_mandiates(request):
#     user_data = request.session.get('user_data', {})
#     NomieeForUserId = user_data.get('User_Id')

#     if not NomieeForUserId:
#         return redirect('login')

#     # Call API and get user data
#     api_url = f'https://vgold.app/vgold_admin/m_api/deactivate_user/{NomieeForUserId}/'
#     try:
#         response = requests.get(api_url)
#         response_data = response.json()
#         nominee_data = response_data.get('message_data', {})
#         # print(nominee_data)
#     except Exception as e:
#         nominee_data = {}
#         # print("Error fetching nominee data:", e)
        
#         # Fetch live bank list from NPCI API
#     bank_list = []
#     try:
#         bank_response = requests.get('https://enachuat.npci.org.in:8086/apiservices_new/getLiveBankDtls')
#         if bank_response.status_code == 200:
#             bank_json = bank_response.json()
#             bank_list = bank_json.get("liveBankList", [])
#             # print("Fetched bank list:", bank_list)
#         else:
#             print("Failed to fetch bank list. Status:", bank_response.status_code)
#     except Exception as e:
#         print("Error fetching bank list:", str(e))
        

#     if request.method == "POST":
#         MsgId = request.POST.get("MsgId", "")
#         Customer_Name = request.POST.get("Customer_Name", "")
#         Customer_Mobile = request.POST.get("Customer_Mobile", "")
#         Customer_EmailId = request.POST.get("Customer_EmailId", "")
#         Customer_AccountNo = request.POST.get("Customer_AccountNo", "")
#         Customer_StartDate = request.POST.get("Customer_StartDate", "")
#         Customer_ExpiryDate = request.POST.get("Customer_ExpiryDate", "")
#         Customer_DebitAmount = request.POST.get("Customer_DebitAmount", "")
#         Customer_MaxAmount = request.POST.get("Customer_MaxAmount", "")
#         Customer_DebitFrequency = request.POST.get("Customer_DebitFrequency", "")
#         Customer_InstructedMemberId = request.POST.get("Customer_InstructedMemberId", "")
#         Short_Code = request.POST.get("Short_Code", "")
#         Customer_SequenceType = request.POST.get("Customer_SequenceType", "")
#         Merchant_Category_Code = request.POST.get("Merchant_Category_Code", "")
#         Customer_Reference1 = request.POST.get("Customer_Reference1", "")
#         Customer_Reference2 = request.POST.get("Customer_Reference2", "")
#         Channel = request.POST.get("Channel", "")
#         UtilCode = request.POST.get("UtilCode", "")
#         Filler1 = request.POST.get("Filler1", "")
#         Filler2 = request.POST.get("Filler2", "")
#         Filler3 = request.POST.get("Filler3", "")
#         Filler4 = request.POST.get("Filler4", "")
#         Filler5 = request.POST.get("Filler5", "")
#         Filler6 = request.POST.get("Filler6", "")
#         Filler7 = request.POST.get("Filler7", "")
#         Filler8 = request.POST.get("Filler8", "")
#         Filler9 = request.POST.get("Filler9", "")
#         Filler10 = request.POST.get("Filler10", "")
        
#         def to_decimal(value, other_value_present):
#             try:
#                 if value.strip() == "" and other_value_present:
#                     return ""
#                 return str(Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN))
#             except (InvalidOperation, TypeError, ValueError, AttributeError):
#                 if other_value_present:
#                     return ""
#                 return "0.00"

#         Customer_DebitAmount = to_decimal(Customer_DebitAmount, other_value_present=bool(Customer_MaxAmount.strip()))
#         Customer_MaxAmount = to_decimal(Customer_MaxAmount, other_value_present=bool(Customer_DebitAmount.strip()))

        
#         # print(Customer_DebitAmount,Customer_MaxAmount)

#         # Concatenate the required fields with the delimiter "|"
#         data_to_hash = f"{Customer_AccountNo}|{Customer_StartDate}|{Customer_ExpiryDate}|{Customer_DebitAmount}|{Customer_MaxAmount}"
#         # print(data_to_hash)
#         # Generate the SHA-2 checksum (SHA-256 is commonly used)
#         checksum = hashlib.sha256(data_to_hash.encode('utf-8')).hexdigest()

#         # Now the checksum is ready to be used
#         # print("Generated Checksum:", checksum)
#         # Store unencrypted values
#         unencrypted_payload = {
#             "MsgId": MsgId,
#             "Customer_Name": Customer_Name,
#             "Customer_Mobile": Customer_Mobile,
#             "Customer_EmailId": Customer_EmailId,
#             "Customer_AccountNo": Customer_AccountNo,
#             "Customer_StartDate": Customer_StartDate,
#             "Customer_ExpiryDate": Customer_ExpiryDate,
#             "Customer_DebitAmount": Customer_DebitAmount,
#             "Customer_MaxAmount": Customer_MaxAmount,
#             "Customer_DebitFrequency": Customer_DebitFrequency,
#             "Customer_InstructedMemberId": Customer_InstructedMemberId,
#             "Short_Code": Short_Code,
#             "Customer_SequenceType": Customer_SequenceType,
#             "Merchant_Category_Code": Merchant_Category_Code,
#             "Customer_Reference1": Customer_Reference1,
#             "Customer_Reference2": Customer_Reference2,
#             "Channel": Channel,
#             "UtilCode": UtilCode,
#             "Filler1": Filler1,
#             "Filler2": Filler2,
#             "Filler3": Filler3,
#             "Filler4": Filler4,
#             "Filler5": Filler5,
#             "Filler6": Filler6,
#             "Filler7": Filler7,
#             "Filler8": Filler8,
#             "Filler9": Filler9,
#             "Filler10": Filler10,
#             "checksum": checksum
#         }

#         print("UNENCRYPTED PAYLOAD:")
#         # print(unencrypted_payload)

#         Customer_Name = encrypt_text_using_api(Customer_Name)
#         # print("Encrypted Customer_Name:", Customer_Name)
        
#         Short_Code = encrypt_text_using_api(Short_Code)

#         Customer_Mobile = encrypt_text_using_api(Customer_Mobile)
#         # print("Encrypted Customer_Mobile:", Customer_Mobile)

#         Customer_EmailId = encrypt_text_using_api(Customer_EmailId)
#         # print("Encrypted Customer_EmailId:", Customer_EmailId)

#         Customer_AccountNo = encrypt_text_using_api(Customer_AccountNo)
#         # print("Encrypted Customer_AccountNo:", Customer_AccountNo)

#         Customer_Reference1 = encrypt_text_using_api(Customer_Reference1)
#         # print("Encrypted Customer_Reference1:", Customer_Reference1)

#         Customer_Reference2 = encrypt_text_using_api(Customer_Reference2)
#         # print("Encrypted Customer_Reference2:", Customer_Reference2)

#         UtilCode = encrypt_text_using_api(UtilCode)
#         # print("Encrypted UtilCode:", UtilCode)

#         # Convert to Decimal with 2 decimal places
#         # def to_decimal(value):
#         #     try:
#         #         return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
#         #     except (InvalidOperation, TypeError):
#         #         return Decimal('0.00')  # or handle as needed
        
#         # def to_decimal(value):
#         #     try:
#         #         return str(Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN))
#         #     except (InvalidOperation, TypeError, ValueError):
#         #         return "0.00"

#         # Customer_DebitAmount = to_decimal(Customer_DebitAmount)
#         # Customer_MaxAmount = to_decimal(Customer_MaxAmount)
     

#         # Construct final payload
#         payload = {
#             "MsgId": MsgId,
#             "Customer_Name": Customer_Name,
#             "Customer_Mobile": Customer_Mobile,
#             "Customer_EmailId": Customer_EmailId,
#             "Customer_AccountNo": Customer_AccountNo,
#             "Customer_StartDate": Customer_StartDate,
#             "Customer_ExpiryDate": Customer_ExpiryDate,
#             "Customer_DebitAmount": Customer_DebitAmount,
#             "Customer_MaxAmount": Customer_MaxAmount,
#             "Customer_DebitFrequency": Customer_DebitFrequency,
#             "Customer_InstructedMemberId": Customer_InstructedMemberId,
#             "Short_Code": Short_Code,
#             "Customer_SequenceType": Customer_SequenceType,
#             "Merchant_Category_Code": Merchant_Category_Code,
#             "Customer_Reference1": Customer_Reference1,
#             "Customer_Reference2": Customer_Reference2,
#             "Channel": Channel,
#             "UtilCode": UtilCode,
#             "Filler1": Filler1,
#             "Filler2": Filler2,
#             "Filler3": Filler3,
#             "Filler4": Filler4,
#             "Filler5": Filler5,
#             "Filler6": Filler6,
#             "Filler7": Filler7,
#             "Filler8": Filler8,
#             "Filler9": Filler9,
#             "Filler10": Filler10,
#             "checksum": checksum
#         }

#         # print(payload)

#         # Send the payload to the external API
#         # try:
#         #     response = requests.post("https://emandateut.hdfcbank.com/Emandate.aspx", data=payload)

#         #     # Log the response for debugging
#         #     print("Response Status Code:", response.status_code)
#         #     print("Response Text:", response.text)

#         #     # You can add error handling or status check if needed
#         #     if response.status_code == 200:
#         #         # success logic, if needed
#         #         pass
#         #     else:
#         #         # failure logic, log error or show message
#         #         print("Failed to post data to HDFC eMandate API")

#         # except Exception as e:
#         #     print("Exception occurred while sending data:", str(e))

#         # return redirect("nominee_mandiates")
        
#         return render(request, 'gold/auto_post_form.html', {'payload': payload})

#     return render(request, 'gold/nominee_mandiates.html', {'nominee_data': nominee_data,'bank_list': bank_list})
import random
import string
def nominee_mandiates(request,id):
    booking_id=id
    
    # api_url = f"http://127.0.0.1:8000/vgold_admin/api/account_id_detail/{booking_id}/"
    api_url = f"https://vgold.app/vgold_admin/api/account_id_detail/{booking_id}/"

    try:
        api_response = requests.get(api_url)
        response_json = api_response.json()

        if response_json.get("message_code") == 1000:
            api_data = response_json.get("message_data", {})
        else:
            api_data = {}
    except Exception as e:
        api_data = {}
    
    user_data = request.session.get('user_data', {})
    NomieeForUserId = user_data.get('User_Id')

    if not NomieeForUserId:
        return redirect('login')

    # Fetch nominee data
    api_url = f'https://vgold.app/vgold_admin/m_api/deactivate_user/{NomieeForUserId}/'
    try:
        response = requests.get(api_url)
        response_data = response.json()
        nominee_data = response_data.get('message_data', {})
    except Exception as e:
        nominee_data = {}

    # Fetch live bank list from NPCI
    bank_list = []
    try:
        bank_response = requests.get('https://enachuat.npci.org.in:8086/apiservices_new/getLiveBankDtls')
        if bank_response.status_code == 200:
            bank_json = bank_response.json()
            bank_list = bank_json.get("liveBankList", [])
            # Sort alphabetically by bankName
            bank_list = sorted(bank_list, key=lambda x: x.get("bankName", "").upper())
    except Exception as e:
        print("Error fetching bank list:", str(e))
        
        
    # Generate auto MsgId using first/last name
    def generate_msg_id(first_name, last_name):
        prefix = (first_name[:1] + last_name[:1]).upper()
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return prefix + random_part  # Total 12 characters

    first_name = user_data.get('UserFirstname', '')
    last_name = user_data.get('UserLastname', '')
    auto_msg_id = generate_msg_id(first_name, last_name)

    if request.method == "POST":
        MsgId = request.POST.get("MsgId", "")
        Customer_Name = request.POST.get("Customer_Name", "")
        Customer_Mobile = request.POST.get("Customer_Mobile", "")
        Customer_EmailId = request.POST.get("Customer_EmailId", "")
        Customer_AccountNo = request.POST.get("Customer_AccountNo", "")
        Customer_StartDate = request.POST.get("Customer_StartDate", "")
        Customer_ExpiryDate = request.POST.get("Customer_ExpiryDate", "")
        Customer_DebitAmount = request.POST.get("Customer_DebitAmount", "")
        Customer_MaxAmount = request.POST.get("Customer_MaxAmount", "")
        Customer_DebitFrequency = request.POST.get("Customer_DebitFrequency", "")
        Customer_InstructedMemberId = request.POST.get("Customer_InstructedMemberId", "")
        Short_Code = request.POST.get("Short_Code", "")
        Customer_SequenceType = request.POST.get("Customer_SequenceType", "")
        Merchant_Category_Code = request.POST.get("Merchant_Category_Code", "")
        Customer_Reference1 = request.POST.get("Customer_Reference1", "")
        Customer_Reference2 = request.POST.get("Customer_Reference2", "")
        Channel = request.POST.get("Channel", "")
        UtilCode = request.POST.get("UtilCode", "")
        Filler1 = request.POST.get("Filler1", "")
        Filler2 = request.POST.get("Filler2", "")
        Filler3 = request.POST.get("Filler3", "")
        Filler4 = request.POST.get("Filler4", "")
        Filler5 = request.POST.get("Filler5", "")
        Filler6 = request.POST.get("Filler6", "")
        Filler7 = request.POST.get("Filler7", "")
        Filler8 = request.POST.get("Filler8", "")
        Filler9 = request.POST.get("Filler9", "")
        Filler10 = request.POST.get("Filler10", "")

        def to_decimal(value, other_value_present):
            try:
                if value.strip() == "" and other_value_present:
                    return ""
                return str(Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN))
            except (InvalidOperation, TypeError, ValueError, AttributeError):
                if other_value_present:
                    return ""
                return "0.00"

        Customer_DebitAmount = to_decimal(Customer_DebitAmount, bool(Customer_MaxAmount.strip()))
        Customer_MaxAmount = to_decimal(Customer_MaxAmount, bool(Customer_DebitAmount.strip()))

        # Generate checksum
        data_to_hash = f"{Customer_AccountNo}|{Customer_StartDate}|{Customer_ExpiryDate}|{Customer_DebitAmount}|{Customer_MaxAmount}"
        checksum = hashlib.sha256(data_to_hash.encode('utf-8')).hexdigest()

        # Store unencrypted payload for debug or display
        unencrypted_payload = {
            "MsgId": MsgId,
            "Customer_Name": Customer_Name,
            "Customer_Mobile": Customer_Mobile,
            "Customer_EmailId": Customer_EmailId,
            "Customer_AccountNo": Customer_AccountNo,
            "Customer_StartDate": Customer_StartDate,
            "Customer_ExpiryDate": Customer_ExpiryDate,
            "Customer_DebitAmount": Customer_DebitAmount,
            "Customer_MaxAmount": Customer_MaxAmount,
            "Customer_DebitFrequency": Customer_DebitFrequency,
            "Customer_InstructedMemberId": Customer_InstructedMemberId,
            "Short_Code": Short_Code,
            "Customer_SequenceType": Customer_SequenceType,
            "Merchant_Category_Code": Merchant_Category_Code,
            "Customer_Reference1": Customer_Reference1,
            "Customer_Reference2": Customer_Reference2,
            "Channel": Channel,
            "UtilCode": UtilCode,
            "Filler1": Filler1,
            "Filler2": Filler2,
            "Filler3": Filler3,
            "Filler4": Filler4,
            "Filler5": Filler5,
            "Filler6": Filler6,
            "Filler7": Filler7,
            "Filler8": Filler8,
            "Filler9": Filler9,
            "Filler10": Filler10,
            "checksum": checksum
        }
        
        nach_payload = {
            "NMUserId": NomieeForUserId,
            "NMMsgId": MsgId,
            "NMCustomerAccountNo": Customer_AccountNo,
            "NMCustomerStartDate": Customer_StartDate,
            "NMCustomerExpiryDate": Customer_ExpiryDate,
            "NMCustomerDebitAmount": float(Customer_DebitAmount or 0.00),
            "NMCustomer_MaxAmount": float(Customer_MaxAmount or 0.00),
            "NMCustomer_DebitFrequency": Customer_DebitFrequency,
            "NMCustomer_InstructedMemberId": Customer_InstructedMemberId,
            "NMShortCode": Short_Code,
            "NMCustomerSequenceType": Customer_SequenceType,
            "NMMerchantCategoryCode": Merchant_Category_Code,
            "NMChannel": Channel,
            "NMCustomer_Reference1": Customer_Reference1,
            "NMCustomer_Reference2": Customer_Reference2,
            "NMUtilCode": UtilCode,
            "Filler1": Filler1,
            "Filler2": Filler2,
            "Filler3": Filler3,
            "Filler4": Filler4,
            "Filler5": Filler5,
            "Filler6": Filler6,
            "Filler7": Filler7,
            "Filler8": Filler8,
            "Filler9": Filler9,
            "Filler10": Filler10,
            "NMStatus": 0,
            "CreatedBy": NomieeForUserId
        }

        # Encrypt values
        Customer_Name = encrypt_text_using_api(Customer_Name)
        Customer_Mobile = encrypt_text_using_api(Customer_Mobile)
        Customer_EmailId = encrypt_text_using_api(Customer_EmailId)
        Customer_AccountNo = encrypt_text_using_api(Customer_AccountNo)
        Customer_Reference1 = encrypt_text_using_api(Customer_Reference1)
        Customer_Reference2 = encrypt_text_using_api(Customer_Reference2)
        Short_Code = encrypt_text_using_api(Short_Code)
        UtilCode = encrypt_text_using_api(UtilCode)

        # Final payload
        payload = {
            "MsgId": MsgId,
            "Customer_Name": Customer_Name,
            "Customer_Mobile": Customer_Mobile,
            "Customer_EmailId": Customer_EmailId,
            "Customer_AccountNo": Customer_AccountNo,
            "Customer_StartDate": Customer_StartDate,
            "Customer_ExpiryDate": Customer_ExpiryDate,
            "Customer_DebitAmount": Customer_DebitAmount,
            "Customer_MaxAmount": Customer_MaxAmount,
            "Customer_DebitFrequency": Customer_DebitFrequency,
            "Customer_InstructedMemberId": Customer_InstructedMemberId,
            "Short_Code": Short_Code,
            "Customer_SequenceType": Customer_SequenceType,
            "Merchant_Category_Code": Merchant_Category_Code,
            "Customer_Reference1": Customer_Reference1,
            "Customer_Reference2": Customer_Reference2,
            "Channel": Channel,
            "UtilCode": UtilCode,
            "Filler1": Filler1,
            "Filler2": Filler2,
            "Filler3": Filler3,
            "Filler4": Filler4,
            "Filler5": Filler5,
            "Filler6": Filler6,
            "Filler7": Filler7,
            "Filler8": Filler8,
            "Filler9": Filler9,
            "Filler10": Filler10,
            "checksum": checksum
        }


        try:
            insert_response = requests.post(
                # "http://127.0.0.1:8000/vgold_admin/m_api/add_nach_mandate/",
                "https://vgold.app/vgold_admin/m_api/add_nach_mandate/",
                json=nach_payload
            )
            response_json = insert_response.json()
            print("Insert Response:", response_json)
            if response_json.get("message_code") == 1000:
                messages.success(request, "NACH Mandate saved successfully.")
            else:
                messages.error(request, "Failed to save mandate.")
        except Exception as e:
            messages.error(request, f"API error: {str(e)}")

        return render(request, 'gold/auto_post_form.html', {'payload': payload})

    return render(request, 'gold/nominee_mandiates.html', {
        'api_data':api_data,
        'nominee_data': nominee_data,
        'bank_list': bank_list,
        'auto_msg_id': auto_msg_id
    })

# def agreement_otp(request,id):
#     account_display_id=id
#     # booking = tblGoldBookingDetails.objects.get(GBAccountId=account_display_id)
#     # user = booking.GBUserId
#     # user_name = f"{user.UserFirstname} {user.UserLastname or ''}".strip()
#     # user_mobileno = user.UserMobileNo
#     # account_id = booking.GBAccountDisplayId
#     # print(user_name,user_mobileno,account_id)
   
#     context = {
#         # 'booking':booking,
#         'mobile': '8600672101',
#         'account_display_id': 'VG001227',
#         'csrf_token': request.META.get("CSRF_COOKIE", ""),  # Ensure CSRF token for JS use
#     }
#     return render(request, 'gold/agrement_otp.html', context)

def agreement_otp(request, id):
    print(id)
    api_url = f"https://vgold.app/vgold_admin/api/account_id_detail/{id}/"
    # api_url = f"http://127.0.0.1:8000/vgold_admin/api/account_id_detail/{id}/"
    api_response_data = {
        "name": "",
        "mobile_no": "",
        "account_id": ""
    }

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            result = response.json()
            print(result)
            if result.get("message_code") == 1000:
                api_response_data = result.get("message_data", {})
    except Exception as e:
        print("API error:", str(e))  # Optional: log error

    context = {
        'name': api_response_data.get("name", ""),
        'mobile': api_response_data.get("mobile_no", ""),
        'account_display_id': api_response_data.get("account_id", ""),
        'csrf_token': request.META.get("CSRF_COOKIE", ""),  # Optional: for JS
    }

    return render(request, 'gold/agrement_otp.html', context)


######################################### Deposite Agreement ################################################
def deposite_agreement(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        print(number,999)
        
        # Prepare the data to send to the API
        payload = {
            "GDAccountDisplayId": number
        }
        
        # API URL
        # api_url = "http://127.0.0.1:8000/vgold_admin/m_api/get_deposite_agreement_copy/"
        api_url = "https://vgold.app/vgold_admin/m_api/get_deposite_agreement_copy/"

        try:
            # Send a POST request to the API
            response = requests.post(api_url, json=payload)
            response_data = response.json() 
            print(response_data) # Parse the JSON response

            if response_data.get('message_code') == 1000:  # Check for success
                agreement_data = response_data.get('message_data', {})
                gb_agreement_seen = agreement_data.get('DDAgreement_Seen')
                gb_agreement_url = agreement_data.get('DepositDocumentURL')
                
                if gb_agreement_seen == 1:
                    payloads={
                        "DepositDocumentAccountId": number
                    }
                    otp_api_url = "https://vgold.app/vgold_admin/m_api/send_deposite_agreement_otp/"
                    # otp_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/send_deposite_agreement_otp/"
                    otp_response = requests.post(otp_api_url, json=payloads).json()

                    if otp_response.get('message_code') == 1000:
                        return JsonResponse({
                            'message': 'OTP verification required',
                            'otp_required': True,
                            'GDAccountDisplayId': number
                        })
                    return JsonResponse({'error': 'Failed to send OTP'}, status=400)
                
                elif gb_agreement_seen == 2:
                    # Directly show the PDF
                    return JsonResponse({
                        'message': 'PDF available',
                        'pdf_url': gb_agreement_url,
                        'otp_required': False
                    })
                else:
                    return JsonResponse({'error': 'Unexpected DDAgreement_Seen value'}, status=400)
            else:
                return JsonResponse({
                    'error': 'Failed to fetch agreement details from API',
                    'message_text': response_data.get('message_text')
                }, status=400)
                
        except requests.exceptions.RequestException as e:
            # Handle API request exceptions
            return JsonResponse({'error': 'API request failed', 'details': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
######################################### Verify Deposite Agreement ######################################
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def verify_deposite_agreement_otp(request):
    if request.method == 'POST':
        try:
            # Parse the request data
            data = json.loads(request.body)
            gb_account_display_id = data.get('GBAccountDisplayId')
            gb_agreement_otp = int(data.get('GBAgreement_Otp'))
            
            print(gb_account_display_id)
            print(gb_agreement_otp)
            
            # Ensure the required fields are provided
            if not gb_account_display_id or not gb_agreement_otp:
                return JsonResponse({'success': False, 'message': 'Missing required fields.'}, status=400)
            
            # Prepare the payload for the external API
            payload = {
                "DDAgreement_Otp": gb_agreement_otp,
                "DepositDocumentAccountId":gb_account_display_id,
            }

            # Call the external API
            external_api_url = "https://vgold.app/vgold_admin/m_api/verify_deposit_agreement_otp/"
            # external_api_url = "http://127.0.0.1:8000/vgold_admin/m_api/verify_deposit_agreement_otp/"
            response = requests.post(external_api_url, json=payload)
            response_data = response.json()
            
            print(response_data)
            
            # Process the response from the API
            if response_data.get('message_code') == 1000:  # Success case
                message_data = response_data.get('message_data', {})
                pdf_url = message_data.get('DepositDocumentURL')
                
                return JsonResponse({
                    'success': True,
                    'pdf_url': pdf_url,
                    'message': response_data.get('message_text', 'Success')
                })
            else:
                # Handle error from the API
                return JsonResponse({
                    'success': False,
                    'message': response_data.get('message_text', 'Retry again')
                }, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
        except requests.RequestException as e:
            return JsonResponse({'success': False, 'message': 'Error connecting to the API.', 'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An unexpected error occurred.', 'error': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

################################################################################# 
def deposite_agreement_otp(request, id):
    print(id)
    api_url = f"https://vgold.app/vgold_admin/api/deposite_account_detail/{id}/"
    # api_url = f"http://127.0.0.1:8000/vgold_admin/api/deposite_account_detail/{id}/"
    api_response_data = {
        "name": "",
        "mobile_no": "",
        "account_id": ""
    }

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            result = response.json()
            print(result)
            if result.get("message_code") == 1000:
                api_response_data = result.get("message_data", {})
    except Exception as e:
        print("API error:", str(e))  # Optional: log error

    context = {
        'name': api_response_data.get("name", ""),
        'mobile': api_response_data.get("mobile_no", ""),
        'account_display_id': api_response_data.get("account_id", ""),
        'csrf_token': request.META.get("CSRF_COOKIE", ""),  # Optional: for JS
    }

    return render(request, 'gold/deposite_agrement_otp.html', context)

#######################################################################################
def payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')

        # Configuration from config file
        api_key = 'D672D5DCFB64471A651287AC44262D'
        merchant_id = 'SG2885'
        client_id = 'hdfcmaster'
        base_url = 'https://smartgatewayuat.hdfcbank.com'
        order_id = "testing-order-one455"
        # return_url = 'https://shop.merchant.com'
        return_url = f"http://127.0.0.1:8000/vgold/payment_status/{order_id}/"
        print(return_url)
        # return HttpResponse(return_url)

        # Encode API key
        encoded_key = base64.b64encode(f"{api_key}:".encode()).decode()

        # Payload for payment session
        payload = {
            "order_id": order_id,  # You should generate unique order_id in production
            "amount": amount,
            "customer_id": "1testing-customer-one",  # Match sample data
            "customer_email": "test@mail.com",
            "customer_phone": "8604613494",
            "payment_page_client_id": client_id,
            "action": "paymentPage",
            "currency": "INR",
            "return_url": return_url,
            "description": "Complete your payment",
            "first_name": "John",
            "last_name": "wick"
        }

        # Headers with auth and identifiers
        headers = {
            "Authorization": f"Basic {encoded_key}",
            "Content-Type": "application/json",
            "x-merchantid": merchant_id,
            "x-customerid": payload['customer_id']
        }

        try:
            response = requests.post(f"{base_url}/session", json=payload, headers=headers)
            response_data = response.json()
            print("Payment API Response:", response_data)

            if response.status_code == 200 and 'payment_links' in response_data:
                # if 'order_id' in response_data and response_data['order_id']:
                #     # request.session['order_id'] = response_data['order_id']
                #     print(f"Order ID '{response_data['order_id']}' stored in session.")
                
                return redirect(response_data['payment_links']['web'])
            else:
                error_message = response_data.get('message', 'Failed to create payment session')
                messages.error(request, f"Error: {error_message}")
        except Exception as e:
            messages.error(request, f"Exception occurred: {str(e)}")

    return render(request, 'gold/payment.html')

import uuid
import re
def regular_payment(request, id):
    amount = id
    # print("Received Amount in regular_payment:", amount)
    # Configuration from config file
    api_key = 'D672D5DCFB64471A651287AC44262D'
    merchant_id = 'SG2885'
    client_id = 'hdfcmaster'
    base_url = 'https://smartgatewayuat.hdfcbank.com'
    # order_id = "testing-order-one865"
    
    # Extract customer name
     # Get customer name from session
    user_data = request.session.get('user_data', {})
    customer_name = user_data.get('UserFirstname', 'user')
    last_name = user_data.get('UserLastname', '')
    mobile_no = str(user_data.get('UserMobileNo', '0000000000'))
    email = user_data.get('UserEmail', 'user@example.com')
    user_id = user_data.get('User_Id', 994)
    
    # Sanitize name: only alphanumeric, lowercase
    email = user_data.get('UserEmail', 'user@example.com')


    # Sanitize name: only alphanumeric, lowercase
    safe_name = re.sub(r'[^a-zA-Z0-9]', '', customer_name).lower()

    # Limit name part to 10 characters max
    name_part = safe_name[:10]

    # Generate a random suffix (remaining to keep total 20 chars)
    remaining_len = 20 - len(name_part)
    random_suffix = uuid.uuid4().hex[:remaining_len]  # use hex for uniqueness

    # Final order_id
    order_id = f"{name_part}{random_suffix}"
    
    # return_url = 'https://shop.merchant.com'
    # return_url = f"http://127.0.0.1:8001/vgold/payment_status/{order_id}/"
    return_url = f"https://vgold.app/vgold/payment_status/{order_id}/"
    # print(return_url)
    # return HttpResponse(return_url)

    # Encode API key
    encoded_key = base64.b64encode(f"{api_key}:".encode()).decode()

    # Payload for payment session
    # payload = {
    #     "order_id": order_id,  # You should generate unique order_id in production
    #     "amount": amount,
    #     "customer_id": "testing-customer-one",  # Match sample data
    #     "customer_email": "sl@mail.com",
    #     "customer_phone": "9850180648",
    #     "payment_page_client_id": client_id,
    #     "action": "paymentPage",
    #     "currency": "INR",
    #     "return_url": return_url,
    #     "description": "Complete your payment",
    #     "first_name": "Testing",
    #     "last_name": "1"
    # }
    payload = {
        "order_id": order_id,  # You should generate unique order_id in production
        "amount": amount,
        "customer_id": "testing-customer-one",  # Match sample data
        # "customer_id": f"user-{user_data.get('User_Id', '0')}", 
        "customer_email": email,
        "customer_phone": mobile_no,
        "payment_page_client_id": client_id,
        "action": "paymentPage",
        "currency": "INR",
        "return_url": return_url,
        "description": "Complete your payment",
        "first_name": customer_name,
        "last_name": last_name
    }

    # Headers with auth and identifiers
    headers = {
        "Authorization": f"Basic {encoded_key}",
        "Content-Type": "application/json",
        "x-merchantid": merchant_id,
        "x-customerid": payload['customer_id']
    }

    try:
        response = requests.post(f"{base_url}/session", json=payload, headers=headers)
        response_data = response.json()
        print("Payment API Response:", response_data)

        if response.status_code == 200 and 'payment_links' in response_data:
            # if 'order_id' in response_data and response_data['order_id']:
            #     # request.session['order_id'] = response_data['order_id']
            #     print(f"Order ID '{response_data['order_id']}' stored in session.")
            
            transaction_payload = {
                "PTUserId": user_id,
                "PTReceive_id": "VGOLD123456789",  # Can be dynamic if needed
                "PTOrder_id": order_id,  # Using generated order_id
                "PTStatus": 0,  # Initially pending
                "PTAmount": amount,
                "CreatedBy": user_id
            }

            try:
                transaction_response = requests.post(
                    # "http://127.0.0.1:8000/vgold_admin/m_api/add_payment_transaction/",
                    "https://vgold.app/vgold_admin/m_api/add_payment_transaction/",
                    json=transaction_payload
                )
                print("Transaction API Response:", transaction_response.json())
            except Exception as e:
                messages.error(request, f"Failed to record transaction: {e}")
            
            return redirect(response_data['payment_links']['web'])
        else:
            error_message = response_data.get('message', 'Failed to create payment session')
            messages.error(request, f"Error: {error_message}")
    except Exception as e:
        messages.error(request, f"Exception occurred: {str(e)}")



# @csrf_exempt
# def payment_status(request,id):
#     """
#     This function will be called as the return_url from the HDFC payment gateway.
#     It retrieves the order_id from the session and then calls the HDFC order status API.
#     """
#     context = {
#         "order_id": "N/A",
#         "payment_status": "Unknown",
#         "amount": "N/A",
#         "message": "An unexpected error occurred or no order ID found."
#     }
    
#     order_id = id
#     print(order_id)
    
#     if order_id :
        
#         # Configuration (same as in payment function, consider centralizing if many functions use it)
#         api_key = 'D672D5DCFB64471A651287AC44262D'
#         merchant_id = 'SG2885'
#         base_url = 'https://smartgatewayuat.hdfcbank.com'

#         # Encode API key
#         encoded_key = base64.b64encode(f"{api_key}:".encode()).decode()

#         # Headers for the order status API call
#         headers = {
#             "Authorization": f"Basic {encoded_key}",
#             "Content-Type": "application/json",
#             "x-merchantid": merchant_id,
#         }

#         try:
#             # Call the HDFC order status API
#             status_response = requests.get(f"{base_url}/orders/{order_id}", headers=headers)
#             status_data = status_response.json()
#             print("Order Status API Response:", status_data)

#             if status_response.status_code == 200:
#                 hdfc_status = status_data.get('status', 'N/A').upper() # Get status and convert to uppercase for consistent checking

#                 if hdfc_status == 'CHARGED':
#                     payment_status_display = 'success'
#                     message = "Payment was successful!"
#                 elif hdfc_status == 'PENDING':
#                     payment_status_display = 'pending'
#                     message = "Payment is pending. Please check again later."
#                 elif hdfc_status == 'FAILED' or hdfc_status == 'CANCELLED':
#                     payment_status_display = 'failed'
#                     message = f"Payment failed. Reason: {status_data.get('resp_message', 'N/A')}"
#                 else:
#                     payment_status_display = 'unknown'
#                     message = f"Payment status is: {hdfc_status}. For more details, contact support."

#                 context = {
#                     "order_id": order_id,
#                     "payment_status": payment_status_display, # Lowercased for HTML template
#                     "amount": status_data.get('amount', 'N/A'),
#                     "message": message,
#                     "customer_email": status_data.get('customer_email', 'N/A'),
#                     "customer_phone": status_data.get('customer_phone', 'N/A'),
#                     "transaction_id": status_data.get('txn_id', 'N/A'),
#                     "payment_method": status_data.get('payment_method', 'N/A'),
#                 }
#                 # You might want to remove the order_id from the session after processing
#                 # del request.session['order_id']
#             else:
#                 error_message = status_data.get('message', 'Failed to retrieve payment status from HDFC.')
#                 context = {
#                     "order_id": order_id,
#                     "payment_status": "error", # Lowercased for HTML template
#                     "message": f"Error retrieving payment status from HDFC: {error_message}"
#                 }
#         except requests.exceptions.RequestException as req_e:
#             context = {
#                 "order_id": order_id,
#                 "payment_status": "error",
#                 "message": f"Network or API connection error: {str(req_e)}"
#             }
#         except Exception as e:
#             context = {
#                 "order_id": order_id,
#                 "payment_status": "error",
#                 "message": f"An unexpected exception occurred: {str(e)}"
#             }
#     else:
#         context = {
#             "order_id": "N/A",
#             "payment_status": "no_order_id",
#             "message": "No order ID found in your session. This might indicate an issue with the payment flow or a direct access to this page."
#         }
    
#     return render(request, 'gold/payment_status.html', context)

from django.utils.timezone import now
@csrf_exempt
def payment_status(request,id):
    """
    This function will be called as the return_url from the HDFC payment gateway.
    It retrieves the order_id from the session and then calls the HDFC order status API.
    """
    context = {
        "order_id": "N/A",
        "payment_status": "Unknown",
        "amount": "N/A",
        "message": "An unexpected error occurred or no order ID found."
    }
    
    order_id = id
    print(order_id)
    
    if order_id :
        
        # Configuration (same as in payment function, consider centralizing if many functions use it)
        api_key = 'D672D5DCFB64471A651287AC44262D'
        merchant_id = 'SG2885'
        base_url = 'https://smartgatewayuat.hdfcbank.com'

        # Encode API key
        encoded_key = base64.b64encode(f"{api_key}:".encode()).decode()

        # Headers for the order status API call
        headers = {
            "Authorization": f"Basic {encoded_key}",
            "Content-Type": "application/json",
            "x-merchantid": merchant_id,
        }

        try:
            # Call the HDFC order status API
            status_response = requests.get(f"{base_url}/orders/{order_id}", headers=headers)
            status_data = status_response.json()
            print("Order Status API Response:", status_data)

            if status_response.status_code == 200:
                hdfc_status = status_data.get('status', 'N/A').upper()
                # hdfc_status = "PENDING_VBV"
                status_id = str(status_data.get('status_id', ''))

                # Default fallback values
                payment_status_display = 'unknown'
                message = f"Payment status is: {hdfc_status}. Please contact support."

                # Mapping HDFC status to user-friendly status
                status_map = {
                    'CHARGED': ('success', "Payment was successful!"),
                    'PENDING_VBV': ('pending', "Payment authentication is in progress. Please wait."),
                    'AUTHORIZED': ('pending', "Transaction authorized. Awaiting capture."),
                    'AUTHORIZING': ('pending', "Awaiting bank authorization."),
                    'STARTED': ('pending', "Transaction is pending due to gateway issues."),
                    'AUTO_REFUNDED': ('failed', "Payment was auto-refunded."),
                    'AUTHENTICATION_FAILED': ('failed', "Authentication failed. Please try again."),
                    'AUTHORIZATION_FAILED': ('failed', "Authorization failed. Bank refused the transaction."),
                    'JUSPAY_DECLINED': ('failed', "Transaction failed during processing. Please retry."),
                    'VOIDED': ('failed', "Transaction was voided."),
                    'VOID_INITIATED': ('pending', "Void is in progress."),
                    'VOID_FAILED': ('failed', "Void request failed."),
                    'CAPTURE_INITIATED': ('pending', "Capture initiated."),
                    'CAPTURE_FAILED': ('failed', "Capture failed."),
                    'FAILED': ('failed', status_data.get('resp_message', "Transaction failed.")),
                    'CANCELLED': ('failed', "Transaction was cancelled."),
                }

                if hdfc_status in status_map:
                    # Inside your `if hdfc_status in status_map:` and when payment is CHARGED
                    if hdfc_status == 'CHARGED':
                        try:
                            # You need to determine how to get the user_id (PPUserId). 
                            # This example assumes it's somehow available; update logic as needed.
                            user_id = request.session.get('user_data', {}).get('User_Id', None)
                            if not user_id:
                                user_id = 994  # Fallback hardcoded for example

                            # Prepare payload
                            partial_payload = {
                                "PPUserId": user_id,
                                "PPDate": now().strftime('%Y-%m-%dT%H:%M'),
                                "PPStatus": 1,
                                "PPAmount": status_data.get('amount', 0),
                                "CreatedBy": user_id,  # Or another user ID if different
                                "PPTransectionId": status_data.get('txn_id', '')
                            }

                            # Send to your internal API
                            response = requests.post(
                                # "http://127.0.0.1:8000/vgold_admin/m_api/add_partial_payment/",
                                "https://vgold.app/vgold_admin/m_api/add_partial_payment/",
                                data=json.dumps(partial_payload),
                                headers={"Content-Type": "application/json"}
                            )

                            print("Partial Payment API Response:", response.status_code, response.text)
                            if response.status_code == 200:
                                resp_data = response.json()
                                context["api_message"] = resp_data.get('message_text', '')

                        except Exception as e:
                            print("Failed to send partial payment:", str(e))
                            
                    payment_status_display, message = status_map[hdfc_status]

                context = {
                    "order_id": order_id,
                    "payment_status": payment_status_display,
                    "amount": status_data.get('amount', 'N/A'),
                    "message": message,
                    "customer_email": status_data.get('customer_email', 'N/A'),
                    "customer_phone": status_data.get('customer_phone', 'N/A'),
                    "transaction_id": status_data.get('txn_id', 'N/A'),
                    "payment_method": status_data.get('payment_method', 'N/A'),
                }

                # You might want to remove the order_id from the session after processing
                # del request.session['order_id']
            else:
                error_message = status_data.get('message', 'Failed to retrieve payment status from HDFC.')
                
                # Still try to extract and show available details from the response
                context = {
                    "order_id": order_id,
                    "payment_status": "error",  # Used for status icon and styling
                    "message": f"Error retrieving payment status from HDFC: {error_message}",
                    "amount": status_data.get('amount', 'N/A'),
                    "customer_email": status_data.get('customer_email', 'N/A'),
                    "customer_phone": status_data.get('customer_phone', 'N/A'),
                    "transaction_id": status_data.get('txn_id', 'N/A'),
                    "payment_method": status_data.get('payment_method', 'N/A'),
                }

        except requests.exceptions.RequestException as req_e:
            context = {
                "order_id": order_id,
                "payment_status": "error",
                "message": f"Network or API connection error: {str(req_e)}"
            }
        except Exception as e:
            context = {
                "order_id": order_id,
                "payment_status": "error",
                "message": f"An unexpected exception occurred: {str(e)}"
            }
    else:
        context = {
            "order_id": "N/A",
            "payment_status": "no_order_id",
            "message": "No order ID found in your session. This might indicate an issue with the payment flow or a direct access to this page."
        }
    
    return render(request, 'gold/payment_status.html', context)


##################################################################################

# def installment_op(request):
#     if request.method == 'POST':
#         pay_type = request.POST.get('pay_type')

#         if pay_type == 'total':
#             booking_nos = request.POST.getlist('booking_no')
#             booking_amounts = request.POST.getlist('booking_amount')

#             total_info = list(zip(booking_nos, booking_amounts))
#             print("=== Total Pay Clicked ===")
#             for b_no, amt in total_info:
#                 print(f"Booking No: {b_no}, Amount: ₹{amt}")

#             total_amount = sum(float(amt) for amt in booking_amounts)
#             return redirect('regular_payment', id=total_amount)

#         elif pay_type == 'partial':
#             partial_amount = request.POST.get('partial_amount')
#             print("=== Partial Pay Clicked ===")
#             print("Partial Amount:", partial_amount)
#             return redirect('regular_payment', id=partial_amount)
        
#     # api_url = 'http://127.0.0.1:8000/vgold_admin/m_api/get_installemnt_info/'
#     api_url = 'https://vgold.app/vgold_admin/m_api/get_installemnt_info/'
#     user_data = request.session.get('user_data', {})
    
#     # Extract user_id from the session data
#     user_id = user_data.get('User_Id')  # Correct key for 'User_Id'
#     print(user_id,"3680")

#     # If user_id is not found in the session data, return an error message
#     if not user_id:
#         return redirect('login') 
    
#     # Prepare the payload for the API call
#     payload = {'user_id': user_id}
#     # payload = {"user_id": 40}

#     try:
#         # Make the API call
#         response = requests.post(api_url, json=payload)
#         response_data = response.json()
#         print(response_data)

#         # Check if the API call was successful
#         if response.status_code == 200 and response_data.get('message_code') == 1000:
#             raw_bookings = []

#             for item in response_data.get('message_data', []):
#                 # Extract the needed data
#                 booking = {
#                     'booking_no': item.get('gold_booking_id', ''),
#                     'installment_amount': float(item.get('current_month_emi_amount', 0.00)),
#                     'tenure': f"{item.get('tennure', 0)} months",
#                     'gold': f"{item.get('gold', 0)} Gm",
#                     'installment_date': item.get('installment_date', '') or item.get('added_date', '') # or item['added_date'] if needed
#                 }
#                 raw_bookings.append(booking)

#             # Calculate total
#             total_installment_amount = sum(b['installment_amount'] for b in raw_bookings)

#             return render(request, 'gold/installment_op.html', {
#                 'bookings': raw_bookings,
#                 'total_amount': total_installment_amount
#             })
#         else:
#             return HttpResponse("Failed to fetch data from API", status=500)

#     except Exception as e:
#         return HttpResponse(f"An error occurred: {str(e)}", status=500)


def installment_op(request):
    if request.method == 'POST':
        pay_type = request.POST.get('pay_type')

        if pay_type == 'total':
            booking_nos = request.POST.getlist('booking_no')
            booking_amounts = request.POST.getlist('booking_amount')

            total_info = list(zip(booking_nos, booking_amounts))
            print("=== Total Pay Clicked ===")
            for b_no, amt in total_info:
                print(f"Booking No: {b_no}, Amount: ₹{amt}")

            total_amount = sum(float(amt) for amt in booking_amounts)
            return redirect('regular_payment', id=total_amount)

        elif pay_type == 'partial':
            partial_amount = request.POST.get('partial_amount')
            print("=== Partial Pay Clicked ===")
            print("Partial Amount:", partial_amount)
            return redirect('regular_payment', id=partial_amount)

    api_url = 'https://vgold.app/vgold_admin/m_api/get_installemnt_info/'
    user_data = request.session.get('user_data', {})
    user_id = user_data.get('User_Id')

    if not user_id:
        return redirect('login')

    payload = {'user_id': user_id}

    try:
        response = requests.post(api_url, json=payload)
        response_data = response.json()
        print(response_data)

        raw_bookings = []
        total_installment_amount = 0
        no_bookings_message = None

        if response.status_code == 200 and response_data.get('message_code') == 1000:
            for item in response_data.get('message_data', []):
                booking = {
                    'booking_no': item.get('gold_booking_id', ''),
                    'installment_amount': float(item.get('current_month_emi_amount', 0.00)),
                    'tenure': f"{item.get('tennure', 0)} months",
                    'gold': f"{item.get('gold', 0)} Gm",
                    'installment_date': item.get('installment_date', '') or item.get('added_date', '')
                }
                raw_bookings.append(booking)

            total_installment_amount = sum(b['installment_amount'] for b in raw_bookings)

        else:
            # If message_code is not 1000 (e.g., 999), show message and empty booking list
            no_bookings_message = "No active bookings available."

        return render(request, 'gold/installment_op.html', {
            'bookings': raw_bookings,
            'total_amount': total_installment_amount,
            'no_bookings_message': no_bookings_message
        })

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
    
    
def nach_form(request):
    user_data = request.session.get('user_data', {})
    
    # Extract user_id from session
    user_id = user_data.get('User_Id')
    
    if not user_id:
        return redirect('login')
    
    api_url = "https://vgold.app/vgold_admin/m_api/gold_booking_history/"
    payload = {'user_id': user_id}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    bookings = []
    try:
        response = requests.post(api_url, data=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data.get("message_code") == 1000:
            bookings = data.get("message_data", [])
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

    return render(request, 'gold/nach_form.html', {'bookings': bookings})
