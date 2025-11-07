*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  riina
    Set Password  riina123
    Set Password Confirmation  riina123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  as
    Set Password  salainen
    Set Password Confirmation  salainen
    Click Button  Register
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  mikko
    Set Password  okkim1
    Set Password Confirmation  okkim1
    Click Button  Register
    Register Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
    Set Username  jonna
    Set Password  jonalankonna
    Set Password Confirmation  jonalankonna
    Click Button  Register
    Register Should Fail With Message  Password can not iclude only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  konsta
    Set Password  konsta123
    Set Password Confirmation  konsta456
    Click Button  Register
    Register Should Fail With Message  Password and confirmation password do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}