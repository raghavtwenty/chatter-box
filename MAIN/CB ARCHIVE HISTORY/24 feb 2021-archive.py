'''CHATTER BOX
SIMPLY LOVABLE
Made in 🤍️️ with 🇮🇳!!!

© DESIGNED & PROGRAMMED BY RAGHAVA, KV COIMBATORE - (BATCH-2020).
CREATED ON 13 DEC 2020.
LAST UPDATED ON 23 FEB 2021.'''


#______________________________________________________________________________________________________________________
'''[CREDITS & SPECIAL MENTIONS]
SHEMEER.K.A - PGT, COMPUTER SCIENCE, KV COIMBATORE.

[VOICE OVER CREDIT]
POORVEKKA, STUDENT, KV CBE - (BATCH-2020).'''


#______________________________________________________________________________________________________________________
#MYSQL DATABASE

'''CREATE TABLE CHATTER_BOX_PROFILES(USERNAME VARCHAR(50) PRIMARY KEY,CHATTER_NAME CHAR(50),CHATTER_PHONE_NUMBER BIGINT,
DATE_OF_BIRTH DATE,GENDER CHAR (20),ACCOUNT_PASSWORD VARCHAR(50));'''


#______________________________________________________________________________________________________________________
#IMPORTING FUNCTIONS
import sys
import mysql.connector as mc
import pygame
import random
import datetime
import pickle


#______________________________________________________________________________________________________________________
#xxxxxxxxxxxxxx CREATING FUNCTIONS xxxxxxxxxxxxx

#ESTABLISHING CONNECTION
db=mc.connect(host='localhost',user='root',password='00000000',database='CHATTER_BOX')
mc1=db.cursor()


#----------------------------------------------------------------------------------------------------------------------
#VOICE OVER
def voiceover(vo):
    pygame.mixer.init()
    pygame.mixer.music.load(vo)
    pygame.mixer.music.play()


#----------------------------------------------------------------------------------------------------------------------
#NOTIFICATION CENTRE
def notification_centre():
    try:
        fh_uname = sin_cb_username
        fh_read_notification=r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/NOTIFICATION CENTRE/NC_'+sin_cb_username+'_NOTIFICATION CENTRE.dat'
        with open(fh_read_notification,'rb') as fh_ncl_notification:
            str = ' '
            while str:
                str = pickle.load(fh_ncl_notification)
                str1 = str.strip('\n')
                print(str1)
            else:
                fh_ncl_notification.close()
    except:
        fh_ncl_notification.close()


#----------------------------------------------------------------------------------------------------------------------
#SECURITY ALERT
def security_alert_fh(sec_alert):
    fh_ncl_sa = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/NOTIFICATION CENTRE/NC_' + cad_sin_cb_username + '_NOTIFICATION CENTRE.dat'
    with open(fh_ncl_sa, 'ab') as notification_cl_sa:
        datetime_str_sa = str(datetime.datetime.now())
        sec_alert_message = '\n\t\t\t\t\t\t⚠️ SECURITY ALERT ⚠️️'
        sec_alert_msg_ncl = sec_alert
        fh_ncl_sec_alert_time = '\t\t[FROM]: CHATTER BOX Team-----[TO]:' + cad_sin_cb_username + '-----[DATE TIME]:' + datetime_str_sa
        pickle.dump(sec_alert_message, notification_cl_sa)
        pickle.dump(fh_ncl_sec_alert_time, notification_cl_sa)
        pickle.dump(sec_alert_msg_ncl, notification_cl_sa)
        notification_cl_sa.close()


