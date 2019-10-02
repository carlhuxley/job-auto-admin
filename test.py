import os
from automate import App_page


EMAIL_USER = os.environ.get('EMAIL_USER')
CWJOB_PASS = os.environ.get('CWJOB_PASS')


page = App_page()

login_seq = [page.page_get('https://www.cwjobs.co.uk/account/signin?ReturnUrl=/'),
               page.send_keys_id('Form_Email', EMAIL_USER),
               page.send_keys_id('Form_Password', CWJOB_PASS),
               page.click_xpath('//*[@id="btnLogin"]')
               ]

page.run_steps(login_seq)
# Add a check to confirm you are logged in before running the following code!

# page.run_steps([page.page_get('https://www.cwjobs.co.uk/job/java-developer/picture-more-ltd-job88086735?r=8-Results'),
#                           page.click_link('APPLY'),
#                           page.click_id('coverLetterText'),
#                           page.click_id('btnSubmit')
#                           ])
