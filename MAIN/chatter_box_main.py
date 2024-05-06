"""CHATTER BOX
SIMPLY LOVABLE
Made in 🤍️️ with 🇮🇳!!!

© ALL COPYRIGHTS RESERVED CHATTER BOX 2021

CREATED ON 13 DEC 2020.
LAST UPDATED ON 08 MARCH 2021."""

# ______________________________________________________________________________________________________________________
"""[CREDIT DASHBOARD]

[SPECIAL MENTION]
SHEMEER.K.A - PGT, COMPUTER SCIENCE, KV COIMBATORE.

[VOICE OVER CREDIT]
POORVEKKA, STUDENT, KV CBE - (BATCH 2020-2021).

[DESIGNED & PROGRAMMED]
RAGHAVA, STUDENT, KV CBE - (BATCH 2020-2021)"""


# ______________________________________________________________________________________________________________________
# MYSQL DATABASE CONNECTION

"""CREATE TABLE CHATTER_BOX_PROFILES(USERNAME VARCHAR(50) PRIMARY KEY,CHATTER_NAME CHAR(50),CHATTER_PHONE_NUMBER BIGINT,
DATE_OF_BIRTH DATE,GENDER CHAR (20),ACCOUNT_PASSWORD VARCHAR(50));"""


# ______________________________________________________________________________________________________________________
# IMPORTING FUNCTIONS

import sys
import mysql.connector as mc
import pygame
import random
import datetime
import pickle


# ______________________________________________________________________________________________________________________
# xxxxxxxxxxxxxx CREATING FUNCTIONS xxxxxxxxxxxxx

# ESTABLISHING CONNECTION
db = mc.connect(
    host="localhost", user="raghav", password="12345678", database="CHATTER_BOX"
)
mc1 = db.cursor()


# ----------------------------------------------------------------------------------------------------------------------
# VOICE OVER
def voiceover(vo):
    pygame.mixer.init()
    pygame.mixer.music.load(vo)
    pygame.mixer.music.play()


# -----------HOME MENU-----------
vo_cb_wi = r"chatter-box/VOICEOVER/cb welcome intend.mp3"
vo_home = r"chatter-box/VOICEOVER/home menu.mp3"
vo_nc_err = r"chatter-box/VOICEOVER/signin nc.mp3"
vo_fb_err = r"chatter-box/VOICEOVER/signin fb.mp3"
vo_chat_err = r"chatter-box/VOICEOVER/signin chat.mp3"
vo_hc_err = r"chatter-box/VOICEOVER/signin hc.mp3"
vo_acc_settings_menu = r"chatter-box/VOICEOVER/account settings.mp3"

# -----------NOTIFICATION CENTRE-----------
vo_nc_listed_below = r"chatter-box/VOICEOVER/nc listed below.mp3"

# -----------ACCOUNT CREATION-----------
vo_ac_ur_name = r"chatter-box/VOICEOVER/enter your name.mp3"
vo_ac_ur_un = r"chatter-box/VOICEOVER/create your new username.mp3"
vo_ac_active_ser = r"chatter-box/VOICEOVER/acc cr un active in servers.mp3"
vo_ac_pn_no = r"chatter-box/VOICEOVER/enter ph no.mp3"
vo_ac_sent_otp = r"chatter-box/VOICEOVER/we send otp.mp3"
vo_ac_invalid_otp = r"chatter-box/VOICEOVER/invalid otp.mp3"
vo_ac_verified = r"chatter-box/VOICEOVER/verified sucs.mp3"
vo_ac_reenter_new_pw = r"chatter-box/VOICEOVER/re enter new ac password.mp3"
vo_ac_pw_mm = r"chatter-box/VOICEOVER/re enter password.mp3"
vo_ac_dob = r"chatter-box/VOICEOVER/enter dob.mp3"
vo_ac_gender = r"chatter-box/VOICEOVER/enter gender.mp3"
vo_ac_final = r"chatter-box/VOICEOVER/acc creation final.mp3"
vo_ac_invalid_dob = r"chatter-box/VOICEOVER/invalid dob.mp3"

# -----------SIGN-IN-----------
vo_urabt_signin = r"chatter-box/VOICEOVER/you r abt to signin.mp3"
vo_signin_ac_un = r"chatter-box/VOICEOVER/enter u r un.mp3"
vo_signin_ac_pw = r"chatter-box/VOICEOVER/enter your account password.mp3"
vo_sigin_wpr = r"chatter-box/VOICEOVER/wrong password reenter.mp3"
vo_sigin_acc_det = r"chatter-box/VOICEOVER/acc det listed below.mp3"
vo_signin_acc_nf = r"chatter-box/VOICEOVER/account not found.mp3"

# -----------CHANGE ACCOUNT DETAILS-----------
vo_cad_menu = r"chatter-box/VOICEOVER/change menu.mp3"
vo_cad_ui_un = r"chatter-box/VOICEOVER/change acc details ui un.mp3"
vo_cad_name = r"chatter-box/VOICEOVER/change acc name.mp3"
vo_cad_nc_updated = r"chatter-box/VOICEOVER/nc updated.mp3"
vo_cad_ph_no = r"chatter-box/VOICEOVER/change ph no.mp3"
vo_cad_dob = r"chatter-box/VOICEOVER/change dob.mp3"
vo_cad_gender = r"chatter-box/VOICEOVER/change gender.mp3"
vo_cad_pw = r"chatter-box/VOICEOVER/change apass.mp3"
vo_cad_delete = r"chatter-box/VOICEOVER/acc delete pass.mp3"
vo_cad_delete_final = r"chatter-box/VOICEOVER/acc deletion final.mp3"

# -----------CHAT-----------
vo_chat_menu = r"chatter-box/VOICEOVER/chat menu.mp3"
vo_chat_cb_un = r"chatter-box/VOICEOVER/enter frnd cbu.mp3"
vo_chat_listed_below = r"chatter-box/VOICEOVER/chats are listed below.mp3"
vo_chat_type_msg = r"chatter-box/VOICEOVER/type your msg here.mp3"
vo_chat_msg_sent_re = r"chatter-box/VOICEOVER/your msg has been sent.mp3"
vo_chat_inc_un = r"chatter-box/VOICEOVER/account not found.mp3"

