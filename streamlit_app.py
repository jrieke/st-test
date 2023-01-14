import numpy as np
import pandas as pd
import streamlit as st


class StreamlitInt(int):
    def foo(self):
        return "foo"

    def changed(self):
        return st.session_state.slider_changed


# a = SpecialInt(5)
# st.write(a)
# st.write(a.foo())

if not "slider_changed" in st.session_state:
    st.session_state.slider_changed = False


# Only do this once.
@st.experimental_singleton
def hack_streamlit():
    original_slider = st.slider

    def special_slider(
        label,
        min_value=None,
        max_value=None,
        value=None,
        step=None,
        format=None,
        key=None,
        help=None,
        *,
        disabled=False,
        label_visibility="visible"
    ):
        def on_change():
            st.session_state.slider_changed = True

        return_value = StreamlitInt(
            original_slider(
                label=label,
                min_value=min_value,
                max_value=max_value,
                value=value,
                step=step,
                format=format,
                key=key,
                help=help,
                disabled=disabled,
                label_visibility=label_visibility,
                on_change=on_change,
            )
        )
        return_value.max_value = max_value
        return return_value

    st.slider = special_slider

hack_streamlit()

"# 💊 Return values on steroids"
"*Just a hacky demo from Johannes on a possible future API for Streamlit 2.0.*"

"We're creating a normal slider:"
with st.echo():
    number = st.slider("My slider", 0, 100, 50)

"Its return value seems to be a normal int:"
with st.echo():
    st.write(number)

"But it's not! It's a special type that inherits from int:"
with st.echo():
    st.write(type(number))

"""
This special type allows us to use the return value as an int – but also do 
advanced stuff on top of it! Some examples below.
"""

"""
---

We can check whether the widget value changed, without using a callback. Try it 
out by moving the slider above (should show `True`). Then press R to rerun without 
changing the slider (should show `False`). 
"""
with st.echo():
    st.write(number.changed())

"---"
"We could let the developer access additional attributes from the widget:"
with st.echo():
    st.write(number.max_value)
    
"""
This example is kinda useless because we explicitly set `max_value` above. But maybe 
there are cool use cases for this!
"""

"""
---

We could use this very handily for selections and other advanced interactivity 
features. This doesn't make much sense for a slider but imagine you have a chart and 
can do:

```python
chart = st.line_chart(..., rerun=["selection", "zoom"])
chart.selection
chart.bounding_box
```
"""

"""
---

We could also use this to allow delta generator + return value usage! Something like:

```python
number = st.slider(...)
st.write(number)
number.text_input(...)
```

Not sure if that improves Streamlit so much. Delta generators are hardly used anyway. 
But it would kinda nicely unify our API. No mix between delta generators and other 
values. Every return value can just be used as a delta generator.
"""

"""
---

More advanced but maybe you can even use this to change the widget on the fly? E.g. you 
can do:

```python
number.set(42)
```

And this would send an update proto to the frontend that updates the number of the 
widget. Might be weird if the app takes a long time to run and then things change later 
on. But it definitely is super easy to understand! 

Would simplify our old coupled sliders example to:

```python
celsius = st.slider("Celsius", 0, 100, 0)
fahrenheit = st.slider("Fahrenheit", 0, 212, 32)

if celsius.changed():
    fahrenheit.set(celsius * 9 / 5 + 32)
elif fahrenheit.changed():
    celsius.set((fahrenheit - 32) * 5 / 9)
```

No callbacks, just a straightforward Python script!
"""


# This always needs to be at the end. Set it to False for the next run.
st.session_state.slider_changed = False
