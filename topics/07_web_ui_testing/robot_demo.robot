*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}                https://www.saucedemo.com
${BROWSER}        Chrome
${VALID_USER}     standard_user
${VALID_PASSWORD}   secret_sauce
${INVALID_USER}   invalid_user
${INVALID_PASSWORD}   wrong_password
${LOGIN_BUTTON}   css:input[type="submit"]
${USERNAME_FIELD}   css:#user-name
${PASSWORD_FIELD}   css:#password
${ERROR_MESSAGE}  css:.error-message-container

*** Test Cases ***
Login With Valid Credentials
    [Documentation]    Verify that a valid user can log in successfully.
    Open Browser To Login Page
    Input Login Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Click Login Button
    Wait Until Page Contains Element    css:#inventory_container    5 seconds
    [Teardown]    Close Browser

Login With Invalid Credentials
    [Documentation]    Verify that an invalid user cannot log in and sees an error message.
    Open Browser To Login Page
    Input Login Credentials    ${INVALID_USER}    ${INVALID_PASSWORD}
    Click Login Button
    Element Should Be Visible    ${ERROR_MESSAGE}
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    [Documentation]    Opens the browser and navigates to the login page.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Input Login Credentials
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}

Click Login Button
    Click Button    ${LOGIN_BUTTON}