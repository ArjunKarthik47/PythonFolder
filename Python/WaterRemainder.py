#import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "The National Academies of Sciences, Engineering, and Medicine suggest that men should drink about 3.7 liters (16 cups) of fluids per day, and women should drink about 2.7 liters (11 cups) of fluids per day.",
            timeout = 5
    )
    #time.sleep(60*60)