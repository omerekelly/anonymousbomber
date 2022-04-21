import requests
import threading

num_times = int(input("Enter number of times to send: "))
message = input("Enter message: ")
link = input("Enter link: ")

def anon_bomber(count, limit):
    for i in range(1,limit):
     count+=1
     response = requests.post(link, data={'message':f'{message}.{count}','btn-msg':''})
     if response.status_code == 200:
         print(f'message sent {count} times')




t1=threading.Thread(target=anon_bomber(0, num_times+1), args=(10,))

t1.start()
t1.join()
print("Done!")