#----------------------------------------------------------------------------------------------------------------------
#CREATE NEW ACCOUNT
def create_new_account():
  vo1 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/enter your name.mp3'
  voiceover(vo1)
  cna_name=str(input('ENTER YOUR NAME:-'))
  cna_username=str(input('CREATE YOUR NEW USERNAME:-'))
  cna_username_tc='SELECT USERNAME FROM CHATTER_BOX_PROFILES;'
  mc1.execute(cna_username_tc)
  cna_username_tc_1=mc1.fetchall()
  for cna_username_traverse in cna_username_tc_1:
   try:
    while cna_username in cna_username_traverse:
         print('''\n⚠️THE USERNAME YOU HAVE ENTERD IS CURRENTLY ACTIVE IN OUR SERVERS,
PLEASE, TRY WITH SOMEOTHER USERNAME.''')
         cna_username = str(input('\nCREATE YOUR NEW USERNAME:-'))
         cna_username_tc = 'SELECT USERNAME FROM CHATTER_BOX_PROFILES;'
         mc1.execute(cna_username_tc)
         cna_username_tc_1 = mc1.fetchall()
    else:
         vo2 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/enter ph no.mp3'
         voiceover(vo2)
         cna_phone_number=int(input('ENTER YOUR PHONE NUMBER:-'))
         cna_otp=random.randrange(100000,999999)
         vo3 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/we send otp.mp3'
         voiceover(vo3)
         print('\n',cna_otp,',IS YOUR OTP FOR CREATING NEW CHATTER BOX ACCOUNT.')
         cna_user_otp=int(input('\nENTER YOUR VERIFICATION CODE HERE:- '))
         while(cna_otp!=cna_user_otp):
              vo5 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/invaild otp.mp3'
              voiceover(vo5)
              print('''\n⚠️THE VERIFICATION CODE YOU HAVE ENTERED IS INVALID,
YOU WILL RECEIVE AN OTP AGAIN, PLEASE ENTER IT CORRECTLY.''')
              cna_otp=random.randrange(100000, 999999)
              print('\n',cna_otp,',IS YOU OTP FOR CREATING NEW CHATTER BOX ACCOUNT.')
              cna_user_otp=int(input('\nENTER YOUR VERIFICATION CODE HERE:-'))
         else:
              vo6 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/verified sucs.mp3'
              voiceover(vo6)
              print('✅VERIFICATION SUCCESSFUL.')
              cna_password=str(input('\nCREATE A NEW PASSWORD:-'))
              vo8 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/re enter new ac password.mp3'
              voiceover(vo8)
              cna_re_password=str(input('RE-ENTER YOUR NEW PASSWORD:-'))
              while (cna_password!=cna_re_password):
                   vo9 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/re enter password.mp3'
                   voiceover(vo9)
                   print('''\n⚠️THE PASSWORD YOU HAVE ENTERED DOESN'T MATCH.
PLEASE, ENTER THE SAME PASSWORD IN BOTH THE COLUMNS.''')
                   cna_password=str(input('\nCREATE A NEW PASSWORD:-'))
                   vo8_1= r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/re enter new ac password.mp3'
                   voiceover(vo8_1)
                   cna_re_password=str(input('RE-ENTER YOUR NEW PASSWORD:-'))
              else:
                       vo10 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/enter dob.mp3'
                       voiceover(vo10)
                       cna_dob=str(input('ENTER YOUR DATE OF BIRTH (YYYY_MM_DD):-'))
                       vo11 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/enter gender.mp3'
                       voiceover(vo11)
                       cna_gender=str(input('ENTER YOUR GENDER:-'))
                       insertval='INSERT INTO CHATTER_BOX_PROFILES(USERNAME,CHATTER_NAME,CHATTER_PHONE_NUMBER,DATE_OF_BIRTH,GENDER,ACCOUNT_PASSWORD) VALUES ( %s, %s, %s, %s, %s, %s)'
                       insertval1=(cna_username,cna_name,cna_phone_number,cna_dob,cna_gender,cna_re_password)
                       mc1.execute(insertval,insertval1)
                       db.commit()

                   #-------------NOTIFICATION CENTRE------------
                       fh_ncl =r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/NOTIFICATION CENTRE/NC_'+cna_username+'_NOTIFICATION CENTRE.dat'
                       with open(fh_ncl,'ab') as notification_cl:
                           notification_cl_wel = '\t\t\t\t\t\t\t\t🔔'+cna_username+'\'s NOTIFICATION CENTRE.'
                           datetime_str = str(datetime.datetime.now())
                           acc_rainbow_enc='\t\t\t\t🟣🔵🟢🟡🟠🔴 YOUR CHATS ARE PROTECTED WITH RAINBOW ENCRYPTION 🏳‍🌈'
                           acc_creation_dt='\t\t\t\t\t\t👤 YOUR ACCOUNT WAS CREATED ON:---'+datetime_str
                           fh_ncl_sender_name_time = '\t\t[FROM]: CHATTER BOX Team-----[TO]:' + cna_name + '-----[DATE TIME]:' + datetime_str
                           pickle.dump(notification_cl_wel,notification_cl)
                           pickle.dump(fh_ncl_sender_name_time,notification_cl)
                           pickle.dump(acc_rainbow_enc,notification_cl)
                           pickle.dump(acc_creation_dt,notification_cl)
                           notification_cl.close()

                           print('\nNOTE:-',cna_username,''',IS YOUR ACCOUNT USERNAME.
THIS USERNAME WILL ASKED WHEN YOU SIGN-IN/UPDATE/DELETE YOUR ACCOUNT.''')
                           print('\nHEY',cna_name,',YOUR CHATTER BOX ACCOUNT HAS BEEN CREATED SECURLY & SUCCESSFULLY.')
                           vo13 = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/account created.mp3'
                           voiceover(vo13)
                           print('IT\'S TIME FOR YOU TO CHAT WITH YOUR FRIENDS.')
                           break
   except:
       print('''\n⚠️THE USERNAME YOU HAVE ENTERD IS CURRENTLY ACTIVE IN OUR SERVERS,
PLEASE, TRY WITH SOMEOTHER USERNAME.''')
       break