# -----------SEARCH-----------
vo_fyf_search = r"chatter-box/VOICEOVER/frnd to searched.mp3"
vo_fyf_similar_search = r"chatter-box/VOICEOVER/account similar search.mp3"

# -----------HAND-CRICKET-----------
vo_hc_menu = r"chatter-box/VOICEOVER/hc menu.mp3"
vo_m_bowl = r"chatter-box/VOICEOVER/machine bowling.mp3"
vo_u_score = r"chatter-box/VOICEOVER/machine batting.mp3"
vo_u_out = r"chatter-box/VOICEOVER/user out.mp3"
vo_u_bowl_fun = r"chatter-box/VOICEOVER/user bowling function.mp3"
vo_m_bat = r"chatter-box/VOICEOVER/user batting.mp3"
vo_u_bowl = r"chatter-box/VOICEOVER/user bowling.mp3"
vo_m_invalid_input = r"chatter-box/VOICEOVER/invalid input.mp3"
vo_m_won = r"chatter-box/VOICEOVER/machine won.mp3"
vo_m_draw = r"chatter-box/VOICEOVER/match draw.mp3"
vo_u_won = r"chatter-box/VOICEOVER/you won match.mp3"

# -----------ABOUT US AND FEEDBACK-----------
vo_af_menu = r"chatter-box/VOICEOVER/about us and feedback.mp3"
vo_about_us = r"chatter-box/VOICEOVER/about us.mp3"
vo_give_us_fb = r"chatter-box/VOICEOVER/give us ur feedback.mp3"
vo_tq_fb = r"chatter-box/VOICEOVER/tq feedback.mp3"

# -----------LOGOUT-----------
vo_logout = r"chatter-box/VOICEOVER/logged out-acc det encrypted.mp3"

# -----------INVALID USER ENTERY IN HOME MENU-----------
vo_invaild_hm = r"chatter-box/VOICEOVER/invalid user input in home menu.mp3"

# -----------RETURNED BACK HOME MENU-----------
vo_returned_back_hm = r"chatter-box/VOICEOVER/returned back to home menu.mp3"


# ----------------------------------------------------------------------------------------------------------------------
# NOTIFICATION CENTRE
def notification_centre():
    try:
        voiceover(vo_nc_listed_below)
        fh_uname = sin_cb_username_small
        fh_read_notification = (
            r"chatter-box/NOTIFICATIONCENTRE/NC_"
            + sin_cb_username_small
            + "_NOTIFICATION CENTRE.dat"
        )
        with open(fh_read_notification, "rb") as fh_ncl_notification:
            str = " "
            while str:
                str = pickle.load(fh_ncl_notification)
                str1 = str.strip("\n")
                print(str1)
            else:
                fh_ncl_notification.close()
    except:
        fh_ncl_notification.close()


# ----------------------------------------------------------------------------------------------------------------------
# SECURITY ALERT
def security_alert_fh(sec_alert):
    fh_ncl_sa = (
        r"chatter-box/NOTIFICATIONCENTRE/NC_"
        + cad_sin_cb_username_small
        + "_NOTIFICATION CENTRE.dat"
    )
    with open(fh_ncl_sa, "ab") as notification_cl_sa:
        datetime_str_sa = str(datetime.datetime.now())
        sec_alert_message = "\n\t\t\t\t\t\t\t\t\t⚠️ SECURITY ALERT ⚠️️"
        sec_alert_msg_ncl = sec_alert
        fh_ncl_sec_alert_time = (
            "\t\t[FROM]: CHATTER BOX Team-----[TO]:"
            + cad_sin_cb_username_small
            + "-----[DATE TIME]:"
            + datetime_str_sa
        )
        pickle.dump(sec_alert_message, notification_cl_sa)
        pickle.dump(fh_ncl_sec_alert_time, notification_cl_sa)
        pickle.dump(sec_alert_msg_ncl, notification_cl_sa)
        notification_cl_sa.close()


