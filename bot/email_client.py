import os

from flask import render_template
from flask_mail import Message

from app import app, config, mail
from app.models import User

SUBJECT_FEEDBACK = {
    'category': 'Запрос на новые компетенции',
    'question': 'Вопрос из бота',
    'feature': 'Запрос на новый функционал для бота'
}


def send_email(telegram_id, message, subject):
    recipients = [os.getenv('EMAIL_PROCHARRITY')]
    user = User.query.get(telegram_id)
    email = user.email
    name = f'{user.last_name} {user.first_name}'
    id = user.external_id
    with app.app_context():
        template = render_template(
            config.PROCHARRITY_TEMPLATE,
            message=message,
            id=id,
            telegram_id=telegram_id,
            email=email,
            name=name
        )
        msg = Message(
            subject=SUBJECT_FEEDBACK[subject],
            recipients=recipients,
            html=template
        )
        mail.send(msg)
    return