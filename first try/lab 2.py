import tweepy
 
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
 
def main():
 
  cfg = { 
    "consumer_key"        : "cbaYof2MIyE78O0oYOl4aecc1",
    "consumer_secret"     : "bLJTCKVL7wDUVOLQIyHevDGjAfga1PVifcSGtryISoUHhuLkRG",
    "access_token"        : "1494408772227411972-MDHqUqKpNL0sMfbk3KcaGFQUfWH4ty",
    "access_token_secret" : "Id8p66fhBn4PxzIhe0fKPA02tZQcJTkk3D9D0ccWjpMQo" 
    }
 
  api = get_api(cfg)

  photo_path = '123.jpg'
  tweet_2 = "hello"
  api.update_status_with_media( status = tweet_2 ,filename = photo_path)
 
 
if __name__ == "__main__":
  main()