# ----------------------------------------------------------------------------------------------------------------------
# CREATE NEW ACCOUNT
def create_new_account():
    voiceover(vo_ac_ur_name)
    cna_name = str(input("🗣ENTER YOUR NAME:-"))
    voiceover(vo_ac_ur_un)
    cna_username = str(input("🗣CREATE YOUR NEW USERNAME:-"))
    cna_username_small = cna_username.lower()
    cna_username_upper = cna_username.upper()
    tup = ()
    tup = tup + (cna_username_small,)
    cna_username_small_tc = "SELECT USERNAME FROM CHATTER_BOX_PROFILES;"
    mc1.execute(cna_username_small_tc)
    cna_username_small_tc_1 = mc1.fetchall()
    try:
        while tup in cna_username_small_tc_1:
            voiceover(vo_ac_active_ser)
            print(
                """\n🗣️THE USERNAME YOU HAVE ENTERD IS CURRENTLY ACTIVE IN OUR SERVERS,
PLEASE, TRY WITH SOMEOTHER USERNAME⚠️"""
            )
            cna_username_small = str(input("\n🗣CREATE YOUR NEW USERNAME:-"))
            tup = ()
            tup = tup + (cna_username_small,)
            cna_username_small_tc = "SELECT USERNAME FROM CHATTER_BOX_PROFILES;"
            mc1.execute(cna_username_small_tc)
            cna_username_small_tc_1 = mc1.fetchall()
        else:
            voiceover(vo_ac_pn_no)
            cna_phone_number = int(input("🗣ENTER YOUR PHONE NUMBER:-"))
            cna_otp = random.randrange(100000, 999999)
            voiceover(vo_ac_sent_otp)
            print("\n", cna_otp, ",IS YOUR OTP FOR CREATING NEW CHATTER BOX ACCOUNT.")
            cna_user_otp = int(input("\n🗣ENTER YOUR VERIFICATION CODE HERE:- "))
            while cna_otp != cna_user_otp:
                voiceover(vo_ac_invalid_otp)
                print(
                    """\n🗣️THE VERIFICATION CODE YOU HAVE ENTERED IS INVALID,
YOU WILL RECEIVE AN OTP AGAIN, PLEASE ENTER IT CORRECTLY⚠️"""
                )
                cna_otp = random.randrange(100000, 999999)
                print(
                    "\n", cna_otp, ",IS YOU OTP FOR CREATING NEW CHATTER BOX ACCOUNT."
                )
                cna_user_otp = int(input("\n🗣ENTER YOUR VERIFICATION CODE HERE:-"))
            else:
                voiceover(vo_ac_verified)
                print("🗣✅VERIFICATION SUCCESSFUL.")
                cna_password = str(input("\n🗣CREATE A NEW PASSWORD:-"))
                voiceover(vo_ac_reenter_new_pw)
                cna_re_password = str(input("🗣RE-ENTER YOUR NEW PASSWORD:-"))
                while cna_password != cna_re_password:
                    voiceover(vo_ac_pw_mm)
                    print(
                        """\n🗣️THE PASSWORD YOU HAVE ENTERED DOESN'T MATCH.
PLEASE, ENTER THE SAME PASSWORD IN BOTH THE COLUMNS⚠️"""
                    )
                    cna_password = str(input("\n🗣CREATE A NEW PASSWORD:-"))
                    voiceover(vo_ac_reenter_new_pw)
                    cna_re_password = str(input("🗣RE-ENTER YOUR NEW PASSWORD:-"))
                else:
                    voiceover(vo_ac_dob)
                    cna_dob = str(input("🗣ENTER YOUR DATE OF BIRTH (YYYY_MM_DD):-"))
                    voiceover(vo_ac_gender)
                    cna_gender = str(input("🗣ENTER YOUR GENDER:-"))
                    insertval = "INSERT INTO CHATTER_BOX_PROFILES(USERNAME,CHATTER_NAME,CHATTER_PHONE_NUMBER,DATE_OF_BIRTH,GENDER,ACCOUNT_PASSWORD) VALUES ( %s, %s, %s, %s, %s, %s)"
                    insertval1 = (
                        cna_username_small,
                        cna_name,
                        cna_phone_number,
                        cna_dob,
                        cna_gender,
                        cna_re_password,
                    )
                    mc1.execute(insertval, insertval1)
                    db.commit()

                    # -------------NOTIFICATION CENTRE------------
                    fh_ncl = (
                        r"chatter-box/NOTIFICATIONCENTRE/NC_"
                        + cna_username_small
                        + "_NOTIFICATION CENTRE.dat"
                    )
                    with open(fh_ncl, "ab") as notification_cl:
                        notification_cl_wel = (
                            "\t\t\t\t\t\t\t\t🔔"
                            + cna_username_small
                            + "'s NOTIFICATION CENTRE."
                        )
                        datetime_str = str(datetime.datetime.now())
                        acc_rainbow_enc = "\t\t\t\t🟣🔵🟢🟡🟠🔴 YOUR CHATS ARE PROTECTED WITH RAINBOW ENCRYPTION 🏳‍🌈"
                        acc_creation_dt = (
                            "\t\t\t\t\t\t👤 YOUR ACCOUNT WAS CREATED ON:---"
                            + datetime_str
                        )
                        fh_ncl_sender_name_time = (
                            "\t\t[FROM]: CHATTER BOX Team-----[TO]:"
                            + cna_name
                            + "-----[DATE TIME]:"
                            + datetime_str
                        )
                        pickle.dump(notification_cl_wel, notification_cl)
                        pickle.dump(fh_ncl_sender_name_time, notification_cl)
                        pickle.dump(acc_rainbow_enc, notification_cl)
                        pickle.dump(acc_creation_dt, notification_cl)
                        notification_cl.close()

                        voiceover(vo_ac_final)
                        print(
                            "\n🗣NOTE:-",
                            cna_username_small,
                            """,IS YOUR ACCOUNT USERNAME.
THIS USERNAME WILL ASKED WHEN YOU SIGN-IN/UPDATE/DELETE YOUR ACCOUNT.""",
                        )
                        print(
                            "\nHEY",
                            cna_name,
                            ",YOUR CHATTER BOX ACCOUNT HAS BEEN CREATED SECURELY & SUCCESSFULLY.",
                        )
                        print("IT'S TIME FOR YOU TO CHAT WITH YOUR FRIENDS.")

    except:
        voiceover(vo_ac_invalid_dob)
        print("\n🗣️INVALID USER ENTERY IN DATE OF BIRTH⚠️")


# ----------------------------------------------------------------------------------------------------------------------
# SIGN-IN
def sign_in():

    global sin_cb_username
    global sin_cb_username_small
    global ur_cb_name2
    global ur_cb_phone_number2
    global ur_cb_gender2
    global ur_cb_dob2
    global ur_cb_password2

    try:
        voiceover(vo_signin_ac_un)
        sin_cb_username = str(input("🗣ENTER YOUR ACCOUNT USERNAME:-"))
        sin_cb_username_small = sin_cb_username.lower()
        voiceover(vo_signin_ac_pw)
        sin_cb_password = str(input("🗣ENTER YOUR ACCOUNT PASSWORD:-"))
        sin_cb_ch_password = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
            sin_cb_username_small
        )
        mc1.execute(sin_cb_ch_password)
        sin_cb_ch_password1 = mc1.fetchone()
        for sin_cb_ch_password2 in sin_cb_ch_password1:
            while sin_cb_password != sin_cb_ch_password2:
                voiceover(vo_sigin_wpr)
                print(
                    """\n🗣️THE PASSWORD YOU HAVE ENTERED IS INVALID,
PLEASE, RE-ENTER YOUR ACCOUNT PASSWORD⚠️"""
                )
                sin_cb_password = str(input("\n🗣ENTER YOUR ACCOUNT PASSWORD:-"))
            else:
                sin_cb_name = "SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                    sin_cb_username_small
                )
                mc1.execute(sin_cb_name, sin_cb_password)
                sin_cb_name1 = mc1.fetchone()
                for sin_cb_name2 in sin_cb_name1:
                    print("""-------------------------------""")
                    voiceover(vo_sigin_acc_det)
                    print("\n🗣HEY", sin_cb_name2, ",WELCOME BACK TO CHATTER BOX.")
                    print(
                        "🗣",
                        sin_cb_name2,
                        ",YOUR CHATTER BOX ACCOUNT DETAILS ARE STATED BELOW,",
                    )
                    ur_cb_name = "SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                        sin_cb_username_small
                    )
                    ur_cb_phone_number = "SELECT CHATTER_PHONE_NUMBER FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                        sin_cb_username_small
                    )
                    ur_cb_dob = "SELECT DATE_OF_BIRTH FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                        sin_cb_username_small
                    )
                    ur_cb_gender = "SELECT GENDER FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                        sin_cb_username_small
                    )
                    ur_cb_password = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                        sin_cb_username_small
                    )

                    mc1.execute(ur_cb_name)
                    ur_cb_name1 = mc1.fetchone()
                    for ur_cb_name2 in ur_cb_name1:
                        a = 1

                    mc1.execute(ur_cb_phone_number)
                    ur_cb_phone_number1 = mc1.fetchone()
                    for ur_cb_phone_number2 in ur_cb_phone_number1:
                        a = 1

                    mc1.execute(ur_cb_dob)
                    ur_cb_dob1 = mc1.fetchone()
                    for ur_cb_dob2 in ur_cb_dob1:
                        a = 1

                    mc1.execute(ur_cb_gender)
                    ur_cb_gender1 = mc1.fetchone()
                    for ur_cb_gender2 in ur_cb_gender1:
                        a = 1

                    mc1.execute(ur_cb_password)
                    ur_cb_password1 = mc1.fetchone()
                    for ur_cb_password2 in ur_cb_password1:
                        a = 1

                    print(
                        """▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼""",
                        """\n🔒 YOUR USERNAME:-""",
                        sin_cb_username_small,
                        """\n👤 YOUR NAME:-""",
                        ur_cb_name2,
                        """\n☎️ YOUR PHONE NUMBER:-""",
                        ur_cb_phone_number2,
                        """\n👦🏻👧🏻 YOUR GENDER:-""",
                        ur_cb_gender2,
                        """\n🐣 YOUR DATE OF BIRTH (YYYY_MM_DD):-""",
                        ur_cb_dob2,
                        """\n🔑 YOUR ACCOUNT PASSWORD:-""",
                        ur_cb_password2,
                        """\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲""",
                    )
    except:
        voiceover(vo_signin_acc_nf)
        print("\n🗣️ACCOUNT NOT FOUND IN OUR SERVERS, TRY WITH SOMEOTHER USERNAME⚠️")


