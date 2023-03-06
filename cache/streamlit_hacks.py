import streamlit as st

# Hacks
st.memoize = st.experimental_memo
st.global_state = st.experimental_singleton
st.app = st.experimental_singleton


def auto_cache(
    func=None, *, copy=None, persist=None, show_spinner=True, max_entries=None, ttl=None
):
    if copy is None:
        try:
            return st.experimental_memo(
                func=func,
                persist=persist,
                show_spinner=show_spinner,
                max_entries=max_entries,
                ttl=ttl,
            )
        except TypeError:
            return st.experimental_singleton(func=func, show_spinner=show_spinner)
    elif copy:
        return st.experimental_memo(
            func=func,
            persist=persist,
            show_spinner=show_spinner,
            max_entries=max_entries,
            ttl=ttl,
        )
    else:
        # TODO: Show log warnings if persist or max_entries or ttl is used with copy=False.
        if persist:
            raise RuntimeWarning("persist=True has no effect if copy=False")
        return st.experimental_singleton(func=func, show_spinner=show_spinner)


st.auto_cache = auto_cache

st.global_state = {}
