import os
import time
from slackclient import SlackClient

# instantiate Slack & Twilio clients
sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    PURPOSE = "This is *Dynamic Index* "+"```We aim To produce winners in the Ongoing Facebook Bot challenge by working together as a Major team, hence mentoring & providing help to Sub-Teams partaking in the Facebook Bot Challenge```"
    if sc.rtm_connect():
        while True:
            new_evts = sc.rtm_read()
            for evt in new_evts:
                if 'subtype' in evt:
                    if evt['subtype'] == 'channel_join' and 'joined' in evt['text']:
                        user_info=sc.api_call("users.info", user=evt['user'])
                        response = "Welcome <@"+user_info['user']['name']+">"+"\n"+PURPOSE
                        sc.api_call("chat.postMessage", channel=evt['channel'], text=response, as_user=True)
                if 'text' in evt:      
                    if evt['type'] == 'message' and "<@U4G8M9WEB>" in evt['text']:
                        user_info=sc.api_call("users.info", user=evt['user'])
                        response = "Hi, <@"+user_info['user']['name']+">"+"\n"+" I only welcome new members to the channel."
                        sc.api_call("chat.postMessage", channel=evt['channel'], text=response, as_user=True)
    else:
        print "Connection Failed, invalid token?"