# ----------------------------------------------------------------------------------------------------------------------
# CHANGE ACCOUNT DETAILS
def change_account_details():

    global sec_alert
    global cad_sin_cb_username_small
    global cad_user_phone_number
    global cad_user_dob

    try:
        voiceover(vo_signin_ac_un)
        cad_sin_cb_username_small = str(input("🗣ENTER YOUR ACCOUNT USERNAME:-"))
        voiceover(vo_signin_ac_pw)
        cad_sin_cb_password = str(input("🗣ENTER YOUR ACCOUNT PASSWORD:-"))
        cad_sin_cb_ch_password = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
            cad_sin_cb_username_small
        )
        mc1.execute(cad_sin_cb_ch_password)
        cad_sin_cb_ch_password1 = mc1.fetchone()
        for cad_sin_cb_ch_password2 in cad_sin_cb_ch_password1:
            while cad_sin_cb_password != cad_sin_cb_ch_password2:
                voiceover(vo_sigin_wpr)
                print(
                    """\n🗣️THE PASSWORD YOU HAVE ENTERED IS INVALID,
PLEASE, RE-ENTER YOUR ACCOUNT PASSWORD CORRECTLY⚠️"""
                )
                cad_sin_cb_password = str(input("\n🗣ENTER YOUR ACCOUNT PASSWORD:-"))
            else:
                cad_sin_cb_name = "SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                    cad_sin_cb_username_small
                )
                mc1.execute(cad_sin_cb_name, cad_sin_cb_password)
                cad_sin_cb_name1 = mc1.fetchone()
                for cad_sin_cb_name2 in cad_sin_cb_name1:
                    voiceover(vo_cad_menu)
                    print("-------------------------------")
                    print("\n🗣HEY", cad_sin_cb_name2, ",WHAT DO YOU LIKE TO CHANGE???.")
                    cad_user_ask = str(
                        input(
                            """\n[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 👤 CHANGE ACCOUNT NAME
[press 2] - 📱 CHANGE PHONE NUMBER
[Press 3] - 🐣 CHANGE DATE OF BIRTH
[Press 4] - 👦🏻👧🏻 CHANGE GENDER
[Press 5] - 🔐 CHANGE ACCOUNT PASSWORD
[Press 6] - 🗑 DELETE YOUR ACCOUNT:-"""
                        )
                    )
                    if cad_user_ask == "1":
                        voiceover(vo_cad_name)
                        print("\n======= 👤 CHANGE ACCOUNT NAME =======")
                        cad_user_name = str(input("🗣ENTER YOUR NEW NAME:-"))
                        cad_user_name1 = "UPDATE CHATTER_BOX_PROFILES SET CHATTER_NAME=%s WHERE USERNAME=%s"
                        cad_user_name2 = (cad_user_name, cad_sin_cb_username_small)
                        mc1.execute(cad_user_name1, cad_user_name2)
                        db.commit()
                        sec_alert = (
                            "\n✅"
                            + cad_sin_cb_name2
                            + ",YOUR ACCOUNT NAME HAS BEEN UPDATED FROM-"
                            + cad_sin_cb_name2
                            + "-TO-"
                            + cad_user_name
                            + "."
                        )
                        security_alert_fh(sec_alert)
                        voiceover(vo_cad_nc_updated)
                        print("\n🗣🛎YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️")
                        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    elif cad_user_ask == "2":
                        voiceover(vo_cad_ph_no)
                        print("\n======= 📱 CHANGE PHONE NUMBER =======")
                        cad_cb_phone_number = "SELECT CHATTER_PHONE_NUMBER FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                            cad_sin_cb_username_small
                        )
                        mc1.execute(cad_cb_phone_number)
                        cad_cb_phone_number1 = mc1.fetchone()
                        for cad_cb_phone_number_traverse in cad_cb_phone_number1:
                            cad_cb_phone_number_traverse_str = str(
                                cad_cb_phone_number_traverse
                            )

                        cad_user_phone_number = str(
                            input("ENTER YOUR NEW PHONE NUMBER:-")
                        )
                        cad_user_phone_number_str = str(cad_user_phone_number)
                        cad_user_phone_number1 = "UPDATE CHATTER_BOX_PROFILES SET CHATTER_PHONE_NUMBER=%s WHERE USERNAME=%s"
                        cad_user_phone_number2 = (
                            cad_user_phone_number,
                            cad_sin_cb_username_small,
                        )
                        mc1.execute(cad_user_phone_number1, cad_user_phone_number2)
                        db.commit()
                        sec_alert = (
                            "\n✅"
                            + cad_sin_cb_name2
                            + ",YOUR ACCOUNT PHONE NUMBER HAS BEEN UPDATED FROM-"
                            + cad_cb_phone_number_traverse_str
                            + "-TO-"
                            + cad_user_phone_number_str
                            + "."
                        )
                        security_alert_fh(sec_alert)
                        voiceover(vo_cad_nc_updated)
                        print("\n🗣🛎YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️")
                        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    elif cad_user_ask == "3":
                        voiceover(vo_cad_dob)
                        print("\n======= 🐣 CHANGE DATE OF BIRTH =======")
                        cad_cb_dob = "SELECT DATE_OF_BIRTH FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                            cad_sin_cb_username_small
                        )
                        mc1.execute(cad_cb_dob)
                        cad_cb_dob1 = mc1.fetchone()
                        for cad_cb_dob_traverse in cad_cb_dob1:
                            cad_cb_dob_traverse_str = str(cad_cb_dob_traverse)
                        try:
                            cad_user_dob = str(
                                input("ENTER YOUR NEW DATE OF BIRTH (YYYY_MM_DD):-")
                            )
                            cad_user_dob1 = "UPDATE CHATTER_BOX_PROFILES SET DATE_OF_BIRTH=%s WHERE USERNAME=%s"
                            cad_user_dob2 = (cad_user_dob, cad_sin_cb_username_small)
                            mc1.execute(cad_user_dob1, cad_user_dob2)
                            db.commit()
                            sec_alert = (
                                "\n✅"
                                + cad_sin_cb_name2
                                + ",YOUR ACCOUNT DATE OF BIRTH HAS BEEN UPDATED FROM-"
                                + cad_cb_dob_traverse_str
                                + "-TO-"
                                + cad_user_dob
                                + "."
                            )
                            security_alert_fh(sec_alert)
                            voiceover(vo_cad_nc_updated)
                            print("\n🗣🛎YOUR NOTIFICATION CENTRE HAS BEEN UPDATED️.️")
                            print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                        except:
                            voiceover(vo_ac_invalid_dob)
                            print("\n🗣️INVALID USER ENTERY IN DATE OF BIRTH⚠️")
                            print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    elif cad_user_ask == "4":
                        voiceover(vo_cad_gender)
                        print("\n======= 👦🏻👧🏻 CHANGE GENDER =======")
                        cad_cb_gender = "SELECT GENDER FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                            cad_sin_cb_username_small
                        )
                        mc1.execute(cad_cb_gender)
                        cad_cb_gender1 = mc1.fetchone()
                        for cad_cb_gender_traverse in cad_cb_gender1:
                            a = 1
                        cad_user_gender = str(input("🗣ENTER YOUR GENDER:-"))
                        cad_user_gender1 = "UPDATE CHATTER_BOX_PROFILES SET GENDER=%s WHERE USERNAME=%s"
                        cad_user_gender2 = (cad_user_gender, cad_sin_cb_username_small)
                        mc1.execute(cad_user_gender1, cad_user_gender2)
                        db.commit()
                        sec_alert = (
                            "\n✅"
                            + cad_sin_cb_name2
                            + ",YOUR ACCOUNT GENDER HAS BEEN UPDATED FROM-"
                            + cad_cb_gender_traverse
                            + "-TO-"
                            + cad_user_gender
                            + "."
                        )
                        security_alert_fh(sec_alert)
                        voiceover(vo_cad_nc_updated)
                        print("\n🗣🛎YOUR NOTIFICATION CENTRE HAS BEEN UPDATED️.️")
                        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    elif cad_user_ask == "5":
                        voiceover(vo_cad_pw)
                        print("\n======= 🔐 CHANGE ACCOUNT PASSWORD =======")
                        cad_cb_password = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                            cad_sin_cb_username_small
                        )
                        mc1.execute(cad_cb_password)
                        cad_cb_password1 = mc1.fetchone()
                        for cad_cb_password_traverse in cad_cb_password1:
                            a = 1
                        cad_user_password = str(input("🗣ENTER YOUR NEW PASSWORD:-"))
                        voiceover(vo_ac_reenter_new_pw)
                        cad_user_password1 = str(input("🗣RE-ENTER YOUR NEW PASSWORD:-"))
                        while cad_user_password != cad_user_password1:
                            voiceover(vo_ac_pw_mm)
                            print(
                                """\n🗣️THE PASSWORD YOU HAVE ENTERED DOESN'T MATCH.
PLEASE, ENTER THE SAME PASSWORD IN BOTH THE COLUMNS⚠️"""
                            )
                            cad_user_password = str(
                                input("\n🗣ENTER YOUR NEW PASSWORD:-")
                            )
                            voiceover(vo_ac_reenter_new_pw)
                            cad_user_password1 = str(
                                input("🗣RE-ENTER YOUR NEW PASSWORD:-")
                            )
                        else:
                            cad_user_password2 = "UPDATE CHATTER_BOX_PROFILES SET ACCOUNT_PASSWORD=%s WHERE USERNAME=%s"
                            cad_user_password3 = (
                                cad_user_password1,
                                cad_sin_cb_username_small,
                            )
                            mc1.execute(cad_user_password2, cad_user_password3)
                            db.commit()
                            sec_alert = (
                                "\n✅"
                                + cad_sin_cb_name2
                                + ",YOUR ACCOUNT PASSWORD HAS BEEN UPDATED FROM-"
                                + cad_cb_password_traverse
                                + "-TO-"
                                + cad_user_password
                                + "."
                            )
                            security_alert_fh(sec_alert)
                            voiceover(vo_cad_nc_updated)
                            print("\n🗣🛎YOUR NOTIFICATION CENTRE HAS BEEN UPDATED.️")
                            print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    elif cad_user_ask == "6":
                        voiceover(vo_cad_delete)
                        print("\n======= 🗑 DELETE YOUR ACCOUNT =======")
                        cad_cb_delete = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                            cad_sin_cb_username_small
                        )
                        mc1.execute(cad_cb_delete)
                        cad_cb_delete1 = mc1.fetchone()
                        for cad_cb_delete_traverse in cad_cb_delete1:
                            a = 1
                        cad_user_delete = str(
                            input(
                                "🗣ENTER YOUR ACCOUNT PASSWORD TO PERMANENTLY DELETE YOUR ACCOUNT:-"
                            )
                        )
                        while cad_cb_delete_traverse != cad_user_delete:
                            voiceover(vo_sigin_wpr)
                            print(
                                """\n🗣️THE PASSWORD YOU HAVE ENTERED IS INVALID,
PLEASE, RE-ENTER YOUR ACCOUNT PASSWORD⚠️"""
                            )
                            cad_cb_delete = "SELECT ACCOUNT_PASSWORD FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                                cad_sin_cb_username_small
                            )
                            mc1.execute(cad_cb_delete)
                            cad_cb_delete1 = mc1.fetchone()
                            for cad_cb_delete_traverse in cad_cb_delete1:
                                a = 1
                            cad_user_delete = str(
                                input("\n🗣ENTER YOUR ACCOUNT PASSWORD:-")
                            )
                        else:
                            cad_user_delete1 = "DELETE FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                                cad_sin_cb_username_small
                            )
                            mc1.execute(cad_user_delete1, cad_sin_cb_username_small)
                            db.commit()
                            voiceover(vo_cad_delete_final)
                            print(
                                "\n🗣",
                                cad_sin_cb_name2,
                                ",THIS IS OUR LAST GOOD BYE! 👋🏻.",
                            )
                            print(
                                "🗣✅",
                                cad_sin_cb_name2,
                                ",YOUR CHATTER BOX ACCOUNT HAS BEEN DELETED PERMANENTLY🗑",
                            )
                            print("😔😞😕")
                            print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                    else:
                        voiceover(vo_returned_back_hm)
                        print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")

    except:
        voiceover(vo_sigin_acc_nf)
        print("\n🗣️ACCOUNT NOT FOUND IN OUR SERVERS, TRY WITH SOMEOTHER USERNAME⚠️")
        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")


