import kivy
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDIconButton
from kivymd.uix.tab import MDTabsBase, MDTabs

class Tabs(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class StaxAttax(MDApp):
    # build app
    def build(self):
        # app icon image
        self.icon = 'staxrat.png'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"

####### functions for unilateral coordinates tab 1 ###############################################  
    def calculate_uni(self):
        # exception handling for coordinate calculations
        try:
            # ap calculation
            ap_bregma = float(self.root.ids.ap_bregma1.text)
            ap_distance = float(self.root.ids.ap_distance1.text)
            ap_sum = str(round((ap_bregma + ap_distance),1))
            self.root.ids.ap_target1.color = [0.6, 0, 0 , 1]
            self.root.ids.ap_target1.text = str(" AP\nTarget\n"+(ap_sum))
            # lm calculation
            lm_bregma = float(self.root.ids.lm_bregma1.text)
            lm_distance = float(self.root.ids.lm_distance1.text)
            lm_sum = str(round((lm_bregma + lm_distance),1))
            self.root.ids.lm_target1.color = [0.8, 0.2, 0.6, 1]
            self.root.ids.lm_target1.text = str(" LM\nTarget\n"+(lm_sum))
            # dv calculation
            dv_bregma = float(self.root.ids.dv_bregma1.text)
            dv_distance = float(self.root.ids.dv_distance1.text)
            dv_sum = str(round((dv_bregma + dv_distance),1))
            self.root.ids.dv_target1.color = [0.4, 0.2, 0.8, 1]
            self.root.ids.dv_target1.text = str(" DV\nTarget\n"+(dv_sum))

            self.root.ids.input_error1.text = str('')

        # error message if coordinate inputs are not int or float numbers
        except ValueError:
            self.root.ids.input_error1.color = [1, 0, 0, 1]
            self.root.ids.input_error1.text = str("!Error! Inputs must be whole numbers or decimal")

    release_count = 0
    def egg_button_on_release(self):
        if self.root.ids.release_count == 0:
            self.root.ids.egg_question()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer()
            self.release_count = 0
            return 

    def egg_question(self):
        self.root.ids.egg_question_text1.color = [0, 1, 0.4, 1]
        self.root.ids.egg_question_text1.text = str("What are the only sure things in the life of a rattus?")


    def egg_answer(self):
        self.root.ids.egg_answer_text1.color = [0, 1, 0.4, 1]
        self.root.ids.egg_answer_text1.text = str("Death and stereo... TAXES!!!")

####### functions for bilateral coordinates tab 2 ###############################################  

    def calculate_bi(self):
            # exception handling for coordinate calculations
            try:
                # ap calculation
                ap_bregma = float(self.root.ids.ap_bregma2.text)
                ap_distance = float(self.root.ids.ap_distance2.text)
                ap_sum = str(round((ap_bregma + ap_distance),1))
                self.root.ids.ap_target2.color = [0.6, 0, 0 , 1]
                self.root.ids.ap_target2.text = str(" AP\nTarget\n"+(ap_sum))
                # lm calculation
                lm_bregma = float(self.root.ids.lm_bregma2.text)
                lm_distance = float(self.root.ids.lm_distance2.text)
                abs_val_lm_dist = abs(lm_distance)
                r_trg = str(round((lm_bregma + abs_val_lm_dist),1))
                l_trg = str(round((lm_bregma - abs_val_lm_dist),1))
                self.root.ids.lm_target_R2.color = [0.8, 0.2, 0.6, 1]
                self.root.ids.lm_target_R2.text = str(" LM R\nTarget\n"+(l_trg))
                self.root.ids.lm_target_L2.color = [0.8, 0.2, 0.6, 1]
                self.root.ids.lm_target_L2.text = str(" LM L\nTarget\n"+(r_trg))
                # dv calculation
                dv_bregma = float(self.root.ids.dv_bregma2.text)
                dv_distance = float(self.root.ids.dv_distance2.text)
                dv_sum = str(round((dv_bregma + dv_distance),1))
                self.root.ids.dv_target2.color = [0.4, 0.2, 0.8, 1]
                self.root.ids.dv_target2.text = str(" DV\nTarget\n"+(dv_sum))

                self.root.ids.input_error2.text = str('')

            # error message if coordinate inputs are not int or float numbers
            except ValueError:
                self.root.ids.input_error2.color = [1, 0, 0, 1]
                self.root.ids.input_error2.text = str("!Error! Inputs must be whole numbers or decimal")

    release_count = 0
    def egg_button_on_release(self):
        if self.root.ids.release_count == 0:
            self.root.ids.egg_question()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer()
            self.release_count = 0
            return 

    def egg_question(self):
        self.root.ids.egg_question_text2.color = [0, 1, 0.4, 1]
        self.root.ids.egg_question_text2.text = str("Did you hear about the rattus that retired?")


    def egg_answer(self):
        self.root.ids.egg_answer_text2.color = [0, 1, 0.4, 1]
        self.root.eds.egg_answer_text2.text = str("Guess it was sick of the rat race!!!")

####### functions for 2x bilateral coordinates tab 3 #############################################
    def calculate_2x_bi(self):
        # exception handling for coordinate calculations
        try:
            # ap calculation 
            ap_bregma = float(self.root.ids.ap_bregma3.text)

            ap_distance1 = float(self.root.ids.ap_distance3_1.text)
            ap_sum1 = str(round((ap_bregma + ap_distance1),1))
            self.root.ids.ap_target3_1.color = [0.6, 0, 0 , 1]
            self.root.ids.ap_target3_1.text = str(" AP\nTarget\n"+(ap_sum1))

            ap_distance2 = float(self.root.ids.ap_distance3_2.text)
            ap_sum2 = str(round((ap_bregma + ap_distance2),1))
            self.root.ids.ap_target3_2.color = [0.6, 0, 0 , 1]
            self.root.ids.ap_target3_2.text = str(" AP\nTarget\n"+(ap_sum2))


            # lm calculation
            lm_bregma = float(self.root.ids.lm_bregma3.text)

            lm_distance1 = float(self.root.ids.lm_distance3_1.text)
            abs_val_lm_dist1 = abs(lm_distance1)
            l_trg1 = str(round((lm_bregma - abs_val_lm_dist1),1))
            r_trg1 = str(round((lm_bregma + abs_val_lm_dist1),1))
            self.root.ids.lm_target_R3_1.color = [0.8, 0.2, 0.6, 1]
            self.root.ids.lm_target_R3_1.text = str(" LM R\nTarget\n"+(l_trg1))
            self.root.ids.lm_target_L3_1.color = [0.8, 0.2, 0.6, 1]
            self.root.ids.lm_target_L3_1.text = str(" LM L\nTarget\n"+(r_trg1))

            lm_distance2 = float(self.root.ids.lm_distance3_2.text)
            abs_val_lm_dist2 = abs(lm_distance2)
            l_trg2 = str(round((lm_bregma - abs_val_lm_dist2),1))
            r_trg2 = str(round((lm_bregma + abs_val_lm_dist2),1))
            self.root.ids.lm_target_R3_2.color = [0.8, 0.2, 0.6, 1]
            self.root.ids.lm_target_R3_2.text = str(" LM R\nTarget\n"+(l_trg2))
            self.root.ids.lm_target_L3_2.color = [0.8, 0.2, 0.6, 1]
            self.root.ids.lm_target_L3_2.text = str(" LM L\nTarget\n"+(r_trg2))


            # dv calculation
            dv_bregma = float(self.root.ids.dv_bregma3.text)

            dv_distance1 = float(self.root.ids.dv_distance3_1.text)
            dv_sum1 = str(round((dv_bregma + dv_distance1),1))
            self.root.ids.dv_target3_1.color = [0.4, 0.2, 0.8, 1]
            self.root.ids.dv_target3_1.text = str(" DV\nTarget\n"+(dv_sum1))

            dv_distance2 = float(self.root.ids.dv_distance3_2.text)
            dv_sum2 = str(round((dv_bregma + dv_distance2),1))
            self.root.ids.dv_target3_2.color = [0.4, 0.2, 0.8, 1]
            self.root.ids.dv_target3_2.text = str(" DV\nTarget\n"+(dv_sum2))

            self.root.ids.input_error3.text = str('')

        # error message if coordinate inputs are not int or float numbers
        except ValueError:
            self.root.ids.input_error3.color = [1, 0, 0, 1]
            self.root.ids.input_error3.text = str("!Error! Inputs must be whole numbers or decimal")

    release_count = 0
    def egg_button_on_release(self):
        if self.root.ids.release_count == 0:
            self.root.ids.egg_question()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer()
            self.release_count = 0
            return 

    def egg_question(self):
        self.root.ids.egg_question_text2.color = [0, 1, 0.4, 1]
        self.root.ids.egg_question_text2.text = str("Have you heard of the eerie rat party place?")


    def egg_answer(self):
        self.root.ids.egg_answer_text2.color = [0, 1, 0.4, 1]
        self.root.eds.egg_answer_text2.text = str("It sounds like you better check out the EAR BAR!!!")

    # function to control switching between tabs
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text

StaxAttax().run()