from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("LoginPage.kv")


class QuizPageApp(App):

    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


class LoginPageApp(App):
    pass


class LoginManager(ScreenManager):
    pass


class Question1Screen(Screen):
    def answer_question(self, is_correct):
        if is_correct:
            self.manager.current = "correct"
        elif not is_correct:
            self.manager.current = "error"


class CorrectScreen(Screen):
    pass


class ErrorScreen(Screen):
    def retry(self):
        self.manager.current = "question1"


QuizPageApp().run()