# ----------------------------------------------------------------------------------------------------------------------
# READING CHATS
def readchat():

    global fh_uidrc

    try:
        fh_uname = sin_cb_username_small
        voiceover(vo_chat_cb_un)
        fh_uidrc = input("\n🗣ENTER YOUR FRIEND CHATTER BOX USERNAME:-")
        fh_readchat_name = (
            r"chatter-box/CHATS/CHAT FROM_" + fh_uidrc + "_TO_" + fh_uname + ".dat"
        )
        with open(fh_readchat_name, "rb") as fh_readchat:
            voiceover(vo_chat_listed_below)
            print("\n🗣📜 CHATS ARE LISTED BELOW:")
            print("\n")
            str = " "
            while str:
                str = pickle.load(fh_readchat)
                str1 = str.strip("\n")
                print(str1)
            else:
                fh_readchat.close()
    except:
        a = 1


# ----------------------------------------------------------------------------------------------------------------------
# SENDING CHATS
def sendchat():

    readchat()
    sin_cb_username_small_str = str(sin_cb_username_small)
    fh_fac_number = fh_uidrc

    try:
        fh_cb_sc_name = (
            "SELECT CHATTER_NAME FROM CHATTER_BOX_PROFILES WHERE USERNAME='{}'".format(
                fh_fac_number
            )
        )
        mc1.execute(fh_cb_sc_name, fh_fac_number)
        fh_cb_sc_name1 = mc1.fetchone()
        for sc_ur_cb_name2 in fh_cb_sc_name1:
            a = 1

        print("\n🗣", ur_cb_name2, ",YOU ARE SENDING MESSAGE TO -", sc_ur_cb_name2, ".")

        # -----------------DIRECT MESSAGE-----------------
        fh_name = (
            r"chatter-box/CHATS/CHAT FROM_"
            + sin_cb_username_small_str
            + "_TO_"
            + fh_fac_number
            + ".dat"
        )
        with open(fh_name, "ab") as fh_sendchat:
            voiceover(vo_chat_type_msg)
            fh_chat = str(input("🗣TYPE YOUR MESSAGE HERE:-"))
            fh_rainbow_enc = "\t\t\t\t\t\t🟣🔵🟢🟡🟠🔴"
            datetime_str = str(datetime.datetime.now())
            fh_sender_name_time = (
                "\t\t[FROM]:"
                + ur_cb_name2
                + "-----[TO]:"
                + sc_ur_cb_name2
                + "-----[DATE TIME]:"
                + datetime_str
            )
            pickle.dump(fh_sender_name_time, fh_sendchat)
            pickle.dump(fh_chat, fh_sendchat)
            pickle.dump(fh_rainbow_enc, fh_sendchat)
            fh_sendchat.close()

        # ------------DUPLICATE SELF MESSAGE---------------
        fh_name_dup = (
            r"chatter-box/CHATS/CHAT FROM_"
            + fh_fac_number
            + "_TO_"
            + sin_cb_username_small_str
            + ".dat"
        )
        with open(fh_name_dup, "ab") as fh_sendchat_dup:
            fh_chat_dup = fh_chat
            fh_sender_name_time_dup = (
                "\t\t[FROM]:"
                + sc_ur_cb_name2
                + "-----[TO]:"
                + ur_cb_name2
                + "-----[DATE TIME]:"
                + datetime_str
            )
            pickle.dump(fh_sender_name_time_dup, fh_sendchat_dup)
            pickle.dump(fh_chat_dup, fh_sendchat_dup)
            fh_sendchat_dup.close()

        # --------------NOTIFICATION CENTRE------------------
        fh_ncl_alert = (
            r"chatter-box/NOTIFICATIONCENTRE/NC_"
            + fh_uidrc
            + "_NOTIFICATION CENTRE.dat"
        )
        with open(fh_ncl_alert, "ab") as notification_cl_a:
            sender_name_ncl_a = (
                "\n\t\t\t\t🫂 YOU HAVE RECEIVED A MESSAGE FROM," + ur_cb_name2 + "."
            )
            notification_canter_alert = fh_chat
            ncl_separator = "\n"
            pickle.dump(ncl_separator, notification_cl_a)
            pickle.dump(sender_name_ncl_a, notification_cl_a)
            pickle.dump(fh_sender_name_time, notification_cl_a)
            pickle.dump(notification_canter_alert, notification_cl_a)
            notification_cl_a.close()

            voiceover(vo_chat_msg_sent_re)
            print(
                "\n🗣🟣🔵🟡🔴 - YOUR MESSAGE HAS BEEN SENT SECURELY WITH RAINBOW ENCRYPTION 🏳‍🌈."
            )
    except:
        voiceover(vo_signin_acc_nf)
        print("🗣️ACCOUNT NOT FOUND IN OUR SERVERS, TRY WITH SOMEOTHER USERNAME⚠️")
        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")