#----------------------------------------------------------------------------------------------------------------------
#SIGN-IN
def sign_in():

    global sin_cb_username
    global ur_cb_name2
    global ur_cb_phone_number2
    global ur_cb_gender2
    global ur_cb_dob2
    global ur_cb_password2

    try:
        sin_cb_username=str(input('ENTER YOUR ACCOUNT USERNAME:-'))
        vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/enter your account password.mp3'
        voiceover(vo)
        sin_cb_password=str(input('ENTER YOUR ACCOUNT PASSWORD:-'))
        sin_cb_ch_password='SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
        mc1.execute(sin_cb_ch_password)
        sin_cb_ch_password1=mc1.fetchone()
        for sin_cb_ch_password2 in sin_cb_ch_password1:
            while sin_cb_password!=sin_cb_ch_password2:
                vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/invalid password.mp3'
                voiceover(vo)
                print('\n⚠️THE PASSWORD YOU HAVE ENTERED IS INVALID FOR THE CORRESPONDING USERNAME,',sin_cb_username,'.')
                sin_cb_password=str(input('ENTER YOUR ACCOUNT PASSWORD:-'))
            else:
                sin_cb_name='SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
                mc1.execute(sin_cb_name,sin_cb_password)
                sin_cb_name1=mc1.fetchone()
                for sin_cb_name2 in sin_cb_name1:
                    print('''-------------------------------''')
                    vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/acc det listed below.mp3'
                    voiceover(vo)
                    print('\nHEY',sin_cb_name2,',WELCOME BACK TO CHATTER BOX.')
                    print(sin_cb_name2,',YOUR CHATTER BOX ACCOUNT DETAILS ARE STATED BELOW,')
                    ur_cb_name='SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
                    ur_cb_phone_number='SELECT CHATTER_PHONE_NUMBER FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
                    ur_cb_dob='SELECT DATE_OF_BIRTH FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
                    ur_cb_gender='SELECT GENDER FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)
                    ur_cb_password='SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(sin_cb_username)

                    mc1.execute(ur_cb_name)
                    ur_cb_name1=mc1.fetchone()
                    for ur_cb_name2 in ur_cb_name1:
                        a=1

                    mc1.execute(ur_cb_phone_number)
                    ur_cb_phone_number1=mc1.fetchone()
                    for ur_cb_phone_number2 in ur_cb_phone_number1:
                        a=1

                    mc1.execute(ur_cb_dob)
                    ur_cb_dob1=mc1.fetchone()
                    for ur_cb_dob2 in ur_cb_dob1:
                        a=1

                    mc1.execute(ur_cb_gender)
                    ur_cb_gender1=mc1.fetchone()
                    for ur_cb_gender2 in ur_cb_gender1:
                        a=1

                    mc1.execute(ur_cb_password)
                    ur_cb_password1=mc1.fetchone()
                    for ur_cb_password2 in ur_cb_password1:
                        a=1

                    print('''\n▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼''',
                          '''\n🔒 YOUR USERNAME:-''',sin_cb_username,
                          '''\n👤 YOUR NAME:-''',ur_cb_name2,
                          '''\n☎️ YOUR PHONE NUMBER:-''',ur_cb_phone_number2,
                          '''\n👦🏻👧🏻 YOUR GENDER:-''',ur_cb_gender2,
                          '''\n🐣 YOUR DATE OF BIRTH (YYYY_MM_DD):-''',ur_cb_dob2,
                          '''\n🔑 YOUR ACCOUNT PASSWORD:-''',ur_cb_password2,
                          '''\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲''')
    except:
        print('\nACCOUNT NOT FOUND IN OUR SERVERS, TRY WITH SOMEOTHER USERNAME.')


