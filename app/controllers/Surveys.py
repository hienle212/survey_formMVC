from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        # self.load_model('WelcomeModel')
        # self.db = self._app.db
  
    def index(self):
        return self.load_view('main.html')
    def process(self, methods=['POST']):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        if 'counter' not in session :
            session['counter'] = 1
        else :
            session['counter'] +=1
        return redirect('/surveys/result')
    def result(self):
        return self.load_view('result.html')    