# ----------------------------------------------------------------------------------------------------------------------
# FIND YOUR FRIENDS
def find_your_friends():
    voiceover(vo_fyf_search)
    fyf = str(input("\nENTER YOUR FRIEND NAME TO BE SEARCHED:-"))
    fyf1 = fyf + "%"
    fyf_search = "SELECT USERNAME, CHATTER_NAME, CHATTER_PHONE_NUMBER FROM CHATTER_BOX_PROFILES WHERE CHATTER_NAME LIKE '{}'".format(
        fyf1
    )
    mc1.execute(fyf_search)
    fyf_search1 = mc1.fetchall()
    voiceover(vo_fyf_similar_search)
    print("ACCOUNTS SIMILAR TO YOUR SEARCH ARE LISTED BELOW.")
    print("\nUSERNAME---NAME---PHONE NUMBER")
    for fyf_search_transverse in fyf_search1:
        print(fyf_search_transverse)


# ----------------------------------------------------------------------------------------------------------------------
# HANDCRICKET WITH MACHINE
def handcricket_with_machine():
    A = ur_cb_name2

    def user_batting():
        global f
        voiceover(vo_hc_menu)
        print("\t\t🏏 WELCOME TO HAND CRICKET GAME.")
        print("\t\t\t👨🏻 HUMAN VS 🖥 MACHNE")
        print("\n\t\tMACHINE WON THE TOSS, AND IT CHOSES TO CHASE.")
        b = 1
        c = 2
        f = 0
        a = 1
        if a == 1:
            print(
                ur_cb_name2,
                ",BATTING. ALLOWED CHARACTERS ARE 0 TO 5. NOT MORE THAN THAT.",
            )
            while a == 1:
                print("=======================================")
                try:
                    d = int(input("🗣USER:🏏BATTING:-"))
                except:
                    print("🗣 ALPHABETS AND SPECIAL CHARACTERS ARE NOT ALLOWED ⚠️")
                if d < 6:
                    e = random.randrange(1, 6)
                    voiceover(vo_m_bowl)
                    print("🗣MACHINE:🎾BOWLING:-", e)
                    if d != e:
                        f = f + d
                        voiceover(vo_u_score)
                        print("\t\t\t\t\t\t🗣YOUR SCORE: ", f)
                    else:
                        voiceover(vo_u_out)
                        print("\n\t\t\t🗣xxxxxxx 🦆🦆🦆 USER OUT! 🦆🦆🦆 xxxxxxxx")
                        print("\t\t\t\t\t✔︎ YOUR TOTAL SCORE: ", f)
                        break
                else:
                    print("\t\t\t🗣 INVALID INPUT ⚠️")

    def user_bowling():
        global f1
        print("\n🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾🎾")
        print("\t\t\t🗣NOW YOU ARE BOWLING.")
        g = 2
        h = 2
        f1 = 0
        if g == h:
            print(ur_cb_name2, ",ALLOWED CHARACTERS ARE 0 TO 5. NOT MORE THAN THAT.")
            while 2 == 2:
                print("=========================================")
                try:
                    i = int(input("🗣USER:🎾BOWLING:-"))
                except:
                    print("🗣 ALPHABETS AND SPECIAL CHACRATERS ARE NOT ALLOWED ⚠️")
                if i > 5:
                    print("\t\t\t🗣 INVALID INPUT ⚠️")
                else:
                    j = random.randrange(1, 6)
                    voiceover(vo_u_bowl)
                    print("🗣MACHINE:🏏BATTING:-", j)
                    if j != i:
                        f1 = f1 + j

                        print("\t\t\t\t\t\t🗣MACHINE SCORE:", f1)
                        if f1 > f:
                            voiceover(vo_m_won)
                            print("\n\t\t\t\t🗣🏆🏆🏆 MACHINE WON THE MATCH  🏆🏆🏆")
                            print(
                                "\t\t\t\t👍🏻👍🏻👍🏻 BETTER LUCK NEXT TIME! 👍🏻👍🏻👍🏻"
                            )
                            break
                    elif j == i:
                        voiceover(vo_m_out)
                        print("\n\t\t\t🗣xxxxxxxx 🦆🦆🦆 MACHINE OUT! 🦆🦆🦆 xxxxxxx")
                        print("\n\t\t\t\t\t✔︎ MACHINE TOTAL SCORE:", f1)
                        break

    user_batting()
    user_bowling()
    if f == f1:
        voiceover(vo_m_draw)
        print("\n\t\t\t\t\t🗣------- MATCH DRAW -------")
        print("\t\t\t👍🏻👍🏻👍🏻 BETTER LUCK NEXT TIME! 👍🏻👍🏻👍🏻")
    elif f > f1:
        voiceover(vo_u_won)
        print("\n\t\t\t\t🗣🏆🏆🏆", ur_cb_name2, "WON THE MATCH 🏆🏆🏆")
        print("\t\t👏🏻👏🏻👏🏻 CONGRAGULATIONS, WELL PLAYED 👏🏻👏🏻👏🏻")