#----------------------------------------------------------------------------------------------------------------------
#CHANGE ACCOUNT DETAILS
def change_account_details():

    global sec_alert
    global cad_sin_cb_username
    global cad_user_phone_number
    global cad_user_dob

    try:
            cad_sin_cb_username=str(input('ENTER YOUR ACCOUNT USERNAME:-'))
            cad_sin_cb_password=str(input('ENTER YOUR ACCOUNT PASSWORD:-'))
            cad_sin_cb_ch_password='SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
            mc1.execute(cad_sin_cb_ch_password)
            cad_sin_cb_ch_password1=mc1.fetchone()
            for cad_sin_cb_ch_password2 in cad_sin_cb_ch_password1:
                while cad_sin_cb_password!=cad_sin_cb_ch_password2:
                    print('\n⚠️THE PASSWORD YOU HAVE ENTERED IS INVALID FOR THE CORRESPONDING USERNAME,',cad_sin_cb_username)
                    cad_sin_cb_password=str(input('ENTER YOUR ACCOUNT PASSWORD:-'))
                else:
                    cad_sin_cb_name='SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                    mc1.execute(cad_sin_cb_name,cad_sin_cb_password)
                    cad_sin_cb_name1=mc1.fetchone()
                    for cad_sin_cb_name2 in cad_sin_cb_name1:
                        print('-------------------------------')
                        print('\nHEY',cad_sin_cb_name2,',WHAT DO YOU WANT TO CHANGE???.')
                        cad_user_ask=str(input('''\n[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 👤 CHANGE ACCOUNT NAME
[press 2] - 📱 CHANGE PHONE NUMBER
[Press 3] - 🐣 CHANGE DATE OF BIRTH
[Press 4] - 👦🏻👧🏻 CHANGE GENDER
[Press 5] - 🔐 CHANGE ACCOUNT PASSWORD
[Press 6] - 🗑 DELETE YOUR ACCOUNT:-'''))
                        if cad_user_ask=='1':
                            print('\n======= 👤 CHANGE ACCOUNT NAME =======')
                            cad_user_name=str(input('ENTER YOUR NEW NAME:-'))
                            cad_user_name1='UPDATE CHATTER_BOX_PROFILES SET CHATTER_NAME=%s WHERE USERNAME=%s'
                            cad_user_name2=(cad_user_name,cad_sin_cb_username)
                            mc1.execute(cad_user_name1,cad_user_name2)
                            db.commit()
                            sec_alert='\n✅'+ cad_sin_cb_name2 +',YOUR ACCOUNT NAME HAS BEEN UPDATED FROM-'+cad_sin_cb_name2+'-TO-'+cad_user_name+'.'
                            security_alert_fh(sec_alert)
                            print('\n⬜️⬜️⬜️⬜️⬜️⬜YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')

                        elif cad_user_ask == '2':
                            print('\n======= 📱 CHANGE PHONE NUMBER =======')
                            cad_cb_phone_number = 'SELECT CHATTER_PHONE_NUMBER FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                            mc1.execute(cad_cb_phone_number)
                            cad_cb_phone_number1=mc1.fetchone()
                            for cad_cb_phone_number_traverse in cad_cb_phone_number1:
                                cad_cb_phone_number_traverse_str=str(cad_cb_phone_number_traverse)

                            cad_user_phone_number=str(input('ENTER YOUR NEW PHONE NUMBER:-'))
                            cad_user_phone_number_str=str(cad_user_phone_number)
                            cad_user_phone_number1='UPDATE CHATTER_BOX_PROFILES SET CHATTER_PHONE_NUMBER=%s WHERE USERNAME=%s'
                            cad_user_phone_number2=(cad_user_phone_number,cad_sin_cb_username)
                            mc1.execute(cad_user_phone_number1,cad_user_phone_number2)
                            db.commit()
                            sec_alert='\n✅'+cad_sin_cb_name2+',YOUR ACCOUNT PHONE NUMBER HAS BEEN UPDATED FROM-'+cad_cb_phone_number_traverse_str+'-TO-'+cad_user_phone_number_str+'.'
                            security_alert_fh(sec_alert)
                            print('\n⬜️⬜️⬜️⬜️⬜️⬜YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')

                        elif cad_user_ask == '3':
                            print('\n======= 🐣 CHANGE DATE OF BIRTH =======')
                            cad_cb_dob = 'SELECT DATE_OF_BIRTH FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                            mc1.execute(cad_cb_dob)
                            cad_cb_dob1=mc1.fetchone()
                            for cad_cb_dob_traverse in cad_cb_dob1:
                                cad_cb_dob_traverse_str=str(cad_cb_dob_traverse)
                            try:
                                cad_user_dob=str(input('ENTER YOUR NEW DATE OF BIRTH (YYYY_MM_DD):-'))
                                cad_user_dob1='UPDATE CHATTER_BOX_PROFILES SET DATE_OF_BIRTH=%s WHERE USERNAME=%s'
                                cad_user_dob2=(cad_user_dob,cad_sin_cb_username)
                                mc1.execute(cad_user_dob1,cad_user_dob2)
                                db.commit()
                                sec_alert='\n✅'+cad_sin_cb_name2+',YOUR ACCOUNT DATE OF BIRTH HAS BEEN UPDATED FROM-'+cad_cb_dob_traverse_str+'-TO-'+cad_user_dob+'.'
                                security_alert_fh(sec_alert)
                                print('\n⬜️⬜️⬜️⬜️⬜️⬜YOUR NOTIFICATION CENTRE HAS BEEN UPDATED️.️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')
                            except:
                                print('\n⚠️INVALID USER ENTERY IN DATE OF BIRTH.')

                        elif cad_user_ask == '4':
                            print('\n======= 👦🏻👧🏻 CHANGE GENDER =======')
                            cad_cb_gender = 'SELECT GENDER FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                            mc1.execute(cad_cb_gender)
                            cad_cb_gender1=mc1.fetchone()
                            for cad_cb_gender_traverse in cad_cb_gender1:
                                a=1
                            cad_user_gender=str(input('ENTER YOUR GENDER:-'))
                            cad_user_gender1='UPDATE CHATTER_BOX_PROFILES SET GENDER=%s WHERE USERNAME=%s'
                            cad_user_gender2=(cad_user_gender,cad_sin_cb_username)
                            mc1.execute(cad_user_gender1,cad_user_gender2)
                            db.commit()
                            sec_alert='\n✅'+cad_sin_cb_name2+',YOUR ACCOUNT GENDER HAS BEEN UPDATED FROM-'+cad_cb_gender_traverse+'-TO-'+cad_user_gender+'.'
                            security_alert_fh(sec_alert)
                            print('\n⬜️⬜️⬜️⬜️⬜️⬜YOUR NOTIFICATION CENTRE HAS BEEN UPDATED️.️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')

                        elif cad_user_ask == '5':
                            print('\n======= 🔐 CHANGE ACCOUNT PASSWORD =======')
                            cad_cb_password = 'SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                            mc1.execute(cad_cb_password)
                            cad_cb_password1=mc1.fetchone()
                            for cad_cb_password_traverse in cad_cb_password1:
                                a=1
                            cad_user_password=str(input('\nENTER YOUR NEW PASSWORD:-'))
                            cad_user_password1 = str(input('RE-ENTER YOUR NEW PASSWORD:-'))
                            while cad_user_password!=cad_user_password1:
                                vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/re enter password.mp3'
                                voiceover(vo)
                                print('''\n⚠️THE PASSWORD YOU HAVE ENTERED DOESN'T MATCH.
PLEASE, ENTER THE SAME PASSWORD IN BOTH THE COLUMNS.''')
                                cad_user_password = str(input('\nENTER YOUR NEW PASSWORD:-'))
                                cad_user_password1 = str(input('RE-ENTER YOUR NEW PASSWORD:-'))
                            else:
                                cad_user_password2 = 'UPDATE CHATTER_BOX_PROFILES SET ACCOUNT_PASSWORD=%s WHERE USERNAME=%s'
                                cad_user_password3 = (cad_user_password1,cad_sin_cb_username)
                                mc1.execute(cad_user_password2,cad_user_password3)
                                db.commit()
                                sec_alert='\n✅'+cad_sin_cb_name2+',YOUR ACCOUNT PASSWORD HAS BEEN UPDATED FROM-'+cad_cb_password_traverse+'-TO-'+cad_user_password+'.'
                                security_alert_fh(sec_alert)
                                print('\n⬜️⬜️⬜️⬜️⬜️⬜YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')

                        elif cad_user_ask == '6':
                            print('\n======= 🗑 DELETE YOUR ACCOUNT =======')
                            cad_cb_delete = 'SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                            mc1.execute(cad_cb_delete)
                            cad_cb_delete1=mc1.fetchone()
                            for cad_cb_delete_traverse in cad_cb_delete1:
                                a=1
                            cad_user_delete=str(input('ENTER YOUR ACCOUNT PASSWORD TO PERMANENTLY DELETE YOUR ACCOUNT:-'))
                            while cad_cb_delete_traverse!=cad_user_delete:
                                print('''\n⚠️THE PASSWORD YOU HAVE ENTERED IS INVALID,
PLEASE, RE-ENTER YOUR ACCOUNT PASSWORD CORRECTLY.''')
                                cad_cb_delete = 'SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                                mc1.execute(cad_cb_delete)
                                cad_cb_delete1 = mc1.fetchone()
                                for cad_cb_delete_traverse in cad_cb_delete1:
                                    a = 1
                                cad_user_delete = str(input('\nENTER YOUR ACCOUNT PASSWORD TO DELETE YOUR ACCOUNT:-'))
                            else:
                                 cad_user_delete1='DELETE FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(cad_sin_cb_username)
                                 mc1.execute(cad_user_delete1,cad_sin_cb_username)
                                 db.commit()
                                 print('\n',cad_sin_cb_name2,',THIS IS OUR LAST GOOD BYE! 👋🏻.')
                                 print('✅',cad_sin_cb_name2,',YOUR CHATTER BOX ACCOUNT HAS BEEN DELETED PERMANENTLY 🗑.')
                                 print('⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️')

    except:
        print('\n⚠️INVALID USERNAME AND PASSWORD, TRY ENTERING CORRECT USERNAME AND CORRESPONDING ACCOUNT PASSWORD.')


