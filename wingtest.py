
import kivy
from kivy.app                import App
from kivy.uix.boxlayout      import BoxLayout
from kivy.uix.floatlayout    import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang               import Builder
from kivy.uix.button         import Button

kivy.require('1.10.1')

'''
Wings test app
Created by Seth Abraham, November 11, 2018

'''

Builder.load_string('''

#:kivy 1.10.1
#

# from box
<TTest>:
    Button:
        id: first
        text: 'Eat me'

    BoxLayout:
    #FloatLayout:
    #RelativeLayout:
        id: second
        #
        # failure to size this layout will result in the outside box
        # not understanding the width of the layout.
        # the behavior is independent of whether this is a box, float or relative
        # This is a failure of our understanding.
        # We expected the layout to look at the sizes of its members and say,
        #  "oh, I see that all my members are fixed width, so I shall set my width"
        # It seems that no such behavior occurs.  Rather, the behavior looks closer to
        #  "oh, I have no preconceived notions of my width, so I will take my que from
        #   the layout i am a part of"
        # Interestingly enough, if you just set the size_hint_x to None, you gain more
        # insight into what is happening.  Just uncommenting size_hint_x causes the
        # center to be sized at 100, the default size.  Again, expecting the layout
        # to notice its height is not appropriate.
        #
        # AND, as a kicker, this observation probably (mostly) explains our funny grid behavior with respect
        # to height.  Remember as soon as we forced a column height, the layout suddenly became
        # maximally sized top to bottom.  We interpreted this as kivy loosing its mind.
        # More likely, what probably was occurring is that when we forced a column height, we got a size hint
        # of None in that dimension.  BUT we had not actually set the height.  So we lost the benefit of
        # of relative sizing in that dimension.  Our solution for the grid was the correct one: manually
        # set the height, because we should have no expectation that this was going to happen automatically.
        # Probably the more mysterious issue is why we did not have to explicitly set the hint to None!
        #
        # Play with this a little, commenting and uncommenting the next two lines
        # and varying the size of the inner widgets.  You can change the layouts of the internal
        # thing here, and you will see that box, float and relative are actually pretty consistant
        # in behavior
        #
        size_hint_x: None
        #width: 200
        Label:
            text: 'Me'
            size_hint_x: None
            width: 450
        Label:
            text: 'Me2'
            size_hint_x: None
            width: 200

    Button:
        id: third
        text: 'Drink me'
''')


class TTest(BoxLayout):
    pass

class TTestApp(App):
    def build(self):
        r = TTest()
        #print(r.ids)
        #print("labels in app:  ",r.ids.keys())
        return r


if __name__ == '__main__':
    TTestApp().run()