# ----------------------------------------------------------------------------------------------------------------------
# ABOUT US
def About_us():
    fh_about_us = open(
        r"chatter-box/ABOUTUS/CHATTER_BOX_ABOUT_US.txt",
        "r",
    )
    str = " "
    while str:
        str = fh_about_us.readline()
        str = str.strip("\n")
        print(str)
    fh_about_us.close()


# ----------------------------------------------------------------------------------------------------------------------
# FEEDBACK
def feedback():
    fb_in = sin_cb_username_small
    fb_fh_rn = r"chatter-box/FEEDBACK/Feedback_by_" + fb_in + ".dat"
    fb_fh_a = open(fb_fh_rn, "a")
    datetime_str = str(datetime.datetime.now())
    fh_sender_name_time = "[FROM]:" + ur_cb_name2 + "-------DATE TIME:" + datetime_str
    fb_fh_a.write(fh_sender_name_time)
    fb_fh_a.write("\n")
    voiceover(vo_give_us_fb)
    fb_ask = str(input("🗣GIVE US YOUR FEEDBACK:-"))
    fb_fh_a.writelines(fb_ask)
    fb_fh_a.write("\n")
    fb_fh_a.close()
    voiceover(vo_tq_fb)
    print("\n🗣", ur_cb_name2, ",WE REALLY APPRECIATE USERS FEEDBACK,")
    print("YOUR VALUABLE FEEDBACK MENT LOT TO US, THANKYOU FOR YOUR INTEREST😘")
    print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")