#----------------------------------------------------------------------------------------------------------------------
#READING CHATS
def readchat():

   global fh_uidrc

   try:
     fh_uname=sin_cb_username
     fh_uidrc=input('ENTER YOUR FRIEND CHATTER BOX USERNAME:-')
     fh_readchat_name=r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/CHATS/CHAT FROM_'+fh_uidrc+'_TO_'+fh_uname+'.dat'
     with open(fh_readchat_name,'rb') as fh_readchat:
         vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/chats are listed below.mp3'
         voiceover(vo)
         print('\n📜 CHATS ARE LISTED BELOW:')
         print('\n')
         str=' '
         while str:
                   str=pickle.load(fh_readchat)
                   str1=str.strip('\n')
                   print(str1)
         else:
                   fh_readchat.close()
                   vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/end of chat.mp3'
                   voiceover(vo)
   except:
       a=1
       #print('\nOOPS,NO CHAT HISTORY FOUND, FOR THE ACCOUNT NUMBER WHICH YOU HAVE ENTERED.')


#----------------------------------------------------------------------------------------------------------------------
#SENDING CHATS
def sendchat():
     readchat()
     sin_cb_username_str=str(sin_cb_username)
     fh_fac_number=fh_uidrc
     try:
         fh_cb_sc_name='SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME=\'{}\''.format(fh_fac_number)
         mc1.execute(fh_cb_sc_name,fh_fac_number)
         fh_cb_sc_name1=mc1.fetchone()
         for sc_ur_cb_name2 in fh_cb_sc_name1:
             a = 1

         print('\n',ur_cb_name2,',YOU ARE SENDING MESSAGE TO -',sc_ur_cb_name2,'.')

         # -----------------DIRECT MESSAGE-----------------
         fh_name=r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/CHATS/CHAT FROM_'+sin_cb_username_str+'_TO_'+fh_fac_number+'.dat'
         with open(fh_name,'ab') as fh_sendchat:
             vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/type your msg here.mp3'
             voiceover(vo)
             fh_chat=str(input('TYPE YOUR MESSAGE HERE:-'))
             fh_rainbow_enc='\t\t\t\t\t\t🟣🔵🟢🟡🟠🔴'
             datetime_str =str(datetime.datetime.now())
             fh_sender_name_time='\t\t[FROM]:'+ur_cb_name2+'-----[TO]:'+sc_ur_cb_name2+'-----[DATE TIME]:'+datetime_str
             pickle.dump(fh_sender_name_time,fh_sendchat)
             pickle.dump(fh_chat,fh_sendchat)
             pickle.dump(fh_rainbow_enc,fh_sendchat)
             fh_sendchat.close()

         #------------DUPLICATE SELF MESSAGE---------------
         fh_name_dup = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/CHATS/CHAT FROM_' + fh_fac_number + '_TO_' + sin_cb_username_str + '.dat'
         with open(fh_name_dup,'ab') as fh_sendchat_dup:
             fh_chat_dup = fh_chat
             fh_sender_name_time_dup='\t\t[FROM]:'+sc_ur_cb_name2+'-----[TO]:'+ur_cb_name2+'-----[DATE TIME]:'+datetime_str
             pickle.dump(fh_sender_name_time_dup, fh_sendchat_dup)
             pickle.dump(fh_chat_dup, fh_sendchat_dup)
             fh_sendchat_dup.close()

         #--------------NOTIFICATION CENTRE------------------
         fh_ncl_alert =r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/NOTIFICATION CENTRE/NC_' + fh_uidrc + '_NOTIFICATION CENTRE.dat'
         with open(fh_ncl_alert, 'ab') as notification_cl_a:
                 sender_name_ncl_a='\n\t\t\t\t🫂 YOU HAVE RECEIVED A MESSAGE FROM,'+ur_cb_name2+'.'
                 notification_canter_alert = fh_chat
                 ncl_separator='\n'
                 pickle.dump(ncl_separator,notification_cl_a)
                 pickle.dump(sender_name_ncl_a,notification_cl_a)
                 pickle.dump(fh_sender_name_time, notification_cl_a)
                 pickle.dump(notification_canter_alert, notification_cl_a)
                 notification_cl_a.close()

                 vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/your msg has been sent.mp3'
                 voiceover(vo)
                 print('\n🟣🔵🟡🔴 - YOUR MESSAGE HAS BEEN SENT SECURELY WITH RAINBOW ENCRYPTION 🏳‍🌈.')
     except:
        print('\n⚠️INVALID USERNAME, TRY ENTERING CORRECT USERNAME.')


