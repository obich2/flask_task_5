from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control space-top1" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-select space-top2" id="classSelect" name="education" aria-label="Default select example">
                                          <option>Начальное</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</zoption>
                                        </select>
                                     </div>
                                     
                                    <label for="classSelect">Какие у Вас есть професии?</label> 
                                    
                                    <div class="form-group form-check space-top3">
                                        <input type="checkbox" class="form-check-input" id="prf1" name="prf1">
                                        <label class="form-check-label" for="prf1">Инженер-исследователь</label>
                                    </div>   
                                     
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prf2" name="prf2">
                                        <label class="form-check-label" for="prf2">Инженер-строитель</label>
                                    </div>    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prf3" name="prf3">
                                        <label class="form-check-label" for="prf3">Пилот</label>
                                    </div>
                                    
                                    <div class="form-group form-check">    
                                        <input type="checkbox" class="form-check-input" id="prf4" name="prf4">
                                        <label class="form-check-label" for="prf4">Метеоролог</label>
                                    </div>    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prf5" name="prf5">
                                        <label class="form-check-label" for="prf5">Инженер по жизнеобеспечению</label>
                                    </div>    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prf6" name="prf6">
                                        <label class="form-check-label" for="prf6">Инженер по радиационной защите</label>
                                    </div>    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prf7" name="prf7">
                                        <label class="form-check-label" for="prf7">Врач</label>
                                    </div>    
                                    
                                    <div class="form-group form-check space-bot1">
                                        <input type="checkbox" class="form-check-input" id="prf8" name="prf8">
                                        <label class="form-check-label" for="prf8">Экзобиолог</label>    
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check space-top3">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        
                                        <div class="form-check space-bot2">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        
                                        <div class="form-group space">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    <label for="photo">Приложите фотографию</label>
                                    
                                    
                                    <div class="form-group space">
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check space-bot2">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    
                                    </div>
        
                                    <button type="submit" class="btn btn-primary">отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        for i in range(1, 9):
            print(request.form.get("prf" + str(i)))
        print(request.form.get('sex'))
        print(request.form.get('about'))
        print(request.form.get('file'))
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')