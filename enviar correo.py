import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura tus credenciales y la información del correo
from_email = 'anderson.pierola.r@uni.pe'
to_email = 'anderson.pierola.r@uni.pe'
password = 'vuht jpum jmne zimf'

# Crea el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = from_email
mensaje['To'] = to_email
mensaje['Subject'] = 'correo de prueba'

cuerpo_del_mensaje = 'Este es un correo de prueba'

mensaje.attach(MIMEText(cuerpo_del_mensaje, 'plain'))

# Inicia una conexión SMTP
smtp_server = 'smtp.gmail.com'  # Servidor SMTP de Gmail
smtp_port = 587  # Puerto de SMTP de Gmail
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Inicia sesión en tu cuenta de correo
server.login(from_email, password)

# Envía el correo
texto_del_correo = mensaje.as_string()
server.sendmail(from_email, to_email, texto_del_correo)

# Cierra la conexión SMTP
server.quit()

print('El correo ha sido enviado con éxito.')