#----------------------------------------------------------------------------------------------------------------------
#HANDCRICKET WITH MACHINE
def handcricket_with_machine():
    def user_batting():
        global f
        print('\t\t🏏 WELCOME TO HAND CRICKET GAME.')
        print('\t\t\t👨🏻 HUMAN VS 🖥 MACHNE')
        b = 1
        c = 2
        f = 0
        print('\n\t\tMACHINE WON THE TOSS, AND IT CHOSES TO CHASE.')
        a = 1
        if a == 1:
            print('YOU ARE BATTING. ALLOWED CHARACTERS 0 TO 5. NOT MORE THAN THAT.')
            while a == 1:
                print('=======================================')
                d = int(input('USER:🏏BATTING:-'))
                if d < 6:
                    e = random.randrange(1, 6)
                    print('MACHINE:🏏BOWLING:-',e)
                    if (d != e):
                        f = f + d
                        print('\t\t\t\t\t\tYOUR SCORE: ', f)
                    else:
                        print('\n\t\t\txxxxxxx 🦆🦆🦆 USER OUT! 🦆🦆🦆 xxxxxxxx')
                        print("\n\t\t\t\t\t✔︎ YOUR TOTAL SCORE: ", f)
                        break
                elif d > 5:
                    print('\t\t\t❌INVALID INPUT.')
                else:
                    print('\t\t\t❌INVALID INPUT.')


    def user_bowling():
            global f1
            print('-------------------------------------------------------')
            print('\n\t\t\tNOW YOU ARE BOWLING.')
            g = 2
            h = 2
            f1 = 0
            if g == h:
                print('ALLOWED CHARACTERS 0 TO 5. NOT MORE THAN THAT.')
                while 2 == 2:
                    print('=========================================')
                    i = int(input('USER:🏏BOWLING:-'))
                    if i > 6:
                        print('\t\t\t❌INVALID INPUT.')
                    else:
                        j=random.randrange(1,6)
                        print('MACHINE:🏏BATTING:-',j)
                        if (j != i):
                            f1 = f1 + j
                            print('\t\t\t\t\t\tMACHINE SCORE:',f1)
                            if f1 > f:
                                print('\n\t\t\t\t🏆🏆🏆 MACHINE WON THE MATCH  🏆🏆🏆')
                                print('\t\t\t\t👍🏻👍🏻👍🏻 BETTER LUCK NEXT TIME! 👍🏻👍🏻👍🏻')
                                break
                        elif j == i:
                            print('\n\t\t\txxxxxxxx 🦆🦆🦆 MACHINE OUT! 🦆🦆🦆 xxxxxxx')
                            print('\n\t\t\t\t\t✔︎ MACHINE TOTAL SCORE:',f1)
                            break

    user_batting()
    user_bowling()
    if f == f1:
            print('\n\t\t\t\t\t------- MATCH DRAW -------')
            print('\t\t\t👍🏻👍🏻👍🏻 BETTER LUCK NEXT TIME! 👍🏻👍🏻👍🏻')
    elif f > f1:
            print('\n\t\t\t\t🏆🏆🏆 YOU WON THE MATCH 🏆🏆🏆')
            print('\t\t👏🏻👏🏻👏🏻 CONGRAGULATIONS, WELL PLAYED 👏🏻👏🏻👏🏻')


