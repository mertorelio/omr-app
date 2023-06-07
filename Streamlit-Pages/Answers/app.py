import streamlit as st
from screen import screen_scan_main

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


def main():
  
    screen_scan_main()

   
if __name__ == "__main__":
    main()
    
    
    
