import pandas as pd
from openpyxl import load_workbook
import time
from datetime import datetime
from plyer import notification
import pyttsx3


engine = pyttsx3.init('sapi5')# Initialize engine for the voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)# Set voice for the reminder


def clean_time(t,m):
    '''
    This function will clean the time and convert it to 24 hours time.
    '''
    temp = int(t.split(':')[0])
    if m=='pm' and temp!=12:
        temp+=12
        return str(temp)+':'+str(t.split(':')[1])+':00'
    else:
        return t+':00'


def check_valid_time(tm):
    '''
    This function is used to check whether the entered time is valid or not.
    '''
    if int(tm.split(':')[0]) >=24:
        return False
    else:
        return True


def speak(audio):
    '''
    This function will be used to give output in form of voice.
    '''
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    diary = load_workbook('ReminderDiary.xlsx')['Sheet1'].values    # Loading workbook.
    next(diary) # Incrementing the excel sheet inorder to avoid header frame.
    df = pd.DataFrame(data=diary,columns=('time','am/pm','task','status'))  # creating dataframe from excel.
    del diary   # deleting the workbook variable which is now of no longer use.
    for index, row in df.iterrows():    # Iterating the diary, checking the schedule
        if row['time'] == None:
            break
        try:
            a_time = clean_time(row['time'].strftime('%H:%M:%S'),row['am/pm'])  # Converting to 24 hour time.
            if not(check_valid_time(a_time)):
                continue
            current_time = datetime.now().strftime('%H:%M:%S')  # getting current time.
            tdelta = datetime.strptime(a_time, '%H:%M:%S') - datetime.strptime(current_time, '%H:%M:%S')   # Calculating the time left for the next reminder.
            del current_time
            tdelta = str(tdelta).split(':')
            secs = int(int(tdelta[0])*3600+int(tdelta[1])*60+int(tdelta[2]))    # Converting the remaining time into seconds.
            del tdelta,a_time
            time.sleep(secs)    # Sending program to sleep mode until next event occurs.
            notification.notify(
                title=row['task'],
                app_icon="D:\Github Projects\Basic-Python-Projects\Task_Reminder\img\Task_Reminder.ico",
                message='Hey ayush its time to complete your following task... '+row['task'],
                timeout=3,
            )   # sending notification in windows.
            time.sleep(1)
            speak('Hey ayush its time to complete your task named '+row['task'])    # Notifying in a voice form.

        except Exception as e:
            print('There is some error in your scheduling')
            print(e)
    print('Its end of your schedule. Have a great day ahead')   # indicating end of schedule.