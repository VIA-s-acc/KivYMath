from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        euler_button = Button(text='Эйлер', on_press=self.go_to_euler_screen)
        adam_button = Button(text='Адам', on_press=self.go_to_adam_screen)
        mod_adam_button = Button(text='Мод. Адам', on_press=self.go_to_mod_adam_screen)
        layout.add_widget(euler_button)
        layout.add_widget(adam_button)
        layout.add_widget(mod_adam_button)
        self.add_widget(layout)


    def go_to_euler_screen(self, instance):
        self.manager.current = 'euler'

    def go_to_adam_screen(self, instance):
        self.manager.current = 'adam'

    def go_to_mod_adam_screen(self, instance):
        self.manager.current = 'mod_adam'


class EulerScreen(Screen):
    def __init__(self, **kwargs):
        super(EulerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        menu_button = Button(text='Menu', size_hint=(0.1, 0.1), pos_hint={'top': 1, 'right': 0.1})
        dropdown = DropDown()
        main_button = Button(text='Main', size_hint_y=None, height=28)
        main_button.bind(on_release=lambda instance: [self.go_to_main_screen(instance), dropdown.dismiss()])
        dropdown.add_widget(main_button)
        adam_button = Button(text='Adam', size_hint_y=None, height=28)
        adam_button.bind(on_release=lambda instance: [self.go_to_adam_screen(instance), dropdown.dismiss()])
        dropdown.add_widget(adam_button)
        mod_adam_button = Button(text='Adam_mod', size_hint_y=None, height=28)
        mod_adam_button.bind(on_release=lambda instance: [self.go_to_mod_adam_screen(instance), dropdown.dismiss()])
        dropdown.add_widget(mod_adam_button)
        menu_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(menu_button, 'text', x))

        layout.add_widget(menu_button)
        # The rest of your layout code goes here
        
        equation_input = TextInput(hint_text="Уравнение: y' = f(x, y)", size_hint=(1, 0.1))
        initial_point_input = TextInput(hint_text='Начальная точка: x0 = p', size_hint=(1, 0.05))
        final_point_input = TextInput(hint_text='Конечная точка: xN = q', size_hint=(1, 0.05))
        initial_condition_input = TextInput(hint_text='Начальное условие: y(x0) = r', size_hint=(1, 0.05))
        error_input = TextInput(hint_text='Погрешность: eps', size_hint=(1, 0.05))
        ok_button = Button(text='Ок', on_press=self.show_solution, size_hint=(1, 0.05) )

        # Create a scrollable label to display the solution
        solution_output = ScrollView(size_hint=(1, 0.5))
        math_formula = r'$y_{n+1} = y_n + f(x_n,y_n) \cdot h$'

        # Create a matplotlib widget and add it to the layout
        solution_label = Label(
            text='y_{n+1} = y_n + f(x_n,y_n) \cdot h', 
            markup=True, 
            size_hint_y=None
        )
        solution_label.bind(width=lambda *x: solution_label.setter('text_size')(solution_label, (solution_label.width, None)),
                                    texture_size=lambda *x: setattr(solution_label, 'height', solution_label.texture_size[1]))
        solution_output.add_widget(solution_label)
        
       

        
        layout.add_widget(equation_input)
        layout.add_widget(initial_point_input)
        layout.add_widget(final_point_input)
        layout.add_widget(initial_condition_input)
        layout.add_widget(error_input)
        layout.add_widget(ok_button)
        layout.add_widget(solution_output)

        self.add_widget(layout)


    def go_to_euler_screen(self, instance):
        self.manager.current = 'euler'

    def go_to_adam_screen(self, instance):
        self.manager.current = 'adam'

    def go_to_mod_adam_screen(self, instance):
        self.manager.current = 'mod_adam'

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

    def show_solution(self, instance):

        # Здесь будет ваш код для отображения решения методом Эйлера
        pass



class AdamScreen(Screen):
    def __init__(self, **kwargs):
        super(AdamScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        text_input = TextInput(hint_text='Введите что-то')
        layout.add_widget(text_input)
        self.add_widget(layout)


class ModAdamScreen(Screen):
    def __init__(self, **kwargs):
        super(ModAdamScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        text_input = TextInput(hint_text='Введите что-то')
        layout.add_widget(text_input)
        self.add_widget(layout)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(EulerScreen(name='euler'))
        sm.add_widget(AdamScreen(name='adam'))
        sm.add_widget(ModAdamScreen(name='mod_adam'))
        return sm


if __name__ == '__main__':
    MyApp().run()