#----------------------------------------------------------------------------------------------------------------------
#ABOUT US
def About_us():
     fh_about_us=open(r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/ABOUT US/CHATTER_BOX_ABOUT_US.txt','r')
     str=' '
     while str:
          str=fh_about_us.readline()
          str=str.strip('\n')
          print(str)
     fh_about_us.close()


#----------------------------------------------------------------------------------------------------------------------
#FEEDBACK
def feedback():
     fb_in=sin_cb_username
     fb_fh_rn=r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/FEEDBACK/Feedback_by_'+fb_in+'.dat'
     fb_fh_a=open(fb_fh_rn,'a')
     datetime_str = str(datetime.datetime.now())
     fh_sender_name_time = '[FROM]:' + ur_cb_name2 + '-------DATE TIME:' + datetime_str
     fb_fh_a.write(fh_sender_name_time)
     fb_fh_a.write('\n')
     vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/give us ur feedback.mp3'
     voiceover(vo)
     fb_ask=str(input('GIVE US YOUR FEEDBACK:-'))
     fb_fh_a.writelines(fb_ask)
     fb_fh_a.write('\n')
     fb_fh_a.close()
     vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/tq feedback.mp3'
     voiceover(vo)
     print('\n',ur_cb_name2,',WE REALLY APPRECIATE USERS FEEDBACK,')
     print('YOUR VALUABLE FEEDBACK MENT LOT TO US, THANKYOU FOR YOUR INTEREST.')


#______________________________________________________________________________
#xxxxxxxxxxxxx MAIN LOOP xxxxxxxxxxxxx

print ('''===============================

              WELCOME TO CHATTER BOX 
              SIMPLY LOVEABLE 
              MADE IN 🤍️ WITH 🇮🇳''')

#vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/home menu.mp3'
#voiceover(vo)

def homeloop():
 while True:
     ml_userinput=str(input('''\n======= 🏠 HOME MENU =======
[Press *] - 🔔 VIEW NOTIFICATION CENTRE
[Press 1] - 👤 ACCOUNT SETTINGS
[Press 2] - 💬 CHAT WITH YOUR FRIENDS
[Press 3] - 🏏 PLAY HAND-CRICKET WITH MACHINE
[Press 4] - 📜 ABOUT US & 📝 FEEDBACK
[Press 5] - 🔒 LOG-OUT FROM CHATTER BOX:-'''))
     if ml_userinput == '*':
         print('\n======= 🔔 NOTIFICATION CENTRE =======')
         try:
            notification_centre()
         except:
            print('PLEASE SIGIN TO YOUR CHATTER BOX ACCOUNT TO VIEW NOTIFICATIONS.')
            homeloop()


     elif ml_userinput=='1':
          print('\n======= 👤 ACCOUNT SETTINGS =======')
          vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/account settings.mp3'
          voiceover(vo)
          ml_ui_ad=str(input('''[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 👤 CREATE NEW CHATTER BOX ACCOUNT
[Press 2] - 🔐 SIGN-IN INTO EXISTING ACCOUNT
[Press 3] - ⚙️ CHANGE ACCOUNT DETAILS:-'''))

          if ml_ui_ad=='1':
              print('\n======= 👤+ CREATE NEW CHATTER BOX ACCOUNT =======')
              create_new_account()

          elif ml_ui_ad=='2':
              vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/you r abt to signin.mp3'
              voiceover(vo)
              print('\n======= 🔐 SIGN-IN CHATTER BOX ACCOUNT =======')
              sign_in()

          elif ml_ui_ad=='3':
              print('\n======= ⚙️ CHANGE ACCOUNT DETAILS =======')
              change_account_details()

          else:
              vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/returned back to home menu.mp3'
              voiceover(vo)


     elif ml_userinput=='2':
          print('\n======= 💬 CHAT WITH YOUR FRIENDS =======')
          try:
              sendchat()
          except:
              print('\nPLEASE SIGIN TO YOUR CHATTER BOX ACCOUNT TO CHAT WITH YOUR FRIENDS.')
              homeloop()


     elif ml_userinput=='3':
          print('\n======= 🏏 PLAY HAND-CRICKET WITH MACHINE =======')
          handcricket_with_machine()
          vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/returned back to home menu.mp3'
          voiceover(vo)


     elif ml_userinput=='4':
          vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/about us and feedback.mp3'
          voiceover(vo)
          print('\n======= 📜 ABOUT US & 📝 FEEDBACK =======')
          ml_ui_au_fb=str(input('''[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 📜 KNOW ABOUT US
[Press 2] - 📝 GIVE US YOUR FEEDBACK:-'''))

          if ml_ui_au_fb=='1':
              print('\n======= 📜 ABOUT US =======')
              vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/about us.mp3'
              voiceover(vo)
              About_us()


          elif ml_ui_au_fb=='2':
              print('\n======= 📝 FEEDBACK =======')
              try:
                  feedback()
              except:
                  print('\nPLEASE SIGIN TO YOUR CHATTER BOX ACCOUNT TO GIVE US YOUR FEEDBACK.')
                  homeloop()
          else:
                vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/returned back to home menu.mp3'
                voiceover(vo)


     elif ml_userinput=='5':
         vo = r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/logged out-acc det encrypted.mp3'
         voiceover(vo)
         print('\n======= 🔒 YOU HAVE LOGGED OUT FROM CHATTER BOX =======')
         print('\nYOUR ACCOUNT DETAILS ARE ENCRYPTED.')
         print('❌❌❌❌❌❌❌❌❌❌❌❌❌')
         a=str(input())
         a1=1
         if 1==a1:
             quit()


     else:
        vo= r'/Users/mac/Documents/PYTHON /CHATTER BOX by raghava/VOICE OVER/invalid user input in home menu.mp3'
        voiceover(vo)
        print('\n======= ❌ INVALID USER INPUT IN HOME MENU =======')
        print('YOU HAVE BEEN RETURNED BACK TO HOME MENU.')


#**********************************************************************************************************************
#MAIN CALL

homeloop()

