import requests,json
import time

ON = 1
OFF = 0
switch_pin=0
ldr_pin=4
status_flag = OFF
bolt_api_key='PLACE YOUR BOLTCLOUD API KEY HERE' #This api key can be found in API tab of bolt cloud login
bolt_id='PLACE YOUR BOLT DEVICE ID HERE' #example BOLT345678. This device id is visible in you boltcloud login devices tab, or products tab



def switch_on():
        r = requests.get("http://cloud.boltiot.com/remote/"+bolt_api_key+"/digitalWrite?pin="+switch_pin+"&state=HIGH&"+
                         "deviceName="+bolt_id)
        print "On"

def switch_off():
        r = requests.get("http://cloud.boltiot.com/remote/"+bolt_api_key+"/digitalWrite?pin="+switch_pin+"&state=LOW&"+
                 "deviceName="+bolt_id)
        print "Off"

def get_ldr_data():
        r = requests.get("http://cloud.boltiot.com/remote/"+bolt_api_key+"/digitalRead?pin="+ldr_pin+"&"+
                         "deviceName="+bolt_id)
        data = json.loads(r.text)
        print "ldr sensor value = ", data['value']
        return data['value']

switch_off()

#note the code below make sure the LDR is not in the same room as the Bulb
#it is ideal that the LDR monitors sunlight from a diff Bolt
#Bulb should be connected to a diff Bolt in the room
#If both are in the same room the code will possibly make the Bulb toggle every 5 secs
while True:
        try:
            ldr_data = int(get_ldr_data())
        if ldr_data == 0 and status_flag == OFF: #Low light, LOW on pin 4
            switch_on()
            status_flag = ON
            print "status",status_flag
        elif ldr_data == 1 and status_flag == ON: #Bright light , HIGH on pin 4
            switch_off()
            status_flag = OFF
            print "status",status_flag
        else:
            pass
        time.sleep(5)
        except Exception as e:
            print e
            time.sleep(5)

