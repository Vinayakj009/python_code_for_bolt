import requests, time

key='YOUR API KEY HERE'
sandbox='YOUR SANDBOX URL HERE'
recipient='YOUR EMAIL HERE' #you can only send mails to yourself
# TO send mail to other users you must first verify the user from mailgun website

def send_mail(body):
    request_url='https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request=requests.post(request_url,auth=('api',key),data={
    'from':'hello@example.com',
    'to':recipient,
    'subject':'Obstacle detected',
    'text': body
    })
    print'Status: {0}'.format(request.status_code)
    print'Body:   {0}'.format(request.text)

while True:
    #replace api_key and BOLT id in the statement below with you Bolt Cloud API key and Bolt hardware ID
    r = requests.get('http://cloud.boltiot.com/remote/api_key/digitalRead?pin=4&deviceName=BOLTXXXXXX')
    data = json.loads(r.text)
    try:
        print data['value']
        obstacle_detected = int(data['value'])
        if obstacle_detected == 0: #LOW volatge on pin 4
                send_mail("Obstacle detected at " + str(time.time()))
    except Exception as e:
        print "Error",e
    time.sleep(5)
