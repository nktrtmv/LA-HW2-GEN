import smtplib
import ssl
import numpy as np
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

#from config import EMAIL_PASSWORD
from settings import EMAIL_ADDRESS, PORT, PATH_TO_TASKS, PATH_TO_STUDENTS, HW_NUMBER, EMAIL_PASSWORD
from student import Student
import logging

if __name__ == '__main__':
    logging.basicConfig(filename="mailer.log", level=logging.INFO)
    log = logging.getLogger("info")
    log.info('logger created')

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = f"ИДЗ №{HW_NUMBER} по Алгебре"
        body = "Исправленная версия ИДЗ. Поменялся 10 номер. Всем решившим неисправленную версию необходимо указать это в решении. Если ещё не решали 10й номер, лучше решать этот."
        students = Student.read_students_csv(PATH_TO_STUDENTS)
        log.info(f'added students:')
        for student in students:
            log.info(f'{student.name} {student.group} {student.email}')
        groups_prev_variant: dict[str, int] = {}

        for variant, student in enumerate(students):
            receiver_email = student.email

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = EMAIL_ADDRESS
            message["To"] = receiver_email
            message["Subject"] = subject

            # Add body to email
            message.attach(MIMEText(body, "plain"))
            if student.group not in groups_prev_variant:
                groups_prev_variant[student.group] = 0

            groups_prev_variant[student.group] += 1

            filename = f"{PATH_TO_TASKS}{student.group}_var{groups_prev_variant[student.group]}.pdf"

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=IHW Algebra {student.group if student.group != '2211' else 'additional'} var{groups_prev_variant[student.group]}.pdf",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()
            try:
                server.sendmail(EMAIL_ADDRESS, receiver_email, text)
                log.info(
                    f'Successfully sent variant {groups_prev_variant[student.group]} to {student.name} {student.group} {student.email}')
            except Exception as e:
                log.info(
                    f'Fail on variant {groups_prev_variant[student.group]}, student {student.name} {student.group} {student.email}: {e}')
            sleep(3 + np.random.randint(0, 3))
