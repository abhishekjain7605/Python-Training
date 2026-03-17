import streamlit as st
import backend as bk

bk = bk.Bank()
st.title("Welcome to Aapka Bank")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if "Show_Balance" not in st.session_state:  
    st.session_state.Show_Balance = False
    
if "Show_Transaction_History" not in st.session_state:
    st.session_state.Show_Transaction_History = False

# Dialog box for creating a new account
@st.dialog("Create a new account")
def create_account_box():
    username = st.text_input("Username")
    password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        if bk.register_new_user(username, password):
            st.error("Account with this name already exists, Please choose a different username")
        else:
            st.success(f"Account created successfully\nWelcome to your new account {username}!")
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()


# Dialog box for logging in to an existing account
@st.dialog("Login to your account")
def login_box():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if bk.login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password")
            
# Dashboard for Deposit and Withdrawal
@st.dialog("Deposit Money")
def deposit_box():
    amount = st.number_input("Enter amount to deposit", min_value=0.0, step=10.0)
    if st.button("Deposit"):
        bk.deposit(st.session_state.username, amount)
        st.success(f"Deposited ₹ {amount} successfully!")
        if st.session_state.Show_Transaction_History:
            st.session_state.Show_Transaction_History = True
        st.rerun()

@st.dialog("Withdraw Money")
def withdrawal_box():
    amount = st.number_input("Enter the amount to withdraw", min_value=0.0, step=10.0)
    if st.button("Withdraw"):
        bk.withdraw(st.session_state.username, amount)
        st.success(f"withdrawed ₹ {amount} successfully!")
        if st.session_state.Show_Transaction_History:
            st.session_state.Show_Transaction_History = True
        st.rerun()




st.sidebar.header("Menu")

# Sidebar before login
if not st.session_state.logged_in:
    
    if st.sidebar.button("Login to your account"):
        login_box()

    if st.sidebar.button("Create a new account"):
        create_account_box()
        
    st.sidebar.button("Admin Login")
 
# Sidebar after login 
else:
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    st.subheader(f"Welcome back, {st.session_state.username}!")
    
    if st.sidebar.button("Deposit"):
        deposit_box()
    if st.sidebar.button("Withdraw"):
        withdrawal_box()
    
    st.sidebar.divider()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # Dashboard after login
    col1, col2 = st.columns(2)

    with col1:
        sub1, sub2 = st.columns(2)
            
        with sub1:
            st.header("Balance")
    with col2:
        sub3, sub4 = st.columns(2)
        with sub4:
            st.write(" ")
            if st.button("👁️"):
                st.session_state.Show_Balance = not st.session_state.Show_Balance
                
        with sub3:
            if st.session_state.Show_Balance:
                st.header(f"₹ {bk.view_balance(st.session_state.username)}")
            else:
                st.header("₹ *****")
    
    col3, col4, col5 = st.columns([0.5,2,1.5])
    with col4:
        st.header("Transaction History")
    
    with col5:
        st.write(" ")
        if st.button("View History"):
            st.session_state.Show_Transaction_History = not st.session_state.Show_Transaction_History
        
    with st.container(border= True):
        t = bk.transaction_history(st.session_state.username)
        if st.session_state.Show_Transaction_History:
            for tt in t:
                st.write(tt)
                
    
            
        