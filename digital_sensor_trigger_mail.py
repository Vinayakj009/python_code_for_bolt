import requests, time

key='PLACE YOUR MAILGUN API KEY HERE'
sandbox='YOUR SANDBOX URL HERE'
recipient='YOUR EMAIL HERE' #you can only send mails to yourself
bolt_api_key='PLACE YOUR BOLTCLOUD API KEY HERE' #This api key can be found in API tab of bolt cloud login
bolt_id='PLACE YOUR BOLT DEVICE ID HERE' #example BOLT345678. This device id is visible in you boltcloud login devices tab, or products tab
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
    r = requests.get('http://cloud.boltiot.com/remote/'+bolt_api_key+'/digitalRead?pin=4&deviceName='+bolt_id)
    data = json.loads(r.text)
    try:
        print data['value']
        obstacle_detected = int(data['value'])
        if obstacle_detected == 0: #LOW volatge on pin 4
                send_mail("Obstacle detected at " + str(time.time()))
    except Exception as e:
        print "Error",e
    time.sleep(5)
