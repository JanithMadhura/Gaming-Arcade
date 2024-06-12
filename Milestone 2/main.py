import time
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


# Initializing variables
total_games_played_in_hangman = 0
total_games_played_in_tictac = 0
total_games_played_in_pianotiles = 0
total_time_spent_hangman = 0
total_time_spent_tictac = 0
total_time_spent_pianotiles = 0
elapsed_time_in_hangman = 0
elapsed_time_in_tictac = 0
elapsed_time_in_pianotiles = 0




class TopicApp(App):
    def build(self):
        # Create a screen manager
        screen_manager = ScreenManager()

        # Create the home screen
        home_screen = Screen(name='home_screen')
        layout = BoxLayout(orientation='vertical')
        topic_label = Label(text='Welcome to the JM Gaming Arcade Dashboard!', font_size=45, pos={0, 200})
        button_a = Button(text='HANGMAN', size_hint=(0.6, None), height=90, pos_hint={'center_x': 0.5} , font_size = 30,background_color=(0, 1, 0, 1))
        button_b = Button(text='TIC TAC TOE', size_hint=(0.6, None), height=90, pos_hint={'center_x': 0.5},font_size = 30,background_color=(0, 1, 0, 1))
        button_c = Button(text='PIANO TILES', size_hint=(0.6, None), height=90, pos_hint={'center_x': 0.5},font_size = 30,background_color=(0, 1, 0, 1))
        button_d = Button(text='TOTAL GAMES PLAYED', size_hint=(0.6, None), height=90, pos_hint={'center_x': 0.5},font_size = 30,background_color=(0, 1, 0, 1))
        button_e = Button(text='TOTAL TIME SPENT IN EACH GAMES', size_hint=(0.6, None), height=90,pos_hint={'center_x': 0.5},font_size = 30,background_color=(0, 1, 0, 1))
        button_f = Button(text='EXIT', size_hint=(0.6, None), height=90, pos_hint={'center_x': 0.5},font_size = 30,background_color=(1, 0, 0, 1))

        def play_game_a():
            global total_games_played_in_hangman
            total_games_played_in_hangman += 1

        def play_game_b():
            global total_games_played_in_tiktac
            total_games_played_in_tictac += 1

        def play_game_c():
            global total_games_played_in_tiktac
            total_games_played_in_pianotiles += 1

        def button_a_clicked(instance):
            start_time = time.time()
            import hangman
            play_game_a()
            end_time = time.time()
            global elapsed_time_in_hangman
            elapsed_time_in_hangman = end_time - start_time + elapsed_time_in_hangman
            del sys.modules['hangman']
            
        time_label_hangman = Label(text='', font_size=30)
        time_label_tictac = Label(text='', font_size=30)
        time_label_pianotiles = Label(text='', font_size=30)
        no_of_hangman = Label(text='', font_size=30)
        no_of_tictac = Label(text='', font_size=30)
        no_of_pianotiles = Label(text='', font_size=30)
        
        def button_b_clicked(instance):
            start_time = time.time()
            import tictac
            play_game_b()
            end_time = time.time()
            global elapsed_time_in_tictac
            elapsed_time_in_tictac = end_time - start_time + elapsed_time_in_tictac
            del sys.modules['tictac']

        def button_c_clicked(instance):
            start_time = time.time()
            import pianotiles
            play_game_c()
            end_time = time.time()
            global elapsed_time_in_tictac
            elapsed_time_in_pianotiles = end_time - start_time + elapsed_time_in_pianotiles
            del sys.modules['tictac']


        def button_d_clicked(instance):
            screen_manager.current = 'games_played_screen'
            no_of_hangman.text = f"Number of hamngman game played: {total_games_played_in_hangman} seconds"
            no_of_tictac.text = f"Number of tictac game played: {total_games_played_in_tictac} seconds"
            no_of_pianotiles.text = f"Number of piano tiles game played: {total_games_played_in_pianotiles} seconds"

        def button_e_clicked(instance):
            screen_manager.current = 'time_spent_screen'
            time_label_hangman.text = f"Elapsed time in hamngman: {elapsed_time_in_hangman} seconds"
            time_label_tictac.text = f"Elapsed time in tictac: {elapsed_time_in_tictac} seconds"
            time_label_pianotiles.text = f"Elapsed time in piano tiles: {elapsed_time_in_pianotiles} seconds"
            
        def button_f_clicked(instance):
            print("Exiting the Gaming Arcade Dashboard. Goodbye!")
            

        
        button_a.bind(on_press=button_a_clicked)
        button_b.bind(on_press=button_b_clicked)
        button_c.bind(on_press=button_c_clicked)
        button_d.bind(on_press=button_d_clicked)
        button_e.bind(on_press=button_e_clicked)
        button_f.bind(on_press=button_f_clicked)

        # Add the widgets to the home screen layout
        layout.add_widget(topic_label)
        layout.add_widget(button_a)
        layout.add_widget(button_b)
        layout.add_widget(button_c)
        layout.add_widget(button_d)
        layout.add_widget(button_e)
        layout.add_widget(button_f)

        
        home_screen.add_widget(layout)

        # Create the games played screen
        games_played_screen = Screen(name='games_played_screen')
        games_played_layout = BoxLayout(orientation='vertical')
        games_played_label = Label(text='', font_size=32)
        games_played_back_button = Button(text='Back', size_hint=(0.6, None), height=90,pos_hint={'center_x': 0.5})

        def games_played_back_button_clicked(instance):
            screen_manager.current = 'home_screen'

        games_played_back_button.bind(on_press=games_played_back_button_clicked)

        # Add the widgets to the games played screen layout
        games_played_layout.add_widget(no_of_hangman)
        games_played_layout.add_widget(no_of_tictac)
        games_played_layout.add_widget(no_of_pianotiles)
        games_played_layout.add_widget(games_played_label)
        games_played_layout.add_widget(games_played_back_button)
        games_played_screen.add_widget(games_played_layout)


        # Create the time spent screen
        time_spent_screen = Screen(name='time_spent_screen')
        time_spent_layout = BoxLayout(orientation='vertical')
        time_spent_label = Label(text='Time Spent in Games', font_size=32)
        time_spent_back_button = Button(text='Back', size_hint=(0.6, None), height=90,pos_hint={'center_x': 0.5})

        def time_spent_back_button_clicked(instance):
            screen_manager.current = 'home_screen'

        time_spent_back_button.bind(on_press=time_spent_back_button_clicked)

        # Add the widgets to the time spent screen layout
        time_spent_layout.add_widget(time_label_hangman)
        time_spent_layout.add_widget(time_label_tictac)
        time_spent_layout.add_widget(time_label_pianotiles)
        time_spent_layout.add_widget(time_spent_back_button)
        time_spent_screen.add_widget(time_spent_layout)
        time_spent_back_button.bind(on_press=time_spent_back_button_clicked)

        

        # Add the screens to the screen manager
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(games_played_screen)
        screen_manager.add_widget(time_spent_screen)

        return screen_manager


# Run the app
if __name__ == '__main__':
    TopicApp().run()
