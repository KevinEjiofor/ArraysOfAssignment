def welcome():
    print(f""" 
        ==============================================================================
                                         N O K I A
        ===============================================================================
        """)
    user = input("enter 1 for menu : ")
    if user == "1":
        menu()
    else:
        print("wrong entry")
        user = input("enter 1 for menu : ")


def phone_book():
    print("""
    =====================================
                 Phone Book
    =====================================
            1. Search
            2. Service Nos. 1
            3. Add name
            4. Erase
            5. Edit
            6. Assign tone
            7. Send b’card  
            8. Options 
            9. Speed dials
            10. Voice tags
            0.  Back """)
    user_entry = input("Enter menu number : ")
    if user_entry == "0":
        menu()
    elif user_entry == "1":
        Search()
    elif user_entry == "2":
        Service_Nos()
    elif user_entry == "3":
        Add_name()
    elif user_entry == "4":
        Erase()
    elif user_entry == "5":
        Edit()
    elif user_entry == "6":
        Assign_tone()
    elif user_entry == "7":
        Send_bcard()
    elif user_entry == "8":
        options()
    elif user_entry == "9":
        Speed_dials()
    elif user_entry == "10":
        Voice_tag()
    else:
        print("wrong entry")
        phone_book()


def Search():
    print("""
    ==================================
            Search
    ==================================
        1. Back
        00. Go to the main menu""""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Search()


def Service_Nos():
    print("""
    ===============================
            Service Nos
    ===============================
            1. Back 
            00. Go to the main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Service_Nos()


def Add_name():
    print(""""
    ==============================
                 Add name
    ==============================
        1. Back
        00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Add_name()


def Erase():
    print("""
    ==============================
                 Erase
    ==============================
            1. Back
            00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Erase()


def Edit():
    print("""
    ===========================
             Edit
    ============================
        1. Back
        00. Main Menu
    """)
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Edit()


def Assign_tone():
    print(""""
    ==========================
             Assign Tone
    ===========================
    1. Back
    00. Main Menu""")

    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Assign_tone()


def Send_bcard():
    print("""
    ====================================
                Send b’card
    ====================================
                1. Back
                00. Main Menu
    """)
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Send_bcard()


def options():
    print("""
    ================================
                options
    ================================
            1. Type of view
            2. Memory status
            3. back
            00. Main Menu
    """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Type_of_view()
    elif user_entry == "2":
        Memory_status()
    elif user_entry == "3":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        options()


def Type_of_view():
    print("""
    ========================================
                 Type of view 
    ========================================    
             1. back
            00. Main Menu
            """)
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        options()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Type_of_view()


def Memory_status():
    print("""
    ===================================
                Memory Status
    ====================================
            1. back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        options()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Memory_status()


def Speed_dials():
    print("""
    =================================
            Speed dials
    =================================
            1. Back
            00. Main Menu
            """)
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Speed_dials()


def Voice_tag():
    print("""
    ====================================
                 Voice Tag
    ====================================
            1. Back 
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        phone_book()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Voice_tag()


def Messages():
    print("""
        ======================================
                        Messages
        ======================================
            1. Write messages
            2. Inbox
            3. Outbox
            4. Picture messages
            5. Templates
            6. Smileys
            7. Message settings
            8. Info service
            9. Voice mailbox number
            10.Service command editor
            0. Back""")

    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Write_messages()
    elif user_entry == "2":
        Inbox()
    elif user_entry == "3":
        Outbox()
    elif user_entry == "4":
        Picture_messages()
    elif user_entry == "5":
        Templates()
    elif user_entry == "6":
        Smileys()
    elif user_entry == "7":
        Message_settings()
    if user_entry == "0":
        menu()
    else:
        Messages()


def Write_messages():
    print("""
    ================================
            Write messages
    =================================
                1. Back 
                00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Write_messages()


def Inbox():
    print("""
    =====================================
                    Inbox
    =====================================
            1. Back
            00.Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Inbox()


def Outbox():
    print("""
    =================================
                Outbox
    =================================
            1. Back
            00.Main Menu""")

    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Outbox()


def Picture_messages():
    print("""
    ==================================
             Picture Messages
    ==================================
            1. Back
            00.Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Picture_messages()


def Templates():
    print("""
    ================================
                Templates
    ================================
             1. Back
            00.Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Templates()


def Smileys():
    print("""
    =======================================
                    Smileys
    =======================================
                1. Back
                00. Main Menu """)
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Smileys()


def Message_settings():
    print(""""
    ===============================
            Message Settings
    ===============================
            1. Set 12
            2. Common 13
            3. Back
            00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Set()
    elif user_entry == "2":
        Common()
    elif user_entry == "3":
        Messages()
    elif user_entry == "00":
        menu()
    else:
        Message_settings()


def Set():
    print("""
    =================================
                Set
    =================================
            1. Message centre number
            2. Messages sent as       
            3. Message validity
            4. back """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Message_Centre_Number()
    elif user_entry == "2":
        Message_Sent_as()
    elif user_entry == "3":
        Message_Validity()
    elif user_entry == "4":
        Messages()

    else:
        Set()


def Message_Centre_Number():
    print("""
    +++++++++++++++++++++++++++++++++++
            Message Centre Number
    ++++++++++++++++++++++++++++++++++++
            1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Message_Centre_Number()


def Message_Sent_as():
    print("""
    +++++++++++++++++++++++++++++++++++++
            Messages Sent
    +++++++++++++++++++++++++++++++++++++
                1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Message_Sent_as()


def Message_Validity():
    print("""
    +++++++++++++++++++++++++++++++++++++
                Message Validity
    +++++++++++++++++++++++++++++++++++++  
              1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Message_Validity()


def Common():
    print("""
    =============================
            Common
    =============================
    1. Delivery reports
    2. Reply via same centre
    3 . Character support
    4. Back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Delivery_Reports()
    elif user_entry == "2":
        Reply()
    elif user_entry == "3":
        Character_support()
    elif user_entry == "4":
        Messages()

    else:
        Common()


def Delivery_Reports():
    print("""
        ++++++++++++++++++++++++++++++++++
                Delivery Reports
        ++++++++++++++++++++++++++++++++++
            1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Delivery_Reports()


def Reply():
    print("""
    +++++++++++++++++++++++++++++++++++++
            Reply via same centre
    +++++++++++++++++++++++++++++++++++++
            1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Reply()


def Character_support():
    print(""""
    +++++++++++++++++++++++++++++++++++
             Character Support
    +++++++++++++++++++++++++++++++++++
            1. Back
            00. Main Menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Set()
    elif user_entry == "00":
        menu()
    else:
        print("wrong entry")
        Character_support()


def chat():
    print("""
    =======================
             chat
    ========================
    0. Back
    """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        chat()


def Call_register():
    print("""
    ================================
            Call register
    ================================
            1. Missed calls
            2. Received calls
            3. Dialled numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs 
            7. Call cost settings
            8. Prepaid credit
            0.Back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Missed_Call()
    elif user_entry == "2":
        Received_calls()
    elif user_entry == "3":
        Dialled_numbers()
    elif user_entry == "4":
        Erase_recent()
    elif user_entry == "5":
        Show_call_duration()
    elif user_entry == "6":
        Show_call_costs()
    elif user_entry == "7":
        Call_cost_settings()
    elif user_entry == "8":
        Prepaid_credit()
    elif user_entry == "0":
        menu()
    else:
        Call_register()


def Missed_Call():
    print("""
       =========================================
                   Missed Call
       =========================================
                   1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Missed_Call()


def Received_calls():
    print("""
    =======================================
                Received Calls
    ======================================= 
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Received_calls()


def Dialled_numbers():
    print("""
    =====================================
                Dialled Numbers
    =====================================              
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Dialled_numbers()


def Erase_recent():
    print("""
    =========================================
                Erase recent call lists
    ==========================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Erase()


def Show_call_duration():
    print("""
    =================================
            Show call duration
    =================================
            1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers
            6. Back
            00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Last_call()
    elif user_entry == "2":
        All()
    elif user_entry == "3":
        Received()
    elif user_entry == "4":
        Dialled()
    elif user_entry == "5":
        Clear_timers()
    elif user_entry == "6":
        Call_register()

    elif user_entry == "00":
        menu()
    else:
        Show_call_duration()


def Last_call():
    print("""
    =========================================
                Last call
    =========================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_duration()
    elif user_entry == "00":
        menu()
    else:
        Last_call()


def All():
    print("""
    ===============================================
                    All calls’ duration
    ===============================================         
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_duration()
    elif user_entry == "00":
        menu()
    else:
        All()


def Received():
    print("""
    ==============================================
                Received calls’ duration
    ==============================================
                 1. Back
                 00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_duration()
    elif user_entry == "00":
        menu()
    else:
        Received()


def Dialled():
    print("""
    ==========================================
            Dialled calls’ duration
    ==========================================
                   1. Back
                 00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_duration()
    elif user_entry == "00":
        menu()
    else:
        Dialled()


def Clear_timers():
    print("""
    ==========================================
                    Clear timers
    ==========================================
                 1. Back
                 00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_duration()
    elif user_entry == "00":
        menu()
    else:
        Clear_timers()


def Show_call_costs():
    print("""
    ===============================
            Show call cost
    ===============================
            1. Last call cost
            2. All calls’ cost
            3. Clear counters
            4. Back
            00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Last_call_cost()
    elif user_entry == "2":
        All_calls_cost()
    elif user_entry == "4":
        Call_register()
    elif user_entry == "5":
        Clear_counters()
    elif user_entry == "00":
        menu()
    else:
        Show_call_costs()


def Last_call_cost():
    print("""
    ======================================
                Last call cost
    ======================================     
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_costs()
    elif user_entry == "00":
        menu()
    else:
        Last_call()


def All_calls_cost():
    print("""
    =============================================
                    All calls’ cost
    =============================================
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_costs()
    elif user_entry == "00":
        menu()
    else:
        All_calls_cost()


def Clear_counters():
    print("""
    ======================================
                Clear counters
    ======================================
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Show_call_costs()
    elif user_entry == "00":
        menu()
    else:
        Clear_counters()


def Call_cost_settings():
    print("""
        ===========================================
                Call  cost setting
        ===========================================
                    1. Call cost limit
                    2. Show costs in
                    3 back
                    00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Call_cost_settings()
    elif user_entry == "2":
        Show_call_costs()
    elif user_entry == "3":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Call_cost_settings()


def Call_cost_limit():
    print("""
        ==============================================
                     Call cost limit
        ==============================================
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_cost_settings()
    elif user_entry == "00":
        menu()
    else:
        Call_cost_limit()


def Show_costs_in():
    print("""
    ===========================================
                 Show costs in
    ============================================
                1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_cost_settings()
    elif user_entry == "00":
        menu()
    else:
        Show_costs_in()


def Prepaid_credit():
    print("""
    ==============================================
                Prepaid credit
    ==============================================
                   1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_register()
    elif user_entry == "00":
        menu()
    else:
        Prepaid_credit()


def Tones():
    print("""
    ==================================
                Tones       
    ==================================
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                0. back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        Tones()


def Settings():
    print("""
    ============================
            Setting
    ============================
            1. Call settings
            2. Phone settings
            3. Security settings
            4. Restore factory settings
             0. Back           """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    elif user_entry == "1":
        Call_settings()
    elif user_entry == "2":
        Phone_settings()
    elif user_entry == "3":
        Security_settings()
    elif user_entry == "4":
        Restore_factory_settings()
    else:
        Settings()


def Restore_factory_settings():
    print("""
    =================================================
                 Restore factory settings
    =================================================
                        1. Back 
                        00. Main Menu""")
    user_entry = input("Enter a menu number: ")
    if user_entry == "1":
        Settings()
    elif user_entry == "00":
        menu()
    else:
        Restore_factory_settings()


def Call_settings():
    print("""
    =====================================
                 Call Setting
    ======================================
                1. Automatic redial
                2. Speed dialling
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Automatic answer 1
                7. Back 
                00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Automatic_redial()
    elif user_entry == "2":
        Speed_dialling()
    elif user_entry == "3":
        Call_waiting()
    elif user_entry == "4":
        Own_number()
    elif user_entry == "5":
        Phone_line()
    elif user_entry == "6":
        Automatic_answer()
    elif user_entry == "7":
        Settings()
    elif user_entry == "00":
        menu()
    else:
        Call_settings()


def Automatic_redial():
    print("""
    ==========================================
                Automatic redial
    ========================================== 
                     1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Automatic_redial()


def Speed_dialling():
    print("""
    =========================================
    
    =========================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Speed_dialling()


def Call_waiting():
    print("""
    =====================================
            Call waiting options
    ======================================  
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Call_waiting()


def Own_number():
    print("""
    =======================================
             Own number sending
    ======================================= 
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Own_number()


def Phone_line():
    print("""
    =========================================
                Phone line in use
    ========================================= 
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Phone_line()


def Automatic_answer():
    print(""""
        ======================================
               Automatic answer 1
        ======================================       
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Automatic_answer()


def Phone_settings():
    print("""   
         ==============================================
                    Phone Settings
         ==============================================       
                1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                5. Lights2
                6. Confirm SIM service actions
                7. Back 
                00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Language()
    elif user_entry == "2":
        Cell_info_display()
    elif user_entry == "3":
        Welcome_note()
    elif user_entry == "5":
        Lights()
    elif user_entry == "6":
        Confirm_SIM()
    elif user_entry == "7":
        Settings()
    elif user_entry == "00":
        menu()
    else:
        Phone_settings()


def Language():
    print("""
    =============================================
                    Language
    =============================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Language()


def Cell_info_display():
    print("""
    ========================================
                 Cell info display
    =======================================
                     1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Cell_info_display()


def Welcome_note():
    print("""
    ===================================
             Welcome note
    ====================================
                       1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Welcome_note()


def Network_selection():
    print("""
        ==============================================
                     Network selection
        ==============================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Network_selection()


def Lights():
    print("""
    =============================================
                    Lights2
    =============================================
                    1. Back
                   00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Lights()


def Confirm_SIM():
    print("""   
    ===========================================================
                    Confirm SIM service actions
    ===========================================================
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Call_settings()
    elif user_entry == "00":
        menu()
    else:
        Confirm_SIM()


def Security_settings():
    print("""
    =====================================
             Security setting
    =====================================
    
                1. PIN code request
                2. Call barring service
                3. Fixed dialling
                4. Closed user group
                5. Phone security
                6. Change access codes
                 7. Back 
                 00. Main Menu""")
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        PIN_code_request()
    elif user_entry == "2":
        Call_barring_service()
    elif user_entry == "3":
        Fixed_dialling()
    elif user_entry == "4":
        Closed_user_group()
    elif user_entry == "5":
        Phone_settings()
    elif user_entry == "6":
        Change_access_codes()
    elif user_entry == "7":
        Settings()
    elif user_entry == "0":
        menu()
    else:
        Security_settings()


def PIN_code_request():
    print("""
    =================================================
                    PIN code request
    ================================================
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        PIN_code_request()


def Call_barring_service():
    print("""
    ==============================================
                Call barring service
    ==============================================  
                 1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        Call_barring_service()


def Fixed_dialling():
    print("""
        ===========================================
                       Fixed dialling
        ============================================
                1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        Fixed_dialling()


def Closed_user_group():
    print("""
    ========================================
                Closed user group
    ========================================
                1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        Closed_user_group()


def Phone_security():
    print("""
    =============================================
                 Phone security
    =============================================
                1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        Phone_settings()


def Change_access_codes():
    print("""
    ==============================================
                Change access codes
    ==============================================
                1. Back
                00. Main menu""")
    user_entry = input("Enter menu number : ")
    if user_entry == "1":
        Security_settings()
    elif user_entry == "00":
        menu()
    else:
        Change_access_codes()


def Call_divert():
    print("""
    ==================================
            Call divert
    =================================
             call divert 
             0. Back """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        Call_divert()


def Games():
    print("""
    =================================
                Game
    =================================
                1. Snake Game
                2. puzzle
                3. Sudo 
                0. Back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    elif user_entry == "1":
        Snake_Game()
    elif user_entry == "2":
        Puzzle()
    elif user_entry == "3":
        Sudo()

    else:
        Games()


def Snake_Game():
    print("""
        =====================================
                         Snake Game
        ===================================== 
                    1. Back
                    00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Games()
    elif user_entry == "00":
        menu()
    else:
        Snake_Game()


def Puzzle():
    print("""
    ============================================
                        Puzzle
    =============================================
                    1. Back
                    00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Games()
    elif user_entry == "00":
        menu()
    else:
        Puzzle()


def Sudo():
    print("""
        ==============================================
                         Sudo
        ==============================================
                            1. Back
                            00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Games()
    elif user_entry == "00":
        menu()
    else:
        Puzzle()


def Calculator():
    print("""
    ========================
            Calculator
    ========================
        Calculator
        0. Back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        Calculator()


def Reminders():
    print("""
    =========================
            Reminder
    =========================
            Reminder
            0. Back
             """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        Reminders()


def Clock():
    print("""
    =================================
                 Clock
    =================================
                1. Alarm clock  
                2. Clock settings 
                3. Date setting
                4. Stopwatch 
                5. Countdown timer   
                6. Auto update of date and time
                0. Back """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    elif user_entry == "1":
        Alarm_clock()
    elif user_entry == "2":
        Clock_settings()
    elif user_entry == "3":
        Date_setting()
    elif user_entry == "4":
        Stopwatch()
    elif user_entry == "5":
        Countdown_timer()
    elif user_entry == "6":
        Auto_update()
    else:
        Clock()


def Alarm_clock():
    print("""  
       =======================================
                     Alarm clock
       =======================================
                    1. Back
                    00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Alarm_clock()


def Clock_settings():
    print("""
    ==================================
                Clock settings 
    ===================================
                1. Back
                 00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Clock_settings()


def Date_setting():
    print("""
    ==================================
                Date settings 
    ===================================
                1. Back
                 00. Main Menu
                            """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Date_setting()


def Stopwatch():
    print("""
     ==================================
                 Stopwatch
     ===================================
                 1. Back
                  00. Main Menu
                             """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Stopwatch()


def Countdown_timer():
    print("""
         ==================================
                    Countdown timer
         ===================================
                     1. Back
                      00. Main Menu
                                 """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Countdown_timer()


def Auto_update():
    print("""
    =========================================
            Auto update of date and time
    ==========================================
                       1. Back
                      00. Main Menu
                                 """)
    user_entry = input("Enter menu number: ")
    if user_entry == "1":
        Clock()
    elif user_entry == "00":
        menu()
    else:
        Auto_update()


def Profiles():
    print("""
    ============================
            Profiles
    ============================
            Profiles
            0. Back """)
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()
    else:
        Profiles()


def SIM_services():
    print("""
    ========================
        Sim services
    ========================
    Sim services
    0.  Back""")
    user_entry = input("Enter menu number: ")
    if user_entry == "0":
        menu()


def menu():
    print(f"""  
                ===================================================                
                                      MENU
                ===================================================                
                            (1) Phone book 
                            (2) Messages     
                            (3) Chat         
                            (4) call register
                            (5) Tones       
                            (6) Settings    
                            (7) Call_divert   
                            (8)Games 
                            (9) Calculator 
                            (10) Reminder    
                            (11) Clock        
                            (12) Profile
                            (13) SIM services
                            (00) Home Screen 
                             """)

    user_entry = input("enter menu number : ")
    if user_entry == "00":
        welcome()
    if user_entry == "1":
        phone_book()
    elif user_entry == "2":
        Messages()
    elif user_entry == "3":
        chat()
    elif user_entry == "4":
        Call_register()
    elif user_entry == "5":
        Tones()
    elif user_entry == "6":
        Settings()
    elif user_entry == "7":
        Call_divert()
    elif user_entry == "8":
        Games()
    elif user_entry == "9":
        Calculator()
    elif user_entry == "10":
        Reminders()
    elif user_entry == "11":
        Clock()
    elif user_entry == "12":
        Profiles()
    elif user_entry == "13":
        SIM_services()

    else:
        menu()


welcome()

menu()
