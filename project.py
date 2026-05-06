import streamlit as st

st.title("**Longest Substring Without Repeating Characters**",text_alignment="center")
word = st.text_input("enter a word") or "Not given"
st.text(f"your entered word is {word}")

if(word == "Not given"):
    word = ""
lp = 0

window= set()
ans = 0
for rp in range(len(word)):
    while(word[rp] in window):
        window.remove(word[lp])
        lp+=1
    
    ans = max(ans,rp-lp+1)
    window.add(word[rp])

code_example = """
lp = 0

window = set()
ans = 0
for rp in range(len(word)):
    while(word[rp] in window):
        window.remove(word[lp])
        lp+=1
    
    ans = max(ans,rp-lp+1)
    window.add(word[rp])

"""
st.code(code_example,language="python")
st.text(f"longest substring without repeating characters: {ans}")

print("done")
