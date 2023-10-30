# tools_n_stuff

--cleanupemail.py usage: 
Copy everything after the TO field in a message header for the emails you'd like to copy. 
Paste that into "input.txt" file, in the same directory as cleanupemail.py 
run the script from a command prompt 
bing bang boom, you've got a csv with just the email addresses. 
I use this for mailing from Word

--authsmtptestemail.py usage: 
This script takes user input for server, user, recipient, password, etc and sends a test email. Useful for troubleshooting issues with SMTP failures on copiers and mailers. 


--recordchecker.py usage: 
it'll ask for domain input and check for A, MX, and txt records. Kinda just a faster way to do all. 


--File_Integrity_Alert.py 
This is kinda just a test I wanted to do. FIM is a way to ensure files are not tampered with. You can see the value of monitoring important files. This does that. You’ve just gotta edit the script for the file(s) you wish to monitor. IRL you’d need to make some adjustments and add it to a task schedule or something. But it creates a log and emails if a change in a files hash is detected. 



--password_gen_year.py
So there are a ton of wordlists but I’ve noticed they’re not updated a ton or at least the ones I’ve seen. So, I created this short script which will take user input and basically just add the year along with a symbol which is a very common password combo. So, you enter “summer” and it’ll output all of those permutation: Summer2023! Summer 2023@ etc. You can enter a number of base words separated by commas. The resulting word list will be written to wordlist.txt


--ipchangealert.ps1 
This powershell script basically just queries https://api.ipify.org which gives a response of the current public IP address. Then, a txt file is made in the same directory as the script called ip.txt. ip.txt stores the last IP address value. And when the script runs again, if the IP has changed, it will send an SMTP alert letting you know. This could be helpful if you don't have a static IP but are hosting something on the public internet. 
