#This is the main of the program. It organizates all the function callings and sets the loop to verify every 10 minutes the mailbox

#Imports the main function and the paths to the folders
import time
from email_checker import verify_email
from util import EXCEL_PATH, BASE_FOLDER

#Sets the timer for the email verifying
def check_emails(intervalo_minutos=10):
    while True:
        print("メールボックスを確認しています")
        verify_email(EXCEL_PATH, BASE_FOLDER)
        print(f"メール確認が {intervalo_minutos}分に始まります")
        
        segundos_restantes = intervalo_minutos * 60
        #Infinite loop that verifies the emails
        while segundos_restantes > 0:
            minutos = segundos_restantes // 60
            segundos = segundos_restantes % 60
            print(f"確認まで後{minutos:02d}分{segundos:02d}秒", end='\r')
            time.sleep(1)
            segundos_restantes -= 1

        print() 

if __name__ == "__main__":
    check_emails()