# ______________________________________________________________________________________________________________________
# xxxxxxxxxxxxx MAIN LOOP xxxxxxxxxxxxx

print(
    """===============================

              WELCOME TO CHATTER BOX
              SIMPLY LOVEABLE
              MADE IN 🤍️ WITH 🇮🇳"""
)

voiceover(vo_home)


def homeloop():
    while True:
        ml_userinput = str(
            input(
                """\n🗣======= 🏠 HOME MENU =======
[Press *] - 🔔 VIEW NOTIFICATION CENTRE
[Press 1] - 👤 ACCOUNT SETTINGS
[Press 2] - 💬 CHAT WITH YOUR FRIENDS
[Press 3] - 🏏 PLAY HAND-CRICKET WITH MACHINE
[Press 4] - 📜 ABOUT US & 📝 FEEDBACK
[Press 5] - 🔒 LOG-OUT FROM CHATTER BOX:-"""
            )
        )
        if ml_userinput == "*":
            print("\n🗣======= 🔔 NOTIFICATION CENTRE =======")
            try:
                notification_centre()
                print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")
            except:
                voiceover(vo_nc_err)
                print(
                    "🗣️PLEASE SIGN-IN TO YOUR CHATTER BOX ACCOUNT TO VIEW NOTIFICATIONS⚠️"
                )
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

        elif ml_userinput == "1":
            print("\n🗣======= 👤 ACCOUNT SETTINGS =======")
            voiceover(vo_acc_settings_menu)
            ml_ui_ad = str(
                input(
                    """[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 👤 CREATE NEW CHATTER BOX ACCOUNT
[Press 2] - 🔐 SIGN-IN INTO EXISTING ACCOUNT
[Press 3] - ⚙️ CHANGE ACCOUNT DETAILS:-"""
                )
            )

            if ml_ui_ad == "1":
                print("\n======= 👤+ CREATE NEW CHATTER BOX ACCOUNT =======")
                create_new_account()
                print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")

            elif ml_ui_ad == "2":
                voiceover(vo_urabt_signin)
                print("\n🗣======= 🔐 SIGN-IN CHATTER BOX ACCOUNT =======")
                sign_in()
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

            elif ml_ui_ad == "3":
                print("\n🗣======= ⚙️ CHANGE ACCOUNT DETAILS =======")
                change_account_details()
            else:
                voiceover(vo_returned_back_hm)
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

        elif ml_userinput == "2":
            print("\n🗣======= 💬 CHAT =======")
            try:
                A = ur_cb_name2
                voiceover(vo_chat_menu)
                ml_chat_menu = str(
                    input(
                        """[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 💬 CHAT WITH YOUR FRIENDS
[Press 2] - 🔍 FIND YOUR FRIENDS:-"""
                    )
                )
                if ml_chat_menu == "1":
                    try:
                        sendchat()
                    except:
                        voiceover(vo_signin_chat)
                        print(
                            "🗣PLEASE SIGN-IN TO YOUR CHATTER BOX ACCOUNT TO CHAT WITH YOUR FRIENDS⚠️"
                        )
                        print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                elif ml_chat_menu == "2":
                    find_your_friends()
                    print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

                else:
                    voiceover(vo_returned_back_hm)
                    print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")
            except:
                voiceover(vo_chat_err)
                print(
                    "🗣PLEASE SIGN-IN TO YOUR CHATTER BOX ACCOUNT TO CHAT WITH YOUR FRIENDS⚠️"
                )
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

        elif ml_userinput == "3":
            print("\n🗣======= 🏏 PLAY HAND-CRICKET WITH MACHINE =======")
            try:
                handcricket_with_machine()
                print("\n🗣YOU HAVE RETURNED BACK TO HOME MENU.")
            except:
                voiceover(vo_hc_err)
                print(
                    "🗣️PLEASE SIGN-IN TO YOUR CHATTER BOX ACCOUNT TO PLAY HAND-CRICKET⚠️"
                )
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")
                homeloop()

        elif ml_userinput == "4":
            voiceover(vo_af_menu)
            print("\n🗣======= 📜 ABOUT US & 📝 FEEDBACK =======")
            ml_ui_au_fb = str(
                input(
                    """[Press 0] - 🏠 RETURN BACK TO HOME MENU
[Press 1] - 📜 KNOW ABOUT US
[Press 2] - 📝 GIVE US YOUR FEEDBACK:-"""
                )
            )

            if ml_ui_au_fb == "1":
                print("\n======= 📜 ABOUT US =======")
                voiceover(vo_about_us)
                About_us()
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")

            elif ml_ui_au_fb == "2":
                print("\n======= 📝 FEEDBACK =======")
                try:
                    feedback()
                except:
                    voiceover(vo_fb_err)
                    print(
                        "🗣️PLEASE SIGN-IN TO YOUR CHATTER BOX ACCOUNT TO GIVE US YOUR FEEDBACK⚠️"
                    )
                    print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")
                    homeloop()
            else:
                print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")
                voiceover(vo_returned_back_hm)

        elif ml_userinput == "5":
            voiceover(vo_logout)
            print("\n🗣======= 🔒 YOU HAVE LOGGED OUT FROM CHATTER BOX =======")
            print("YOUR ACCOUNT DETAILS ARE ENCRYPTED.")
            print("❌❌❌❌❌❌❌❌❌❌❌❌❌")
            a = str(input())
            a1 = 1
            if 1 == a1:
                quit()

        else:
            voiceover(vo_invaild_hm)
            print("\n🗣======= ⚠️ INVALID USER INPUT IN HOME MENU ⚠️ =======")
            print("🗣YOU HAVE RETURNED BACK TO HOME MENU.")


# **********************************************************************************************************************
# MAIN CALL

homeloop()
