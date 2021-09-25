import smtplib

print("---------------------------")
print("|                         |")
print("|  Mail Sender            |")
print("|  Version 1.0 by Marek_p |")
print("|                         |")
print("---------------------------")

sender_email = "váš gmail"
rec_email = input(str("Email Příjemce: "))
password = input(str("Heslo Odesílatele: "))
message = input(str("Zpráva: "))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Úspěšně přihlášen")
server.sendmail(sender_email, rec_email, message)
print("Email byl poslán na", rec_email)
