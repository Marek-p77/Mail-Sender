import smtplib

print("---------------------------")
print("|                         |")
print("|  Mail Sender            |")
print("|  Version 1.0 by Marek_p |")
print("|                         |")
print("---------------------------")

sender_email = "váš gmail"
rec_email = input(str("Email Příjemce: "))
password = input(str("Heslo Odesílatele: ")) # Zeptá se vás na heslo k "sender_mail"
message = input(str("Zpráva: ")) # Zeptá se vás na zprávu

server = smtplib.SMTP('smtp.gmail.com', 587) # Adresa a port mail serveru
server.starttls() # Vytvoření spojení
server.login(sender_email, password) # Přihlášení
print("Úspěšně přihlášen")
server.sendmail(sender_email, rec_email, message) # Odeslání mailu
print("Email byl poslán na", rec_email)
