*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  niina
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ni
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  niina
    Set Password  niina12
    Set Password Confirmation  niina12
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Valid Username And Invalid Password
    Set Username  niina
    Set Password  niinaniina
    Set Password Confirmation  niinaniina
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  niina
    Set Password  niinaniina
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  niina
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  niina
    Set Password  niina123
    Submit Credentials to Login
    Login Should Succeed

Login After Failed Registration
    Set Username  niina
    Set Password  niinaniina
    Set Password Confirmation  niinaniina
    Submit Credentials
    Register Should Fail With Message  Invalid password
    Click Link  Login
    Set Username  niina
    Set Password  niinaniina
    Submit Credentials to Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Reset Application Create User And Go To Register Page    
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Submit Credentials to Login
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}