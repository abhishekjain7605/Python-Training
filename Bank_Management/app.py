import streamlit as st
import backend as bk

bk = bk.Bank()
st.title("Welcome to Aapka Bank")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""


# Dialog box for creating a new account
@st.dialog("Create a new account")
def create_account_box():
    username = st.text_input("Username")
    password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        if bk.register_new_user(username, password):
            st.error("Account with this name already exists, Please choose a different username")
        else:
            st.success("Account created successfully\nWelcome to your new account {username}!")
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
    st.write(f"Welcome back, {st.session_state.username}!")
    st.write("Your banking dashboard will appear here!")
    st.metric(label="Current Balance", value="Rs")
    
    st.sidebar.divider()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()