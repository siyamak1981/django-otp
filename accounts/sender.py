from kavenegar import *
def send_otp(otp):
    try:
        api = KavenegarAPI('544654624F3452376F3043363432494567396C682B67314D7845595273324355304F4A3149425362464B493D')
        params = {
            'sender': '',#optional
            'receptor': f'{otp.receiver}',#multiple mobile number, split by comma
            'message': f'{otp.code} کد تایید شما',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)


