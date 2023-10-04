import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    logger.info(f'Посетитель просматривает главную страницу.')
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная</title>
    </head>
    <body>
        <h1>Добро пожаловать в наш высокотехнологичный мир!</h1>
                
    </body>
    </html>
    """
    return HttpResponse(html_content)

def about(request):
    logger.info(f'Посетитель просматривает страницу "О себе".')
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <p>Мы предлагаем широкий ассортимент компьютерной техники и аксессуаров по выгодным ценам.</p>
        <p>Найдите идеальное решение для всех своих IT-потребностей среди тысячи продуктов, представленных в нашем каталоге. Мы гордимся высоким качеством и надежностью каждого товара.</p>
        <p>Оптимизируйте свой рабочий процесс и повысьте производительность с нашими мощными компьютерами и ноутбуками. У нас есть модели для всех задач и бюджетов.</p>
        <p>Подберите идеальный комплектующий для сборки своего уникального ПК, начиная с процессоров и видеокарт, заканчивая охлаждением и корпусами с инновационным дизайном.</p>
        <p>Наши эксперты готовы помочь вам с выбором и консультацией, чтобы каждая покупка приносила максимальную пользу и удовлетворение.</p>
        <p>Мы стремимся предоставить вам не только продукты, но и надежное партнерство в мире высоких технологий. Покупайте с уверенностью в завтрашнем дне!</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)